# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/2.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

- No unreleased changes yet.

## [0.2.0] - 2026-09-20

### Added

- A working Textual interface with the notes list and editor layout.
- A reusable `NoteResult` dataclass for UI and CRUD data transfer.
- Expanded note querying and retrieval helpers for the app's interface layer.
- Module-level documentation and NumPy-style docstrings throughout the package.

### Changed

- Updated the package version to `0.2.0`.
- Refined the project metadata and README to reflect the current app state.
- Kept the SQLAlchemy CRUD layer as the data source for the new interface.

### Fixed

- Standardized the SQLite database path to `sqlite:///notes.db`.
- Ensured the project entry point matches the current Textual app implementation.

## [0.1.0] - 2026-09-17

### Added

- SQLAlchemy database setup backed by SQLite.
- `Note` model with title, content, creation time, and auto-incrementing ID.
- CRUD operations for creating, reading, updating, and deleting notes.
- Search notes by title.
- Initial Textual dependency for the upcoming terminal interface.

[Unreleased]: https://github.com/python-neo/my-notes/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/python-neo/my-notes/releases/tag/v0.2.0
[0.1.0]: https://github.com/python-neo/my-notes/releases/tag/v0.1.0
