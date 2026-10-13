# Cursor Automations

Import these workflows via **Cursor → Automations → New** and copy prompts/schedules from each YAML file.

| File | Schedule | Purpose |
|------|----------|---------|
| `daily-garp-scan.yaml` | Weekdays 8:30 AM ET | Score watchlist, swap candidates |
| `daily-penny-scan.yaml` | Daily 7:00 AM MST (`America/Phoenix`) | Cursor Automation companion — mega-cap + both penny universes via `penny-scanner` |
| GitHub Action `daily-penny9.yml` | Daily 7:00 AM MST | Durable runner: mega-cap core + primary 9 + secondary 20, macro brief, email digest |
| `weekly-portfolio-pulse.yaml` | Monday 8:00 AM | Full portfolio review |
| `monthly-dca-review.yaml` | 1st of month 9:00 AM | DCA allocation plan |
| `earnings-alert.yaml` | Weekdays 7:00 AM | Earnings calendar + checklist |
| `quarterly-goal-check.yaml` | Jan/Apr/Jul/Oct 1st | Monte Carlo goal tracking |

## Prerequisites

1. MCP servers configured (`config/MCP_SETUP.md`)
2. GitHub repo: `singro86/StocksScanner` (cloud automations + Actions checkout)
3. Email: put `RESEND_API_KEY`, `NOTIFY_EMAIL_TO`, `NOTIFY_EMAIL_FROM` in gitignored `config/wsli.env` (local) and the same names as GitHub Actions secrets (weekday job)

## GitHub Action — penny morning job

[`.github/workflows/daily-penny9.yml`](../.github/workflows/daily-penny9.yml) runs **every day at 7:00 AM America/Phoenix** (MST year-round). It does **not** use Cursor MCP. Local runs of `daily-penny9-scan.py` load `config/wsli.env` automatically.

1. Repo is `https://github.com/singro86/StocksScanner`
2. Add repository secrets `RESEND_API_KEY`, `NOTIFY_EMAIL_TO`, `NOTIFY_EMAIL_FROM`
3. Run **Actions → Daily penny scans → Run workflow** once to test (and to arm the schedule)

Secrets are referenced by **name** (`${{ secrets.RESEND_API_KEY }}`). Never paste the key value into the workflow file — it is committed to the repo and becomes public history.

The job never places trades. During paper trading the buy line is **Buy (paper)** at most. One HTML digest email covers mega-cap core (pinned top), penny Top 10, and a Markets & macro brief (gold / Fed / US–Iran).

### Three sleeves, one scanner

`scripts/scoring/daily-penny9-scan.py --digest` is the weekday command. `--universe <path>` still scans one YAML. The `slug` key inside that YAML decides the output filenames, so the tiers never overwrite each other.

| Universe | Tier | Names | Outputs |
|----------|------|-------|---------|
| [`portfolio/mega-cap-scan-universe.yaml`](../portfolio/mega-cap-scan-universe.yaml) | mega_cap_core | 4 (NVDA, MSFT, GOOGL, AAPL) | `research/timeseries/mega-cap.csv`, `<date>-mega-cap-scan.md` |
| [`portfolio/penny9-universe.yaml`](../portfolio/penny9-universe.yaml) | primary | 9 | `research/timeseries/penny9.csv`, `<date>-penny9-scan.md` |
| [`portfolio/penny-secondary-watchlist.yaml`](../portfolio/penny-secondary-watchlist.yaml) | secondary | 20 | `research/timeseries/penny-secondary.csv`, `<date>-penny-secondary-scan.md` |

Mega-cap and secondary names are flagged `quality: watch` and never take the morning paper Buy. The secondary tier only builds price history until a name earns a real GARP score. Macro headlines use Google News RSS; gold uses Yahoo `GC=F`.

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
