# Secondary penny watchlist scan — 2026-11-07

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | VFF | Secondary 20 | Watch | 2.88 | +3.23 | +15.20 | 2.65 | 63.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | ARKO | Secondary 20 | Watch | 3.97 | +2.85 | +4.75 | 3.95 | 47.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | SABR | Secondary 20 | Watch | 1.69 | +0.30 | +4.01 | 1.66 | 53.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | ALTO | Secondary 20 | Watch | 3.74 | +1.91 | +2.47 | 3.62 | 65.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | GDRX | Secondary 20 | Watch | 3.51 | +0.57 | +0.57 | 3.50 | 56.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | GORO | Secondary 20 | Watch | 3.15 | +0.32 | -0.32 | 3.24 | 41.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | SPRO | Secondary 20 | Watch | 1.03 | +0.98 | -2.83 | 1.11 | 42.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | UWMC | Secondary 20 | Watch | 1.52 | -6.75 | -3.19 | 1.33 | 72.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | CYH | Secondary 20 | Watch | 2.21 | -3.07 | -7.92 | 2.66 | 33.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | AREC | Secondary 20 | Watch | 1.09 | +14.98 | -10.66 | 1.16 | 47.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | NAGE | Secondary 20 | Watch | 2.07 | -1.90 | -11.16 | 2.45 | 32.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | ABUS | Secondary 20 | Watch | 3.66 | -0.27 | -13.06 | 4.13 | 30.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | AISP | Secondary 20 | Watch | 1.79 | +2.87 | -13.94 | 2.11 | 40.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | MDXG | Secondary 20 | Watch | 3.31 | +0.92 | -14.69 | 3.97 | 22.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | TYGO | Secondary 20 | Watch | 0.73 | +1.80 | -16.76 | 0.89 | 44.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | HLLY | Secondary 20 | Watch | 2.10 | -1.87 | -20.15 | 2.54 | 38.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | VRRM | Secondary 20 | Watch | 2.19 | -5.60 | -21.79 | 2.88 | 33.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | AMPY | Secondary 20 | Watch | 3.33 | +4.72 | -22.01 | 4.21 | 19.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | TBLA | Secondary 20 | Watch | 2.00 | -7.83 | -42.28 | 3.27 | 9.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | SITC | Secondary 20 | Watch | 0.67 | -81.29 | -82.09 | 3.41 | 9.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-11-07 America/Phoenix. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- Mega-cap core (NVDA / MSFT / GOOGL / AAPL) is display-only in the digest top section — never the morning paper Buy.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
