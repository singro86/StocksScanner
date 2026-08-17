#!/usr/bin/env python3
"""beforeShellExecution: block buys during 15% drawdown review-only mode."""
import sys
from pathlib import Path

try:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from hook_utils import (
        allow_shell,
        deny_shell,
        get_drawdown_state,
        is_buy_command,
        is_wsli_dry_run,
        read_stdin_json,
    )

    data = read_stdin_json()
    command = data.get("command", "") or ""

    if not is_buy_command(command):
        allow_shell()

    if is_wsli_dry_run(command):
        allow_shell()

    state = get_drawdown_state()
    if state["mode"] == "review_only":
        deny_shell(
            f"Drawdown review-only mode — new buys blocked. Peak CAD ${state['peak']:,.0f}, current ${state['current']:,.0f}.",
            "Drawdown protocol active. Scoring and review only until within recovery threshold of peak.",
        )

    allow_shell()
except Exception as exc:
    print(__import__("json").dumps({"permission": "allow", "agent_message": str(exc)}))
    sys.exit(0)
