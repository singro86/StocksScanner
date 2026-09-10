# Secondary penny watchlist scan — 2026-09-10

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | SABR | Secondary 20 | Watch | 2.18 | +1.92 | +4.35 | 2.15 | 55.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | AMPY | Secondary 20 | Watch | 5.01 | +1.93 | +0.30 | 4.84 | 55.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | ABUS | Secondary 20 | Watch | 5.12 | -1.06 | +0.29 | 5.03 | 72.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | VFF | Secondary 20 | Watch | 2.88 | -3.06 | -0.38 | 2.78 | 69.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | MDXG | Secondary 20 | Watch | 4.51 | -3.53 | -0.77 | 4.43 | 61.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | TBLA | Secondary 20 | Watch | 3.77 | +1.75 | -1.18 | 3.80 | 57.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | CYH | Secondary 20 | Watch | 2.87 | -2.88 | -1.21 | 2.94 | 37.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | TYGO | Secondary 20 | Watch | 1.04 | +0.48 | -2.34 | 1.10 | 40.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | GDRX | Secondary 20 | Watch | 3.35 | +0.45 | -2.75 | 3.53 | 39.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | SITC | Secondary 20 | Watch | 2.83 | +0.64 | -3.48 | 2.96 | 31.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | ALTO | Secondary 20 | Watch | 3.96 | -1.62 | -3.77 | 4.11 | 41.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | SPRO | Secondary 20 | Watch | 1.16 | -0.85 | -4.92 | 1.21 | 36.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | NAGE | Secondary 20 | Watch | 3.01 | -1.31 | -5.05 | 3.14 | 41.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | AISP | Secondary 20 | Watch | 2.00 | -1.48 | -6.10 | 2.08 | 48.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | HLLY | Secondary 20 | Watch | 2.75 | -5.67 | -6.31 | 2.98 | 36.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | ARKO | Secondary 20 | Watch | 4.37 | -1.69 | -7.91 | 4.64 | 43.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | UWMC | Secondary 20 | Watch | 1.33 | -2.56 | -7.93 | 1.46 | 42.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | AREC | Secondary 20 | Watch | 2.22 | -3.90 | -9.02 | 2.55 | 36.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | GORO | Secondary 20 | Watch | 3.48 | -4.01 | -10.21 | 3.43 | 58.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | VRRM | Secondary 20 | Watch | 3.71 | -0.51 | -11.64 | 4.35 | 6.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-09-10 America/Toronto. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
