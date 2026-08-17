---
name: rotation-analyzer
description: Compares hold vs candidate swap using Rebalance-MCP compare_swaps and run_backtest. Use when user asks should I swap X for Y or rotate holdings.
---

# Rotation Analyzer

## Steps

1. Score both tickers via Rebalance-MCP `score_tickers` (garp preset)
2. Run `compare_swaps` — require delta >= 15 (from profile.yaml)
3. Run `run_backtest` on proposed swap if delta passes
4. Check sector concentration (max 40%) and single-stock limit (20%)

## Output

```markdown
## Swap Analysis: {HOLD} → {CANDIDATE}

- Hold score: XX | Candidate score: YY | Delta: ZZ
- Swap recommended: Yes/No (delta >= 15 required)
- Backtest summary: [from Rebalance-MCP]
- Risk: [concentration, sector, tax in TFSA N/A]
```

## If recommended

Hand off to `trade-proposal` for dry-run sell + buy tickets.
