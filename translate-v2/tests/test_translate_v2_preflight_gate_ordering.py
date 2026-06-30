#!/usr/bin/env python3
"""Public checks for relay preflight ordering around contract gates."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PREFLIGHT = ROOT / "scripts" / "translate_v2_preflight_check.py"


def run_preflight(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(PREFLIGHT), *args],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )


def before_send_args(contract_status: str) -> list[str]:
    return [
        "before-send",
        "--operator",
        "local",
        "--surface",
        "web-relay",
        "--prompt-file",
        "prompt.md",
        "--raw-capture-plan",
        "capture full prompt and full output",
        "--contract-status",
        contract_status,
    ]


def test_preflight_blocks_before_send_when_contract_gate_is_not_ok() -> None:
    result = run_preflight(before_send_args("TRANSLATE_V2_CONTRACT_GATE_STATUS=BLOCKED"))
    assert result.returncode == 2
    assert "before-send:contract-not-ok" in result.stdout


def test_preflight_allows_before_send_after_contract_gate_ok() -> None:
    result = run_preflight(before_send_args("TRANSLATE_V2_CONTRACT_GATE_STATUS=OK"))
    assert result.returncode == 0
    assert "TRANSLATE_V2_PREFLIGHT_STATUS=OK" in result.stdout


if __name__ == "__main__":
    test_preflight_blocks_before_send_when_contract_gate_is_not_ok()
    test_preflight_allows_before_send_after_contract_gate_ok()
    print("preflight/gate ordering tests passed")
