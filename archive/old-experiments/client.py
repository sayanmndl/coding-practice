import sys
import asyncio
import json
from typing import List, Dict, Any, Optional
from contextlib import AsyncExitStack

import httpx
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from llama_cpp import Llama
import json
import requests
from datetime import datetime

# -----------------------------
# Configuration Parameters
# -----------------------------
MODEL_PATH      = "/Users/sayanmandal/workspaces/models/qwen3_1_7b/Qwen3-1.7B-Q8_0.gguf"  # Path to the GGUF model file
N_CTX           = 4096     # Context window size (max number of tokens in context)
N_THREADS       = 8        # Number of CPU threads to use for inference
N_GPU_LAYERS    = 32        # Number of GPU layers to offload (0 = CPU only)
SEED            = 42       # Random seed for reproducibility
USE_MMAP        = True     # Use memory-mapped model file
USE_MLOCK       = False    # Lock model into RAM (requires USE_MMAP=False)
LOW_VRAM        = False    # Reduce VRAM usage (trading compute for memory)
F16_KV          = True     # Use f16 key/value cache
LOGITS_ALL      = False    # Return logits for all tokens
EMBEDDING       = False    # Enable embedding mode


class CodeRAGClient:
    LLM_ENDPOINT = "http://localhost:8000/v1/chat/completions"

    def __init__(self, server_script: str):
        self.server_script = server_script
        self.session: Optional[ClientSession] = None
        self.exit_stack = AsyncExitStack()
        self.llm = Llama(
                        model_path=MODEL_PATH,
                        n_ctx=N_CTX,
                        n_threads=N_THREADS,
                        n_gpu_layers=N_GPU_LAYERS,
                        seed=SEED,
                        use_mmap=USE_MMAP,
                        use_mlock=USE_MLOCK,
                        low_vram=LOW_VRAM,
                        f16_kv=F16_KV,
                        logits_all=LOGITS_ALL,
                        embedding=EMBEDDING,
                    )

        # dynamic memory & controls
        self.tools: List[Dict[str, str]] = []
        self.messages: List[Dict[str, str]] = []
        self.long_term_memory: str = ""
        self.step_counter: int = 0
        self.max_steps: int = 10
        self.history_limit: int = 20
        self.history_trim_size: int = 10

    async def connect(self):
        """Launch your MCP server and grab its tools."""
        if not self.server_script.endswith(('.py', '.js')):
            raise ValueError("Server script must end in .py or .js")
        ### [comment: here ensure that the python script is running in python virtual environment. Also I plan to use some paths to config file as args as well]  ###
        cmd = "python" if self.server_script.endswith(".py") else "node"
        params = StdioServerParameters(command=cmd, args=[self.server_script], env=None)
        transport = await self.exit_stack.enter_async_context(stdio_client(params))
        stdio, write = transport
        self.session = await self.exit_stack.enter_async_context(ClientSession(stdio, write))
        await self.session.initialize()

        # discover your tools
        tool_list = (await self.session.list_tools()).tools
        ### [comment: here I want to make sure it know what the arguments are for the tool, will the description suffice or does it need more info. should i make it explcit in the server script?] ###
        self.tools = [
            {"name": t.name, "description": t.description, "input_schema": t.inputSchema}
            for t in tool_list
        ]
        print("✅ Connected. Tools:", [t["name"] for t in self.tools])

    def _build_system_prompt(self) -> str:
        ### {Lets rename this I will use a custom name. Make it extemely detailed system prompt. startin from You are a {name} ###
        lines = ["You are a code-analysis assistant with access to these tools:"]
        for t in self.tools:
            lines.append(f"- {t['name']}: {t['description']}\n\t{{\"tool_name\":\"{t['name']}\", \"parameters\":{t['input_schema']}}}")
        lines.append(
            "\nWhen you want to call a tool, emit exactly the JSON object by itself, for example:\n"
            "```json\n"
            "{\"tool_call\":{\"tool_name\":\"retrieve_functions\",\"parameters\":{\"query\":\"foo\"}}}\n"
            "```\n"
            "and then wait for the result before proceeding.\n\n"
            "You may plan dynamically as many steps as you need, up to 10 total tool calls.  "
            "Specifically, when fetching parent function bodies, do not exceed 3 levels of parents or more than 10 parent functions.\n\n"
            "The client will track every tool call.  You also have:\n"
            "- **Short-term memory**: the last few messages in `self.messages`\n"
            "- **Long-term memory**: a running bullet-list summary of completed steps\n\n"
            "Use them both to self-correct.  When you are done or reach 10 tool calls, emit no more JSON and instead produce your final detailed summary of data flow, control flow, inputs/outputs, and test-case guidance."
        )
        return "\n".join(lines)

    async def request_llm(self,
                          messages: List[Dict[str, str]],
                          max_tokens: int = 1000) -> Dict[str, Any]:
        """Send an OpenAI-compatible chat request to your private LLM."""
        
        response = self.llm.create_chat_completion(
                        messages = messages,
                    )

        return response

    async def _summarize_memory(self) -> str:
        """Ask the LLM to bullet-summarize the conversation so far."""
        prompt = (
            "Summarize the following conversation into up to 5 bullet points, each describing a completed step:\n\n"
            + "\n".join(f"{m['role'].upper()}: {m['content']}" for m in self.messages)
        )
        summary_resp = await self.request_llm([
            {"role": "system", "content": "You are a concise summarizer."},
            {"role": "user",   "content": prompt}
        ], max_tokens=300)
        return summary_resp["choices"][0]["message"]["content"]

    async def analyze_code(self, query: str) -> str:
        """
        Main dynamic loop:
          • inject system + initial user prompt
          • loop: call LLM, parse JSON tool_call → call tool → feed result → repeat
          • track & prune memory, stop at 10 tool calls or when LLM emits no JSON
          • finally solicit a detailed summary
        """
        # reset memory & counters
        self.messages = []
        self.long_term_memory = ""
        self.step_counter = 0

        system_prompt = self._build_system_prompt()
        self.messages.append({"role": "system", "content": system_prompt})
        # seed long-term memory as an empty system message
        self.messages.append({"role": "system", "content": "LONG_TERM_MEMORY: (none yet)"})
        self.messages.append({
            "role": "user",
            "content": f"I want to deeply analyze the code for `{query}`.  Begin whenever you're ready."
        })

        while True:
            # prune & summarize if history too long
            if len(self.messages) > self.history_limit:
                summary = await self._summarize_memory()
                self.long_term_memory += "\n" + summary
                recent = self.messages[-self.history_trim_size:]
                self.messages = [
                    {"role": "system", "content": system_prompt},
                    {"role": "system", "content": "LONG_TERM_MEMORY:" + self.long_term_memory}
                ] + recent

            # get next LLM turn
            llm_out = await self.request_llm(self.messages)
            content = llm_out['choices'][0]['message']['content'].strip()

            # try parsing JSON tool_call
            try:
                payload = json.loads(content)
                tc = payload["tool_call"]
                name = tc["tool_name"]
                params = tc["parameters"]
            except (json.JSONDecodeError, KeyError, TypeError):
                # no valid JSON → assume reasoning or final summary
                self.messages.append({"role": "assistant", "content": content})
                # if we've hit the tool cap, ask final summary
                if self.step_counter >= self.max_steps or not content.startswith("{"):
                    self.messages.append({
                        "role": "user",
                        "content": "Tool-call limit reached or no more JSON. Please provide your final detailed summary."
                    })
                    final = await self.request_llm(self.messages)
                    return final['choices'][0]['message']['content']
                # else continue hoping for JSON next turn
                continue

            # we got a tool call
            self.step_counter += 1
            if self.step_counter > self.max_steps:
                # backstop
                self.messages.append({
                    "role": "assistant",
                    "content": f"🔔 Reached max tool calls ({self.max_steps})."
                })
                self.messages.append({
                    "role": "user",
                    "content": "Please provide your final detailed summary."
                })
                final = await self.request_llm(self.messages)
                return final["choices"][0]["message"]["content"]

            # execute the tool
            tool_resp = await self.session.call_tool(name, params)
            self.messages.append({
                "role": "assistant",
                "content": f"[tool {name} →]\n{tool_resp.content}"
            })
            # loop for the LLM to consume that result

    async def close(self):
        await self.exit_stack.aclose()


async def main():
    if len(sys.argv) != 2:
        print("Usage: python client.py <path_to_graphrag_server>")
        sys.exit(1)

    client = CodeRAGClient(sys.argv[1])
    try:
        await client.connect()
        while True:
            q = input("\nEnter function or patch (or 'quit'): ").strip()
            if q.lower() == "quit":
                break
            summary = await client.analyze_code(q)
            print("\n=== FINAL SUMMARY ===\n")
            print(summary)
    finally:
        await client.close()

if __name__ == "__main__":
    asyncio.run(main())
