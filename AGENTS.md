# InquirerPrompt — Agent Guidelines

## Project Overview

This is a community-maintained fork of [kazhala/InquirerPy](https://github.com/kazhala/InquirerPy),
published on PyPI as **InquirerPrompt**. The fork keeps the library healthy with bug fixes,
compatibility updates, and feature contributions that upstream hasn't merged.

- **Upstream:** `kazhala/InquirerPy` (branch `master`)
- **Fork main:** `main` (stable, tagged releases)
- **Fork dev:** `dev` (integration branch — all feature branches merge here first)
- **PyPI package:** `InquirerPrompt` (import name stays `InquirerPy`)

## Branch Model

```
upstream/master → main (stable releases)
                   └── dev (integration)
                        ├── feat/*     (new features)
                        ├── fix/*      (bug fixes)
                        └── chore/*    (maintenance)
```

- Feature/fix branches branch off `dev` and merge back into `dev`.
- `dev` merges into `main` for releases.
- `main` always matches the latest tagged release.

## Self-Contained Branches

**Every branch must be self-contained** — all related changes go on the same branch:

- **Code changes** — the feature/fix implementation
- **Tests** — unit tests for the new behavior
- **Documentation** — README sections, docstrings, examples
- **Changelog** — if applicable

Do **not** split a feature across multiple branches. Do **not** commit documentation
for a feature to `dev` or `main` separately — add it on the feature branch so the
branch tells the complete story.

When merging a branch into `dev`, all its documentation comes with it automatically.

## Development

### Setup

```bash
git clone https://github.com/tobiashochguertel/InquirerPrompt.git
cd InquirerPrompt
git remote add upstream https://github.com/kazhala/InquirerPy.git
uv sync
```

### Running Tests

```bash
uv run pytest tests/ -q
```

Note: Some tests require a TTY and may fail in CI environments due to
`prompt_toolkit`'s `create_pipe_input()` behavior. This is a pre-existing
issue, not caused by changes.

### Creating a Feature Branch

```bash
git checkout dev
git checkout -b feat/my-feature
# implement, test, document
git push origin feat/my-feature
```

### Upstream Sync

```bash
git fetch upstream
git checkout main
git merge upstream/master
git push origin main
# then merge main into dev
git checkout dev
git merge main
git push origin dev
```

## Code Style

- Python 3.9+ (type hints required)
- Follow existing patterns in `InquirerPy/prompts/`
- Use `expand_formatted_text()` from `InquirerPy.utils` for choice name rendering
- Keep backward compatibility — plain string choice names must always work
- Docstrings: Google style, matching existing prompts

## Key Files

| File | Purpose |
|------|---------|
| `InquirerPy/utils.py` | Shared utilities, `get_style()`, `expand_formatted_text()` |
| `InquirerPy/base/control.py` | `Choice` dataclass, `InquirerPyUIListControl` |
| `InquirerPy/base/complex.py` | `BaseComplexPrompt` — prompt message rendering |
| `InquirerPy/prompts/list.py` | `ListPrompt` (select) — base for most list prompts |
| `InquirerPy/prompts/checkbox.py` | `CheckboxPrompt` |
| `InquirerPy/prompts/rawlist.py` | `RawlistPrompt` |
| `InquirerPy/prompts/expand.py` | `ExpandPrompt` |
| `InquirerPy/prompts/fuzzy.py` | `FuzzyPrompt` |
| `tests/test_colored_choices.py` | Tests for HTML/ANSI/FormattedText choice names |
| `examples/colored_choices.py` | Demo for colored choices |
