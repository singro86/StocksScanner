"""Shared utilities for Cursor investment agent hooks."""
from __future__ import annotations

import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PORTFOLIO = ROOT / "portfolio"
PROFILE_PATH = PORTFOLIO / "profile.yaml"
PEAK_PATH = PORTFOLIO / "peak-value.yaml"
TRANSACTIONS_PATH = PORTFOLIO / "transactions.log.md"
CACHE_DIR = PORTFOLIO / "cache"
AUDIT_LOG = CACHE_DIR / "hook-audit.log"


def read_stdin_json() -> dict:
    try:
        raw = sys.stdin.read()
        if not raw.strip():
            return {}
        return json.loads(raw)
    except json.JSONDecodeError:
        return {}


def emit(obj: dict) -> None:
    print(json.dumps(obj))
    sys.exit(0)


def allow_shell() -> None:
    emit({"permission": "allow"})


def deny_shell(user_message: str, agent_message: str) -> None:
    emit(
        {
            "permission": "deny",
            "user_message": user_message,
            "agent_message": agent_message,
        }
    )


def ask_shell(user_message: str, agent_message: str) -> None:
    emit(
        {
            "permission": "ask",
            "user_message": user_message,
            "agent_message": agent_message,
        }
    )


def load_yaml_simple(path: Path) -> dict:
    """Minimal YAML reader for flat/nested keys used in profile.yaml."""
    if not path.exists():
        return {}
    text = path.read_text(encoding="utf-8")
    result: dict = {}
    stack: list[tuple[int, dict]] = [(-1, result)]

    key_re = re.compile(r"^(\s*)([\w_]+):\s*(.*)$")
    for line in text.splitlines():
        if not line.strip() or line.strip().startswith("#"):
            continue
        m = key_re.match(line)
        if not m:
            continue
        indent = len(m.group(1).replace("\t", "  "))
        key = m.group(2)
        val = m.group(3).strip()

        while stack and indent <= stack[-1][0]:
            stack.pop()
        parent = stack[-1][1]

        if val == "" or val == "|":
            parent[key] = {}
            stack.append((indent, parent[key]))
        elif val.startswith("[") and val.endswith("]"):
            inner = val[1:-1].strip()
            if not inner:
                parent[key] = []
            else:
                parts = [p.strip().strip('"').strip("'") for p in inner.split(",")]
                parsed: list = []
                for p in parts:
                    try:
                        parsed.append(int(p))
                    except ValueError:
                        try:
                            parsed.append(float(p))
                        except ValueError:
                            if p.lower() in ("true", "false"):
                                parsed.append(p.lower() == "true")
                            else:
                                parsed.append(p)
                parent[key] = parsed
        elif val.lower() == "true":
            parent[key] = True
        elif val.lower() == "false":
            parent[key] = False
        elif val.lower() == "null":
            parent[key] = None
        elif (val.startswith('"') and val.endswith('"')) or (
            val.startswith("'") and val.endswith("'")
        ):
            parent[key] = val[1:-1]
        else:
            try:
                parent[key] = int(val)
            except ValueError:
                try:
                    parent[key] = float(val)
                except ValueError:
                    parent[key] = val
    return result


def get_profile() -> dict:
    data = load_yaml_simple(PROFILE_PATH)
    return data.get("investor", data)


def is_wsli_trade_command(command: str) -> bool:
    c = command.lower()
    return "wsli" in c and re.search(r"\b(buy|sell)\b", c)


def is_wsli_dry_run(command: str) -> bool:
    return "--dry-run" in command.lower() or "-dry-run" in command.lower()


def is_wsli_command(command: str) -> bool:
    return "wsli" in command.lower()


def paper_trading_complete() -> bool:
    profile = get_profile()
    execution = profile.get("execution", {})
    if isinstance(execution, dict):
        return bool(execution.get("paper_trading_complete", False))
    return False


def get_drawdown_state() -> dict:
    peak_data = load_yaml_simple(PEAK_PATH)
    profile = get_profile()
    drawdown_cfg = profile.get("drawdown", {})
    pause_at = 15
    recovery_within = 10
    if isinstance(drawdown_cfg, dict):
        pause_at = drawdown_cfg.get("pause_new_buys_at_pct", 15)
        recovery_within = drawdown_cfg.get("recovery_within_pct_of_peak", 10)

    peak = peak_data.get("peak_value_cad", 0) or 0
    current = peak_data.get("current_value_cad", 0) or 0
    mode = peak_data.get("mode", "normal")

    if peak > 0 and current > 0:
        drop_pct = ((peak - current) / peak) * 100
        if drop_pct >= pause_at:
            mode = "review_only"
        elif drop_pct <= recovery_within:
            mode = "normal"

    return {
        "peak": peak,
        "current": current,
        "mode": mode,
        "pause_at": pause_at,
    }


def is_buy_command(command: str) -> bool:
    return bool(re.search(r"\bwsli\b.*\bbuy\b", command, re.I))


def count_recent_trades(hours: int = 1) -> int:
    if not TRANSACTIONS_PATH.exists():
        return 0
    text = TRANSACTIONS_PATH.read_text(encoding="utf-8")
    now = datetime.now(timezone.utc)
    count = 0
    for line in text.splitlines():
        if not line.startswith("## "):
            continue
        try:
            ts_part = line[3:20]
            ts = datetime.strptime(ts_part, "%Y-%m-%d %H:%M")
            ts = ts.replace(tzinfo=timezone.utc)
            if (now - ts).total_seconds() <= hours * 3600:
                if "BUY" in line.upper() or "SELL" in line.upper():
                    count += 1
        except ValueError:
            continue
    return count


def count_trades_today() -> int:
    if not TRANSACTIONS_PATH.exists():
        return 0
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    text = TRANSACTIONS_PATH.read_text(encoding="utf-8")
    return sum(
        1
        for line in text.splitlines()
        if line.startswith(f"## {today}") and ("BUY" in line.upper() or "SELL" in line.upper())
    )


def audit_log(event: str, detail: str) -> None:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).isoformat()
    with AUDIT_LOG.open("a", encoding="utf-8") as f:
        f.write(f"{ts}\t{event}\t{detail}\n")
