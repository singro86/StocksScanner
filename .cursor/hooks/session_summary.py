#!/usr/bin/env python3
"""stop: session summary with open items."""
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from hook_utils import emit, get_drawdown_state, paper_trading_complete, read_stdin_json

read_stdin_json()  # consume input
drawdown = get_drawdown_state()
paper = not paper_trading_complete()

parts = [
    "## Session Summary",
    f"- Time: {datetime.now(timezone.utc).isoformat()}",
    f"- Paper trading: {'active' if paper else 'graduated'}",
    f"- Drawdown mode: {drawdown['mode']}",
    "- Check research/reports/ for memos and dry-run tickets.",
    "- Pending user approvals: review any trade tickets presented this session.",
]
if paper:
    parts.append("- Reminder: live wsli trades blocked until paper trading graduation.")

emit({"followup_message": "\n".join(parts)})
