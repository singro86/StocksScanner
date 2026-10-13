# Cursor Automations

Import these workflows via **Cursor → Automations → New** and copy prompts/schedules from each YAML file.

| File | Schedule | Purpose |
|------|----------|---------|
| `daily-garp-scan.yaml` | Weekdays 8:30 AM ET | Score watchlist, swap candidates |
| `daily-penny-scan.yaml` | Daily 7:00 AM MST (`America/Phoenix`) | Cursor Automation companion — mega-cap + both penny universes via `penny-scanner` |
| GitHub Action `daily-penny9.yml` | Daily 7:00 AM MST | Durable runner: mega-cap core + primary 9 + secondary 20, macro brief, top-5 penny email |
| `daily-market-movers.yaml` | Weekdays 7:00 AM MST | Cursor Automation companion — Yahoo movers top-10 Buy/Hold/Sell |
| GitHub Action `daily-market-movers.yml` | Weekdays 7:00 AM MST | Durable runner: liquid movers, time series, email digest |
| `weekly-portfolio-pulse.yaml` | Monday 8:00 AM | Full portfolio review |
| `monthly-dca-review.yaml` | 1st of month 9:00 AM | DCA allocation plan |
| `earnings-alert.yaml` | Weekdays 7:00 AM | Earnings calendar + checklist |
| `quarterly-goal-check.yaml` | Jan/Apr/Jul/Oct 1st | Monte Carlo goal tracking |

## Prerequisites

1. MCP servers configured (`config/MCP_SETUP.md`)
2. GitHub repo: `singro86/StocksScanner` (cloud automations + Actions checkout)
3. Email: put `RESEND_API_KEY`, `NOTIFY_EMAIL_TO`, `NOTIFY_EMAIL_FROM` in gitignored `config/wsli.env` (local) and the same names as GitHub Actions secrets (weekday job)

## GitHub Action — market movers morning job

[`.github/workflows/daily-penny9.yml`](../.github/workflows/daily-penny9.yml) runs **every day at 7:00 AM America/Phoenix** (MST year-round). It does **not** use Cursor MCP. Local runs of `daily-penny9-scan.py` load `config/wsli.env` automatically.

[`.github/workflows/daily-market-movers.yml`](../.github/workflows/daily-market-movers.yml) runs weekdays at 7:00 AM Mountain Standard Time (`America/Phoenix`, UTC−7, no daylight saving). It does **not** use Cursor MCP. Local runs of `daily-market-movers-scan.py` load `config/wsli.env` automatically.

1. Repo is `https://github.com/singro86/StocksScanner`
2. Add repository secrets `RESEND_API_KEY`, `NOTIFY_EMAIL_TO`, `NOTIFY_EMAIL_FROM`
3. Run **Actions → Daily market movers → Run workflow** once to test (and to arm the schedule)

Secrets are referenced by **name** (`${{ secrets.RESEND_API_KEY }}`). Never paste the key value into the workflow file — it is committed to the repo and becomes public history.

The penny job never places trades. During paper trading the buy line is **Buy (paper)** at most. One HTML digest leads with the Markets & macro brief (gold / Fed / US–Iran), then mega-cap core, then the **top 5** penny names.

### Three sleeves, one scanner

`scripts/scoring/daily-penny9-scan.py --digest` is the daily command. `--universe <path>` still scans one YAML. The `slug` key inside that YAML decides the output filenames, so the tiers never overwrite each other.

| Universe | Tier | Names | Outputs |
|----------|------|-------|---------|
| [`portfolio/mega-cap-scan-universe.yaml`](../portfolio/mega-cap-scan-universe.yaml) | mega_cap_core | 4 (NVDA, MSFT, GOOGL, AAPL) | `research/timeseries/mega-cap.csv`, `<date>-mega-cap-scan.md` |
| [`portfolio/penny9-universe.yaml`](../portfolio/penny9-universe.yaml) | primary | 9 | `research/timeseries/penny9.csv`, `<date>-penny9-scan.md` |
| [`portfolio/penny-secondary-watchlist.yaml`](../portfolio/penny-secondary-watchlist.yaml) | secondary | 20 | `research/timeseries/penny-secondary.csv`, `<date>-penny-secondary-scan.md` |

Mega-cap and secondary names are flagged `quality: watch` and never take the morning paper Buy. The secondary tier only builds price history until a name earns a real GARP score. Macro headlines use Google News RSS; gold uses Yahoo `GC=F`.

### How the movers scanner works

`scripts/scoring/daily-market-movers-scan.py` pulls Yahoo `day_gainers` / `day_losers` / `most_actives`, filters price ≥ $5 and liquidity, overlays holdings + GARP watchlist, then writes:

| Output | Path |
|--------|------|
| Time series | `research/timeseries/market-movers.csv` |
| Markdown | `research/reports/<date>-market-movers-scan.md` |
| Config | [`config/market-movers.yaml`](../config/market-movers.yaml) |

The movers job never places trades. During paper trading the buy line is **Buy (paper)** at most. One HTML digest emails the **top 10** liquid movers, ranked Buy → Sell → Hold → Watch → Avoid.

### Resend sender rules

Resend rejects any `from` address on an unverified domain, so a Gmail address cannot be the sender.

| Setup | `NOTIFY_EMAIL_FROM` | Allowed `NOTIFY_EMAIL_TO` |
|-------|---------------------|---------------------------|
| No verified domain (default) | `onboarding@resend.dev` | Only the Resend account owner's email |
| Verified domain at [resend.com/domains](https://resend.com/domains) | `anything@yourdomain.com` | Any recipient |

If the send fails, the brief is written to `portfolio/cache/email-outbox/` and the job still succeeds — the CSV and report are never lost to an email error.

## Email integration

After each automation, optionally run:

```powershell
.\scripts\notify\send-email.ps1 -Subject "..." -Body "..." -Type daily_scan
```

Or chain in automation prompt: "After saving report, run scripts/notify/send-email.ps1"

## Paper trading

All automations respect `paper_trading_complete: false` — dry-run and research only.
