#!/usr/bin/env python3
"""sessionStart: inject portfolio context summary."""
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from hook_utils import (  # noqa: E402
    PEAK_PATH,
    PROFILE_PATH,
    emit,
    get_drawdown_state,
    get_profile,
    load_yaml_simple,
    paper_trading_complete,
)

profile = get_profile()
drawdown = get_drawdown_state()
paper = not paper_trading_complete()

lines = [
    "## Portfolio Session Context",
    f"- Paper trading: {'ACTIVE (dry-run only)' if paper else 'Complete — live allowed with approval'}",
    f"- Drawdown mode: {drawdown['mode']}",
    f"- Broker: {profile.get('broker', 'wealthsimple')} | Account priority: {profile.get('account_priority', 'TFSA')}",
    f"- Growth style: {profile.get('growth_style', 'garp').upper()}",
]

if PEAK_PATH.exists():
    peak = load_yaml_simple(PEAK_PATH)
    if peak.get("current_value_cad"):
        lines.append(f"- Portfolio value (CAD): ${peak.get('current_value_cad', 0):,.0f}")

lines.append(f"- Session started: {datetime.now(timezone.utc).isoformat()}")
lines.append("- Run scripts/wsli/sync-portfolio.ps1 if you traded manually in Wealthsimple.")
lines.extend(
    [
        "",
        "## Runtime mandate (always on)",
        "- Agent spec: `.cursor/agents/garp-portfolio-manager.md` + `docs/AGENT_SYSTEM.md`",
        "- Rule: `.cursor/rules/agent-mandatory-workflow.mdc` — use skills + MCP; never guess prices",
        "- MCP: Rebalance-MCP (GARP) · FinanceKit (quotes) · Equibles (SEC/screener) · Portfolio-MCP (quant)",
        "- Penny: `penny-scanner` skill · `portfolio/penny9-universe.yaml` · `portfolio/penny-secondary-watchlist.yaml`",
        "- Secondary pennies are quality: watch — never auto-buy. No live wsli during paper trading.",
    ]
)

emit({"additional_context": "\n".join(lines)})
