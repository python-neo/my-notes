from datetime import datetime

from sqlalchemy import DateTime, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from .database import Base


class Note (Base) :
    __tablename__ = "Notes"

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