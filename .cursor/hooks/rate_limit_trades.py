#!/usr/bin/env python3
"""beforeShellExecution: enforce trade rate limits from profile.yaml."""
import sys
from pathlib import Path

try:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from hook_utils import (
        allow_shell,
        count_recent_trades,
        count_trades_today,
        deny_shell,
        get_profile,
        is_wsli_dry_run,
        is_wsli_trade_command,
        read_stdin_json,
    )

    data = read_stdin_json()
    command = data.get("command", "") or ""

    if not is_wsli_trade_command(command) or is_wsli_dry_run(command):
        allow_shell()

    profile = get_profile()
    execution = profile.get("execution", {})
    max_hour = 3
    max_day = 5
    if isinstance(execution, dict):
        max_hour = execution.get("max_trades_per_hour", 3)
        max_day = execution.get("max_trades_per_day", 5)

    hourly = count_recent_trades(hours=1)
    daily = count_trades_today()

    if hourly >= max_hour:
        deny_shell(
            f"Hourly trade limit reached ({hourly}/{max_hour}). Wait before next live trade.",
            "Rate limit exceeded for last hour.",
        )

    if daily >= max_day:
        deny_shell(
            f"Daily trade limit reached ({daily}/{max_day}). Resume tomorrow.",
            "Daily trade limit exceeded per profile.yaml.",
        )

    allow_shell()
except Exception as exc:
    print(__import__("json").dumps({"permission": "allow", "agent_message": str(exc)}))
    sys.exit(0)
