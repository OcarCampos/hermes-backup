---
name: unraid
version: 1.0.1
description: Query and monitor Unraid servers via the GraphQL API. Use when the user asks to check Unraid, monitor servers, get disk temperatures, read logs, list shares, check array status, containers, VMs, or any Unraid system monitoring.
prerequisites:
  commands: [curl, jq]
metadata:
  hermes:
    tags: [unraid, server, monitoring, graphql, homelab]
---

# Unraid API Skill

Query and monitor Unraid servers using the GraphQL API. Access all 27 read-only endpoints for system monitoring, disk health, logs, containers, VMs, and more.

## Quick Start

Set your Unraid server credentials:

```bash
export UNRAID_URL="https://your-unraid-server/graphql"
export UNRAID_API_KEY="***"
```

**Get API Key:** Settings → Management Access → API Keys → Create (select "Viewer" role)

Helper script at `~/.hermes/skills/devops/unraid/scripts/`:

```bash
./scripts/unraid-query.sh -q "{ online }"
```

## GraphQL API Structure

Unraid 7.2+ uses GraphQL (not REST):
- **Single endpoint:** `/graphql` for all queries
- **Request exactly what you need:** Specify fields in query
- **No container logs:** Docker container output logs not accessible via API

## Common Tasks

### System Monitoring

```bash
./scripts/unraid-query.sh -q "{ online }"
./scripts/unraid-query.sh -q "{ metrics { cpu { percentTotal } memory { used total percentTotal } } }"
./scripts/dashboard.sh                          # Complete multi-server dashboard
```

### Disk Health

```bash
./examples/disk-health.sh
```

### Array Status

```bash
./scripts/unraid-query.sh -q "{ array { state parityCheckStatus { status progress errors } } }"
```

### Logs

```bash
./scripts/unraid-query.sh -q "{ logFiles { name size modifiedAt } }"
./examples/read-logs.sh syslog 20
```

### Containers & VMs

```bash
./scripts/unraid-query.sh -q "{ docker { containers { names image state status } } }"
./scripts/unraid-query.sh -q "{ vms { name state cpus memory } }"
```
Note: Container output logs NOT accessible via API. Use `docker logs` via SSH.

### Shares

```bash
./scripts/unraid-query.sh -q "{ shares { name comment } }"
./scripts/unraid-query.sh -q "{ shares { name } }"
```

### Notifications

```bash
./scripts/unraid-query.sh -q "{ notifications { overview { unread { info warning alert total } } } }"
```

## Helper Script Usage

```bash
./scripts/unraid-query.sh -u URL -k API_KEY -q "QUERY"

# Format options
-f json    # Raw JSON (default)
-f pretty  # Pretty-printed JSON
-f raw     # Just the data (no wrapper)
```

## Reference Files

- `references/endpoints.md` - Complete list of all 27 API endpoints
- `references/troubleshooting.md` - Common errors and solutions
- `references/api-reference.md` - Detailed field documentation
