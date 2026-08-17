# Cursor Automations

Import these workflows via **Cursor → Automations → New** and copy prompts/schedules from each YAML file.

| File | Schedule (ET) | Purpose |
|------|---------------|---------|
| `daily-garp-scan.yaml` | Weekdays 8:30 AM | Score watchlist, swap candidates |
| `daily-penny-scan.yaml` | Weekdays 8:30 AM | Cursor Automation companion — both penny universes via `penny-scanner` |
| GitHub Action `daily-penny9.yml` | Weekdays 8:30 AM ET | Durable runner: 9-name + 20-name secondary, time series, email paper recommendation |
| `weekly-portfolio-pulse.yaml` | Monday 8:00 AM | Full portfolio review |
| `monthly-dca-review.yaml` | 1st of month 9:00 AM | DCA allocation plan |
| `earnings-alert.yaml` | Weekdays 7:00 AM | Earnings calendar + checklist |
| `quarterly-goal-check.yaml` | Jan/Apr/Jul/Oct 1st | Monte Carlo goal tracking |

## Prerequisites

1. MCP servers configured (`config/MCP_SETUP.md`)
2. Repo pushed to GitHub (for cloud automations git checkout)
3. Email optional: set `RESEND_API_KEY`, `NOTIFY_EMAIL_TO` in environment (local) or GitHub Actions secrets (penny-9 workflow)

## GitHub Action — penny morning job

[`.github/workflows/daily-penny9.yml`](../.github/workflows/daily-penny9.yml) runs weekdays at 8:30 AM America/Toronto. It does **not** use Cursor MCP.

1. Push this repo to GitHub and enable Actions on the default branch
2. Add repository secrets `RESEND_API_KEY`, `NOTIFY_EMAIL_TO`, `NOTIFY_EMAIL_FROM`
3. Run **Actions → Daily penny scans → Run workflow** once to test

Secrets are referenced by **name** (`${{ secrets.RESEND_API_KEY }}`). Never paste the key value into the workflow file — it is committed to the repo and becomes public history.

The job never places trades. During paper trading the buy line is `PAPER_CANDIDATE` at most.

### Two universes, one scanner

`scripts/scoring/daily-penny9-scan.py --universe <path>` scans any universe YAML. The `slug` key inside that YAML decides the output filenames, so the two tiers never overwrite each other.

| Universe | Tier | Names | Outputs |
|----------|------|-------|---------|
| [`portfolio/penny9-universe.yaml`](../portfolio/penny9-universe.yaml) | primary | 9 | `research/timeseries/penny9.csv`, `<date>-penny9-scan.md` |
| [`portfolio/penny-secondary-watchlist.yaml`](../portfolio/penny-secondary-watchlist.yaml) | secondary | 20 | `research/timeseries/penny-secondary.csv`, `<date>-penny-secondary-scan.md` |

Every secondary name is flagged `quality: watch`, and `decide()` returns `WATCH` for that flag. The secondary tier therefore cannot produce a buy line — it only builds price history until a name earns a real GARP score.

### Resend sender rules

Resend rejects any `from` address on an unverified domain, so a Gmail address cannot be the sender.

| Setup | `NOTIFY_EMAIL_FROM` | Allowed `NOTIFY_EMAIL_TO` |
|-------|---------------------|---------------------------|
| No verified domain (default) | `onboarding@resend.dev` | Only the Resend account owner's email |
| Verified domain at [resend.com/domains](https://resend.com/domains) | `anything@yourdomain.com` | Any recipient |

Verified working on 2026-08-14 with `onboarding@resend.dev`. If the send fails, the brief is written to `portfolio/cache/email-outbox/` and the job still succeeds — the CSV and report are never lost to an email error.

## Email integration

After each automation, optionally run:

```powershell
.\scripts\notify\send-email.ps1 -Subject "..." -Body "..." -Type daily_scan
```

Or chain in automation prompt: "After saving report, run scripts/notify/send-email.ps1"

## Paper trading

All automations respect `paper_trading_complete: false` — dry-run and research only.
