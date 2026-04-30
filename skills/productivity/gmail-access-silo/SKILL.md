---
name: gmail-access-silo
description: Access O'car's Gmail (ocarnork138@gmail.com) from the Silo. Documents the correct toolchain since himalaya is not configured and gws CLI needs to be installed first.
version: 1.0.0
tags: [email, gmail, google-workspace, silo]
author: Hermes
license: private
---

# Gmail Access from the Silo

## Current Toolchain

O'car's Gmail is accessed via the **Google Workspace CLI (`gws`)** — NOT `himalaya` (which is not configured).

The Python wrapper lives at:
```
~/.hermes/skills/productivity/google-workspace/scripts/google_api.py
```

## Setup Sequence (one-time)

1. **Check if `gws` is available:**
   ```bash
   gws --version
   ```
   If `command not found` → install via npm:
   ```bash
   npm install -g @googleworkspace/cli
   ```

2. **Verify auth:**
   ```bash
   python3 ~/.hermes/skills/productivity/google-workspace/scripts/google_api.py gmail search "is:unread" --max 5
   ```

## Usage

All Gmail queries go through the API wrapper:
```bash
GAPI="python3 ~/.hermes/skills/productivity/google-workspace/scripts/google_api.py"

# Search unread from specific sender
$GAPI gmail search "is:unread from:machbank" --max 10

# Get full email body
$GAPI gmail get MESSAGE_ID
```

## Notes

- `himalaya` is NOT configured — do not attempt to use it
- `gws` is the correct Google Workspace CLI tool
- OAuth token at `~/.hermes/google_token.json`
- `google-workspace` skill documentation is at `~/.hermes/skills/productivity/google-workspace/SKILL.md`
