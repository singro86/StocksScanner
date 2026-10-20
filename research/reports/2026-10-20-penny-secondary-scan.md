# Secondary penny watchlist scan — 2026-10-20

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | SITC | Secondary 20 | Watch | 3.65 | +2.67 | +19.44 | 3.21 | 61.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | UWMC | Secondary 20 | Watch | 1.11 | +5.19 | +8.25 | 1.15 | 45.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | SPRO | Secondary 20 | Watch | 1.23 | +9.38 | +6.52 | 1.18 | 51.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | ABUS | Secondary 20 | Watch | 4.33 | +2.36 | +5.35 | 4.46 | 35.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | GORO | Secondary 20 | Watch | 3.47 | +2.06 | +2.97 | 3.35 | 63.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | VFF | Secondary 20 | Watch | 2.66 | +4.72 | +0.76 | 2.79 | 34.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | GDRX | Secondary 20 | Watch | 3.46 | +2.52 | +0.14 | 3.35 | 59.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | ARKO | Secondary 20 | Watch | 4.11 | +1.86 | +0.12 | 4.15 | 48.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | TBLA | Secondary 20 | Watch | 3.46 | +0.29 | +0.00 | 3.40 | 55.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | HLLY | Secondary 20 | Watch | 2.52 | +1.41 | -0.59 | 2.44 | 60.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | VRRM | Secondary 20 | Watch | 2.99 | +6.41 | -0.66 | 2.99 | 44.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | AMPY | Secondary 20 | Watch | 4.54 | +0.22 | -1.52 | 4.39 | 63.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | NAGE | Secondary 20 | Watch | 2.51 | +0.40 | -2.71 | 2.73 | 27.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | CYH | Secondary 20 | Watch | 2.88 | +4.17 | -3.85 | 2.85 | 50.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | AISP | Secondary 20 | Watch | 2.15 | +6.43 | -4.02 | 2.08 | 59.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | ALTO | Secondary 20 | Watch | 3.56 | +1.86 | -5.70 | 3.68 | 42.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | MDXG | Secondary 20 | Watch | 4.30 | -1.71 | -8.21 | 4.62 | 31.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | TYGO | Secondary 20 | Watch | 0.84 | +1.28 | -10.22 | 0.87 | 37.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | SABR | Secondary 20 | Watch | 1.57 | -4.27 | -13.26 | 1.93 | 4.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | AREC | Secondary 20 | Watch | 1.11 | -1.33 | -15.85 | 1.58 | 4.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-10-20 America/Phoenix. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- Mega-cap core (NVDA / MSFT / GOOGL / AAPL) is display-only in the digest top section — never the morning paper Buy.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
