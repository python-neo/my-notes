# my-notes

`my-notes` is a small Python notes app built around SQLAlchemy and a Textual
terminal interface. The package now includes both the database-backed CRUD layer
and a working notebook-style UI for viewing and editing notes.

## Current status

- SQLAlchemy-backed SQLite database and schema setup
- Create, read, update, and delete operations for notes
- Title-based note search
- Textual app with a note index and editor panel
- Project entry point wired to the UI (`my-notes` -> `my_notes.ui:main`)

The app is now usable as both a Python library and a terminal interface. The
main data access layer remains in `my_notes.notes`, while the UI lives in
`my_notes.ui` and `my_notes.index`.

## Requirements

- Python 3.12 or newer
- [uv](https://docs.astral.sh/uv/) recommended for environment and dependency management

## Installation

Clone the repository and install the project with its development dependencies:

```bash
uv sync --extra dev
```

To activate the environment manually:

```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS/Linux
source .venv/bin/activate
```

## Usage

The CRUD functions are available from `my_notes.notes`:

```python
from my_notes.notes import (
    delete_note,
    get_all_notes,
    get_note_by_id,
    new_note,
    search_notes,
    update_note,
)

new_note("Shopping list", "- Coffee\n- Bread")

notes = get_all_notes()
shopping_notes = search_notes("Shopping")

note = get_note_by_id(1)
if note is not None:
    print(note.title, note.content)

update_note(1, title="Updated shopping list", content=None)
delete_note(1)
```

The database is created automatically as `notes.db` in the working directory.

## Data model

Each note contains:

| Field | Type | Description |
| --- | --- | --- |
| `note_id` | integer | Auto-incrementing primary key |
| `title` | string | Required title, up to 256 characters |
| `content` | text | Required note content |
| `created_at` | datetime | Set when the note is created |

## Project layout

```text
src/my_notes/
├── database.py  # SQLAlchemy engine and declarative base
├── models.py    # Note model
└── notes.py     # CRUD and title-search operations
```

## Development

Run the formatter and linter with:

```bash
uv run ruff check .
uv run ruff format --check .
```

## Documentation

- [Contributing](contributing.md)
- [Changelog](changelog.md)

## Roadmap

- Build the Textual terminal interface
- Connect note creation, editing, searching, and deletion to the interface
- Add automated tests for the database and CRUD layer
- Add configurable database location
