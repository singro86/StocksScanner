# Secondary penny watchlist scan — 2026-10-29

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | UWMC | Secondary 20 | Watch | 1.56 | +4.00 | +35.65 | 1.21 | 73.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | AREC | Secondary 20 | Watch | 1.31 | +7.36 | +18.00 | 1.34 | 32.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | SABR | Secondary 20 | Watch | 1.66 | +3.44 | +7.47 | 1.74 | 33.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | VRRM | Secondary 20 | Watch | 3.33 | +5.89 | +5.89 | 2.98 | 68.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | TYGO | Secondary 20 | Watch | 0.95 | +2.88 | +2.99 | 0.90 | 56.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | TBLA | Secondary 20 | Watch | 3.55 | +1.93 | +2.22 | 3.41 | 57.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | HLLY | Secondary 20 | Watch | 2.65 | +0.57 | +2.12 | 2.49 | 59.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | SITC | Secondary 20 | Watch | 3.81 | +0.66 | +2.00 | 3.42 | 88.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | AISP | Secondary 20 | Watch | 2.19 | -3.52 | +1.86 | 2.19 | 40.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | ABUS | Secondary 20 | Watch | 4.26 | -1.27 | +1.31 | 4.27 | 52.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | ALTO | Secondary 20 | Watch | 3.63 | -0.68 | +1.25 | 3.66 | 44.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | NAGE | Secondary 20 | Watch | 2.52 | -0.98 | -0.20 | 2.57 | 36.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | MDXG | Secondary 20 | Watch | 3.91 | -1.01 | -0.51 | 4.34 | 27.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | SPRO | Secondary 20 | Watch | 1.12 | -4.27 | -0.89 | 1.15 | 42.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | GDRX | Secondary 20 | Watch | 3.54 | +1.87 | -2.35 | 3.44 | 55.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | AMPY | Secondary 20 | Watch | 4.30 | -1.94 | -2.82 | 4.45 | 44.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | GORO | Secondary 20 | Watch | 3.25 | -1.96 | -2.84 | 3.32 | 43.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | VFF | Secondary 20 | Watch | 2.58 | +0.19 | -4.61 | 2.64 | 43.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | ARKO | Secondary 20 | Watch | 3.71 | +0.41 | -9.52 | 4.03 | 29.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | CYH | Secondary 20 | Watch | 2.35 | -11.47 | -19.07 | 2.81 | 34.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-10-29 America/Phoenix. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- Mega-cap core (NVDA / MSFT / GOOGL / AAPL) is display-only in the digest top section — never the morning paper Buy.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
