---
name: weekly-report-archiving
description: Archive O'car's batch end-of-week reports into TASKS.md and monthly archive files
trigger: "O'car sends weekly TSV report with fecha;título;descripción"
---

# Weekly Report Archiving Workflow

## When to use
O'car reports his week in a batch (not daily). Archive each end-of-week report to TASKS.md and the monthly archive file.

## Input format
O'car sends a TSV table: `fecha;título;descripción`

## Archive steps

### 1. DONE tasks → TASKS.md
Add each entry as `[●]` with the date as a `## YYYY-MM-DD` header above it:
```
## 2026-05-22
[●] **Reunión SCCM** — Reunión con SCCM
```

### 2. DONE tasks → monthly archive (e.g. `tasks/2026-05.md`)
Group entries under `## Week of May 18–22` sub-header using the same `[●]` format.

### 3. Projection tasks → TASKS.md as `[ ]`
Add projected tasks for next week as pending `[ ]` items with target dates noted inline.

### 4. Special cases
- If harvest window or deadline has passed (e.g. Lemon Haze May 10), flag in TASKS.md: `[May 22: harvest window passed — needs update on status]`
- EAUB report transformation: note in entry if it's continuation from previous day
- Cross-references: if a task appeared in prior projections and is now DONE, note the source projection date

## Naming conventions
See `tasks/README.md` inside the workspace for file naming standards.

## Projects active May 2026
- embalselaspalmas.cl (web)
- SIC-NS (SRS report development)
- Cuncumen (riego project)
- EAUB (BIM Unit monthly reports)
- SCCM (meetings)