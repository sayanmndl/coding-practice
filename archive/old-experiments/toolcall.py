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
N_GPU_LAYERS    = 0        # Number of GPU layers to offload (0 = CPU only)
SEED            = 42       # Random seed for reproducibility
USE_MMAP        = True     # Use memory-mapped model file
USE_MLOCK       = False    # Lock model into RAM (requires USE_MMAP=False)
LOW_VRAM        = False    # Reduce VRAM usage (trading compute for memory)
F16_KV          = True     # Use f16 key/value cache
LOGITS_ALL      = False    # Return logits for all tokens
EMBEDDING       = False    # Enable embedding mode

# Instantiate the Llama model with all options set explicitly
llm = Llama(
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

# -----------------------------
# Generation Parameters
# -----------------------------
MAX_TOKENS        = 256      # Maximum tokens to generate
TEMPERATURE       = 0.7      # Sampling temperature
TOP_K             = 50       # Top-K sampling
TOP_P             = 0.95     # Top-P (nucleus) sampling
REPEAT_PENALTY    = 1.1      # Repetition penalty
PRESENCE_PENALTY  = 0.0      # Presence penalty
FREQUENCY_PENALTY = 0.0      # Frequency penalty
STOP_SEQUENCES    = ["\n###"]  # One or more stop sequences
ECHO_INPUT        = False    # Whether to echo the prompt in the output
STREAM            = False    # Streaming output (set to True for callbacks)
LOGPROBS          = None     # Return log probabilities for top tokens

# -----------------------------
# Prepare your prompt
# -----------------------------
prompt_header = "Please summarize the following text:\n\n"
source_text   = (
    "LlamaCpp is a lightweight C++ implementation of the LLaMA model that..."
)
prompt = prompt_header + source_text

# -----------------------------
# Non-streaming Generation Example
# -----------------------------
result = llm.generate(
    prompt=prompt,
    max_tokens=MAX_TOKENS,
    temperature=TEMPERATURE,
    top_k=TOP_K,
    top_p=TOP_P,
    repeat_penalty=REPEAT_PENALTY,
    presence_penalty=PRESENCE_PENALTY,
    frequency_penalty=FREQUENCY_PENALTY,
    stop=STOP_SEQUENCES,
    echo=ECHO_INPUT,
    stream=STREAM,
    logprobs=LOGPROBS,
)
print(result.choices[0].text)

# -----------------------------
# Tool Call Scenario Example
# -----------------------------
def get_time() -> str:
    """
    Example tool: returns the current UTC time in ISO format.
    """
    return datetime.utcnow().isoformat()

def add_numbers(a: int, b: int) -> int:
    """
    Example tool: adds two integers.
    """
    return a + b

TOOLS = {
    "get_time": get_time,
    "add_numbers": add_numbers,
}

def handle_tool_call(response_text: str):
    try:
        payload = json.loads(response_text)
        if "tool_call" in payload:
            name = payload["tool_call"]["tool_name"]
            params = payload["tool_call"]["parameters"]
            fn = TOOLS.get(name)
            if fn:
                return fn(**params)
    except json.JSONDecodeError:
        pass
    return response_text

# Example usage
tool_prompt = (
    "You can call a tool by returning a JSON object. "
    "Generate a tool_call for adding 5 and 7."
)
response = llm.generate(prompt=tool_prompt, max_tokens=50, temperature=0.0, echo=True)
res_text = response.choices[0].text.strip()
print("LLM response:", res_text)
print("Tool result:", handle_tool_call(res_text))

# -----------------------------
# MCP Tool Call Scenario Example
# -----------------------------
def search_web(query: str) -> str:
    return f"[Simulated results for '{query}']"

TOOLS["search_web"] = search_web
mcp_prompt = (
    "Return an MCP tool_call JSON to search the web for 'llamacpp usage'."
)
mcp_resp = llm.generate(prompt=mcp_prompt, max_tokens=60, temperature=0.0, echo=True)
mcp_text = mcp_resp.choices[0].text.strip()
print("MCP response:", mcp_text)
print("MCP result:", handle_tool_call(mcp_text))

# -----------------------------
# MCP Server Script Example
# -----------------------------
# Save this as mcp_server.py and run with: uvicorn mcp_server:app --reload
from fastapi import FastAPI
from pydantic import BaseModel

class ToolCall(BaseModel):
    tool_name: str
    parameters: dict

app = FastAPI()

@app.post("/tool_call")
async def call_tool(call: ToolCall):
    if call.tool_name == "get_time":
        return {"result": get_time()}
    return {"error": f"Unknown tool: {call.tool_name}"}

# -----------------------------
# Client Usage of MCP Server
# -----------------------------
def remote_get_time() -> str:
    payload = {"tool_call": {"tool_name": "get_time", "parameters": {}}}
    resp = requests.post("http://localhost:8000/tool_call", json=payload["tool_call"])
    data = resp.json()
    return data.get("result")

TOOLS["remote_get_time"] = remote_get_time

# Example MCP client prompt
mcp_client_prompt = (
    "Return an MCP tool_call JSON to call get_time remotely."
)
client_resp = llm.generate(prompt=mcp_client_prompt, max_tokens=50, temperature=0.0, echo=True)
client_text = client_resp.choices[0].text.strip()
print("MCP client response:", client_text)
print("Remote get_time result:", handle_tool_call(client_text))


tool_prompt = (
    "You can call a tool by returning a JSON object. "
    "Generate a tool_call for adding 5 and 7."
)
response = llm.create_chat_completion(
      messages = [
        {
          "role": "system",
          "content": "A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user's questions. The assistant calls functions with appropriate input when necessary"

        },
        {
          "role": "user",
          "content": "Give me the sum of 107  and 254"
        }
      ],
      tools=[{
        "type": "function",
        "function": {
          "name": "add_numbers",
          "parameters": {
            "type": "object",
            "title": "add_numbers",
            "properties": {
              "a": {
                "title": "a",
                "type": "integer"
              },
              "b": {
                "title": "b",
                "type": "integer"
              }
            },
            "required": [ "a", "b" ]
          }
        }
      }],
      tool_choice={
        "type": "function",
        "function": {
          "name": "add_numbers"
        }
      }
)