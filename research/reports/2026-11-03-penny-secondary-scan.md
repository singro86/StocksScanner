# Secondary penny watchlist scan — 2026-11-03

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | VFF | Secondary 20 | Watch | 2.87 | +9.77 | +10.62 | 2.63 | 64.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | SABR | Secondary 20 | Watch | 1.70 | +1.50 | +8.65 | 1.70 | 44.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | HLLY | Secondary 20 | Watch | 2.75 | -0.18 | +6.39 | 2.55 | 65.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | UWMC | Secondary 20 | Watch | 1.61 | +2.55 | +3.21 | 1.26 | 79.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | GDRX | Secondary 20 | Watch | 3.50 | -1.27 | +0.72 | 3.47 | 56.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | ARKO | Secondary 20 | Watch | 3.87 | +0.39 | +0.39 | 3.98 | 40.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | TBLA | Secondary 20 | Watch | 3.38 | -1.31 | -0.15 | 3.44 | 47.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | SITC | Secondary 20 | Watch | 3.67 | +0.00 | -2.39 | 3.48 | 82.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | ALTO | Secondary 20 | Watch | 3.57 | +2.00 | -4.03 | 3.63 | 42.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | TYGO | Secondary 20 | Watch | 0.90 | +2.22 | -6.22 | 0.90 | 52.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | NAGE | Secondary 20 | Watch | 2.34 | -2.34 | -6.25 | 2.52 | 38.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | SPRO | Secondary 20 | Watch | 1.04 | +0.48 | -8.33 | 1.13 | 43.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | ABUS | Secondary 20 | Watch | 3.92 | -1.88 | -8.51 | 4.20 | 36.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | AREC | Secondary 20 | Watch | 1.06 | -2.30 | -9.40 | 1.25 | 36.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | AISP | Secondary 20 | Watch | 2.04 | +1.49 | -10.92 | 2.18 | 46.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | AMPY | Secondary 20 | Watch | 3.81 | -0.89 | -11.90 | 4.38 | 30.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | GORO | Secondary 20 | Watch | 2.75 | -2.31 | -14.22 | 3.26 | 33.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | VRRM | Secondary 20 | Watch | 2.67 | -0.19 | -14.81 | 2.97 | 41.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | MDXG | Secondary 20 | Watch | 3.17 | -3.20 | -18.59 | 4.17 | 14.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | CYH | Secondary 20 | Watch | 2.12 | +0.71 | -25.53 | 2.73 | 17.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-11-03 America/Phoenix. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- Mega-cap core (NVDA / MSFT / GOOGL / AAPL) is display-only in the digest top section — never the morning paper Buy.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
