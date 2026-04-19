---
name: bimbao-development
description: Bimbao BIM CRUD web app — frontend/backend integration workflow, auth infrastructure, Docker setup, and branch conventions
category: software-development
tags: [php, laravel, datastar, jwt, docker, bimbao, mvc]
---

# Bimbao Development Workflow

Bimbao is a BIM CRUD web app with 3 GitHub repos:
- **bimbao-frontend** — DataStar + vanilla JS (delivered as `bimbao-frontend-handover.tar.gz`)
- **bimbao-backend** — PHP MVC, DataStar wiring, JWT HttpOnly cookies, MariaDB
- **bimbao-database** — DB schemas

Repos at: `/mnt/data/Developing/`

## Frontend → Backend Integration Workflow

1. Read `bimbao-frontend/README.md` and `HANDOVER.md`
2. Copy `bimbao-frontend-handover.tar.gz` to backend folder
3. Read backend `README.md` and `devlogs/` for architecture context
4. Delegate to opencode with GLM-5, passing: frontend docs + backend structure + integration goal
5. Create `testing` branch, commit, push for review
6. After review, merge to `main`

## Branch Convention
- `testing` — for review before merging
- PR against `main` for final merge

## Auth Infrastructure (key decisions from devlog 003)
- JWT stored in **HttpOnly cookie** (not localStorage)
- `AuthMiddleware` checks both `Authorization` header and `jwt` cookie
- `/auth/logout` invalidates cookie immediately
- **DataStar fallback**: if JS disabled, backend re-renders full view with error/success injected (preserves user input)
- `confirm_password` field in registration

## Docker Setup
```yaml
# docker-compose.yml
services: Nginx + PHP 8.2-FPM + MariaDB + PhpMyAdmin (port 8081)
```

## Devlog Location
`/mnt/data/Developing/bimbao-backend/devlogs/YYYYMMDD.md`

Format: session title, devlog number (e.g. `003-auth-infrastructure-refinement`), changes made, next steps.

## Useful Commands
```bash
# Pull latest
git pull origin <branch>

# Create testing branch
git checkout -b testing
git add . && git commit -m "description" && git push -u origin testing

# Compare with main
git diff main..testing --stat
```
