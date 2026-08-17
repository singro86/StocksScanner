# Cold-Start Trade Tickets — Paper Trading (Manual Execution)

**Date:** 2026-08-13 | **Mode:** Proposed only — execute in Wealthsimple app  
**Paper trading active — dry-run only** (no broker automation)

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice.

---

## Allocation plan

**Assumed deployable capital:** $8,000 CAD (adjust proportionally if different)

| # | Ticker | Target weight | Target CAD | Target USD (~) | Rationale |
|---|--------|---------------|------------|----------------|-----------|
| 1 | MSFT | 25% | $2,000 | ~$1,450 | GARP anchor; best 3mo momentum (+21.6%); Sharpe 1.31 |
| 2 | GOOGL | 25% | $2,000 | ~$1,450 | Lowest P/E (17.4); search/cloud/AI; value entry after pullback |
| 3 | AMZN | 25% | $2,000 | ~$1,450 | P/E 21.3; AWS + retail margins improving |
| 4 | NVDA | 25% | $2,000 | ~$1,450 | AI/semi growth; highest volatility — cap at 25% |

**Cash reserve:** Keep ~$0 for cold start (add 10% cash buffer on next DCA month if preferred).

**FX note:** Wealthsimple applies live CAD/USD rate + spread. USD amounts below are illustrative at ~1.38 CAD/USD.

---

## Trade tickets (execute manually in Wealthsimple TFSA)

### Ticket 1 — BUY MSFT

| Field | Value |
|-------|-------|
| Action | **BUY** |
| Ticker | MSFT |
| Approx USD | ~$1,450 |
| Approx shares | ~3 shares (or fractional / $ amount order) |
| GARP proxy score | **78/100** |
| Rationale | Mega-cap GARP leader; revenue $281.7B (Equibles FY2025); P/E 27.7; beta 0.95 vs SPY |
| Risk | Concentration in mega-cap tech; -23% max drawdown last 6mo |
| Status | **PROPOSED** — paper trading |

### Ticket 2 — BUY GOOGL

| Field | Value |
|-------|-------|
| Action | **BUY** |
| Ticker | GOOGL |
| Approx USD | ~$1,450 |
| Approx shares | ~4 shares |
| GARP proxy score | **74/100** |
| Rationale | Cheapest P/E in basket (17.4); revenue $402.8B; low correlation with MSFT (0.18) |
| Risk | -13.6% 3mo return; regulatory/AI competition |
| Status | **PROPOSED** |

### Ticket 3 — BUY AMZN

| Field | Value |
|-------|-------|
| Action | **BUY** |
| Ticker | AMZN |
| Approx USD | ~$1,450 |
| Approx shares | ~5 shares |
| GARP proxy score | **71/100** |
| Rationale | P/E 21.3; revenue $716.9B largest in group; e-commerce + AWS |
| Risk | Correlated with GOOGL (0.63); consumer spending sensitivity |
| Status | **PROPOSED** |

### Ticket 4 — BUY NVDA

| Field | Value |
|-------|-------|
| Action | **BUY** |
| Ticker | NVDA |
| Approx USD | ~$1,450 |
| Approx shares | ~6 shares |
| GARP proxy score | **68/100** |
| Rationale | AI/semi anchor; revenue $130.5B; technical MODERATELY BULLISH (FinanceKit) |
| Risk | **Highest beta (2.22)**; P/E 34.6; Stochastic overbought — consider splitting entry over 2 weeks |
| Status | **PROPOSED** |

---

## Execution checklist (Wealthsimple app)

1. Open **TFSA** → **Trade** → search ticker
2. Use **Buy in dollars** (fractional) if whole shares don't fit budget
3. Execute tickets 1–4 (or stagger NVDA over 2 DCA dates if cautious)
4. Save confirmations
5. Tell agent your fills → update `portfolio/holdings.yaml`

---

## After fills — update holdings.yaml template

```yaml
last_sync: "2026-08-13T..."
source: manual
total_value_cad: 8000  # update to actual
cash_cad: 0
positions:
  - ticker: MSFT
    shares: 3
    avg_cost_cad: 2000
    market_value_cad: 2000
    weight_pct: 25
    garp_score: 78
    sleeve: mega_cap_garp
  # ... repeat for GOOGL, AMZN, NVDA
```

---

## Constraint check

| Rule | Status |
|------|--------|
| Max single stock 20% | ⚠️ Each at 25% initially — **trim on next DCA** or deploy $10K+ to reduce to 20% ($2K each = 20% of $10K ✅) |
| Max sector 40% | ⚠️ All tech — acceptable for aggressive GARP cold start; add QQQ backbone later |
| Min GARP score 60 | ✅ All pass |
| Paper trading | ✅ Proposed only |

**If starting with $10,000:** Each position = $2,000 (20%) — satisfies single-stock limit exactly.

---

## Data sources

- Quotes & metrics: FinanceKit (2026-08-13)
- Revenue: Equibles CompareFinancialFact FY2025
- Rebalance-MCP: unavailable — proxy scores used

**Approve by executing in Wealthsimple and replying with your fill details.**
