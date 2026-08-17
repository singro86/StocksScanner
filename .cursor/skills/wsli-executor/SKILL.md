---
name: wsli-executor
description: Executes approved wsli trades after dry-run — dry-run confirm, live buy/sell with TRADE_APPROVED gate, logs to transactions.log.md. Use when user approves execute the trade after trade proposal.
---

# wsli Executor

## Prerequisites

- User explicitly approved trade in chat
- Dry-run already completed and shown
- `paper_trading_complete: true` for live trades (else dry-run only)
- Not in drawdown review-only mode (for buys)
- `PAUSE_ALL_TRADING` not set

## Live execution steps

1. Confirm trade details with user one final time
2. Set environment: `TRADE_APPROVED=true` for this command only
3. Run `scripts/wsli/execute-trade.ps1 -Action buy|sell -Ticker X -Shares N`
4. Append to `portfolio/transactions.log.md`
5. Run `scripts/wsli/sync-portfolio.ps1`
6. Update `portfolio/peak-value.yaml` if new high

## Paper trading mode

Run dry-run only via `scripts/wsli/dry-run-trade.ps1`; do not set TRADE_APPROVED.

## Log format (transactions.log.md)

```markdown
## YYYY-MM-DD HH:MM — BUY MSFT — 2 shares — $900 CAD — GARP 78 — Approved by user
```

Remind ToS warning on first live trade of session.
