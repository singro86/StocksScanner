---
name: bull-bear-debate
description: Produces structured bull vs bear investment case using Equibles fundamentals and GARP valuation guardrails. Use when user asks should I buy X, or before opening a new position.
---

# Bull-Bear Debate

## Steps

1. Run `garp-scorer` for baseline score
2. Pull fundamentals via Equibles (10-K summary, earnings, margins)
3. Fetch live quote via FinanceKit
4. Build bull case (growth, moat, valuation support)
5. Build bear case (risks, competition, valuation stretch)
6. Reverse DCF: what growth rate is market pricing in?

## Output

Save to `research/reports/YYYY-MM-DD-{TICKER}-bull-bear.md` using template in `research-standards.mdc`.

## Paper trading

Increment `graduation_criteria.bull_bear_memos.completed` in `portfolio/paper-trading.yaml`.

## Verdict

Buy / Hold / Avoid — only Buy if GARP score >= 60 and bull case outweighs bear on valuation.
