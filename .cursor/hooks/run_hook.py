#!/usr/bin/env python3
"""Wrap hook scripts to always emit valid JSON on failure."""
import json
import runpy
import sys
from pathlib import Path


def main():
    if len(sys.argv) < 2:
        print(json.dumps({"permission": "allow"}))
        return
    target = Path(sys.argv[1])
    if not target.exists():
        print(json.dumps({"permission": "allow", "agent_message": f"Hook not found: {target}"}))
        return
    runpy.run_path(str(target), run_name="__hook__")


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception as exc:
        print(json.dumps({"permission": "allow", "agent_message": f"Hook wrapper error: {exc}"}))
        sys.exit(0)
