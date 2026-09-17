
from collections.abc import Generator
from contextlib import contextmanager

from sqlalchemy import select
from sqlalchemy.orm import Session

from .database import engine
from .models import Note


@contextmanager
def _get_session () -> Generator [Session, None, None] :
    """
    Create a database session context manager.

    Yields
    ------
    Session
        An SQLAlchemy database session.

    Raises
    ------
    Exception
        Re-raises any exception that occurs inside the context.
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
    """
    Delete a note from the database.

    Parameters
    ----------
    note_id : int
        The ID of the note to delete.
    """
    with _get_session () as session :
        note = session.get (Note, note_id)

        if note is not None :
            session.delete (note)


def get_all_notes () -> list [Note] :
    """
    Retrieve all notes from the database.

    Returns
    -------
    list[Note]
        A list containing all notes.
    """
    with _get_session () as session :
        statement = select (Note)
        notes = session.scalars (statement).all ()

        return [note for note in notes]


def get_note_by_id (note_id : int) -> Note | None :
    """
    Retrieve a note by its ID.

    Parameters
    ----------
    note_id : int
        The ID of the note to retrieve.

    Returns
    -------
    Note or None
        The matching note, or None if no note exists.
    """
    with _get_session () as session :
        note = session.get (Note, note_id)

        return note


def new_note (title : str, content : str) -> None :
    """
    Create a new note in the database.

    Parameters
    ----------
    title : str
        The title of the new note.
    content : str
        The Markdown content of the new note.
    """
    with _get_session () as session :
        session.add (
            Note (
                title = title,
                content = content,
            )
        )


def search_notes (query : str) -> list [Note] :
    """
    Search notes by title.

    Parameters
    ----------
    query : str
        The text to search for in note titles.

    Returns
    -------
    list[Note]
        A list of notes whose titles contain the query.
    """
    with _get_session () as session :
        statement = select (Note).where (
            Note.title.contains (query)
        )

        notes = session.scalars (statement).all ()

        return [note for note in notes]


def update_note (
    note_id : int,
    title : str | None,
    content : str | None,
) -> None :
    """
    Update an existing note.

    Parameters
    ----------
    note_id : int
        The ID of the note to update.
    title : str or None
        The new title. If None, the title is unchanged.
    content : str or None
        The new Markdown content. If None, the content is unchanged.
    """
    with _get_session () as session :
        note = session.get (Note, note_id)

        if note is None :
            return

        if title is not None :
            note.title = title

        if content is not None :
            note.content = content