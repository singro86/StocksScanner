---
name: penny-scanner
description: Screens and daily-scans the GARP penny universes — the 9-name primary list and the 20-name secondary watchlist. Use when the user asks for penny stocks, 3x rerate, daily scan, secondary watchlist, IRWD, or sub-$5 names.
---

# Penny Scanner

Two universes, one script. Never mix them into `watchlist.yaml` core slots without a GARP score >= 60.

| Universe | File | Quality | Daily outputs |
|----------|------|---------|---------------|
| Primary (9) | `portfolio/penny9-universe.yaml` | mix of pass / watch / avoid | `research/timeseries/penny9.csv`, `research/reports/YYYY-MM-DD-penny9-scan.md` |
| Secondary (20) | `portfolio/penny-secondary-watchlist.yaml` | all `watch` | `research/timeseries/penny-secondary.csv`, `research/reports/YYYY-MM-DD-penny-secondary-scan.md` |

## Daily scan

```powershell
uv run --python 3.12 --with tzdata --no-project python .\scripts\scoring\daily-penny9-scan.py --digest
```

That writes both time series, both markdown briefs, plus one ranked HTML email (`Buy / Sell / Hold / Watch / Avoid`) covering all 29 names. The GitHub Action `.github/workflows/daily-penny9.yml` runs this weekdays at 8:30 America/Toronto. This job never calls `wsli` and never sets `TRADE_APPROVED`.

## Quality flags (enforced in `decide()`)

- `pass` — may become `PAPER_CANDIDATE` if not stretched (close > 1.25× SMA20), not RSI >= 75, and not already near `three_x_usd`
- `watch` — never auto-promoted. Secondary list is entirely `watch`
- `avoid` — never a buy because it bounced

Max one candidate per morning. Prefer IRWD when it is `pass`.

## New-name screen (Equibles, not daily prices)

When adding or refreshing the secondary list:

1. Equibles `ScreenStocks`: US listing, price $0.50–$5, market cap >= $50M, TTM net income > 0, dollar volume >= $1M, no going-concern
2. FinanceKit quotes for 52-week range, beta, P/E
3. Drop OTC / pink (Wealthsimple + profile rules). Drop names already in penny-9
4. Cap at 20. Rank by 52-week range / price as a **range proxy**, not a return forecast
5. Flag every new name `quality: watch` until Rebalance-MCP GARP >= 60 **and** an earnings-quality read confirms operating profit (not a settlement / asset sale)
6. Write the YAML. Do not put secondary names into `watchlist.yaml` screener_slots except the one satellite that already passed (IRWD)

## 3x rerate

Only IRWD has a documented 3–12 month ~3x path (old $10–$14 range / peer P/E gap). See `research/reports/2026-08-14-IRWD-research.md`. A wide 52-week range is not a 3x thesis.

## Rules

- Paper trading: recommendations are `PAPER_CANDIDATE` at most
- No live Wealthsimple order from this skill
- If Rebalance-MCP is down, do not upgrade `watch` → `pass`
- Reserve Equibles quota; the daily job uses Yahoo bars on purpose
