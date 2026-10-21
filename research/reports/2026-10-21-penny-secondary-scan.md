# Secondary penny watchlist scan — 2026-10-21

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | SITC | Secondary 20 | Watch | 3.68 | +1.10 | +21.85 | 3.24 | 57.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | UWMC | Secondary 20 | Watch | 1.11 | +0.91 | +9.90 | 1.14 | 43.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | AISP | Secondary 20 | Watch | 2.31 | +6.71 | +9.76 | 2.10 | 53.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | VFF | Secondary 20 | Watch | 2.79 | +4.70 | +8.79 | 2.78 | 46.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | GDRX | Secondary 20 | Watch | 3.60 | +2.42 | +6.66 | 3.37 | 66.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | GORO | Secondary 20 | Watch | 3.42 | +0.15 | +6.06 | 3.33 | 61.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | SPRO | Secondary 20 | Watch | 1.18 | -3.28 | +5.36 | 1.18 | 42.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | AMPY | Secondary 20 | Watch | 4.43 | -1.77 | +2.07 | 4.40 | 52.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | TBLA | Secondary 20 | Watch | 3.46 | +0.43 | +1.32 | 3.40 | 58.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | HLLY | Secondary 20 | Watch | 2.49 | -1.19 | +0.40 | 2.44 | 57.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | ABUS | Secondary 20 | Watch | 4.20 | -3.00 | +0.24 | 4.43 | 37.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | ARKO | Secondary 20 | Watch | 4.01 | -0.37 | -0.62 | 4.14 | 42.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | VRRM | Secondary 20 | Watch | 2.92 | -2.99 | -0.68 | 2.96 | 46.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | ALTO | Secondary 20 | Watch | 3.62 | +1.69 | -2.16 | 3.67 | 47.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | TYGO | Secondary 20 | Watch | 0.85 | +0.45 | -2.77 | 0.87 | 42.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | NAGE | Secondary 20 | Watch | 2.45 | -2.39 | -3.16 | 2.70 | 34.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | CYH | Secondary 20 | Watch | 2.85 | +0.17 | -4.20 | 2.84 | 57.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | AREC | Secondary 20 | Watch | 1.10 | +0.46 | -9.43 | 1.54 | 3.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | SABR | Secondary 20 | Watch | 1.52 | -2.87 | -14.33 | 1.90 | 5.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | MDXG | Secondary 20 | Watch | 3.85 | -8.87 | -17.98 | 4.57 | 21.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-10-21 America/Phoenix. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- Mega-cap core (NVDA / MSFT / GOOGL / AAPL) is display-only in the digest top section — never the morning paper Buy.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
