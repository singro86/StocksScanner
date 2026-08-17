# 1MillionPortfolio — Agent System Reference

Complete specification for the North America GARP Portfolio Manager agent.  
**Mandate:** The always-on rule [`.cursor/rules/agent-mandatory-workflow.mdc`](../.cursor/rules/agent-mandatory-workflow.mdc) requires the agent to follow this document every session.

---

## 1. Overview

### Purpose

AI-powered **Growth At Reasonable Price (GARP)** portfolio manager for a Canadian beginner investing via **Wealthsimple Trade (TFSA)** toward a **$1M CAD north star** (realistic Dec 2027 milestone: ~$30K CAD).

### Architecture

```
You (Wealthsimple app)
    ↑ manual execution
Cursor Agent ← AGENTS.md + `.cursor/agents/garp-portfolio-manager.md` + mandatory rule + 13 skills
    ↑ hooks (safety gates, context, audit)
MCP: FinanceKit | Equibles | Rebalance-MCP* | Portfolio-MCP*
    ↑
portfolio/ (profile, holdings, watchlist, penny9, penny-secondary, peak-value, paper-trading)
research/reports/ + research/timeseries/
automations/ (scheduled workflows — import in Cursor Automations)
.github/workflows/daily-penny9.yml (weekday penny scans)
scripts/ (notify, scoring/daily-penny9-scan.py, wsli* optional legacy)

* Rebalance-MCP / Portfolio-MCP — use when online; FinanceKit + Equibles as fallback
```

### Current execution mode

| Setting | Value |
|---------|-------|
| Mode | **Manual** — user trades in Wealthsimple app |
| Paper trading | **Active** until `paper_trading_complete: true` |
| Broker CLI | Disabled (wsli optional/legacy — not required) |
| Capital | ~$8,000 CAD |
| Cold-start core | MSFT, NVDA, GOOGL, AMZN |

---

## 2. Agent details

### Identity

**Name:** North America GARP Portfolio Manager  
**Persona:** Aggressive growth with valuation guardrails; educator for beginners; honest about goals and risk.

### Primary files

| File | Role |
|------|------|
| [`AGENTS.md`](../AGENTS.md) | Agent persona and operating principles |
| [`.cursor/agents/garp-portfolio-manager.md`](../.cursor/agents/garp-portfolio-manager.md) | Custom subagent — invoke for investing / penny / trade tasks |
| [`portfolio/profile.yaml`](../portfolio/profile.yaml) | Investor config, constraints, execution flags |
| [`portfolio/paper-trading.yaml`](../portfolio/paper-trading.yaml) | Phase 0 graduation tracker |
| [`portfolio/holdings.yaml`](../portfolio/holdings.yaml) | Positions (update after every manual trade) |
| [`portfolio/watchlist.yaml`](../portfolio/watchlist.yaml) | 20-stock GARP core + screener slots |
| [`portfolio/penny9-universe.yaml`](../portfolio/penny9-universe.yaml) | Primary 9-name GARP penny screen |
| [`portfolio/penny-secondary-watchlist.yaml`](../portfolio/penny-secondary-watchlist.yaml) | Secondary 20-name watch-only pennies |
| [`portfolio/peak-value.yaml`](../portfolio/peak-value.yaml) | Drawdown protocol (15% pause) |

### Mandatory disclaimer

Include in every recommendation:

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

### Trade ticket format

```
Action | Ticker | Shares | CAD Amount | Buy Price | GARP Score | Rationale | Risk | Today bias
```

### Goal honesty

Never imply $1M by Dec 2027 without compound-growth math. Show contributions + realistic return scenarios.

---

## 3. Skills (13)

Location: [`.cursor/skills/`](../.cursor/skills/)

| Skill | Trigger | Action |
|-------|---------|--------|
| `portfolio-onboarding` | Starting out, first session | TFSA, GARP intro, cold-start allocation |
| `garp-scorer` | Score stock, GARP analysis | Rebalance-MCP 5-dim scoring (or FinanceKit+Equibles fallback) |
| `bull-bear-debate` | Should I buy X? | Structured bull/bear memo before new positions |
| `rotation-analyzer` | Swap X for Y? | compare_swaps, delta >= 15 |
| `stock-research` | Analyze ticker | Full memo → `research/reports/` |
| `portfolio-review` | Review portfolio | Holdings, drift, benchmark vs QQQ |
| `trade-proposal` | What to buy? | Scored trade tickets for manual WS execution |
| `dca-planner` | $X this month | GARP-ranked DCA split |
| `goal-tracker` | On track for $1M? | Monte Carlo + honest milestones |
| `earnings-watch` | Earnings season | Calendar + pre-earnings checklist |
| `penny-scanner` | Pennies, 3x, daily scan, secondary 20 | Scan penny-9 + secondary-20; IRWD only 3x vehicle |
| `wsli-executor` | Legacy semi-auto | Optional; manual mode preferred |
| `trading-fundamentals` | Learn trading | 8-module curriculum → `LEARNING_ROADMAP.md` |

**Rule:** Match user intent to the skill above; read the skill's `SKILL.md` before executing that workflow.

---

## 4. Instructions (rules)

Location: [`.cursor/rules/`](../.cursor/rules/)

| Rule | Scope | Purpose |
|------|-------|---------|
| **`agent-mandatory-workflow.mdc`** | **alwaysApply: true** | **Session checklist — MANDATORY every run** |
| `investment-core.mdc` | alwaysApply | Disclaimer, GARP, goal honesty, beginner education |
| `trade-safety.mdc` | alwaysApply | Paper trading, limits, drawdown, kill switch |
| `garp-scoring.mdc` | alwaysApply | 5-dim thresholds, MCP routing, rotation rules |
| `portfolio-data.mdc` | `portfolio/**` | YAML schema, CAD conventions, penny universe files |
| `research-standards.mdc` | `research/**` | Bull/bear template, cite MCP sources |

---

## 5. Hooks

Location: [`.cursor/hooks.json`](../.cursor/hooks.json) + [`.cursor/hooks/`](../.cursor/hooks/)

Hooks run automatically; the agent must not bypass them.

| Event | Script | Behavior |
|-------|--------|----------|
| `sessionStart` | `session_start.py` | Inject portfolio context + runtime mandate (paper, drawdown, MCP, penny universes) |
| `beforeShellExecution` | `kill_switch.py` | Block wsli if `PAUSE_ALL_TRADING=true` |
| `beforeShellExecution` | `drawdown_gate.py` | Block buys in 15% drawdown review-only mode |
| `beforeShellExecution` | `rate_limit_trades.py` | Max 3/hr, 5/day trades |
| `beforeShellExecution` | `gate_wsli_trades.py` | Paper trading + TRADE_APPROVED gate |
| `beforeMCPExecution` | `audit_and_cache_mcp.py` | Audit log + cache to `portfolio/cache/` |
| `beforeSubmitPrompt` | `block_secrets_and_risk.py` | Block API keys; flag reckless prompts |
| `afterFileEdit` | `validate_portfolio_edit.py` | Validate portfolio YAML edits |
| `subagentStop` | `chain_research_pipeline.py` | Chain research → scoring follow-up |
| `stop` | `session_summary.py` | Session summary + open tickets |

---

## 6. MCP servers

Config template: [`config/mcp.template.json`](../config/mcp.template.json)  
Setup guide: [`config/MCP_SETUP.md`](../config/MCP_SETUP.md)

| Server | ID (Cursor) | Purpose | When to use |
|--------|-------------|---------|-------------|
| **FinanceKit** | `user-financekit` | Live quotes, technicals, compare | **Every** price check; daily scans |
| **Equibles** | `user-equibles` | SEC, earnings, fundamentals, screener | Research, bull-bear, earnings (not routine quotes) |
| **Rebalance-MCP** | `user-rebalance-mcp` | GARP scoring, swaps, backtests | Primary scoring when server online |
| **Portfolio-MCP** | `user-portfolio-mcp` | Sharpe, Monte Carlo, optimization | Goal tracker, risk review |

### MCP routing (mandatory)

| Task | Primary | Fallback |
|------|---------|----------|
| Live price | FinanceKit `multi_quote` / `stock_quote` | — |
| GARP score | Rebalance-MCP `score_tickers` | FinanceKit + Equibles proxy score |
| SEC / earnings | Equibles | — |
| Monte Carlo | Portfolio-MCP | Manual math + disclaimer |
| Screener | Equibles | watchlist.yaml static core |

**Never guess prices or fundamentals.** If MCP fails, say "data unavailable."

Equibles quota: **100/day** — reserve for deep research and screener.

---

## 7. Plugins, automations, and tools

### Cursor Automations

Import from [`automations/`](../automations/) via Cursor Automations UI:

| Automation | Schedule (ET) | Purpose |
|------------|---------------|---------|
| `daily-garp-scan.yaml` | Weekdays 8:30 AM | Watchlist scoring, swap flags |
| `daily-penny-scan.yaml` | Weekdays 8:30 AM | Both penny universes via `penny-scanner` (optional if GitHub Action runs) |
| `weekly-portfolio-pulse.yaml` | Monday 8:00 AM | Full portfolio review |
| `monthly-dca-review.yaml` | 1st of month 9:00 AM | DCA allocation |
| `earnings-alert.yaml` | Weekdays 7:00 AM | Earnings calendar |
| `quarterly-goal-check.yaml` | Jan/Apr/Jul/Oct 1st | Goal projection |

### GitHub Action

[`.github/workflows/daily-penny9.yml`](../.github/workflows/daily-penny9.yml) is the durable weekday runner for both penny lists. Secrets: `RESEND_API_KEY`, `NOTIFY_EMAIL_TO`, `NOTIFY_EMAIL_FROM`. Never paste keys into the workflow file.

### Scripts

| Path | Purpose |
|------|---------|
| `scripts/scoring/daily-penny9-scan.py` | Yahoo bars → CSV + report for any universe YAML |
| `scripts/notify/send-email.ps1` | Resend email alerts |
| `scripts/notify/drawdown-alert.ps1` | Drawdown email |
| `scripts/scoring/daily-garp-scan.ps1` | Scan report template |
| `scripts/wsli/*.ps1` | Legacy wsli wrappers (optional) |

### Data directories

| Path | Purpose |
|------|---------|
| `portfolio/` | Source of truth for profile, holdings, penny universes |
| `research/reports/` | Agent output (memos, tickets, daily scans, learning) |
| `research/timeseries/` | `penny9.csv` and `penny-secondary.csv` |
| `portfolio/cache/` | MCP audit cache + email outbox (hooks) |

No Cursor marketplace plugins are required. The stack is MCP + repo scripts + GitHub Actions.

---

## 8. Session workflow (every agent run)

1. Read `portfolio/profile.yaml`, `holdings.yaml`, `peak-value.yaml`, `paper-trading.yaml`
2. Announce paper trading status if active
3. Use MCP for any market data (FinanceKit minimum)
4. Select and follow the matching **skill** (`penny-scanner` for sub-$5 / 3x / daily scan)
5. Obey all **rules** (especially trade-safety + garp-scoring)
6. Output trade tickets in standard format; save reports to `research/reports/`
7. Secondary pennies stay `quality: watch` until GARP >= 60 and an earnings-quality review
8. Update `holdings.yaml` when user confirms fills
9. End with disclaimer + next recommended action

---

## 9. Paper trading graduation

Criteria in `portfolio/paper-trading.yaml`:

- 4 weeks elapsed
- 20 daily GARP scans
- 5 bull-bear memos
- 3 trade ticket reviews
- User confirmation
- Set `paper_trading_complete: true` in profile.yaml

---

## 10. Learning path

See [`.cursor/skills/trading-fundamentals/LEARNING_ROADMAP.md`](../.cursor/skills/trading-fundamentals/LEARNING_ROADMAP.md)  
Progress: [`research/reports/learning-log.md`](../research/reports/learning-log.md)
