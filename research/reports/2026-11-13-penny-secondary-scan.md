# Secondary penny watchlist scan — 2026-11-13

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | AMPY | Secondary 20 | Watch | 4.06 | +0.99 | +21.92 | 4.03 | 42.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | HLLY | Secondary 20 | Watch | 2.47 | +4.66 | +17.62 | 2.54 | 47.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | ABUS | Secondary 20 | Watch | 4.08 | +1.12 | +11.34 | 4.06 | 46.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | SABR | Secondary 20 | Watch | 1.86 | -1.84 | +10.68 | 1.68 | 66.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | TBLA | Secondary 20 | Watch | 2.19 | +3.05 | +9.75 | 2.94 | 22.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | CYH | Secondary 20 | Watch | 2.29 | +3.85 | +3.85 | 2.49 | 32.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | GDRX | Secondary 20 | Watch | 3.58 | +2.14 | +2.14 | 3.54 | 50.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | SITC | Secondary 20 | Watch | 0.67 | -3.08 | +0.75 | 2.80 | 5.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | ARKO | Secondary 20 | Watch | 3.98 | -2.81 | +0.38 | 3.96 | 55.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | GORO | Secondary 20 | Watch | 3.16 | -3.66 | +0.32 | 3.24 | 51.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | NAGE | Secondary 20 | Watch | 2.07 | -3.27 | +0.00 | 2.35 | 37.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | SPRO | Secondary 20 | Watch | 1.01 | +0.84 | -2.10 | 1.08 | 43.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | ALTO | Secondary 20 | Watch | 3.63 | -2.05 | -2.83 | 3.65 | 48.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | MDXG | Secondary 20 | Watch | 3.17 | -2.31 | -4.38 | 3.62 | 22.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | AREC | Secondary 20 | Watch | 1.02 | -0.48 | -5.96 | 1.11 | 46.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | AISP | Secondary 20 | Watch | 1.60 | -3.89 | -10.34 | 1.98 | 22.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | VFF | Secondary 20 | Watch | 2.43 | -4.33 | -15.62 | 2.66 | 45.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | VRRM | Secondary 20 | Watch | 1.83 | -6.63 | -16.44 | 2.64 | 14.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | UWMC | Secondary 20 | Watch | 1.25 | -1.18 | -17.43 | 1.41 | 40.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | TYGO | Secondary 20 | Watch | 0.60 | -5.47 | -18.20 | 0.84 | 27.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-11-13 America/Phoenix. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- Mega-cap core (NVDA / MSFT / GOOGL / AAPL) is display-only in the digest top section — never the morning paper Buy.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
