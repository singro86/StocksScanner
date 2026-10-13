# Market movers scan — 2026-10-12

**Gate:** Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.

Official Rebalance-MCP GARP scores are not computed in this job. A live ticket still needs GARP ≥ 60.

Universe: Yahoo `day_gainers` / `day_losers` / `most_actives` + holdings/watchlist overlay. Showing top 10 of 65 candidates.

| Rec | Count |
|-----|------:|
| Buy (paper) | 2 |
| Buy | 0 |
| Sell | 0 |
| Hold | 14 |
| Watch | 29 |
| Avoid | 20 |

| # | Ticker | Rec | Price | 1d | 5d | RelVol | RSI | Source | Why |
|--:|--------|-----|------:|---:|---:|-------:|----:|--------|-----|
| 1 | MANH | Buy (paper) | $217.89 | +6.34% | +6.05% | 2.04 | 62.1 | day_gainers | Liquid mover above SMA20 with volume confirmation. Paper ticket only — GARP ≥ 60 still required before any live buy. |
| 2 | FIZZ | Buy (paper) | $32.15 | +5.34% | +7.74% | 1.54 | 57.0 | day_gainers | Liquid mover above SMA20 with volume confirmation. Paper ticket only — GARP ≥ 60 still required before any live buy. |
| 3 | FIGS | Watch | $17.74 | +12.42% | +30.15% | 3.28 | 78.7 | day_gainers | Extended or overbought — wait for a cleaner entry. |
| 4 | TTMI | Avoid | $110.33 | -8.83% | -17.13% | 2.55 | 33.4 | day_losers | Sharp drop below SMA20 and not held — do not catch the knife from this scan. |
| 5 | MMED | Avoid | $18.80 | -4.62% | -6.75% | 4.64 | 30.6 | most_actives | Sharp drop below SMA20 and not held — do not catch the knife from this scan. |
| 6 | FICO | Watch | $740.00 | +10.85% | +7.31% | 1.64 | 35.2 | day_gainers | On the move but signals mixed — research only until GARP ≥ 60. |
| 7 | SMTC | Avoid | $168.28 | -10.15% | -12.73% | 1.73 | 46.4 | day_losers | Sharp drop below SMA20 and not held — do not catch the knife from this scan. |
| 8 | NESR | Avoid | $20.90 | -8.25% | -13.21% | 1.70 | 3.3 | day_losers | Sharp drop below SMA20 and not held — do not catch the knife from this scan. |
| 9 | LITE | Watch | $995.41 | -9.78% | -8.82% | 1.32 | 54.8 | day_losers | On the move but signals mixed — research only until GARP ≥ 60. |
| 10 | IONQ | Avoid | $36.27 | -9.07% | -15.59% | 1.31 | 35.8 | day_losers+most_actives | Sharp drop below SMA20 and not held — do not catch the knife from this scan. |

## Disclaimer

I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. This job never calls wsli and never sets TRADE_APPROVED.
