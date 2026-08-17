#!/usr/bin/env python3
"""beforeShellExecution: kill switch for all wsli commands."""
import os
import sys
from pathlib import Path

try:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from hook_utils import allow_shell, deny_shell, is_wsli_command, read_stdin_json

    data = read_stdin_json()
    command = data.get("command", "") or ""

    if not is_wsli_command(command):
        allow_shell()

    if os.environ.get("PAUSE_ALL_TRADING", "").lower() in ("true", "1", "yes"):
        deny_shell(
            "PAUSE_ALL_TRADING is enabled — all wsli commands blocked.",
            "Kill switch active. Unset PAUSE_ALL_TRADING to resume.",
        )

    allow_shell()
except Exception as exc:
    print(__import__("json").dumps({"permission": "allow", "agent_message": str(exc)}))
    sys.exit(0)
