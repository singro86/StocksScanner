# Secondary penny watchlist scan — 2026-10-23

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | UWMC | Secondary 20 | Watch | 1.34 | +16.52 | +27.62 | 1.15 | 53.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | TYGO | Secondary 20 | Watch | 1.01 | +9.61 | +23.03 | 0.88 | 68.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | VRRM | Secondary 20 | Watch | 3.10 | -1.11 | +8.57 | 2.95 | 62.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | SITC | Secondary 20 | Watch | 3.71 | -0.67 | +8.31 | 3.31 | 73.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | AISP | Secondary 20 | Watch | 2.17 | +0.70 | +5.61 | 2.13 | 55.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | GDRX | Secondary 20 | Watch | 3.52 | -2.86 | +4.66 | 3.39 | 57.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | ALTO | Secondary 20 | Watch | 3.60 | +0.42 | +4.49 | 3.66 | 39.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | AMPY | Secondary 20 | Watch | 4.56 | +2.94 | +2.94 | 4.42 | 55.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | VFF | Secondary 20 | Watch | 2.58 | -4.61 | +2.17 | 2.73 | 42.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | SPRO | Secondary 20 | Watch | 1.10 | -2.21 | +0.46 | 1.17 | 44.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | CYH | Secondary 20 | Watch | 2.88 | -0.86 | +0.17 | 2.84 | 57.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | AREC | Secondary 20 | Watch | 1.14 | +2.70 | +0.00 | 1.46 | 8.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | TBLA | Secondary 20 | Watch | 3.43 | -1.15 | -0.29 | 3.40 | 59.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | ABUS | Secondary 20 | Watch | 4.20 | -0.24 | -0.47 | 4.36 | 30.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | HLLY | Secondary 20 | Watch | 2.48 | -4.81 | -0.60 | 2.45 | 60.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | NAGE | Secondary 20 | Watch | 2.43 | -3.57 | -2.41 | 2.65 | 30.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | GORO | Secondary 20 | Watch | 3.30 | -1.49 | -2.65 | 3.32 | 52.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | ARKO | Secondary 20 | Watch | 3.91 | -4.52 | -4.63 | 4.11 | 31.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | SABR | Secondary 20 | Watch | 1.52 | -0.97 | -9.23 | 1.83 | 9.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | MDXG | Secondary 20 | Watch | 3.87 | -1.53 | -12.64 | 4.49 | 29.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-10-23 America/Phoenix. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- Mega-cap core (NVDA / MSFT / GOOGL / AAPL) is display-only in the digest top section — never the morning paper Buy.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
