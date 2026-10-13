# Secondary penny watchlist scan — 2026-10-13

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | HLLY | Secondary 20 | Watch | 2.54 | +3.46 | +9.70 | 2.46 | 54.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | CYH | Secondary 20 | Watch | 3.00 | +2.74 | +9.49 | 2.86 | 49.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | TYGO | Secondary 20 | Watch | 0.94 | +6.34 | +9.17 | 0.91 | 58.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | TBLA | Secondary 20 | Watch | 3.46 | +1.76 | +7.12 | 3.45 | 53.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | AISP | Secondary 20 | Watch | 2.26 | -8.13 | +7.11 | 2.04 | 61.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | VRRM | Secondary 20 | Watch | 3.02 | +3.42 | +7.09 | 3.13 | 34.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | GDRX | Secondary 20 | Watch | 3.46 | -0.57 | +5.81 | 3.35 | 60.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | AMPY | Secondary 20 | Watch | 4.62 | +2.33 | +3.01 | 4.39 | 67.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | MDXG | Secondary 20 | Watch | 4.70 | -2.79 | +1.62 | 4.70 | 44.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | ALTO | Secondary 20 | Watch | 3.75 | +2.46 | +0.00 | 3.77 | 51.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | GORO | Secondary 20 | Watch | 3.37 | -1.75 | +0.00 | 3.39 | 37.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | ARKO | Secondary 20 | Watch | 4.11 | -1.32 | -2.26 | 4.21 | 39.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | SPRO | Secondary 20 | Watch | 1.16 | -1.70 | -2.52 | 1.19 | 38.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | NAGE | Secondary 20 | Watch | 2.58 | -1.90 | -4.09 | 2.86 | 26.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | SITC | Secondary 20 | Watch | 3.06 | -0.65 | -4.38 | 3.12 | 54.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | SABR | Secondary 20 | Watch | 1.81 | -3.46 | -5.47 | 2.09 | 18.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | VFF | Secondary 20 | Watch | 2.62 | +0.00 | -6.09 | 2.87 | 25.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | ABUS | Secondary 20 | Watch | 4.12 | -0.72 | -8.04 | 4.66 | 25.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | UWMC | Secondary 20 | Watch | 1.03 | +0.98 | -14.17 | 1.19 | 30.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | AREC | Secondary 20 | Watch | 1.32 | -11.67 | -22.06 | 1.79 | 7.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-10-13 America/Phoenix. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- Mega-cap core (NVDA / MSFT / GOOGL / AAPL) is display-only in the digest top section — never the morning paper Buy.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
