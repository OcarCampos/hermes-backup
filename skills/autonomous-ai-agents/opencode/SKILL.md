---
name: opencode
description: Coding agent orchestrator for refactoring, architecture, and senior dev planning. Use when delegating code tasks, feature development, or complex refactors to an autonomous coding agent.
homepage: https://opencode.ai/docs/cli/
prerequisites:
  commands: [opencode]
metadata:
  hermes:
    tags: [coding, agent, autonomous, code, opencode]
---

# OpenCode CLI

OpenCode is an AI coding agent with a terminal interface for development tasks.

## Setup (once)

- `opencode auth login` - Configure API keys for providers (stored in `~/.local/share/opencode/auth.json`).
- `opencode auth list` - List authenticated providers.
- `opencode auth logout` - Clear credentials.

## Common Commands

- Interactive TUI: `opencode [project_dir]`
- Single shot run: `opencode run "Explain this code"`
- Start Web UI: `opencode web --port 4096`
- Start API Server: `opencode serve --port 4096`
- Attach to server: `opencode attach http://localhost:4096`

## Agent Automation (Non-Interactive)

- **Required**: Use `opencode run` with `--dangerously-skip-permissions` for fully automated workflows.
- Refactoring: `opencode run "Refactor user.ts" --dangerously-skip-permissions --dir /path/to/project`
- Architecture: `opencode run "Plan DB schema" --dangerously-skip-permissions --dir /path/to/project`
- **Working automation command** (tested Apr 2026):
  ```sh
  opencode run "Your task description" \
    --dangerously-skip-permissions \
    --dir /absolute/path/to/project \
    --model zai-coding-plan/glm-4.7
  ```
- **Flags**:
  - `--dangerously-skip-permissions`: Required for non-interactive/automated mode. Without this, `opencode run` exits with help text.
  - `--model`: Select provider/model (long form, not `-m`).
  - `--dir`: Absolute path to project directory.
  - `--auto-accept`: Do NOT rely on this — it does not work as documented for automation; use `--dangerously-skip-permissions` instead.

## Management

- **Agents**: `opencode agent create` / `opencode agent list`
- **MCP**: `opencode mcp add` / `opencode mcp list` / `opencode mcp auth [name]`
- **Models**: `opencode models [provider]` / `opencode models --refresh`

## Github Integration

- Install: `opencode github install`
- Run: `opencode github run`

## Notes

- Set `OPENCODE_SERVER_PASSWORD` for Basic Auth in `serve`/`web` modes.
- Use `opencode session list` to view active sessions.
- Export sessions with `opencode export [sessionID]`.
