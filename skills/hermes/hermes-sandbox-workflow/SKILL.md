---
name: hermes-sandbox-workflow
description: Write Python scripts to disk then execute with terminal — the reliable pattern for multi-step tasks in the Hermes execute_code sandbox.
tags: [hermes, sandbox, terminal, execute-code, workflow]
version: 1.0.0
author: Hermes Agent
license: MIT
---

# Hermes Sandbox Workflow

## The Problem

`execute_code` runs in an isolated sandbox (`/tmp/hermes_sandbox_XXXX`). Within a single `execute_code` call:
- `hermes_tools` imports are available (terminal, read_file, etc.)
- BUT each call starts fresh — no state persists between calls
- Chaining `terminal()` inside `execute_code` works for simple commands, but complex multi-line scripts often fail due to escaping/quoting issues

## The Solution: Write-then-Run

For any script that needs more than 2-3 tool calls, write it to a file first, then execute with `terminal` in a separate call:

**Step 1 — Write the script:**
```python
from hermes_tools import terminal, write_file  # or just write_file

script = """
import csv
from collections import defaultdict

categories = defaultdict(int)
with open('/mnt/data/Developing/hermes-workspace/finance/expenses/202604-expenses.csv') as f:
    reader = csv.reader(f, delimiter=';')
    next(reader)
    for row in reader:
        if len(row) >= 5:
            cat = row[1]
            amount_str = row[3].replace('$', '').replace(',', '').strip('"')
            categories[cat] += int(amount_str)

total = sum(categories.values())
print(f"Total: ${total:,}")
"""

write_file('/tmp/my_script.py', script)
print("Script written.")
```

**Step 2 — Run with terminal:**
```bash
python3 /tmp/my_script.py
```

## Why This Works

| Approach | Problem |
|----------|---------|
| Single `execute_code` with inline `terminal("python3 -c '...'")` | Shell escaping噩梦 for complex Python — quotes, newlines, dollar signs all conflict |
| Multiple `execute_code` calls chaining `terminal()` | Each sandbox call is independent — imports/tool availability may vary |
| `execute_code` → write file → `terminal` | Sandbox persists the file to `/tmp` between calls — clean separation |

## Key Insight

The `execute_code` sandbox is `/tmp/hermes_sandbox_XXXX/`. Files written there with `write_file` persist for the session. Use `terminal` (which runs on the host system, not in the sandbox) to execute them.

## When to Use

- CSV parsing / financial data processing
- Any task requiring 3+ tool calls with logic between them
- Complex string manipulation with regex
- Data aggregation or filtering across multiple files
- Any task where you'd otherwise chain multiple `terminal()` calls with messy escaping
