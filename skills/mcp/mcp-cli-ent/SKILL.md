---
name: mcp-cli-ent
description: MCP (Model Context Protocol) client for on-demand tool calls without loading into agent context window. Use to call MCP servers ad-hoc, manage sessions, and discover server capabilities.
homepage: https://github.com/EstebanForge/mcp-cli-ent
prerequisites:
  commands: [mcp-cli-ent]
metadata:
  hermes:
    tags: [mcp, protocol, tools, client]
---

# MCP CLI-Ent

Command-line tool for interacting with Model Context Protocol (MCP) servers without loading their tool definitions into the agent's context window.

## Setup

- **Config File**: `~/.config/mcp-cli-ent/mcp_servers.json`
- **Create Config**: `mcp-cli-ent create-config`
- **Verify Install**: `mcp-cli-ent version`

## Common Commands

- **List Servers**: `mcp-cli-ent list-servers`
- **List Tools**: `mcp-cli-ent list-tools [server-name]`
- **List Resources**: `mcp-cli-ent list-resources [server-name]`
- **Call Tool**: `mcp-cli-ent call-tool <server> <tool> [json-args]`

## Session Management

Persistent sessions for stateful servers (e.g., browser automation):

- **Start Session**: `mcp-cli-ent session start <server>`
- **List Sessions**: `mcp-cli-ent session list`
- **Session Status**: `mcp-cli-ent session status <server>`
- **Stop Session**: `mcp-cli-ent session stop <server>`

## Daemon Management

The daemon manages persistent sessions:

- **Start (Background)**: `mcp-cli-ent daemon start`
- **Start (Foreground)**: `mcp-cli-ent daemon start --foreground`
- **Status**: `mcp-cli-ent daemon status`
- **Logs**: `mcp-cli-ent daemon logs --tail 100`

## Configuration

Example `mcp_servers.json`:

```json
{
  "mcpServers": {
    "server-name": {
      "enabled": true,
      "command": "npx",
      "args": ["-y", "@server/package"],
      "env": { "API_KEY": "***" }
    }
  }
}
```

## Usage Examples

- **Get Documentation**:
  `mcp-cli-ent call-tool context7 get-library-docs '{"context7CompatibleLibraryID": "/EstebanForge/hyperpress", "query": "custom block"}'`
- **Browser Automation**:
  `mcp-cli-ent session start chrome-devtools`
  `mcp-cli-ent call-tool chrome-devtools navigate '{"url": "https://example.com"}'`
