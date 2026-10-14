import sys
import argparse
import asyncio

# Use standard library imports, not vendored ones
import rich
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.box import ROUNDED

try:
    from prompt_toolkit.application import Application
    from prompt_toolkit.buffer import Buffer
    from prompt_toolkit.document import Document
    from prompt_toolkit.layout import Layout, HSplit, VSplit
    from prompt_toolkit.layout.containers import Window
    from prompt_toolkit.layout.controls import FormattedTextControl, BufferControl
    from prompt_toolkit.layout.processors import Processor, Transformation, ConditionalProcessor
    from prompt_toolkit.key_binding import KeyBindings
    from prompt_toolkit.styles import Style
    from prompt_toolkit.filters import Condition
    from prompt_toolkit.formatted_text import ANSI
    from prompt_toolkit.widgets import Frame
    from prompt_toolkit.layout.dimension import Dimension
    from prompt_toolkit.layout.margins import ScrollbarMargin
    from prompt_toolkit.application.current import get_app
except Exception:
    Application = None

def draw_ui(placeholder: str = 'Try "edit CardModal.jsx to..."'):
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

async def interactive_mode():
    if Application is None:
        Console().print('Interactive mode requires prompt_toolkit to be available.', style='bold red')
        return

    if not (sys.stdin.isatty() and sys.stdout.isatty()):
        Console().print('Interactive mode requires a terminal (TTY). Falling back to the static demo.', style='bold red')
        return

    async def configuration_stage() -> dict:
        config_items = [
            {'label': 'LLM', 'type': 'radio', 'options': ['GPT‑3.5', 'GPT‑4'], 'index': 0},
            {'label': 'Multi‑agent', 'type': 'toggle', 'value': False},
        ]
        selected = 0

        def build_config_fragments():
            fragments = []
            for i, item in enumerate(config_items):
                style_name = 'class:config.selected' if i == selected else 'class:config'
                if item['type'] == 'radio':
                    options = item.get('options', [])
                    index = item.get('index', 0)
                    value = options[index] if options and 0 <= index < len(options) else ''
                elif item['type'] == 'toggle':
                    value = 'Yes' if item.get('value', False) else 'No'
                else:
                    value = ''
                line = f"{item['label']}: "
                fragments.append((style_name, line))
                fragments.append((style_name, value))
                fragments.append(('', '\n'))
            return fragments

        config_control = FormattedTextControl(text=build_config_fragments)
        config_window = Window(content=config_control, wrap_lines=False, always_hide_cursor=True, style='class:config_window')

        header_text_cfg = Text()
        header_text_cfg.append('🐋 ', style='bold blue')
        header_text_cfg.append('ORCA: ', style='bold white')
        header_text_cfg.append('Orchestrating Agents', style='bold white')
        header_console = Console(record=True, width=80)
        header_console.print(Panel(header_text_cfg, border_style='red', padding=(0, 1), box=ROUNDED))
        rendered_header = header_console.export_text()
        header_control = FormattedTextControl(ANSI(rendered_header))
        header_window = Window(content=header_control, height=3, style='class:header_window')

        footer_control = FormattedTextControl([('class:config.footer', 'Use ↑/↓ to navigate, ←/→ to change values, Enter to continue, Esc to quit')])
        footer_window = Window(content=footer_control, height=1, dont_extend_height=True, style='class:footer_window')

        config_root = HSplit([header_window, config_window, footer_window], padding=1)
        kb_conf = KeyBindings()

        @kb_conf.add('up')
        def _up(event):
            nonlocal selected
            selected = (selected - 1) % len(config_items)
            event.app.invalidate()

        @kb_conf.add('down')
        def _down(event):
            nonlocal selected
            selected = (selected + 1) % len(config_items)
            event.app.invalidate()

        @kb_conf.add('left')
        @kb_conf.add('right')
        def _toggle(event):
            if 0 <= selected < len(config_items):
                item = config_items[selected]
                if item['type'] == 'radio':
                    options = item.get('options', [])
                    if options:
                        idx = item.get('index', 0)
                        item['index'] = (idx + (1 if event.key_sequence[0].key == 'right' else -1)) % len(options)
                elif item['type'] == 'toggle':
                    item['value'] = not item.get('value', False)
                event.app.invalidate()

        @kb_conf.add('enter')
        def _enter(event):
            event.app.exit(result=True)

        @kb_conf.add('escape')
        @kb_conf.add('c-c')
        def _abort(event):
            event.app.exit(result=False)

        config_style = Style.from_dict({
            'config_window': 'bg:#012d36 #c0c0c0',
            'config.selected': 'bold #e06c75',
            'config': '#c0c0c0',
            'footer_window': 'italic #5f7f87',
        })

        app = Application(layout=Layout(config_root), key_bindings=kb_conf, full_screen=True, style=config_style)
        result = await app.run_async()
        if not result:
            return None
        cfg = {}
        for item in config_items:
            key = item['label']
            if item['type'] == 'radio':
                options = item.get('options', [])
                index = item.get('index', 0)
                cfg[key] = options[index] if options and 0 <= index < len(options) else ''
            else:
                cfg[key] = item.get('value', False)
        return cfg

    config = await configuration_stage()
    if config is None:
        return

    llm_choice = config.get('LLM', 'GPT‑3.5')
    multi_agent = bool(config.get('Multi‑agent', False))

    agent_names = ['agent1']
    if multi_agent:
        agent_names.append('agent2')
    agent_colors = {'agent1': '#56b6c2', 'agent2': '#c678dd'}
    current_agent_index = 0

    agent_running = False
    cancel_agent = False
    show_config_options = False
    selected_config_option = 0

    conversation_data = []

    def build_conversation_fragments():
        fragments = []
        for style_class, message in conversation_data:
            fragments.append((f'class:{style_class}', message))
            fragments.append(('', '\n'))
        return fragments

    class FollowAutoScrollControl(FormattedTextControl):
        def __init__(self, *args, **kwargs):
            self.follow = True
            super().__init__(*args, **kwargs)

        def is_focusable(self) -> bool:
            return True

        def reset_follow(self) -> None:
            self.follow = True

        def mouse_handler(self, mouse_event):
            from prompt_toolkit.mouse_events import MouseEventType
            if mouse_event.event_type == MouseEventType.SCROLL_UP:
                self.follow = False
            return NotImplemented

    conversation_control = FollowAutoScrollControl(text=build_conversation_fragments)
    
    conversation_window = Window(
        content=conversation_control,
        wrap_lines=True,
        right_margins=[ScrollbarMargin(display_arrows=True)],
        height=Dimension(weight=1) 
    )

    def refresh_conversation():
        conversation_control.text = build_conversation_fragments
        if conversation_control.follow:
            conversation_window.vertical_scroll = 1000000
        try:
            get_app().invalidate()
        except Exception:
            pass

    input_buffer = Buffer()

    class PlaceholderProcessor(Processor):
        def __init__(self, placeholder: str, style: str = 'class:placeholder'):
            self.placeholder = placeholder
            self.style = style

        def apply_transformation(self, ti):
            if ti.document.text:
                return ti
            return Transformation([(self.style, self.placeholder)])

    placeholder_processor = ConditionalProcessor(
        PlaceholderProcessor('Try "edit CardModal.jsx to..."'),
        Condition(lambda: not input_buffer.text)
    )

    prompt_control = FormattedTextControl([('class:prompt', '> ')])
    prompt_window = Window(width=2, content=prompt_control)
    input_control = BufferControl(buffer=input_buffer, input_processors=[placeholder_processor], focusable=True, focus_on_click=True)
    input_window = Window(content=input_control)
    input_row = VSplit([prompt_window, input_window])
    input_frame = Frame(body=input_row, style='class:input_frame')

    header_text = Text()
    header_text.append('🐋 ', style='bold blue')
    header_text.append('ORCA: ', style='bold')
    header_text.append('Orchestrating Agents', style='bold')
    header_console = Console(record=True, width=80)
    header_console.print(Panel(header_text, border_style='red', padding=(0, 1), box=ROUNDED))
    rendered_header = header_console.export_text()
    header_control = FormattedTextControl(ANSI(rendered_header))
    header_window = Window(content=header_control, height=3)

    shortcuts_control = FormattedTextControl([('class:shortcuts', 'Ctrl-H for help | Ctrl-G to scroll to bottom')])
    shortcuts_window = Window(content=shortcuts_control, height=1)

    root_container = HSplit([
        header_window,
        Window(height=1, char='─', style='class:line'),
        conversation_window,
        Window(height=1, char='─', style='class:line'),
        input_frame,
        shortcuts_window
    ])
    layout = Layout(root_container, focused_element=input_window)

    style = Style.from_dict({
        '': 'bg:#012d36 #c0c0c0',
        'line': '#5f5f87',
        'user-msg': 'bold #61afef',
        'system-msg': '#98c379',
        'agent1-msg': agent_colors.get('agent1', '#56b6c2'),
        'agent2-msg': agent_colors.get('agent2', '#c678dd'),
        'tool-msg': 'bold #e5c07b',
        'input_disabled': 'bg:#013a48 #5f7f87',
        'prompt': '#e5c07b',
        'input_frame': 'border:#5f5f87',
        'placeholder': 'italic #5f7f87',
        'shortcuts': 'italic #5f7f87',
        'config.selected': 'bold #e06c75',
    })

    kb = KeyBindings()

    @kb.add('c-c')
    @kb.add('c-q')
    def _(event):
        event.app.exit()

    @kb.add('escape')
    def _(event):
        nonlocal cancel_agent
        if agent_running:
            cancel_agent = True

    @kb.add('c-o')
    def _(event):
        nonlocal show_config_options
        show_config_options = not show_config_options
        if show_config_options:
            update_config_bar()
        else:
            shortcuts_control.text = [('class:shortcuts', 'Ctrl-H for help | Ctrl-G to scroll to bottom')]
        event.app.invalidate()
    
    @kb.add('up', filter=Condition(lambda: show_config_options))
    @kb.add('down', filter=Condition(lambda: show_config_options))
    def _(event):
        nonlocal selected_config_option
        selected_config_option = (selected_config_option + 1) % 2
        update_config_bar()
        event.app.invalidate()

    @kb.add('left', filter=Condition(lambda: show_config_options))
    @kb.add('right', filter=Condition(lambda: show_config_options))
    def _(event):
        nonlocal llm_choice, multi_agent, agent_names, current_agent_index
        if selected_config_option == 0:
            llm_choice = 'GPT‑4' if llm_choice == 'GPT‑3.5' else 'GPT‑3.5'
        elif selected_config_option == 1:
            multi_agent = not multi_agent
            agent_names = ['agent1', 'agent2'] if multi_agent else ['agent1']
            current_agent_index = 0
        update_config_bar()
        event.app.invalidate()

    @kb.add('c-g')
    def _(event):
        conversation_control.reset_follow()
        refresh_conversation()

    async def wait_with_spinner(agent_name: str, duration: float):
        nonlocal cancel_agent
        frames = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
        spinner_message = f'🐋 ORCA - {agent_name}: processing…'
        conversation_data.append(('system-msg', f'{spinner_message} {frames[0]}'))
        refresh_conversation()

        start_time = asyncio.get_event_loop().time()
        frame_index = 0
        while asyncio.get_event_loop().time() - start_time < duration and not cancel_agent:
            await asyncio.sleep(0.1)
            frame_index += 1
            conversation_data[-1] = ('system-msg', f'{spinner_message} {frames[frame_index % len(frames)]}')
            refresh_conversation()
        
        if conversation_data and conversation_data[-1][1].startswith(spinner_message):
            conversation_data.pop()
        refresh_conversation()

    def update_config_bar():
        nonlocal selected_config_option
        llm_style = 'class:config.selected' if selected_config_option == 0 else 'class:shortcuts'
        multi_style = 'class:config.selected' if selected_config_option == 1 else 'class:shortcuts'
        llm_str = f'LLM: {llm_choice}'
        multi_str = f'Multi‑agent: {"Yes" if multi_agent else "No"}'
        
        shortcuts_control.text = [
            (llm_style, llm_str),
            ('class:shortcuts', ' | '),
            (multi_style, multi_str)
        ]

    @kb.add('c-h')
    def _(event):
        conversation_data.append((
            'system-msg',
            'Hotkeys:\n'
            '  Ctrl-C / Ctrl-Q: Exit\n'
            '  Ctrl-H: Show this help\n'
            '  Ctrl-O: Toggle config options\n'
            '  Ctrl-G: Scroll to latest message\n'
            '  Esc: Cancel current agent'
        ))
        refresh_conversation()

    @kb.add('enter')
    async def _(event):
        nonlocal agent_running, cancel_agent
        if agent_running:
            return
        user_text = input_buffer.text.strip()
        if not user_text:
            return
            
        conversation_control.reset_follow()
        conversation_data.append(('user-msg', f'👤 User: {user_text}'))
        input_buffer.reset()
        refresh_conversation()

        agent_running = True
        cancel_agent = False
        input_row.style = 'class:input_disabled'
        
        await agent_loop(user_text)

        agent_running = False
        cancel_agent = False
        input_row.style = ''
        refresh_conversation()

    async def agent_loop(command: str):
        nonlocal current_agent_index
        agent_name = agent_names[current_agent_index]
        agent_style = f'{agent_name}-msg'
        if multi_agent:
            current_agent_index = (current_agent_index + 1) % len(agent_names)

        steps = [
            (f'🐋 ORCA - {agent_name}: Thinking...', agent_style, 1.0),
            (f'🐋 ORCA - {agent_name} - 🛠️ Tool call: processing {command}', 'tool-msg', 1.5),
            (f'🐋 ORCA - {agent_name}: Compiling results...', agent_style, 1.0),
            (f'🐋 ORCA - {agent_name}: Here are the details you requested.', agent_style, 0),
        ]

        for message, style, duration in steps:
            if cancel_agent:
                conversation_data.append(('system-msg', 'Agent loop cancelled by user.'))
                refresh_conversation()
                return
            conversation_data.append((style, message))
            refresh_conversation()
            if duration > 0:
                await wait_with_spinner(agent_name, duration)

    application = Application(
        layout=layout,
        key_bindings=kb,
        full_screen=True,
        style=style,
        mouse_support=True
    )
    await application.run_async()

def main():
    parser = argparse.ArgumentParser(description="ORCA Agent TUI")
    parser.add_argument("--interactive", action="store_true", help="Run the interactive terminal UI")
    parser.add_argument("--debug", action="store_true", help="Enable debug output to stderr")
    args = parser.parse_args()
    
    global debug_print
    if args.debug:
        def real_debug_print(*args, **kwargs):
            print("[DEBUG]", *args, file=sys.stderr, **kwargs)
        debug_print = real_debug_print
    else:
        debug_print = lambda *a, **k: None

    if args.interactive:
        try:
            asyncio.run(interactive_mode())
        except Exception as e:
            Console().print(f"[bold red]Interactive mode error:[/] {e}")
            if args.debug:
                import traceback
                traceback.print_exc()
    else:
        draw_ui()

if __name__ == "__main__":
    main()