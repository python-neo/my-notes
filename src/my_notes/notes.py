"""CRUD helpers for reading, creating, updating, and deleting notes.

Notes
-----
This module contains the database operations used by the Textual interface and
by external library consumers.
"""

from collections.abc import Generator
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import datetime

from sqlalchemy import select
from sqlalchemy.orm import Session

from .database import engine
from .models import Note


@dataclass (frozen = True, slots = True)
class NoteResult :
    """Lightweight note payload returned from query operations.

    Attributes
    ----------
    note_id : int
        Unique identifier for the note.
    title : str
        Title shown in the UI and search results.
    content : str
        Full note body.
    created_at : datetime
        Timestamp when the note was created.
    """
    note_id : int
    title : str
    content : str
    created_at : datetime

@contextmanager
def _get_session () -> Generator [Session, None, None] :
    """Create a SQLAlchemy session context manager.

    Yields
    ------
    Session
        Database session used for note data access.

    Raises
    ------
    Exception
        Re-raises any exception after rolling back the transaction.
    """
    session = Session (engine)

    try :
        yield session
        session.commit ()
    except :
        session.rollback ()
        raise
    finally :
        session.close ()


def delete_note (note_id : int) -> None :
    """Delete a note from the database.

    Parameters
    ----------
    note_id : int
        Identifier of the note to remove.
    """
    with _get_session () as session :
        note = session.get (Note, note_id)

        if note is not None :
            session.delete (note)


def get_all_notes () -> list [NoteResult] :
    """Return all stored notes as lightweight result objects.

    Returns
    -------
    list[NoteResult]
        Notes ordered by the database default sort order.
    """
    with _get_session () as session :
        statement = select (Note)
        notes = session.scalars (statement).all ()

        return [
            NoteResult (note.note_id, note.title, note.content, note.created_at)
            for note in notes
        ]


def get_note_by_id (note_id : int) -> Note | None :
    """Return a single note by its identifier.

    Parameters
    ----------
    note_id : int
        Identifier of the note to retrieve.

    Returns
    -------
    Note or None
        Matching note object, or ``None`` when no note exists.
    """
    with _get_session () as session :
        note = session.get (Note, note_id)

        return note


def new_note (title : str, content : str) -> None :
    """Create a new note in the database.

    Parameters
    ----------
    title : str
        Title for the new note.
    content : str
        Markdown or plain text content to store.
    """
    with _get_session () as session :
        session.add (
            Note (
                title = title,
                content = content,
            )
        )


def search_notes (query : str) -> list [NoteResult] :
    """Search notes by title.

    Parameters
    ----------
    query : str
        Text to match against note titles.

    Returns
    -------
    list[NoteResult]
        Notes whose titles contain the search string.
    """
    with _get_session () as session :
        statement = select (Note).where (
            Note.title.contains (query)
        )

        notes = session.scalars (statement).all ()

        return [
            NoteResult (note.note_id, note.title, note.content, note.created_at)
            for note in notes
        ]


def update_note (
    note_id : int,
    title : str | None,
    content : str | None,
) -> None :
    """Update an existing note.

    Parameters
    ----------
    note_id : int
        Identifier of the note to modify.
    title : str or None
        New title. If ``None``, the current title is preserved.
    content : str or None
        New content. If ``None``, the current content is preserved.
    """
    with _get_session () as session :
        note = session.get (Note, note_id)

        if note is None :
            return

        if title is not None :
            note.title = title

        if content is not None :
            note.content = content