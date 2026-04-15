---
name: qbittorrent
version: 1.0.0
description: Manage torrents with qBittorrent via WebUI API. Use when the user asks to list torrents, add torrent, pause/resume/delete torrents, check download status, or manage qBittorrent.
prerequisites:
  commands: [curl]
metadata:
  hermes:
    tags: [torrent, qbittorrent, download, seeding]
---

# qBittorrent WebUI API

Manage torrents via qBittorrent's WebUI API (v4.1+). Runs at `http://localhost:8080`.

## Setup

Credentials stored in: `/home/ocarjohann/bck/credentials/qbittorrent/config.json`
(Alternative path sometimes referenced: `~/.clawdbot/credentials/qbittorrent/config.json`)

```json
{
  "url": "http://localhost:8080",
  "username": "ocarjohann",
  "password": "***"
}
```

**Usage with non-default credential path — pass env vars directly:**
```bash
QBIT_URL=http://localhost:8080 \
QBIT_USER=ocarjohann \
QBIT_PASS=$(cat /home/ocarjohann/bck/credentials/qbittorrent/config.json | python3 -c "import sys,json; print(json.load(sys.stdin)['password'])") \
~/.hermes/skills/devops/qbittorrent/scripts/qbit-api.sh add "magnet:..."
```
```

## Quick Reference

Scripts at `~/.hermes/skills/devops/qbittorrent/scripts/`

### List Torrents

```bash
./scripts/qbit-api.sh list                    # All torrents
./scripts/qbit-api.sh list --filter downloading
./scripts/qbit-api.sh list --filter seeding
./scripts/qbit-api.sh list --filter paused
./scripts/qbit-api.sh list --category movies
```

Filters: `all`, `downloading`, `seeding`, `completed`, `paused`, `active`, `inactive`, `stalled`, `errored`

### Get Torrent Info

```bash
./scripts/qbit-api.sh info <hash>
./scripts/qbit-api.sh files <hash>
./scripts/qbit-api.sh trackers <hash>
```

### Add Torrent

```bash
./scripts/qbit-api.sh add "magnet:?xt=..." --category movies
./scripts/qbit-api.sh add-file /path/to/file.torrent --paused
```

### Control Torrents

```bash
./scripts/qbit-api.sh pause <hash>       # or "all"
./scripts/qbit-api.sh resume <hash>     # or "all"
./scripts/qbit-api.sh delete <hash>     # keep files
./scripts/qbit-api.sh delete <hash> --files  # delete files too
./scripts/qbit-api.sh recheck <hash>
```

### Categories & Tags

```bash
./scripts/qbit-api.sh categories
./scripts/qbit-api.sh tags
./scripts/qbit-api.sh set-category <hash> movies
./scripts/qbit-api.sh add-tags <hash> "important,archive"
```

### Transfer Info

```bash
./scripts/qbit-api.sh transfer        # global speed/stats
./scripts/qbit-api.sh speedlimit     # current limits
./scripts/qbit-api.sh set-speedlimit --down 5M --up 1M
```

### App Info

```bash
./scripts/qbit-api.sh version
./scripts/qbit-api.sh preferences
```

## Response Format

Torrent object includes: `hash`, `name`, `state`, `progress`, `dlspeed`, `upspeed`, `eta`, `size`, `downloaded`, `uploaded`, `category`, `tags`, `save_path`

States: `downloading`, `stalledDL`, `uploading`, `stalledUP`, `pausedDL`, `pausedUP`, `queuedDL`, `queuedUP`, `checkingDL`, `checkingUP`, `error`, `missingFiles`
