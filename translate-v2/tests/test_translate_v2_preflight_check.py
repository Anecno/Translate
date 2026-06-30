#!/usr/bin/env python3
"""Regression tests for public relay preflight checks."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "translate_v2_preflight_check.py"


def run_cmd(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )


def test_before_send_requires_contract_ok() -> None:
    result = run_cmd(
        [
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
            "BLOCKED",
        ]
    )
    assert result.returncode == 2
    assert "before-send:contract-not-ok" in result.stdout


def test_before_send_ok() -> None:
    result = run_cmd(
        [
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
            "TRANSLATE_V2_CONTRACT_GATE_STATUS=OK",
        ]
    )
    assert result.returncode == 0
    assert "TRANSLATE_V2_PREFLIGHT_STATUS=OK" in result.stdout


def test_after_result_requires_artifact_lint_ok() -> None:
    result = run_cmd(
        [
            "after-result",
            "--surface",
            "web-relay",
            "--raw-capture-file",
            "raw.md",
            "--artifact-lint-status",
            "BLOCKED",
            "--output-captured",
            "full output captured",
        ]
    )
    assert result.returncode == 2
    assert "after-result:artifact-lint-not-ok" in result.stdout


def test_after_result_ok() -> None:
    result = run_cmd(
        [
            "after-result",
            "--surface",
            "web-relay",
            "--raw-capture-file",
            "raw.md",
            "--artifact-lint-status",
            "TRANSLATE_V2_ARTIFACT_LINT_STATUS=OK",
            "--output-captured",
            "full output captured",
        ]
    )
    assert result.returncode == 0
    assert "TRANSLATE_V2_PREFLIGHT_STATUS=OK" in result.stdout


if __name__ == "__main__":
    test_before_send_requires_contract_ok()
    test_before_send_ok()
    test_after_result_requires_artifact_lint_ok()
    test_after_result_ok()
    print("preflight tests passed")
