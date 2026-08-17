# Missed weekday penny-scan email — 2026-08-17

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only.**

## Root cause

The weekday job never ran this morning because there was no scheduler attached to a remote. `.github/workflows/daily-penny9.yml` is a GitHub Action (weekdays 8:30 America/Toronto). This folder was **not a git repository**, so the workflow could not live on GitHub, could not receive repository secrets, and could not fire. The Cursor Automation YAML in `automations/daily-penny-scan.yaml` was also never imported (`gitConfig.repo` empty). Last successful local test was 2026-08-14.

## Catch-up scan (this session)

Both universes were scanned locally at ~11:33 AM America/Toronto using Yahoo daily bars (not Equibles).

| Universe | Report | Today bias |
|----------|--------|------------|
| Primary 9 | `research/reports/2026-08-17-penny9-scan.md` | **PAPER_CANDIDATE: IRWD** $4.38 (Yahoo 2026-08-17). Not a live order. Official GARP still required (>= 60) before any Buy. |
| Secondary 20 | `research/reports/2026-08-17-penny-secondary-scan.md` | NONE — every name is `watch`. |

Email was **not** delivered. `config/wsli.env` has `NOTIFY_EMAIL_TO` / `NOTIFY_EMAIL_FROM` but `RESEND_API_KEY` is empty, so the briefs were saved to `portfolio/cache/email-outbox/` (gitignored).

## Fix in progress

1. Load gitignored `config/wsli.env` inside `daily-penny9-scan.py` so local and Actions runs share the same secret names.
2. Initialize git and push a **private** GitHub repo.
3. Store Actions secrets by **name** (`RESEND_API_KEY`, `NOTIFY_EMAIL_TO`, `NOTIFY_EMAIL_FROM`) and run `workflow_dispatch` once to arm the schedule.

Sources: Yahoo Finance daily bars 2026-08-17; local scanner `scripts/scoring/daily-penny9-scan.py`.
