# Secondary penny watchlist scan — 2026-09-02

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | AMPY | Secondary 20 | Watch | 4.99 | +0.00 | +6.85 | 4.62 | 71.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | MDXG | Secondary 20 | Watch | 4.58 | +1.22 | +5.42 | 4.34 | 63.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | ALTO | Secondary 20 | Watch | 4.17 | +3.86 | +4.64 | 4.23 | 54.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | TBLA | Secondary 20 | Watch | 3.84 | +2.95 | +3.78 | 3.86 | 48.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | GDRX | Secondary 20 | Watch | 3.55 | +2.60 | +2.16 | 3.58 | 47.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | VFF | Secondary 20 | Watch | 2.93 | +3.17 | +1.74 | 2.57 | 76.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | TYGO | Secondary 20 | Watch | 1.06 | +0.00 | +0.95 | 1.15 | 28.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | ARKO | Secondary 20 | Watch | 4.71 | +4.67 | +0.86 | 4.96 | 58.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | HLLY | Secondary 20 | Watch | 2.89 | +0.70 | +0.00 | 3.03 | 37.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | ABUS | Secondary 20 | Watch | 5.14 | +1.08 | -1.06 | 4.87 | 72.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | SPRO | Secondary 20 | Watch | 1.22 | +1.25 | -1.22 | 1.22 | 54.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | SITC | Secondary 20 | Watch | 2.98 | +2.93 | -1.49 | 3.01 | 46.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | CYH | Secondary 20 | Watch | 2.90 | -0.85 | -2.19 | 2.95 | 49.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | GORO | Secondary 20 | Watch | 3.76 | +5.03 | -2.84 | 3.02 | 71.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | NAGE | Secondary 20 | Watch | 3.17 | +1.44 | -2.90 | 3.12 | 60.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | UWMC | Secondary 20 | Watch | 1.45 | +5.84 | -3.97 | 1.47 | 46.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | VRRM | Secondary 20 | Watch | 4.21 | +1.08 | -4.85 | 4.64 | 30.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | AISP | Secondary 20 | Watch | 2.11 | +2.93 | -6.22 | 2.06 | 52.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | SABR | Secondary 20 | Watch | 2.08 | +3.73 | -7.74 | 2.13 | 51.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | AREC | Secondary 20 | Watch | 2.38 | +3.03 | -10.86 | 2.63 | 35.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-09-02 America/Toronto. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
