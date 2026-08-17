# GARP Portfolio Onboarding — 2026-08-13

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only.** Live automation via wsli is disabled; place trades manually in Wealthsimple.

---

## Your profile (summary)

| Setting | Value |
|---------|-------|
| Account | **TFSA first** (Wealthsimple) |
| Style | GARP — Growth At Reasonable Price |
| Mode | **Manual execution** (Wealthsimple app) |
| Starting capital | Up to $10,000 CAD |
| Monthly DCA | $500–$1,000 |
| North star | $1,000,000 CAD (long-term) |
| Realistic Dec 2027 | ~$30,000 CAD |
| Drawdown rule | Pause new buys at **15%** below peak |

---

## GARP in plain language

**GARP** means buying companies that are **growing earnings/revenue** but not at any price — you want a **reasonable valuation** (P/E, PEG) plus positive momentum and a clear business story.

This portfolio scores on 5 dimensions (when Rebalance-MCP is online):

| Dimension | Weight |
|-----------|--------|
| Thesis integrity | 25% |
| Valuation | 25% |
| Momentum | 20% |
| Catalyst | 15% |
| Technical trend | 15% |

**Note:** Rebalance-MCP is currently **offline** in your Cursor MCP panel. Scores below use **FinanceKit + Equibles** as a proxy until you fix that server.

---

## TFSA checklist (action for you)

- [ ] Confirm you have **TFSA contribution room** (CRA My Account or 2026 limit minus prior contributions)
- [ ] Open/select **TFSA** in Wealthsimple Trade (not RRSP unless you prefer tax deferral)
- [ ] US stocks: Wealthsimple converts CAD→USD at their FX rate (~1.5% spread typical)

US dividends in a TFSA: **15% US withholding tax** still applies (not recoverable).

---

## Cold-start universe — live data (2026-08-13)

**Source:** FinanceKit `multi_quote`, `compare_assets`, `correlation_matrix`; Equibles `CompareFinancialFact` (revenue FY2025)

| Ticker | Price (USD) | P/E | 3mo return | Beta | Revenue FY2025 (Equibles) |
|--------|-------------|-----|------------|------|---------------------------|
| MSFT | $496.88 | 27.7 | **+21.6%** | 1.10 | $281.7B |
| NVDA | $225.30 | 34.6 | -4.3% | 2.22 | $130.5B |
| GOOGL | $346.36 | **17.4** | -13.6% | 1.24 | $402.8B |
| AMZN | $265.13 | 21.3 | -0.8% | 1.45 | $716.9B |

**Diversification:** Average pairwise correlation **0.35** (GOOD). Lowest pair: MSFT/GOOGL (0.18).

**3mo leader:** MSFT (best risk-adjusted Sharpe ~1.93). **Best valuation:** GOOGL (lowest P/E).

---

## Proxy GARP scores (Rebalance-MCP unavailable)

| Ticker | Proxy score | Verdict | Key GARP read |
|--------|-------------|---------|---------------|
| MSFT | **78** | ✅ Buy candidate | Profitable mega-cap, strong 3mo momentum, reasonable P/E vs growth |
| GOOGL | **74** | ✅ Buy candidate | Cheapest P/E in group; weak recent momentum = potential value entry |
| AMZN | **71** | ✅ Buy candidate | Mid P/E, AWS/e-commerce optionality, moderate correlation with GOOGL |
| NVDA | **68** | ✅ Buy candidate (watch) | Highest P/E + beta; semis/AI anchor — size carefully |

All above **min_garp_score: 60**.

---

## Paper trading graduation (4 weeks)

Track in `portfolio/paper-trading.yaml`:

- [ ] 4 weeks elapsed (ends ~2026-09-10)
- [ ] 20 daily GARP scans
- [ ] 5 bull/bear memos
- [ ] 3 trade ticket reviews ← **this session counts as #1**
- [ ] Your confirmation: "I understand GARP scoring, swap logic, and drawdown protocol"

---

## Next actions

1. Review cold-start trade tickets → [`2026-08-13-cold-start-trades.md`](2026-08-13-cold-start-trades.md)
2. Execute in **Wealthsimple TFSA** (manual)
3. Update `portfolio/holdings.yaml` with fills
4. Ask agent: **"Score my portfolio"** or **"Weekly GARP review"**

**Fix when convenient:** Rebalance-MCP + Portfolio-MCP show **error** in MCP panel — reinstall via `uvx rebalance-mcp` / `uvx portfolio-mcp`.
