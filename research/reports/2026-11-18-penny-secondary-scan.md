# Secondary penny watchlist scan — 2026-11-18

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | ABUS | Secondary 20 | Watch | 4.11 | +1.48 | +5.93 | 4.04 | 44.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | AMPY | Secondary 20 | Watch | 3.98 | +2.05 | +3.38 | 3.95 | 43.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | SITC | Secondary 20 | Watch | 0.68 | +0.47 | +0.34 | 2.35 | 4.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | GORO | Secondary 20 | Watch | 3.32 | +3.43 | -1.19 | 3.21 | 51.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | TBLA | Secondary 20 | Watch | 2.02 | -1.46 | -1.46 | 2.73 | 16.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | HLLY | Secondary 20 | Watch | 2.47 | +0.41 | -1.59 | 2.54 | 45.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | AISP | Secondary 20 | Watch | 1.60 | -3.61 | -4.19 | 1.90 | 15.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | MDXG | Secondary 20 | Watch | 3.18 | +0.00 | -4.22 | 3.49 | 15.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | NAGE | Secondary 20 | Watch | 1.94 | -4.90 | -7.62 | 2.27 | 32.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | GDRX | Secondary 20 | Watch | 3.36 | -3.17 | -7.95 | 3.54 | 43.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | SABR | Secondary 20 | Watch | 1.71 | +1.79 | -9.04 | 1.69 | 54.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | ARKO | Secondary 20 | Watch | 3.73 | -4.85 | -12.03 | 3.94 | 48.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | ALTO | Secondary 20 | Watch | 3.33 | -7.64 | -13.41 | 3.65 | 35.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | UWMC | Secondary 20 | Watch | 1.17 | +0.86 | -13.97 | 1.42 | 28.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | SPRO | Secondary 20 | Watch | 0.87 | -3.00 | -14.31 | 1.04 | 21.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | TYGO | Secondary 20 | Watch | 0.57 | -0.54 | -15.89 | 0.80 | 23.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | VRRM | Secondary 20 | Watch | 1.72 | +3.61 | -16.50 | 2.46 | 3.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | CYH | Secondary 20 | Watch | 1.86 | -7.92 | -18.78 | 2.36 | 32.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | VFF | Secondary 20 | Watch | 2.17 | -5.24 | -19.33 | 2.60 | 36.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | AREC | Secondary 20 | Watch | 0.85 | +1.71 | -20.52 | 1.07 | 26.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-11-18 America/Phoenix. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- Mega-cap core (NVDA / MSFT / GOOGL / AAPL) is display-only in the digest top section — never the morning paper Buy.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
