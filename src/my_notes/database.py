"""Database configuration and initialization for the project.

Notes
-----
This module defines the shared SQLAlchemy declarative base and the SQLite
engine used elsewhere in the app.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase


class Base (DeclarativeBase) : 
    """Declarative base for all ORM models.

    Attributes
    ----------
    metadata : sqlalchemy.MetaData
        SQLAlchemy metadata registry for mapped models.
    """

engine = create_engine ("sqlite:///notes.db")

from .models import Note # noqa: I001, F401

Base.metadata.create_all (engine)