---
name: tasks-md-logging
description: Log O'car's end-of-day work activities to ~/workspace/tasks/TASKS.md
---
# TASKS.md Logging Workflow

## Purpose
Log O'car's end-of-day work activities to `~/workspace/tasks/TASKS.md`.

## File Location
`/mnt/data/Developing/hermes-workspace/tasks/TASKS.md`

## Structure
```
# TASKS.md — O'car's BIM work log

## ACTIVE PROJECTS
[NNN] — [PROJECT CODE | PROJECT NAME] — [STATUS]
<!-- description -->
<!-- / -->

## BIM DT Research
...

## DONE
[DATE] — [TASK TITLE] [STATUS]
<!-- description -->
<!-- / -->
```

### Active Projects
- Each project is a collapsible HTML comment block (`<!-- -->`)
- Status: `[active]`, `[completed]`, `[on hold]`
- Inside the block: description lines that can be **appended to** for ongoing work
- When completed: move the whole block to DONE, add completion date + description

### DONE Section
- Format: `[DATE] — [TASK TITLE] [STATUS]`
- Status options: `[completed]`, `[cancelled]`
- Block same structure as active projects

## End-of-Day Logging Procedure

1. **Read README.md first** — `tasks/README.md` has the format reference
2. **Read TASKS.md** — get current state of all active projects
3. **Identify project match**:
   - If task belongs to an existing active project → **append to its description** with date header
   - If new project → create new entry in ACTIVE PROJECTS with `[active]`
   - If task is one-off/not a project → add to DONE with today's date
4. **Read the exact current tail of the target entry** before patching (to avoid context drift)
5. **Patch using skill_manage(action='patch')** with old_string/new_string — preserve the `<!-- / -->` closing tag
6. **Verify** the patch worked cleanly

## Common Project Names (from memory)
- `E-377 AsBuilt` — E-377 as-built blueprints
- `IDOM BIM360` — IDOM advanced pre project (BIM360)
- `L. Serrano` entries — meetings/reviews with L. Serrano (plinth corrections, etc.)

## Patching Rules
- **Append**: read current tail, use it as `old_string`, add new lines + closing tag as `new_string`
- **Move to DONE**: copy entire block, patch ACTIVE with removal marker, paste into DONE with date
- **Never delete** `<!-- / -->` closing tags
- Use `replace_all=False` unless replacing a clearly unique string
