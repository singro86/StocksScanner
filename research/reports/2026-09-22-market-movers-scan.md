# Market movers scan — 2026-09-22

**Gate:** Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.

Official Rebalance-MCP GARP scores are not computed in this job. A live ticket still needs GARP ≥ 60.

Universe: Yahoo `day_gainers` / `day_losers` / `most_actives` + holdings/watchlist overlay. Showing top 10 of 63 candidates.

| Rec | Count |
|-----|------:|
| Buy (paper) | 2 |
| Buy | 0 |
| Sell | 0 |
| Hold | 10 |
| Watch | 37 |
| Avoid | 14 |

| # | Ticker | Rec | Price | 1d | 5d | RelVol | RSI | Source | Why |
|--:|--------|-----|------:|---:|---:|-------:|----:|--------|-----|
| 1 | VKTX | Buy (paper) | $39.13 | +29.95% | +30.65% | 9.19 | 65.5 | day_gainers+most_actives | Liquid mover above SMA20 with volume confirmation. Paper ticket only — GARP ≥ 60 still required before any live buy. |
| 2 | ONON | Buy (paper) | $29.70 | +8.69% | +10.97% | 3.42 | 65.0 | day_gainers+most_actives | Liquid mover above SMA20 with volume confirmation. Paper ticket only — GARP ≥ 60 still required before any live buy. |
| 3 | CLDX | Avoid | $35.17 | -7.18% | -8.67% | 8.22 | 30.9 | day_losers | Sharp drop below SMA20 and not held — do not catch the knife from this scan. |
| 4 | INOD | Watch | $71.02 | +16.33% | +30.62% | 2.01 | 83.0 | day_gainers | Extended or overbought — wait for a cleaner entry. |
| 5 | VICR | Watch | $265.11 | +18.41% | +44.10% | 1.66 | 79.1 | day_gainers | Extended or overbought — wait for a cleaner entry. |
| 6 | SGRY | Watch | $15.61 | +14.28% | +14.36% | 2.02 | 58.9 | day_gainers | Buy trimmed — max 2 paper candidates per morning. |
| 7 | PLNT | Avoid | $42.46 | -9.76% | -16.43% | 2.23 | 19.2 | day_losers | Sharp drop below SMA20 and not held — do not catch the knife from this scan. |
| 8 | SRAD | Watch | $13.72 | +9.41% | +3.08% | 2.17 | 64.7 | day_gainers | Buy trimmed — max 2 paper candidates per morning. |
| 9 | LPLA | Avoid | $309.45 | -6.87% | -9.45% | 2.60 | 20.0 | day_losers | Sharp drop below SMA20 and not held — do not catch the knife from this scan. |
| 10 | WGS | Avoid | $89.70 | -8.30% | -5.21% | 1.94 | 55.6 | day_losers | Sharp drop below SMA20 and not held — do not catch the knife from this scan. |

## Fetch errors

- SQ: HTTP Error 404: Not Found

## Disclaimer

I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. This job never calls wsli and never sets TRADE_APPROVED.
