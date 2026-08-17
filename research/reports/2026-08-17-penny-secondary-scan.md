# Secondary penny watchlist scan — 2026-08-17

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Recommendations are PAPER_CANDIDATE at most, never LIVE_BUY.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. Every name on this list is flagged `watch`, so the scanner cannot promote any of them. Getting to a candidate requires a Rebalance-MCP GARP score of 60 or better plus an earnings-quality review.

| Ticker | Close | 1d % | 5d % | SMA20 | RSI14 | Quality | Action |
|--------|------:|-----:|-----:|------:|------:|---------|--------|
| ABUS | 4.75 | 1.61 | 3.38 | 4.50 | 64.8 | watch | WATCH |
| AISP | 1.97 | 0.26 | -3.20 | 1.95 | 51.8 | watch | WATCH |
| ALTO | 4.20 | 0.36 | -0.83 | 4.58 | 44.7 | watch | WATCH |
| AMPY | 4.82 | 0.73 | 15.74 | 4.13 | 78.8 | watch | WATCH |
| AREC | 2.85 | -0.87 | 0.17 | 2.21 | 88.2 | watch | WATCH |
| ARKO | 4.74 | -2.37 | 0.74 | 6.74 | 15.6 | watch | WATCH |
| CYH | 2.93 | -2.33 | -0.34 | 2.90 | 59.0 | watch | WATCH |
| GDRX | 3.69 | -1.21 | 0.68 | 3.34 | 67.3 | watch | WATCH |
| GORO | 2.81 | 2.36 | 13.97 | 2.36 | 76.4 | watch | WATCH |
| HLLY | 3.08 | -0.80 | -2.68 | 2.84 | 68.3 | watch | WATCH |
| MDXG | 4.21 | -1.52 | -1.52 | 4.24 | 43.0 | watch | WATCH |
| NAGE | 2.98 | -1.49 | -2.46 | 3.21 | 38.0 | watch | WATCH |
| SABR | 2.23 | 0.00 | 7.73 | 1.96 | 67.0 | watch | WATCH |
| SITC | 2.90 | -1.86 | -3.81 | 3.66 | 10.6 | watch | WATCH |
| SPRO | 1.22 | -1.22 | -3.57 | 1.23 | 54.9 | watch | WATCH |
| TBLA | 3.87 | -4.57 | -5.73 | 4.63 | 32.0 | watch | WATCH |
| TYGO | 1.18 | -3.69 | -3.69 | 1.55 | 34.8 | watch | WATCH |
| UWMC | 1.51 | -5.03 | 7.09 | 1.70 | 40.0 | watch | WATCH |
| VFF | 2.62 | 3.36 | 10.34 | 2.14 | 77.3 | watch | WATCH |
| VRRM | 4.63 | -1.80 | -5.41 | 4.72 | 58.3 | watch | WATCH |

Prices: Yahoo Finance daily bars, 2026-08-17 America/Toronto. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Max one candidate per morning.
- `avoid` never becomes a buy because it bounced.
- `watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
