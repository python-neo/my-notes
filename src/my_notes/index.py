"""Tree widget used to list notes in the Textual interface.

Notes
-----
Provides the sidebar tree that shows available notes and their identifiers.
"""

from textual.widgets import Tree

from .notes import *


class Index (Tree) :
    """Sidebar tree that lists available note titles.

    Parameters
    ----------
    id : str
        Identifier for the widget.
    label : str
        Label displayed in the root node.
    """
    def __init__ (self, id : str, label : str) -> None :
        super ().__init__ (label = label, id = id)

    def on_mount (self) :
        """Populate the tree when the widget is attached to the app."""
        self.populate_tree ()
        super ().on_mount ()

    def populate_tree (self) -> None :
        """Refresh the list of notes shown in the sidebar."""
        self.root.remove_children ()
        notes = get_all_notes ()

        for note in notes :
            self.root.add_leaf (
                label = note.title,
                data = note.note_id
            )

        self.root.expand ()