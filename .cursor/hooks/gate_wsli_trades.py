#!/usr/bin/env python3
"""beforeShellExecution: gate live wsli trades — require dry-run + approval + paper graduation."""
import os
import sys
from pathlib import Path

try:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from hook_utils import (
        allow_shell,
        deny_shell,
        is_wsli_dry_run,
        is_wsli_trade_command,
        paper_trading_complete,
        read_stdin_json,
    )

    data = read_stdin_json()
    command = data.get("command", "") or ""

    if not is_wsli_trade_command(command):
        allow_shell()

    if is_wsli_dry_run(command):
        allow_shell()

    if not paper_trading_complete():
        deny_shell(
            "Paper trading is active — live wsli trades are blocked. Use --dry-run only.",
            "Paper trading active. Run dry-run only until graduation criteria in portfolio/paper-trading.yaml are met.",
        )

    if os.environ.get("TRADE_APPROVED", "").lower() != "true":
        deny_shell(
            "Live wsli trade blocked — user approval required. Set TRADE_APPROVED=true only after explicit approval.",
            "Run wsli with --dry-run first, present ticket to user, then retry with TRADE_APPROVED=true after approval.",
        )

    allow_shell()
except Exception as exc:
    print(
        __import__("json").dumps(
            {
                "permission": "allow",
                "agent_message": f"gate_wsli_trades hook error (fail-open): {exc}",
            }
        )
    )
    sys.exit(0)
