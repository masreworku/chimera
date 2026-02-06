# Chimera

Project Chimera — research and tooling for event-driven agents and integrations.

## Quick overview

- **Purpose:** workspace for researching, prototyping, and integrating services (event bus, semantic memory, Twitter integration, etc.).
- **Contents:** source code in `src/`, documentation in `docs/`, runnable examples and scripts in `scripts/`, and tests in `tests/`.

## Quickstart (Windows PowerShell)

1. Create a virtual environment and activate it:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

3. Run tests:

```powershell
pytest -q
```

Or use the provided Make targets (when available):

```powershell
make setup
make docker-test
```

## Development

- Run the main application (example): `python main.py`.
- Scripts and utilities: see `scripts/` for small helpers such as `post_tweet.py`.
- Use `src/` for library code and integrations; unit tests live in `tests/`.

## Docker

There is a `Dockerfile` at the repo root for containerized runs. Example:

```powershell
docker build -t chimera .
docker run --rm chimera
```

## Environment recommendations

- Recommended: use the project's virtual environment in `.venv`.
- The project pins pip in documentation historically; use a recent pip for best compatibility.

## Project structure

- `src/` — project packages and modules
- `tests/` — unit and integration tests
- `docs/` — ADRs and design notes
- `scripts/` — small runnable helpers
- `Dockerfile`, `Makefile`, `pyproject.toml`, `requirements.txt`

## Contributing

- Open issues and PRs with a clear description and reproducible steps.
- Include tests for new features or bug fixes.

## License & contact

Add a `LICENSE` file if you wish to make the license explicit. For questions, open an issue or contact the repository owner.

