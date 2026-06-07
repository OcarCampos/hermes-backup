---
name: weekly-report-workflow
description: End-of-week report generation and task archival for O'car. Reads TASKS.md, generates Spanish-format weekly report in chat, archives done tasks to tasks-archive.md, cleans TASKS.md.
---
# Weekly Report Workflow

## Trigger
End of week (Friday) — user wants to compile weekly report and archive done tasks.

## Alternative: User-provided task list (ad-hoc archive)
Sometimes O'car reports done tasks without giving a full formatted report — e.g. pasting a raw semicolon list.
When that happens:
1. Read TASKS.md and tasks-archive.md to understand current state
2. Add each done task to TASKS.md with `DONE` tag
3. Archive each to tasks-archive.md in archive format
4. Projection items (e.g. "next week May 25-29") → add as new pending tasks to TASKS.md
5. Flag any stale tasks (e.g. harvest dates that have passed) for follow-up

1. **Read current TASKS.md** to get all done tasks from the week
2. **Read tasks-archive.md** to confirm archive format: `date_created;date_completed;tag;status;title;description`
3. **Generate report in chat** with format:
   ```
   # Informe Semanal — DD-DD de mes de 2026
   fecha;título;descripción
   ```
   One line per task, semicolon-delimited, Spanish.
4. **Archive**: append each done task to `tasks-archive.md` using archive format
   - `date_created` = date from TASKS.md (first column)
   - `date_completed` = same date (all tasks completed same day they were created)
   - `tag` = first tag from TASKS.md
   - `status` = "done"
   - `title` = task title
   - `description` = description from TASKS.md
5. **Clean TASKS.md**: delete archived entries, keep only active/pending
6. **Confirm**: list remaining active/pending tasks

## Report Output Format (for sending)
When O'car asks "give me the weekly report so I can send it," generate CSV in this format:
```
DD-MM-YYYY;work;short title;full description of what was done, outcomes, and relevant context
DD-MM-YYYY;work;short title;full description
...
```

**Format rules:**
- Semicolon-separated, no spaces after semicolons
- Date = actual day work was done (not today, not when reported)
- Title = brief (one line, <80 chars)
- Desc = substantive — what was done, with whom, outcomes, next steps
- No date duplication — each row gets its actual day
- ALWAYS verify all 5 weekdays (Mon–Fri) are included — Monday is frequently missed, check carefully before delivering

**Common mistake:** Do NOT use today's date (05-06-2026) for all entries. Each day gets its own date.

## Archive Format (tasks-archive.md)
```
date_created;date_completed;tag;status;title;description
```
Example: `04-05-2026;04-05-2026;work;done;Audio transcription script for PBX calls;Created Python script to transcribe...`

## Notes
- All dates in DD-MM-YYYY format
- Week reference: Monday-Friday of the week
- Reports are in Spanish (user's workplace is Chile)
- Active/pending items typically: E-377 AsBuilt, Bimbao development, Autodesk renewal, garden tasks, personal projects

**Important — O'car's reporting pattern:**
O'car sends one message per day he worked, typically in the morning or evening of the same day. When he says "I did X on Wednesday," log it as Wednesday. Do NOT second-guess dates or reconstruct events — take the day's attribution at face value. He keeps a physical paper log and the Telegram messages are the authoritative record. Mixing up day attribution frustrates him.
