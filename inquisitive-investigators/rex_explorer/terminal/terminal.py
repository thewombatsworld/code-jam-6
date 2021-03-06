from typing import Any

from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import (
    ObjectProperty,
    StringProperty,
    NumericProperty,
    ColorProperty
)

from .dispatcher import Shell
from .termio import TerminalInput
from ..utils.paths import TERMINAL_KV, FONT

Builder.load_file(TERMINAL_KV)


class Terminal(BoxLayout, Shell):
    terminal_input = ObjectProperty()
    recycle_view = ObjectProperty()

    foreground_color = ColorProperty((1, 1, 1, 1))
    background_color = ColorProperty((0, 0, 0, 1))

    font_name = StringProperty(FONT)
    font_size = NumericProperty(11)

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(Terminal, self).__init__(*args, **kwargs)

    def on_output(self, output: bytes) -> None:
        self.terminal_input.on_output(output)

    def on_cwd_change(self, cwd: str) -> None:
        self.terminal_input.on_cwd_change(cwd)

    def on_complete(self) -> None:
        self.terminal_input.on_complete()
        self.terminal_input.focus = True
