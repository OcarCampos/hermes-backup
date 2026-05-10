---
name: weekly-report-workflow
description: End-of-week report generation and task archival for O'car. Reads TASKS.md, generates Spanish-format weekly report in chat, archives done tasks to tasks-archive.md, cleans TASKS.md.
---
# Weekly Report Workflow

## Trigger
End of week (Friday) — user wants to compile weekly report and archive done tasks.

## Steps

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
