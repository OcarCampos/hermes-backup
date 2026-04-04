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

- **Required**: Use `opencode run` with `--auto-accept` for automated workflows.
- Refactoring: `opencode run "Refactor user.ts" --auto-accept --dir /path/to/project`
- Architecture: `opencode run "Plan DB schema" --auto-accept --dir /path/to/project`
- **Flags**:
  - `--auto-accept`: Bypass "Do you want to proceed?" prompts.
  - `--dir`: Specify absolute path to project directory.

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
