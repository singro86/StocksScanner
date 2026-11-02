# Secondary penny watchlist scan — 2026-11-02

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | UWMC | Secondary 20 | Watch | 1.57 | +0.00 | +11.35 | 1.24 | 77.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | HLLY | Secondary 20 | Watch | 2.75 | +4.56 | +7.42 | 2.53 | 61.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | VFF | Secondary 20 | Watch | 2.61 | +4.40 | +2.76 | 2.62 | 48.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | SABR | Secondary 20 | Watch | 1.67 | +3.09 | +1.83 | 1.71 | 40.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | TBLA | Secondary 20 | Watch | 3.43 | -1.01 | +1.48 | 3.43 | 47.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | ARKO | Secondary 20 | Watch | 3.85 | +1.58 | +0.26 | 4.00 | 37.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | GDRX | Secondary 20 | Watch | 3.55 | +1.72 | -0.28 | 3.46 | 55.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | AREC | Secondary 20 | Watch | 1.08 | -11.07 | -0.46 | 1.28 | 32.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | SITC | Secondary 20 | Watch | 3.67 | -1.61 | -1.34 | 3.46 | 79.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | NAGE | Secondary 20 | Watch | 2.40 | +3.00 | -1.64 | 2.54 | 38.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | SPRO | Secondary 20 | Watch | 1.04 | -1.89 | -2.80 | 1.14 | 40.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | ALTO | Secondary 20 | Watch | 3.50 | -4.11 | -4.37 | 3.64 | 33.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | ABUS | Secondary 20 | Watch | 4.00 | -4.99 | -4.76 | 4.23 | 44.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | TYGO | Secondary 20 | Watch | 0.88 | -0.71 | -6.33 | 0.90 | 45.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | AISP | Secondary 20 | Watch | 2.01 | -3.37 | -6.94 | 2.19 | 39.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | GORO | Secondary 20 | Watch | 2.81 | -11.08 | -9.94 | 3.29 | 31.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | VRRM | Secondary 20 | Watch | 2.68 | -4.29 | -13.27 | 2.97 | 39.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | AMPY | Secondary 20 | Watch | 3.84 | -10.07 | -13.71 | 4.42 | 26.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | MDXG | Secondary 20 | Watch | 3.28 | -15.46 | -14.80 | 4.24 | 15.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | CYH | Secondary 20 | Watch | 2.10 | -12.50 | -28.57 | 2.77 | 16.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-11-02 America/Phoenix. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- Mega-cap core (NVDA / MSFT / GOOGL / AAPL) is display-only in the digest top section — never the morning paper Buy.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
