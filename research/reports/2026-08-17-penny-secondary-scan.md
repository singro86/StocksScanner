# Secondary penny watchlist scan — 2026-08-17

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Recommendations are PAPER_CANDIDATE at most, never LIVE_BUY.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. Every name on this list is flagged `watch`, so the scanner cannot promote any of them. Getting to a candidate requires a Rebalance-MCP GARP score of 60 or better plus an earnings-quality review.

| Ticker | Close | 1d % | 5d % | SMA20 | RSI14 | Quality | Action |
|--------|------:|-----:|-----:|------:|------:|---------|--------|
| ABUS | 4.78 | 2.25 | 4.03 | 4.50 | 65.7 | watch | WATCH |
| AISP | 2.00 | 2.30 | -1.23 | 1.95 | 53.7 | watch | WATCH |
| ALTO | 4.20 | 0.36 | -0.83 | 4.58 | 44.7 | watch | WATCH |
| AMPY | 4.83 | 0.94 | 15.99 | 4.13 | 79.0 | watch | WATCH |
| AREC | 2.88 | -0.00 | 1.05 | 2.21 | 89.7 | watch | WATCH |
| ARKO | 4.75 | -1.96 | 1.17 | 6.74 | 15.7 | watch | WATCH |
| CYH | 2.93 | -2.33 | -0.34 | 2.90 | 59.0 | watch | WATCH |
| GDRX | 3.71 | -0.67 | 1.23 | 3.34 | 68.1 | watch | WATCH |
| GORO | 2.87 | 4.32 | 16.15 | 2.36 | 77.2 | watch | WATCH |
| HLLY | 3.08 | -0.80 | -2.06 | 2.87 | 63.4 | watch | WATCH |
| MDXG | 4.21 | -1.41 | -1.41 | 4.24 | 43.2 | watch | WATCH |
| NAGE | 3.00 | -0.83 | -1.80 | 3.21 | 38.6 | watch | WATCH |
| SABR | 2.23 | 0.22 | 7.97 | 1.96 | 67.2 | watch | WATCH |
| SITC | 2.92 | -1.18 | -3.15 | 3.66 | 10.7 | watch | WATCH |
| SPRO | 1.22 | -1.22 | -1.22 | 1.22 | 52.9 | watch | WATCH |
| TBLA | 3.88 | -4.07 | -5.93 | 4.57 | 30.7 | watch | WATCH |
| TYGO | 1.18 | -3.44 | -3.44 | 1.55 | 34.9 | watch | WATCH |
| UWMC | 1.51 | -4.72 | 7.45 | 1.70 | 40.1 | watch | WATCH |
| VFF | 2.62 | 3.56 | 10.55 | 2.14 | 77.4 | watch | WATCH |
| VRRM | 4.63 | -1.80 | -2.21 | 4.76 | 58.2 | watch | WATCH |

Prices: Yahoo Finance daily bars, 2026-08-17 America/Toronto. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Max one candidate per morning.
- `avoid` never becomes a buy because it bounced.
- `watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
