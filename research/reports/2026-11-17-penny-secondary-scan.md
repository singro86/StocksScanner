# Secondary penny watchlist scan — 2026-11-17

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | AMPY | Secondary 20 | Watch | 3.90 | -3.23 | +11.11 | 3.97 | 40.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | ABUS | Secondary 20 | Watch | 4.05 | +0.25 | +6.02 | 4.04 | 41.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | TBLA | Secondary 20 | Watch | 2.05 | -2.38 | +1.49 | 2.80 | 17.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | SITC | Secondary 20 | Watch | 0.68 | -4.70 | -0.50 | 2.50 | 4.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | AISP | Secondary 20 | Watch | 1.66 | +3.11 | -1.77 | 1.94 | 16.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | GDRX | Secondary 20 | Watch | 3.47 | -1.14 | -1.98 | 3.55 | 50.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | SABR | Secondary 20 | Watch | 1.68 | -2.33 | -5.08 | 1.69 | 55.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | NAGE | Secondary 20 | Watch | 2.04 | +1.49 | -5.12 | 2.30 | 33.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | MDXG | Secondary 20 | Watch | 3.18 | +0.00 | -5.64 | 3.51 | 16.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | HLLY | Secondary 20 | Watch | 2.46 | -1.99 | -5.75 | 2.54 | 45.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | ALTO | Secondary 20 | Watch | 3.60 | -2.17 | -6.25 | 3.66 | 46.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | CYH | Secondary 20 | Watch | 2.02 | -5.16 | -6.91 | 2.41 | 31.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | ARKO | Secondary 20 | Watch | 3.92 | -2.61 | -7.55 | 3.96 | 58.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | GORO | Secondary 20 | Watch | 3.21 | -1.23 | -7.76 | 3.22 | 46.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | SPRO | Secondary 20 | Watch | 0.90 | -4.72 | -10.76 | 1.06 | 20.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | VFF | Secondary 20 | Watch | 2.29 | -0.87 | -14.23 | 2.63 | 39.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | UWMC | Secondary 20 | Watch | 1.16 | -2.52 | -15.94 | 1.42 | 27.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | TYGO | Secondary 20 | Watch | 0.57 | +1.60 | -17.39 | 0.81 | 26.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | VRRM | Secondary 20 | Watch | 1.66 | -4.60 | -19.42 | 2.52 | 10.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | AREC | Secondary 20 | Watch | 0.84 | -6.67 | -22.22 | 1.08 | 29.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-11-17 America/Phoenix. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- Mega-cap core (NVDA / MSFT / GOOGL / AAPL) is display-only in the digest top section — never the morning paper Buy.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
