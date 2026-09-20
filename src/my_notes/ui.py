"""Textual interface for the my-notes application.

Notes
-----
Defines the main application window and bootstraps the UI entry point.
"""

from datetime import datetime
from pathlib import Path
from typing import ClassVar

from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal
from textual.widgets import Static, TextArea

from .index import Index
from .notes import *

BASE_DIR = Path (__file__).parent

class Notes (App) :
    """Main Textual application for browsing and editing notes.

    Attributes
    ----------
    BINDINGS : list[Binding]
        Keyboard shortcuts available to the user.
    CSS_PATH : Path
        Stylesheet used to theme the interface.
    """
    BINDINGS : ClassVar = [
        Binding ("Ctrl+Q", "quit", "Quit the program", priority = True)
    ]
    CSS_PATH = BASE_DIR / "stylesheet.tcss"

    def on_mount (self) -> None :
        """Initialize the clock and refresh it when the app mounts."""
        self.set_interval (1, self.update_time)
        self.update_time ()

    def update_time (self) -> None :
        """Refresh the status bar clock with the current local time."""
        now = datetime.now ().astimezone ()
        timer = self.query_one ("#time", Static)
        timer.update (now.strftime ("  %H:%M"))

    def compose (self) -> ComposeResult :
        """Build the layout for the notes index and editor.

        Returns
        -------
        ComposeResult
            Textual widgets for the app shell.
        """
        with Horizontal (id = "main") :
            yield Index (id = "index", label = "Notes")
            yield TextArea (id = "editor")

        with Horizontal (id = "status_bar") :
            yield Static (id = "time")

def main () -> None :
    """Start the Textual notes application."""
    notes = Notes ()
    notes.run ()