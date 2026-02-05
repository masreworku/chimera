# GitHub Copilot instructions for chimera 🚀

## Purpose
Provide concise, project-specific guidance for AI coding agents working in this repository. Keep suggestions narrowly tied to discoverable patterns and files.

## Quick snapshot (what I found)
- Repository currently contains only two files:
  - `.vscode/mcp.json` — defines a single MCP HTTP server entry `tenxfeedbackanalytics` (url: `https://mcppulse.10academy.org/proxy`) with custom headers `X-Device: windows` and `X-Coding-Tool: vscode`.
  - `.github/copilot-instructions.md` — this file (was empty; now populated).

---

## Actionable guidance (do these first) ✅
- Confirm the project type and intended language with the repository owner before adding or modifying source files (no source files were detected).
- Use the MCP config (`.vscode/mcp.json`) when attempting integration work that requires the `tenxfeedbackanalytics` service. Example header usage when calling the service:
  ```http
  X-Device: windows
  X-Coding-Tool: vscode
  ```
- If you add new code, include a minimal `README.md` at the repo root describing the build and test commands for that language/toolchain.

## Naming, structure, and conventions 🔧
- There are no discovered source files or language-specific conventions to follow yet — create idiomatic layouts for the chosen stack (e.g., `src/`, `tests/`) and record them in `README.md`.
- Keep MCP server configuration in `.vscode/mcp.json` and update it if integration endpoints or auth methods change.

## How to propose changes (PR guidance) 📝
- Create small, focused PRs with a clear description of the goal and the commands to reproduce (build/test/run).
- When adding a new language/toolchain, include a short example of how to run the project locally (one-liners) and a CI workflow file (`.github/workflows/ci.yml`) that exercises those steps.

## When an agent should ask for clarification ❓
- If there is any ambiguity about the intended runtime, framework, or CI expectations, ask the repo owner for the preferred language, build system, and test runner.
- Ask for credentials or permissions before attempting to access external services or push to protected branches.

## Files to update when the repo grows 📎
- Add or amend `README.md` with build/test/debug commands.
- Add language-specific config (`package.json`, `pyproject.toml`, `Dockerfile`, etc.) as needed and document usage.
- Keep this file (`.github/copilot-instructions.md`) up to date with any project-specific patterns discovered later.

---

If anything here is unclear or you want the instructions to target a specific language or workflow (Node, Python, Docker, etc.), tell me and I will update this file accordingly. — GitHub Copilot (using Raptor mini, Preview)
