---
name: sqlite-session-db-repair
description: Diagnose and repair corrupted Hermes state.db (SQLite session/search DB)
triggers:
  - "session search fails"
  - "database disk image is malformed"
  - "sqlite corrupt"
---

# SQLite Session DB Repair

Repair a corrupted `state.db` (Hermes session/search DB) when session search fails with "database disk image is malformed".

## Diagnosis

```python
import sqlite3
db_path = '/path/to/state.db'
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Check integrity
cur.execute("PRAGMA integrity_check;")
print(cur.fetchone()[0])  # "ok" = healthy, "*** in database main ***" = corrupted

# Check tables individually
cur.execute("SELECT COUNT(*) FROM sessions;")   # should work even if FTS is broken
cur.execute("SELECT COUNT(*) FROM messages;")   # may fail if messages B-tree corrupted
cur.execute("SELECT COUNT(*) FROM messages_fts;")  # FTS virtual table

# Check WAL status
cur.execute("PRAGMA wal_checkpoint(TRUNCATE);")
print(cur.fetchone())  # (0,0,0) = nothing to flush; (1,1,N) = WAL had N pages
```

## Key Learnings

- **Error says `sessions.db` but actual DB is `state.db`** — misleading error message
- **WAL checkpoint result (0,0,0)** means no uncommitted WAL data, not a failure
- **`INSERT INTO messages_fts(...) VALUES('rebuild')` fails** if FTS B-tree pages are corrupted (error 11 = SQLITE_CORRUPT)
- **LIMIT/OFFSET pagination spirals** — SQLite OFFSET operates on query rows, not physical storage. Once you hit a corrupted page boundary, offset-based loops runaway. **Use primary key range queries instead.**
- **Sessions table is often readable even when messages and FTS are corrupted**

## Repair Strategy

### Option A: Rebuild FTS only (if messages table is intact)
```python
conn = sqlite3.connect(db_path)
cur = conn.cursor()
cur.execute("INSERT INTO messages_fts(messages_fts) VALUES('rebuild');")
conn.commit()
```
If this fails → corruption is in the FTS B-tree pages → go to Option B/C.

### Option B: Export readable data, rebuild fresh DB

1. **Backup first:**
```python
import shutil
shutil.copy2(db_path, db_path + '.backup')
```

2. **Read sessions (usually intact):**
```python
cur.execute("SELECT * FROM sessions;")
sessions = cur.fetchall()
```

3. **Read messages with primary key range (avoid OFFSET):**
```python
last_id = 0
batch_size = 50
all_messages = []
while True:
    cur.execute(f"SELECT * FROM messages WHERE id > {last_id} ORDER BY id LIMIT {batch_size};")
    rows = cur.fetchall()
    if not rows: break
    for r in rows:
        all_messages.append(r)
    last_id = rows[-1][0]  # last id from batch
```

4. **Create new clean DB and re-import.**

### Option C: Full reset (fastest when data is mostly lost)
```python
import shutil, os
backup = db_path + '.corrupted.backup'
shutil.copy2(db_path, backup)
for p in [db_path, db_path + '-wal', db_path + '-shm']:
    if os.path.exists(p): os.remove(p)
# Recreate schema (see below)
```

## Hermes state.db Schema

```python
conn = sqlite3.connect(db_path)
cur = conn.cursor()

cur.execute("CREATE TABLE schema_version (version INTEGER PRIMARY KEY, applied_at REAL)")
cur.execute("INSERT INTO schema_version VALUES (1, ?)", (datetime.now().timestamp(),))

cur.execute("""CREATE TABLE sessions (
    id TEXT PRIMARY KEY, source TEXT NOT NULL, user_id TEXT, model TEXT,
    model_config TEXT, system_prompt TEXT, parent_session_id TEXT,
    started_at REAL NOT NULL, ended_at REAL, end_reason TEXT,
    message_count INTEGER DEFAULT 0, tool_call_count INTEGER DEFAULT 0,
    input_tokens INTEGER DEFAULT 0, output_tokens INTEGER DEFAULT 0,
    cache_read_tokens INTEGER DEFAULT 0, cache_write_tokens INTEGER DEFAULT 0,
    reasoning_tokens INTEGER DEFAULT 0, billing_provider TEXT,
    billing_base_url TEXT, billing_mode TEXT, estimated_cost_usd REAL,
    actual_cost_usd REAL, cost_status TEXT, cost_source TEXT,
    pricing_version TEXT, title TEXT
)""")

cur.execute("""CREATE TABLE messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT, session_id TEXT NOT NULL,
    role TEXT NOT NULL, content TEXT, tool_call_id TEXT,
    tool_calls TEXT, tool_name TEXT, timestamp REAL NOT NULL,
    token_count INTEGER, finish_reason TEXT, reasoning TEXT,
    reasoning_details TEXT, codex_reasoning_items TEXT,
    FOREIGN KEY (session_id) REFERENCES sessions(id)
)""")

cur.execute("CREATE INDEX idx_messages_session_id ON messages(session_id)")
cur.execute("CREATE INDEX idx_messages_timestamp ON messages(timestamp)")

cur.execute("""CREATE VIRTUAL TABLE messages_fts USING fts5(
    content, session_id UNINDEXED, role UNINDEXED,
    content='messages', content_rowid='id'
)""")

conn.commit()
```

## Prevention

- WAL accumulation (large `-wal` file) indicates connections not closing properly
- Regular `PRAGMA wal_checkpoint(TRUNCATE)` via cron can help
- The gateway uses `acquire_scoped_lock()` per bot token — ensure all code paths release locks on exit
