# Secondary penny watchlist scan — 2026-10-12

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | AISP | Secondary 20 | Watch | 2.46 | +1.65 | +21.78 | 2.03 | 69.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | HLLY | Secondary 20 | Watch | 2.46 | -1.21 | +7.42 | 2.47 | 36.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | MDXG | Secondary 20 | Watch | 4.83 | +3.43 | +6.15 | 4.70 | 42.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | CYH | Secondary 20 | Watch | 2.92 | +5.80 | +5.80 | 2.86 | 43.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | GORO | Secondary 20 | Watch | 3.43 | +0.59 | +5.54 | 3.40 | 44.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | TBLA | Secondary 20 | Watch | 3.40 | -1.45 | +3.98 | 3.47 | 41.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | GDRX | Secondary 20 | Watch | 3.48 | +1.46 | +3.57 | 3.35 | 52.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | TYGO | Secondary 20 | Watch | 0.89 | -0.11 | +2.90 | 0.91 | 37.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | AMPY | Secondary 20 | Watch | 4.51 | +1.12 | +1.81 | 4.41 | 64.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | VRRM | Secondary 20 | Watch | 2.92 | -0.68 | +1.74 | 3.16 | 26.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | SPRO | Secondary 20 | Watch | 1.18 | -1.67 | +1.72 | 1.19 | 32.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | ARKO | Secondary 20 | Watch | 4.16 | +1.22 | -1.19 | 4.22 | 35.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | NAGE | Secondary 20 | Watch | 2.63 | -2.23 | -1.87 | 2.88 | 25.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | SABR | Secondary 20 | Watch | 1.88 | -1.05 | -2.59 | 2.10 | 18.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | ALTO | Secondary 20 | Watch | 3.66 | -1.88 | -3.43 | 3.79 | 38.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | VFF | Secondary 20 | Watch | 2.62 | -2.24 | -3.68 | 2.88 | 30.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | SITC | Secondary 20 | Watch | 3.10 | -2.21 | -9.36 | 3.10 | 53.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | ABUS | Secondary 20 | Watch | 4.15 | -1.66 | -11.13 | 4.71 | 23.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | AREC | Secondary 20 | Watch | 1.50 | -5.66 | -13.79 | 1.82 | 7.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | UWMC | Secondary 20 | Watch | 1.02 | -5.56 | -20.93 | 1.21 | 26.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-10-12 America/Denver. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- Mega-cap core (NVDA / MSFT / GOOGL / AAPL) is display-only in the digest top section — never the morning paper Buy.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
