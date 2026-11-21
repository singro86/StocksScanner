# Secondary penny watchlist scan — 2026-11-21

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | SITC | Secondary 20 | Watch | 0.66 | -3.92 | -0.03 | 2.05 | 4.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | ABUS | Secondary 20 | Watch | 4.02 | -1.23 | -1.71 | 4.02 | 50.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | MDXG | Secondary 20 | Watch | 3.05 | -1.93 | -4.98 | 3.40 | 29.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | HLLY | Secondary 20 | Watch | 2.29 | -7.66 | -7.66 | 2.52 | 39.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | AMPY | Secondary 20 | Watch | 3.70 | -7.73 | -9.09 | 3.88 | 47.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | GORO | Secondary 20 | Watch | 2.92 | +2.10 | -9.32 | 3.17 | 53.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | TYGO | Secondary 20 | Watch | 0.54 | -5.91 | -9.98 | 0.75 | 25.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | AISP | Secondary 20 | Watch | 1.44 | -5.88 | -10.00 | 1.83 | 17.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | NAGE | Secondary 20 | Watch | 1.84 | -1.60 | -11.11 | 2.21 | 30.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | SABR | Secondary 20 | Watch | 1.64 | -7.87 | -11.83 | 1.71 | 48.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | UWMC | Secondary 20 | Watch | 1.11 | +1.83 | -11.90 | 1.40 | 19.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | AREC | Secondary 20 | Watch | 0.91 | +2.03 | -12.14 | 1.05 | 38.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | VRRM | Secondary 20 | Watch | 1.60 | -5.33 | -13.04 | 2.31 | 5.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | TBLA | Secondary 20 | Watch | 1.86 | +0.54 | -16.59 | 2.57 | 16.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | VFF | Secondary 20 | Watch | 2.01 | -3.37 | -16.94 | 2.54 | 29.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | GDRX | Secondary 20 | Watch | 2.92 | -3.31 | -17.98 | 3.47 | 31.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | ALTO | Secondary 20 | Watch | 2.98 | -3.25 | -18.58 | 3.59 | 30.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | ARKO | Secondary 20 | Watch | 3.21 | +0.00 | -19.75 | 3.87 | 32.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | SPRO | Secondary 20 | Watch | 0.74 | -10.17 | -25.80 | 1.01 | 18.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | CYH | Secondary 20 | Watch | 1.62 | +0.62 | -27.68 | 2.23 | 34.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-11-21 America/Phoenix. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- Mega-cap core (NVDA / MSFT / GOOGL / AAPL) is display-only in the digest top section — never the morning paper Buy.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
