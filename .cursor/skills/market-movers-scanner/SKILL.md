---
name: market-movers-scanner
description: Weekday market-movers scan — Yahoo day gainers/losers/most actives, liquid filter, top-10 Buy/Hold/Sell email. Use when user asks for market movers, stocks on the move, daily movers digest, or top 10 recommendations from the morning scan.
---

# Market Movers Scanner

Replaces the scheduled penny digest. Surfaces liquid names that are actually moving today.

## Run

```powershell
uv run --python 3.12 --with tzdata --no-project python .\scripts\scoring\daily-market-movers-scan.py
```

Flags: `--no-email` (reports only), `--top N`, `--config path`.

GitHub Action: `.github/workflows/daily-market-movers.yml` — weekdays 7:00 AM Mountain Standard Time (`America/Phoenix`). Never calls `wsli` / Equibles / Rebalance-MCP.

## Config

[`config/market-movers.yaml`](../../../config/market-movers.yaml) — screeners, min price ($5), volume floors, max buys, overlay toggles.

## Outputs

| Artifact | Path |
|----------|------|
| Time series | `research/timeseries/market-movers.csv` |
| Markdown | `research/reports/YYYY-MM-DD-market-movers-scan.md` |
| Email | Top 10 HTML digest via Resend |

## Recommendation rules

- **Buy (paper)** — strong up-move, above SMA20, RSI &lt; 75, volume confirmation; max 2/day; paper gate
- **Hold** — holdings overlay or mixed / already owned
- **Sell** — held name breaking down below SMA20 on elevated volume
- **Watch / Avoid** — extended, overbought, or sharp non-held drops

Live tickets still need official GARP ≥ 60. This job is educational alerts only.

## Overlay

Always merges `portfolio/holdings.yaml` + `portfolio/watchlist.yaml` (skips benchmark sleeve) so core names get Hold/Sell context even when not top movers.

## Related

Penny universes remain on disk for **on-demand** use via `penny-scanner` — they are not emailed on a schedule anymore.
