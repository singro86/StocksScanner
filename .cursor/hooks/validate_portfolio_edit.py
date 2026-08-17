#!/usr/bin/env python3
"""afterFileEdit: validate portfolio YAML constraint hints."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from hook_utils import emit, get_profile, read_stdin_json

data = read_stdin_json()
file_path = data.get("file_path") or data.get("path") or ""

if "portfolio" not in file_path.replace("\\", "/"):
    emit({})

profile = get_profile()
constraints = profile.get("constraints", {})
max_single = 20
if isinstance(constraints, dict):
    max_single = constraints.get("max_single_stock_pct", 20)

emit(
    {
        "additional_context": (
            f"Portfolio file edited: {file_path}. "
            f"Verify single-stock weights stay <= {max_single}% and sync with wsli if holdings changed."
        ),
    }
)
