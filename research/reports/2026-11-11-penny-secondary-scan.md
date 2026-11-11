# Secondary penny watchlist scan — 2026-11-11

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | AMPY | Secondary 20 | Watch | 3.83 | +9.12 | +10.06 | 4.06 | 38.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | ALTO | Secondary 20 | Watch | 3.85 | +0.13 | +9.86 | 3.64 | 66.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | GORO | Secondary 20 | Watch | 3.37 | -3.16 | +9.42 | 3.25 | 50.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | SABR | Secondary 20 | Watch | 1.87 | +5.65 | +7.47 | 1.66 | 71.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | AREC | Secondary 20 | Watch | 1.07 | -0.92 | +7.44 | 1.12 | 47.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | ARKO | Secondary 20 | Watch | 4.25 | +0.12 | +5.07 | 3.97 | 55.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | MDXG | Secondary 20 | Watch | 3.31 | -1.78 | +3.44 | 3.76 | 24.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | GDRX | Secondary 20 | Watch | 3.62 | +2.40 | -2.55 | 3.53 | 50.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | CYH | Secondary 20 | Watch | 2.31 | +6.22 | -3.15 | 2.56 | 32.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | SPRO | Secondary 20 | Watch | 1.02 | +1.49 | -4.21 | 1.09 | 39.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | ABUS | Secondary 20 | Watch | 3.88 | +1.57 | -4.43 | 4.08 | 38.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | VFF | Secondary 20 | Watch | 2.69 | +0.75 | -8.19 | 2.67 | 49.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | AISP | Secondary 20 | Watch | 1.69 | -0.09 | -8.73 | 2.03 | 25.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | HLLY | Secondary 20 | Watch | 2.50 | -4.02 | -13.62 | 2.55 | 47.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | NAGE | Secondary 20 | Watch | 2.09 | -2.79 | -17.06 | 2.39 | 36.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | VRRM | Secondary 20 | Watch | 2.05 | -0.48 | -17.34 | 2.74 | 15.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | UWMC | Secondary 20 | Watch | 1.35 | -1.81 | -19.82 | 1.39 | 59.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | TBLA | Secondary 20 | Watch | 2.06 | +1.73 | -25.00 | 3.07 | 15.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | TYGO | Secondary 20 | Watch | 0.68 | -1.68 | -31.96 | 0.86 | 35.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | SITC | Secondary 20 | Watch | 0.67 | -1.34 | -81.97 | 3.05 | 4.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-11-11 America/Phoenix. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- Mega-cap core (NVDA / MSFT / GOOGL / AAPL) is display-only in the digest top section — never the morning paper Buy.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
