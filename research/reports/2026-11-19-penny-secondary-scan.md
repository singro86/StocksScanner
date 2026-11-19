# Secondary penny watchlist scan — 2026-11-19

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | HLLY | Secondary 20 | Watch | 2.48 | +0.41 | +5.08 | 2.53 | 46.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | ABUS | Secondary 20 | Watch | 4.07 | -0.97 | +0.99 | 4.03 | 45.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | AMPY | Secondary 20 | Watch | 4.01 | +0.75 | -0.25 | 3.93 | 44.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | SITC | Secondary 20 | Watch | 0.68 | +0.59 | -1.53 | 2.20 | 4.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | MDXG | Secondary 20 | Watch | 3.11 | -2.20 | -4.01 | 3.44 | 15.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | SABR | Secondary 20 | Watch | 1.78 | +4.09 | -6.32 | 1.71 | 60.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | AISP | Secondary 20 | Watch | 1.53 | -4.38 | -8.38 | 1.87 | 17.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | TYGO | Secondary 20 | Watch | 0.57 | +1.36 | -9.64 | 0.78 | 26.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | NAGE | Secondary 20 | Watch | 1.87 | -3.61 | -12.62 | 2.24 | 34.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | GORO | Secondary 20 | Watch | 2.86 | -13.86 | -12.80 | 3.19 | 42.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | TBLA | Secondary 20 | Watch | 1.85 | -8.42 | -13.15 | 2.65 | 15.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | VRRM | Secondary 20 | Watch | 1.69 | -1.74 | -13.78 | 2.39 | 4.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | AREC | Secondary 20 | Watch | 0.89 | +3.88 | -13.87 | 1.06 | 30.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | GDRX | Secondary 20 | Watch | 3.02 | -10.12 | -13.96 | 3.51 | 36.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | UWMC | Secondary 20 | Watch | 1.09 | -6.84 | -14.17 | 1.42 | 17.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | ALTO | Secondary 20 | Watch | 3.08 | -7.51 | -16.98 | 3.62 | 29.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | SPRO | Secondary 20 | Watch | 0.83 | -5.46 | -17.37 | 1.03 | 21.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | VFF | Secondary 20 | Watch | 2.08 | -4.15 | -18.11 | 2.57 | 36.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | ARKO | Secondary 20 | Watch | 3.21 | -13.94 | -21.71 | 3.90 | 34.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | CYH | Secondary 20 | Watch | 1.61 | -13.44 | -27.15 | 2.30 | 28.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-11-19 America/Phoenix. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- Mega-cap core (NVDA / MSFT / GOOGL / AAPL) is display-only in the digest top section — never the morning paper Buy.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
