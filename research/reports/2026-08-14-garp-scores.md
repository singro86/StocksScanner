# GARP scores — IRWD, PLX, IDN

**Date:** 2026-08-14 | **Tool:** Rebalance-MCP `score_tickers` preset `garp`

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only.** ~4 weeks remaining (Phase 0 ends 2026-09-10).

## Result: scores unavailable

Rebalance-MCP did not load in this session (`serverStatus: error` on live tool discovery; `mcp_auth` timed out). Portfolio-MCP was also unavailable. **No official 5-dimension GARP composite was produced.**

Per [portfolio/profile.yaml](../../portfolio/profile.yaml) `min_garp_score: 60` and AGENTS.md: **no name is a Buy** until `score_tickers` with preset `garp` returns **>= 60**.

| Ticker | Official GARP | Verdict |
|--------|---------------|---------|
| IRWD | unavailable | Not a Buy — paper watch / 3x rerate candidate only |
| PLX | unavailable | Not a Buy — secondary watch |
| IDN | unavailable | Not a Buy — crash watch only |

When the server is back, re-run `score_tickers` on `IRWD,PLX,IDN` with preset `garp` and write the breakdown into this file (or a dated follow-up). Until then, use Equibles + FinanceKit research in:

- [2026-08-14-IRWD-research.md](2026-08-14-IRWD-research.md)
- [2026-08-14-PLX-research.md](2026-08-14-PLX-research.md)
- [2026-08-14-IDN-watch.md](2026-08-14-IDN-watch.md)

Do **not** treat the qualitative notes in those memos as a substitute composite score.
