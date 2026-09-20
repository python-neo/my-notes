"""SQLAlchemy model definitions for stored notes.

Notes
-----
Defines the ORM model used by the CRUD layer and the Textual UI.
"""

from datetime import datetime

from sqlalchemy import DateTime, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from .database import Base


class Note (Base) :
    """Representation of a saved note in the SQLite database.

    Attributes
    ----------
    note_id : int
        Auto-incrementing primary key for the note.
    title : str
        Short title for the note.
    content : str
        Body text of the note.
    created_at : datetime
        Timestamp for when the note was created.
    """
    __tablename__ = "notes"

    note_id : Mapped [int] = mapped_column (
        primary_key = True,
        autoincrement = True
    )

    title : Mapped [str] = mapped_column (
        String (256),
        nullable = False
    )

    content : Mapped [str] = mapped_column (
        Text,
        nullable = False
    )

    created_at : Mapped [datetime] = mapped_column (
        DateTime,
        default = datetime.now
    )