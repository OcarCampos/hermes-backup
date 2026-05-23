---
name: lemon-haze-grow-log
description: Edit the Lemon Haze grow log safely — do NOT use execute_code+write_file on files >10KB (corrupts them).
---

# Lemon Haze Grow Log — File Editing Protocol

## Context
The lemon-haze.md file lives at `/mnt/data/Developing/hermes-workspace/garden/lemon-haze.md`. It has 50+ Day entries (Day 8 through Day 104+) plus Irrigation Log, Grow Setup Details, and Tips & Observations sections.

## Safe Edits — MUST USE terminal sed OR patch

### DO NOT use execute_code + write_file
`execute_code` with `write_file` (from hermes_tools) corrupts files > ~10KB. The sandbox appears to truncate stdout at ~500 chars, and write_file writes based on that truncated read — destroying the file. Confirmed empirically (503-byte corrupt output instead of 20KB original).

### Safe approaches (in order of preference):
1. **terminal + sed** — for inserting lines at specific positions or appending after a line number
2. **patch with very unique context** — for replacing blocks. Must include 10+ lines of surrounding context for uniqueness since patterns like "## Day N" repeat throughout
3. **read_file + terminal cat heredoc** — use terminal to write atomically

## Day Calculation
- Day 1 = February 6, 2026 (sprout date)
- Day N = (today - Feb 6, 2026) + 1

## Stage Estimation
- Day < 50: Vegetative
- Day 50-56: Pre-Flowering
- Day > 56: Flowering