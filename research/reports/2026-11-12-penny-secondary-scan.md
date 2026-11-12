# Secondary penny watchlist scan — 2026-11-12

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 19 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | AMPY | Secondary 20 | Watch | 4.02 | +4.42 | +26.41 | 4.05 | 39.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | SABR | Secondary 20 | Watch | 1.90 | +1.06 | +13.10 | 1.67 | 74.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | HLLY | Secondary 20 | Watch | 2.36 | -5.98 | +10.28 | 2.54 | 47.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | ABUS | Secondary 20 | Watch | 4.03 | +3.87 | +9.81 | 4.07 | 44.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | AREC | Secondary 20 | Watch | 1.03 | -4.19 | +8.65 | 1.11 | 44.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | ARKO | Secondary 20 | Watch | 4.10 | -3.30 | +6.22 | 3.97 | 61.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | GORO | Secondary 20 | Watch | 3.27 | -2.68 | +4.14 | 3.25 | 49.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | NAGE | Secondary 20 | Watch | 2.13 | +1.67 | +1.19 | 2.37 | 39.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | GDRX | Secondary 20 | Watch | 3.51 | -3.84 | +0.57 | 3.53 | 48.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | MDXG | Secondary 20 | Watch | 3.24 | -2.41 | -1.22 | 3.69 | 23.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | TBLA | Secondary 20 | Watch | 2.13 | +3.90 | -1.84 | 3.00 | 19.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | SPRO | Secondary 20 | Watch | 1.00 | -1.96 | -1.96 | 1.08 | 38.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | CYH | Secondary 20 | Watch | 2.21 | -3.49 | -3.07 | 2.52 | 29.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | AISP | Secondary 20 | Watch | 1.67 | +0.00 | -4.02 | 2.00 | 23.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | VFF | Secondary 20 | Watch | 2.54 | -5.58 | -8.96 | 2.67 | 48.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | TYGO | Secondary 20 | Watch | 0.64 | -5.61 | -11.88 | 0.85 | 25.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | VRRM | Secondary 20 | Watch | 1.96 | -4.85 | -15.52 | 2.70 | 15.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | UWMC | Secondary 20 | Watch | 1.28 | -5.88 | -21.47 | 1.40 | 40.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | SITC | Secondary 20 | Watch | 0.70 | +2.76 | -80.50 | 2.93 | 5.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-11-12 America/Phoenix. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Fetch errors

- ALTO: The read operation timed out

## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- Mega-cap core (NVDA / MSFT / GOOGL / AAPL) is display-only in the digest top section — never the morning paper Buy.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
