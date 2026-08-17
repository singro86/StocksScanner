---
name: goal-tracker
description: Runs Monte Carlo projection via Portfolio-MCP and tracks progress toward $1M north star with honest milestone math. Use when user asks am I on track for 1 million or goal progress.
---

# Goal Tracker

## Steps

1. Read `portfolio/profile.yaml` goals and contributions
2. Read current value from `portfolio/holdings.yaml`
3. Call Portfolio-MCP `run_monte_carlo` with contribution schedule
4. Show scenarios: conservative (7%), moderate (10%), aggressive (12%) annual returns

## Required honesty

Always show:
- Total capital invested to date
- Current portfolio value
- Realistic 2027 milestone (~$30K CAD)
- Years to $1M at current contribution rate for each scenario

## Output

Save to `research/reports/YYYY-MM-DD-goal-tracker.md`

Never claim $1M by Dec 2027 without showing the math (~5800% required return).
