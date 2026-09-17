# Contributing to my-notes

Thanks for taking an interest in `my-notes`.

## Development setup

The project requires Python 3.12 or newer and uses `uv` for dependency management:

```bash
uv sync --extra dev
```

## Checks

Before opening a pull request, run the linter and formatter check:

```bash
uv run ruff check .
uv run ruff format --check .
```

## Pull requests

- Keep changes focused and consistent with the existing code style.
- Add or update tests when changing CRUD behavior.
- Update the documentation or changelog when the user-facing behavior changes.
- Include a short summary of the change and the checks you ran.

## Development direction

The current implementation is a SQLAlchemy-backed CRUD layer. The next major piece is the Textual terminal interface, so UI changes should keep the database and CRUD layer separate from presentation concerns.
