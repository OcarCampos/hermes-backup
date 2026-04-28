---
name: session-recovery
description: Recover conversation history from ~/.hermes/sessions/ when session_search DB is corrupted
triggers:
  - "session_search fails"
  - "database disk image is malformed"
  - "finding last message from date"
  - "recovering conversation history"
---

# Session Recovery — When session_search DB is Corrupted

## Trigger
When `session_search` fails with "database disk image is malformed" or returns empty/incomplete results.

## What to Do

### Step 1 — Inspect the sessions directory
```bash
ls -laht ~/.hermes/sessions/
```
Files of interest:
- `session_YYYYMMDD_HHMMSS_*.json` — Session metadata container (has embedded messages array)
- `YYYYMMDD_HHMMSS_*.jsonl` — Raw message stream (one JSON object per line, the actual conversation)

### Step 2 — Find the right session
- Sessions are ordered by modification time — most recent at top
- Cron sessions are prefixed `session_cron_`
- For a specific date, grep for the date in jsonl files:
```bash
grep "2026-04-24" ~/.hermes/sessions/*.jsonl | tail -5
```

### Step 3 — Read messages from jsonl
The `.jsonl` file has the most complete message history with timestamps:
```python
import json
with open('/home/ocarjohann/.hermes/sessions/20260424_080624_c34a3f33.jsonl') as f:
    for line in f:
        line = line.strip()
        if not line: continue
        try:
            obj = json.loads(line)
            if obj.get('role') == 'user':
                print(obj.get('timestamp'))
                print(str(obj.get('content',''))[:200])
        except: pass
```

### Step 4 — Cross-reference with session .json
The `session_*.json` file may have additional context (title, message count). The jsonl is the source of truth for message content and timestamps.

### Key Files
- `~/.hermes/sessions/` — All session files
- `state.db` — The SQLite DB that session_search uses (may be corrupted)
- `sessions.json` — Session index

## Notes
- The `.json` session files contain a `messages` array with full message objects
- The `*.jsonl` files contain the raw message stream — one line per message
- Both have `timestamp` and `role` fields
- User messages have `"role": "user"`, assistant messages have `"role": "assistant"`
