# Secondary penny watchlist scan — 2026-11-09

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | GORO | Secondary 20 | Watch | 3.39 | +7.62 | +20.64 | 3.24 | 49.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | ALTO | Secondary 20 | Watch | 3.82 | +2.14 | +9.14 | 3.63 | 66.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | ARKO | Secondary 20 | Watch | 4.20 | +5.79 | +9.09 | 3.95 | 55.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | VFF | Secondary 20 | Watch | 2.84 | -1.39 | +8.81 | 2.66 | 57.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | AREC | Secondary 20 | Watch | 1.17 | +7.34 | +7.83 | 1.14 | 54.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | SABR | Secondary 20 | Watch | 1.80 | +6.83 | +7.78 | 1.66 | 66.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | CYH | Secondary 20 | Watch | 2.26 | +2.26 | +7.62 | 2.63 | 31.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | SPRO | Secondary 20 | Watch | 1.07 | +3.88 | +2.88 | 1.10 | 35.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | GDRX | Secondary 20 | Watch | 3.65 | +3.99 | +2.82 | 3.51 | 55.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | MDXG | Secondary 20 | Watch | 3.32 | +0.30 | +1.22 | 3.89 | 24.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | NAGE | Secondary 20 | Watch | 2.28 | +10.14 | -5.00 | 2.43 | 42.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | HLLY | Secondary 20 | Watch | 2.61 | +24.29 | -5.09 | 2.55 | 52.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | UWMC | Secondary 20 | Watch | 1.48 | -2.63 | -5.73 | 1.36 | 68.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | ABUS | Secondary 20 | Watch | 3.72 | +1.64 | -7.00 | 4.11 | 28.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | TYGO | Secondary 20 | Watch | 0.76 | +3.40 | -13.34 | 0.88 | 45.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | AISP | Secondary 20 | Watch | 1.73 | -3.35 | -13.93 | 2.08 | 31.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | AMPY | Secondary 20 | Watch | 3.20 | -3.90 | -16.67 | 4.14 | 18.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | VRRM | Secondary 20 | Watch | 2.13 | -2.74 | -20.52 | 2.84 | 25.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | TBLA | Secondary 20 | Watch | 2.15 | +7.50 | -37.32 | 3.21 | 16.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | SITC | Secondary 20 | Watch | 0.67 | +0.79 | -81.65 | 3.29 | 7.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-11-09 America/Phoenix. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- Mega-cap core (NVDA / MSFT / GOOGL / AAPL) is display-only in the digest top section — never the morning paper Buy.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
