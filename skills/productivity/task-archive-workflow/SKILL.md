---
name: task-archive-workflow
description: Task tracking workflow for the Nork138 workspace — TASKS.md, ==DONE==, and archive management.
---
# Task Archive Workflow

## Overview
Task management system for the Nork138 workspace at `/mnt/data/Developing/hermes-workspace/`.

## Weekly Report Generation

**Critical rule: ==DONE== is NOT cleared until AFTER the weekly report is generated and the user confirms archival.** Never delete or clear DONE entries before the user explicitly archives. The user expects DONE to persist across sessions until Friday archival.

The weekly report is a **work log**, not just a closed-tasks list. It records what you did with your time — whether a task was finished or will continue the following week.

**What goes into the weekly report:**
- All tasks that had work done during the week, regardless of completion status
- Closed/completed items → `==DONE==` → reported as done → archived after report confirmed
- Open/ongoing items → `==TASKS==` → reported as in-progress → stay in TASKS.md

**Do NOT** generate the report from `==DONE==` alone. Scan all task entries for week-dated log notes.

### Weekly report (Friday)
1. Scan ALL tasks in TASKS.md (both ==TASKS== and ==DONE==) for entries dated within the week
2. Generate report from all week-dated entries:
   - Closed items (in ==DONE==) → reported as completed
   - Open items (in ==TASKS==) → reported as in-progress/continuing next week
3. Report in Spanish, semicolon-delimited CSV format:
   ```
   DD-MM-YYYY;work;Task Title;Brief description.
   ```
4. **Wait for user confirmation before archiving**
5. Move ONLY the closed (==DONE==) entries to archive/YYYY-MM.md
6. Clear ==DONE== section

### Archive Format (tasks-archive.md)
```
date_created;date_completed;tag;status;title;description
```
When created and completed are the same day, both dates are identical (e.g., `25-05-2026;25-05-2026`).
## Sections in TASKS.md

- `==TASKS==` — active, waiting, pending tasks (all tags)
- `==DONE==` — completed tasks from the **current week only**. Accumulates here as you go during the week — never empty during active work. Only cleared after the weekly report is generated.
- `==ARCHIVE==` — staging marker only (empty after weekly report clears DONE)

## Core Principle: Activity-Level Tracking

Each distinct logical unit of work (a meeting, a conversion run, a review session, a support call, a template correction) is a **separate DONE entry** in TASKS.md. You do NOT wait for the parent project to be finished.

- A meeting with L. Serrano → one DONE entry, same day
- A PDF conversion batch run → one DONE entry, same day
- A template correction → one DONE entry, same day
- The full project (e.g. "SRS report") stays in `==TASKS==` with log entries showing progress until fully closed

This ensures the weekly report accurately reflects how time was spent, not just what was closed.

### End of day
1. Do NOT immediately archive — leave tasks in `==DONE==`
2. `==DONE==` is ready for the weekly report whenever it is generated

### The Archive Format
Entries in `archive/YYYY-MM.md` use two dates:
```
YYYY-MM-DD;YYYY-MM-DD;tag;status;Title — Description
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
- Budget tracking: `finance/budget/YYYYMM.csv` — monthly budget vs actuals
- Both are aggregated from TASKS.md for budget reporting
