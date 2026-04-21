---
name: task-archive-workflow
description: Task tracking workflow for the Nork138 workspace — TASKS.md, ==DONE==, and archive management.
---
# Task Archive Workflow

## Overview
Task management system for the Nork138 workspace at `/mnt/data/Developing/hermes-workspace/`.

## File Structure

| File | Purpose |
|------|---------|
| `TASKS.md` | Active + current-week done tasks |
| `archive/YYYY-MM.md` | Permanent archive of completed tasks |

## Sections in TASKS.md

- `==TASKS==` — active, waiting, pending tasks (all tags)
- `==DONE==` — completed tasks from the **current week only**
- `==ARCHIVE==` — staging marker only (empty after weekly report clears DONE)

## The Critical Rule

**`==DONE==` is NOT archived until the weekly report is generated.**

Weekly report = Friday (or on-demand). Only then are DONE tasks moved to `archive/YYYY-MM.md`.

During the week: DONE stays in TASKS.md so it's visible and reportable at any time.

## Daily Workflow

### Logging a done task
Add entry to `==DONE==` in TASKS.md:
```
DD-MM-YYYY;tag;completed;Title;Mon DD: Description of what was done.
```

### End of day
1. Do NOT immediately archive — leave tasks in `==DONE==`
2. `==DONE==` is ready for the weekly report whenever it's generated

### Weekly report (Friday)
1. Generate report from `==DONE==` content
2. Move DONE entries to `archive/YYYY-MM.md` with two-date format: `date_created;date_completed;tag;status;title;description`
3. Clear `==DONE==` section

### The Archive Format
Entries in `archive/YYYY-MM.md` use two dates:
```
DD-MM-YYYY;DD-MM-YYYY;tag;status;Title;Description
date_created;date_completed
```

## Pitfalls

### Premature Archiving
**Symptom:** User asks to see done tasks or generate a weekly report, but entries are already gone from TASKS.md.
**Cause:** Entries were archived immediately instead of waiting for Friday.
**Fix:** Keep `==DONE==` populated throughout the week. Only move to archive after weekly report is generated.

### Archive Format Inconsistency
**Symptom:** `archive/YYYY-MM.md` has mixed formats — some entries with two dates, some with one.
**Cause:** Entries added manually with inconsistent formats.
**Fix:** Always use `date_created;date_completed` format in archive files. Second date = when marked done.

## Tag Definitions
- `work` — BIM projects, client deliverables, Luis Serrano reports
- `home` — Household tasks, watering, rent, appointments
- `personal` — Side projects, Prusa business, programming
- `finance` — Bill payments, investments, tax filing
- `3dprint` — 3D printing business and projects
- `garden` — Plant care, grow logs

## Related
- Finance expenses: `finance/YYYYMM-expenses.csv` — monthly expense tracking
- Supermarket purchases: `supermarket/YYYYMM-history.csv` — shopping history
- Both are aggregated from TASKS.md for budget reporting
