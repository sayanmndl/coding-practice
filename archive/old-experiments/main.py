import sys
import argparse
import asyncio
import os
from enum import Enum, auto
from typing import Literal

# Import Rich components from the standard library, not the one vendored by pip
try:
    import rich
    from rich.console import Console
    from rich.panel import Panel
    from rich.text import Text
    from rich.box import ROUNDED
    from rich.style import Style
except ImportError:
    rich = None # Sentinel for rich library

# Try to import Textual, fail gracefully if not installed
try:
    from textual.app import App, ComposeResult
    from textual.binding import Binding
    from textual.containers import Vertical, Horizontal, ScrollableContainer
    from textual.reactive import reactive
    from textual.screen import Screen
    from textual.widgets import (
        Button, Footer, Header, Input, RichLog, Static, Label, ProgressBar
    )
    from textual.worker import Worker
    from textual.timer import Timer
except ImportError:
    App = None # Sentinel to indicate Textual is not available

# This function remains unchanged for the static demo fallback
def draw_ui(placeholder: str = 'Try "edit CardModal.jsx to..."'):
    if rich is None:
        print("Rich library not found. Cannot draw static UI.")
        return
    console = Console()
    header_text = Text()
    header_text.append('🐋 ', style='bold blue')
    header_text.append('ORCA: ', style='bold')
    header_text.append('Orchestrating Agents', style='bold')
    header_panel = Panel(header_text, border_style='red', padding=(0, 1), box=ROUNDED)

    input_text = Text()
    input_text.append('> ', style='bold')
    if placeholder:
        input_text.append(placeholder, style='dim italic')
    input_panel = Panel(input_text, border_style='grey50', padding=(0, 1), box=ROUNDED)
    shortcuts_text = Text('Ctrl-H for help', style='grey50')

    console.print(header_panel)
    console.print()
    console.print(input_panel)
    console.print()
    console.print(shortcuts_text)


def debug_print(*args, **kwargs):
    # This will be replaced with a real debug_print function if --debug is used
    pass

# --- Textual Implementation ---
# Only define these classes if the Textual import was successful
if App is not None and rich is not None:

    class ConfigScreen(Screen[dict | None]):
        """Screen for initial app configuration, keyboard-driven."""
        
        # UI State
        selected_row = reactive(0)
        selected_col = reactive(0) # 0: row nav, 1-N: options in row
        config_file_path = reactive("")

        # Configuration Data
        TEMPLATES = ["solo (general agent)", "duo (research + execute)", "team (plan research execute)"]
        LLMS = {
            "Anthropic": ["Sonnet-4", "Opus-4"],
            "OpenAI": ["GPT-4o-mini", "GPT-5"],
            "Google": ["Gemini-2.5-Flash", "Gemini-2.5-Pro"]
        }
        
        template_choice = reactive(0)
        llm_vendor_choice = reactive(0)
        llm_model_choices = reactive({vendor: 0 for vendor in LLMS})
        
        project_path = reactive(os.getcwd())
        tools = reactive({'FS': True, 'RAG': True, 'HITL': True, 'Term': False})
        max_iters = reactive(30)

        BINDINGS = [
            Binding("up", "navigate_or_toggle('up')", "Up", show=False, priority=True),
            Binding("down", "navigate_or_toggle('down')", "Down", show=False, priority=True),
            Binding("left", "navigate_left", "Navigate Left", show=False),
            Binding("right", "navigate_right", "Navigate Right", show=False),
            Binding("enter", "submit", "Submit", show=False),
            Binding("escape", "cancel", "Cancel", show=False),
        ]
        
        @property
        def is_custom_config_active(self) -> bool:
            """Check if the config file input has text."""
            return bool(self.config_file_path)

        def compose(self) -> ComposeResult:
            """
            Creates the UI for the configuration screen.
            NOTE: The layout here is simplified by removing a redundant Vertical container
            to ensure the ScrollableContainer behaves correctly.
            """
            header_panel = self.app.get_header(style_override="bold white")
            with ScrollableContainer(id="config_scroll"):
                yield Static(header_panel, id="config_header")
                with Vertical(id="config_options"):
                    # Config file row
                    with Horizontal(classes="config-row", id="row_0"):
                        yield Static("Agent Config File:", classes="config-label")
                        yield Input(placeholder="path/to/config.yaml", id="config_file_input", classes="config-input")
                    
                    yield Static("[dim]OR[/dim]", id="or_separator")
                    
                    # Template row
                    with Horizontal(classes="config-row", id="row_1"):
                        yield Static("Template:", classes="config-label")
                        yield Static(id="template_value", classes="config-value")
                    
                    # LLM row
                    with Horizontal(classes="config-row", id="row_2"):
                        yield Static("LLM:", classes="config-label")
                        yield Static(id="llm_value", classes="config-value")
                    
                    # Tools row
                    with Horizontal(classes="config-row", id="row_3"):
                        yield Static("Tools & Settings:", classes="config-label")
                        yield Static(id="tools_value", classes="config-value")
                    
                    # Project path row
                    with Horizontal(classes="config-row", id="row_4"):
                        yield Static("Project Path:", classes="config-label")
                        yield Input(value=self.project_path, id="project_path_input", classes="config-input")

                yield Static("Use arrows to navigate & change, Enter to continue", classes="footer-help")

        def on_mount(self) -> None:
            """Initial render of the options."""
            self.update_options_display()
            self.query_one("#config_file_input").focus()

        def on_input_changed(self, event: Input.Changed) -> None:
            """Called when the text in the input changes."""
            if event.input.id == "config_file_input":
                self.config_file_path = event.value
            elif event.input.id == "project_path_input":
                self.project_path = event.value
            self.update_options_display()

        def update_options_display(self) -> None:
            """Renders the configuration options based on the current state."""
            is_disabled = self.is_custom_config_active

            # --- Row Highlighting ---
            for i in range(5):
                try:
                    row = self.query_one(f"#row_{i}")
                    row.remove_class("selected-row")
                    if self.selected_row == i and self.selected_col == 0 and not (is_disabled and i != 0):
                        row.add_class("selected-row")
                except Exception:
                    pass
            
            # --- Template Value ---
            template_str = self.TEMPLATES[self.template_choice]
            if self.selected_row == 1 and self.selected_col > 0 and not is_disabled:
                template_str = f"[underline #e06c75]{template_str}[/]"
            elif is_disabled:
                template_str = f"[#5f7f87]{template_str}[/]"
            self.query_one("#template_value", Static).update(Text.from_markup(template_str))

            # --- LLM Value ---
            vendors = list(self.LLMS.keys())
            vendor_name = vendors[self.llm_vendor_choice]
            models = self.LLMS[vendor_name]
            model_name = models[self.llm_model_choices[vendor_name]]
            
            vendor_display = vendor_name
            model_display = model_name
            
            if self.selected_row == 2 and not is_disabled:
                if self.selected_col == 1:
                    vendor_display = f"[underline #e06c75]{vendor_display}[/]"
                elif self.selected_col == 2:
                    model_display = f"[underline #e06c75]{model_display}[/]"
            
            if is_disabled:
                llm_str = f"[#5f7f87]{vendor_display} / {model_display}[/]"
            else:
                llm_str = f"{vendor_display} / {model_display}"
            
            self.query_one("#llm_value", Static).update(Text.from_markup(llm_str))

            # --- Tools Value ---
            tools_parts = []
            for i, (name, enabled) in enumerate(self.tools.items()):
                symbol = "✓" if enabled else "✕"
                tool_str = f"{name}{symbol}"
                if self.selected_row == 3 and self.selected_col == (i + 1) and not is_disabled:
                    tool_str = f"[underline #e06c75]{tool_str}[/]"
                tools_parts.append(tool_str)
            
            max_iters_str = f"{self.max_iters}"
            if self.selected_row == 3 and self.selected_col == 5 and not is_disabled:
                max_iters_str = f"[underline #e06c75]{max_iters_str}[/]"

            tools_display = "  ".join(tools_parts) + f"     Max Iters: {max_iters_str}"
            if is_disabled:
                tools_display = f"[#5f7f87]{tools_display}[/]"
            
            self.query_one("#tools_value", Static).update(Text.from_markup(tools_display))

            # --- Input Focus and Style ---
            config_input = self.query_one("#config_file_input")
            path_input = self.query_one("#project_path_input")

            # Reset styles
            config_input.remove_class("focused-input")
            path_input.remove_class("focused-input")

            # Set focus and highlight active input
            focused_input = None
            if self.selected_row == 0:
                focused_input = config_input
            elif self.selected_row == 4:
                focused_input = path_input
            
            if focused_input:
                if not focused_input.has_focus:
                    focused_input.focus()
                focused_input.add_class("focused-input")
            else:
                if config_input.has_focus or path_input.has_focus:
                    self.screen.set_focus(None)

        def watch_selected_row(self, old_row: int, new_row: int) -> None:
            """
            Called when the selected_row reactive attribute changes.
            This method handles auto-scrolling to keep the selection visible.
            """
            # We use call_after_refresh to ensure the DOM is updated before we query it.
            self.call_after_refresh(self._scroll_to_selection)

        def _scroll_to_selection(self) -> None:
            """Scrolls the currently selected row into view."""
            try:
                row_widget = self.query_one(f"#row_{self.selected_row}")
                # Use Textual's built-in method to ensure the widget is visible.
                self.query_one("#config_scroll").scroll_to_widget(row_widget, animate=False)
                debug_print(f"Scrolled to widget: #row_{self.selected_row}")
            except Exception as e:
                debug_print(f"Failed to scroll to #row_{self.selected_row}: {e}")

        def action_navigate_or_toggle(self, direction: str) -> None:
            """Handles up/down key presses for navigation or toggling values."""
            if self.is_custom_config_active and self.selected_row != 0:
                 # If using a config file, only allow navigating up/down from non-config rows
                 # if the config file input is empty.
                 if self.config_file_path: return

            delta = -1 if direction == "up" else 1
            
            if self.selected_col > 0: # In edit mode
                if self.selected_row == 1: # Template
                    self.template_choice = (self.template_choice + delta) % len(self.TEMPLATES)
                elif self.selected_row == 2: # LLM
                    if self.selected_col == 1: # Vendor
                        self.llm_vendor_choice = (self.llm_vendor_choice + delta) % len(self.LLMS)
                    elif self.selected_col == 2: # Model
                        vendor = list(self.LLMS.keys())[self.llm_vendor_choice]
                        num_models = len(self.LLMS[vendor])
                        self.llm_model_choices[vendor] = (self.llm_model_choices[vendor] + delta) % num_models
                elif self.selected_row == 3: # Tools / Max Iters
                    if 1 <= self.selected_col <= 4: # Tools
                        tool_name = list(self.tools.keys())[self.selected_col - 1]
                        self.tools[tool_name] = not self.tools[tool_name]
                    elif self.selected_col == 5: # Max Iters
                        self.max_iters = max(1, self.max_iters + delta)

            else: # In row navigation mode
                self.selected_row = (self.selected_row + delta) % 5
            
            self.update_options_display()

        def action_navigate_left(self) -> None:
            """Handles left key press to move focus out of options."""
            if self.is_custom_config_active: return
            self.selected_col = max(0, self.selected_col - 1)
            self.update_options_display()

        def action_navigate_right(self) -> None:
            """Handles right key press to move focus into options."""
            if self.is_custom_config_active: return
            max_cols = 0
            if self.selected_row == 1: max_cols = 1
            elif self.selected_row == 2: max_cols = 2
            elif self.selected_row == 3: max_cols = 5
            
            if max_cols > 0:
                self.selected_col = min(max_cols, self.selected_col + 1)
            self.update_options_display()

        def action_submit(self) -> None:
            if self.is_custom_config_active:
                config = {"config_file": self.config_file_path}
            else:
                vendor = list(self.LLMS.keys())[self.llm_vendor_choice]
                model_idx = self.llm_model_choices[vendor]
                model = self.LLMS[vendor][model_idx]
                config = {
                    "template": self.TEMPLATES[self.template_choice],
                    "llm_vendor": vendor,
                    "llm_model": model,
                    "LLM": f"{vendor}/{model}", # For backward compatibility
                    "project_path": self.project_path,
                    "tools": self.tools,
                    "max_iters": self.max_iters,
                }
            self.dismiss(config)
        
        def action_cancel(self) -> None:
            self.dismiss(None)

    class OrcaApp(App):
        """An interactive TUI for Orchestrating Agents."""

        TITLE = "ORCA: Orchestrating Agents"
        SUB_TITLE = "Ctrl-H for help | Ctrl-O for options"

        CSS = """
        Screen {
            background: #012d36;
            color: #c0c0c0;
        }
        #header {
            height: auto;
            padding: 0 1;
        }
        #conversation_log {
            height: 1fr;
            border: blank;
            background: #334561;
            padding: 0 1;
        }
        #terminal_log {
            height: 30%;
            border: round #5f5f87;
            background: #012028;
            padding: 0 1;
            display: none;
        }
        #input_frame {
            height: 3;
            padding: 0 1;
            border: round #5f5f87;
        }
        #input_frame:focus-within {
            border: round #e5c07b;
        }
        Input {
            width: 1fr;
            border: none;
            background: transparent;
            padding: 0;
            margin: 0 1;
        }
        #input_prompt {
            width: auto;
            height: 1;
            padding-top: 1;
            color: #98c379;
        }
        Input.-placeholder {
            color: #5f7f87;
            text-style: italic;
        }
        Input:disabled {
            background: #013a48;
            color: #5f7f87;
        }
        .user-msg { color: #61afef; text-style: bold; }
        .system-msg { color: #98c379; }
        .agent-processing-msg { color: #828a93; } /* Light gray for processing */
        .agent-final-msg { color: #98c379; text-style: bold; } /* Bold green for final answer */
        .agent1-color { color: #56b6c2; } /* Cyan */
        .agent2-color { color: #c678dd; } /* Magenta */
        .agent3-color { color: #d19a66; } /* Yellow/Orange */
        .tool-msg { color: #e5c07b; } /* Orange for tool calls */

        /* Config Screen */
        #config_scroll {
            width: 100%;
            height: 100%;
            padding: 1;
            overflow-y: auto;
            align: center top;
        }
        #config_header {
            width: 100%;
            margin-bottom: 1;
            text-align: center;
        }
        #config_options { 
            width: 90%;
            max-width: 80;
            min-width: 60;
            padding: 1;
            height: auto;
        }
        .config-row {
            height: 3;
            width: 100%;
            align: left middle;
            margin-bottom: 0;
        }
        .config-label {
            width: 18;
            height: 3;
            margin: 0;
            text-align: right;
            margin-right: 2;
            content-align: right middle;
        }
        .config-input {
            width: 1fr;
            height: 3;
            border: round #5f5f87;
            margin: 0;
        }
        .config-input.focused-input {
            border: round #e06c75;
        }
        .config-value {
            width: 1fr;
            height: 3;
            margin: 0;
            content-align: left middle;
        }
        #or_separator { 
            text-align: center; 
            height: 1;
            margin: 1 0;
        }
        .footer-help { 
            color: #5f7f87; 
            text-style: italic; 
            margin-top: 1;
            text-align: center;
        }
        .selected-row {
            background: #013a48;
        }
        
        #progress_bar {
            display: none;
            height: 1;
            padding: 0 1;
        }
        #options_bar {
            display: none;
            width: 100%;
            height: 1;
            text-align: center;
            color: #5f7f87;
            text-style: italic;
            padding: 0 1;
        }
        """

        BINDINGS = [
            Binding("ctrl+c", "quit", "Quit", show=True, priority=True),
            Binding("escape", "cancel_agent_or_focus", "Cancel/Defocus", show=False),
            Binding("ctrl+h", "show_help", "Help", show=False),
            Binding("ctrl+o", "toggle_config", "Config", show=True),
            Binding("ctrl+t", "toggle_terminal", "Terminal", show=True),
        ]

        show_options_bar = reactive(False)
        selected_option_bar = reactive(0)
        current_agent_index = reactive(0)
        show_terminal = reactive(False)
        agent_mode = reactive(False)

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.config: dict | None = None
            self.agent_names = ['orca']
            self.agent_colors = ['agent1-color', 'agent2-color', 'agent3-color']
            self.agent_worker: Worker | None = None
            self.options_bar = Static(id="options_bar")

        def get_header(self, style_override: str = "bold") -> Panel:
            header_text = Text()
            header_text.append('🐋 ', style='bold blue')
            header_text.append('ORCA: ', style=style_override)
            header_text.append('Orchestrating Agents', style=style_override)
            
            if self.config and self.config.get("Multi‑agent"):
                agent_name = self.agent_names[self.current_agent_index]
                header_text.append(f" (Talking to: {agent_name})", style="dim")

            return Panel(header_text, border_style='red', padding=(0, 1), box=ROUNDED)

        def compose(self) -> ComposeResult:
            yield Static(id="header")
            yield RichLog(id="conversation_log", wrap=True, highlight=True, markup=True, auto_scroll=True)
            yield RichLog(id="terminal_log", wrap=True, highlight=True, markup=True, auto_scroll=True)
            yield ProgressBar(id="progress_bar", total=None)
            with Horizontal(id="input_frame"):
                yield Static("$ ", id="input_prompt")
                yield Input(placeholder='Enter a command or @ to talk to an agent')
            yield self.options_bar
            yield Footer()

        def on_mount(self) -> None:
            self.query_one("#header", Static).update(self.get_header())
            self.push_screen(ConfigScreen(), self.set_config)
            self.query_one(Input).focus()

        def set_config(self, config: dict | None) -> None:
            if config is None:
                self.exit()
                return
            self.config = config
            if self.config.get("Multi‑agent"):
                self.agent_names = ['agent1', 'agent2', 'agent3']
            self.query_one(Input).focus()
            self.update_header()

        def watch_show_terminal(self, show: bool) -> None:
            self.query_one("#terminal_log").styles.display = "block" if show else "none"

        def watch_agent_mode(self, agent_mode: bool) -> None:
            self.query_one("#input_prompt").update("> " if agent_mode else "$ ")

        def update_header(self) -> None:
            self.query_one("#header", Static).update(self.get_header())

        async def on_input_changed(self, event: Input.Changed) -> None:
            if event.value.startswith('@'):
                self.agent_mode = True
            else:
                self.agent_mode = False

        async def on_key(self, event) -> None:
            if event.key == "tab" and self.query_one(Input).value.startswith('@'):
                event.prevent_default()
                # Simple tab completion for the first agent
                self.query_one(Input).value = f"@{self.agent_names[0]} "
                self.query_one(Input).cursor_position = len(self.query_one(Input).value)

        async def on_input_submitted(self, event: Input.Submitted) -> None:
            user_text = event.value.strip()
            if not user_text:
                return

            if self.agent_mode:
                if self.agent_worker:
                    return
                log = self.query_one("#conversation_log")
                log.write(f"👤 [b #61afef]User:[/] {user_text}")
                event.input.clear()
                self.agent_worker = self.run_worker(self.agent_loop(user_text), exclusive=True)
            else:
                # Terminal mode
                terminal_log = self.query_one("#terminal_log")
                terminal_log.write(f"$ {user_text}")
                # Simulate a command
                await self.run_command(user_text)
                event.input.clear()

        async def run_command(self, command: str):
            """Simulates running a terminal command."""
            terminal_log = self.query_one("#terminal_log")
            try:
                proc = await asyncio.create_subprocess_shell(
                    command,
                    stdout=asyncio.subprocess.PIPE,
                    stderr=asyncio.subprocess.PIPE)

                stdout, stderr = await proc.communicate()

                if stdout:
                    terminal_log.write(stdout.decode())
                if stderr:
                    terminal_log.write(f"[red]{stderr.decode()}[/red]")
            except Exception as e:
                terminal_log.write(f"[red]Error: {e}[/red]")

        async def agent_loop(self, command: str) -> None:
            self.query_one(Input).disabled = True
            progress_bar = self.query_one(ProgressBar)
            progress_bar.styles.display = "block"
            log = self.query_one("#conversation_log")
            try:
                agent_name = self.agent_names[self.current_agent_index]
                agent_color = self.agent_colors[self.current_agent_index]

                def agent_log(message: str, message_style: str, is_final: bool = False):
                    orca_style = "agent-final-msg" if is_final else "agent-processing-msg"
                    # Special case for tool calls to keep the whole prefix orange
                    if message_style == "tool-msg":
                        log.write(f"[{agent_color}]🐋 ORCA - {agent_name}:[/] [{message_style}]{message}[/]")
                    else:
                        log.write(f"[{orca_style}]🐋 ORCA[/][{agent_color}] - {agent_name}:[/] [{message_style}]{message}[/]")

                agent_log("Hello, let me check that for you…", "agent-processing-msg")
                await asyncio.sleep(1.5)
                
                agent_log("Tool call: processing " + command, "tool-msg")
                await asyncio.sleep(1.5)

                agent_log("Results found", "agent-final-msg", is_final=True)
                await asyncio.sleep(1.0)

                agent_log("Here are the details you requested.", "agent-final-msg", is_final=True)

            except asyncio.CancelledError:
                log.write(" Agent loop cancelled.", "system-msg")
            finally:
                progress_bar.styles.display = "none"
                self.query_one(Input).disabled = False
                self.query_one(Input).focus()
                self.agent_worker = None

        def action_quit(self) -> None:
            self.exit()

        def action_cancel_agent_or_focus(self) -> None:
            """Handle Escape key. Cancels agent or removes focus from input."""
            if self.agent_worker:
                self.agent_worker.cancel()
            elif self.focused and isinstance(self.focused, Input):
                self.screen.set_focus(None)

        def action_toggle_config(self) -> None:
            self.show_options_bar = not self.show_options_bar

        def action_toggle_terminal(self) -> None:
            self.show_terminal = not self.show_terminal
        
        def on_key(self, event) -> None:
            if self.show_options_bar:
                num_options = 3 if self.config.get("Multi‑agent") else 1
                
                if event.key in ("up", "down"):
                    if event.key == "up":
                        self.selected_option_bar = (self.selected_option_bar - 1) % num_options
                    else:
                        self.selected_option_bar = (self.selected_option_bar + 1) % num_options
                    self.update_options_bar_content()
                    event.stop()
                elif event.key in ("left", "right"):
                    if self.selected_option_bar == 0: # LLM
                        self.config['LLM'] = "GPT-4" if self.config['LLM'] == "GPT-3.5" else "GPT-3.5"
                    elif self.selected_option_bar == 1: # Multi-agent
                        self.config['Multi‑agent'] = not self.config['Multi‑agent']
                        if self.config['Multi‑agent']:
                            self.agent_names = ['agent1', 'agent2', 'agent3']
                        else:
                            self.agent_names = ['agent1']
                            self.current_agent_index = 0
                        self.update_header()
                    elif self.selected_option_bar == 2: # Active Agent
                        if event.key == "right":
                            self.current_agent_index = (self.current_agent_index + 1) % len(self.agent_names)
                        else:
                            self.current_agent_index = (self.current_agent_index - 1) % len(self.agent_names)
                    
                    self.update_options_bar_content()
                    event.stop()
                elif event.key == "enter":
                    self.show_options_bar = False
                    event.stop()

        def action_show_help(self) -> None:
            help_text = (
                'Hotkeys:\n'
                '  [b]Ctrl-C:[/] Exit\n'
                '  [b]Ctrl-H:[/] Show this help\n'
                '  [b]Ctrl-O:[/] Toggle config options bar\n'
                '  [b]Esc:[/] Cancel agent action or defocus input'
            )
            self.query_one(RichLog).write(help_text, style="system-msg")


def interactive_mode():
    if App is None:
        Console().print('Interactive mode requires the "textual" package to be installed.', style='bold red')
        return
    app = OrcaApp()
    app.run()
    if rich is not None:
        draw_ui()


def main():
    parser = argparse.ArgumentParser(description="ORCA Agent demo UI")
    parser.add_argument("--interactive", action="store_true", help="Run the interactive terminal UI instead of the static demo")
    parser.add_argument("--debug", action="store_true", help="Enable debug output")
    args = parser.parse_args()
    if args.interactive:
        try:
            if args.debug:
                # This is a simple way to enable debug printing to a file
                # so it doesn't interfere with the TUI.
                log_file = open("debug_orca.log", "w")
                def debug_print_func(*args, **kwargs):
                    print("[DEBUG]", *args, file=log_file, **kwargs)
                    log_file.flush()
                global debug_print
                debug_print = debug_print_func
            interactive_mode()
        except Exception as e:
            Console().print(f"[bold red]Interactive mode error:[/] {e}")
            if args.debug:
                import traceback
                traceback.print_exc()
            draw_ui()
    else:
        draw_ui()

if __name__ == "__main__":
    main()
