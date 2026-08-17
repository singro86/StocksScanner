#!/usr/bin/env python3
"""subagentStop: chain research → scoring follow-up when research subagent completes."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from hook_utils import emit, read_stdin_json

data = read_stdin_json()
subagent_type = (data.get("subagent_type") or data.get("subagentType") or "").lower()
status = (data.get("status") or "").lower()

if subagent_type in ("explore", "generalpurpose") and status in ("completed", "success", ""):
    emit(
        {
            "followup_message": (
                "Research subagent finished. Run garp-scorer on any tickers identified. "
                "Penny / sub-$5 names go through the penny-scanner skill — do not auto-promote "
                "secondary watchlist names. Update portfolio/watchlist.yaml scores if applicable."
            ),
        }
    )

emit({})
