---
name: trade-proposal
description: Scores candidates, validates constraints, runs wsli dry-run, and presents trade ticket for user approval. Use when user asks what to buy, rebalance, or for trade recommendations.
---

# Trade Proposal

## Pre-checks

1. Read `portfolio/profile.yaml` — paper trading, drawdown mode, limits
2. If drawdown review-only: **refuse new buys**
3. If paper trading active: dry-run only, say "Paper trading active — dry-run only"

## Steps

1. Score candidate(s) via Rebalance-MCP (garp)
2. Verify: score >= 60, weight <= 20%, sector <= 40%
3. Run `scripts/wsli/dry-run-trade.ps1 -Action buy -Ticker X -Amount CAD`
4. Present trade ticket:

```
Action | Ticker | Shares | CAD Amount | GARP Score | Rationale | Risk | Dry-run output
```

## Approval

Wait for explicit user approval before live execution. Hand off to `wsli-executor`.

## Paper trading

Log dry-run to `portfolio/paper-trading.yaml` dry_run_log; increment completed count.
