# Secondary penny watchlist scan — 2026-10-01

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | AISP | Secondary 20 | Watch | 2.35 | +26.07 | +24.07 | 1.96 | 71.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | SITC | Secondary 20 | Watch | 3.46 | +2.67 | +14.57 | 2.99 | 84.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | SPRO | Secondary 20 | Watch | 1.29 | +7.03 | +3.60 | 1.19 | 64.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | TYGO | Secondary 20 | Watch | 0.89 | -1.92 | +1.42 | 0.97 | 34.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | AMPY | Secondary 20 | Watch | 4.39 | +4.39 | +1.27 | 4.56 | 32.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | UWMC | Secondary 20 | Watch | 1.22 | +2.97 | -0.41 | 1.29 | 30.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | ALTO | Secondary 20 | Watch | 3.70 | +0.27 | -1.07 | 3.89 | 36.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | MDXG | Secondary 20 | Watch | 4.63 | -0.64 | -1.70 | 4.68 | 54.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | HLLY | Secondary 20 | Watch | 2.37 | +0.42 | -2.47 | 2.63 | 32.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | TBLA | Secondary 20 | Watch | 3.35 | -0.15 | -2.75 | 3.63 | 24.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | ARKO | Secondary 20 | Watch | 4.08 | -1.09 | -3.66 | 4.38 | 25.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | AREC | Secondary 20 | Watch | 1.80 | +0.84 | -3.99 | 2.04 | 24.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | GDRX | Secondary 20 | Watch | 3.23 | -1.98 | -4.02 | 3.39 | 40.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | CYH | Secondary 20 | Watch | 2.75 | -3.85 | -4.51 | 2.91 | 38.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | ABUS | Secondary 20 | Watch | 4.62 | -3.45 | -5.43 | 4.99 | 20.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | VFF | Secondary 20 | Watch | 2.92 | +0.52 | -6.25 | 2.95 | 53.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | VRRM | Secondary 20 | Watch | 3.04 | -1.77 | -6.31 | 3.49 | 27.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | NAGE | Secondary 20 | Watch | 2.73 | -6.48 | -9.28 | 3.02 | 24.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | SABR | Secondary 20 | Watch | 2.04 | -4.01 | -9.56 | 2.18 | 42.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | GORO | Secondary 20 | Watch | 3.13 | -1.72 | -10.94 | 3.56 | 24.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-10-01 America/Toronto. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
