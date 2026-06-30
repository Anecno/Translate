#!/usr/bin/env python3
"""Regression tests for the public contract gate."""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "translate_v2_contract_gate.py"


def run_gate(text: str) -> subprocess.CompletedProcess[str]:
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "contract.md"
        path.write_text(text, encoding="utf-8")
        return subprocess.run(
            [sys.executable, str(SCRIPT), str(path)],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )


def test_contract_blocks_missing_evidence() -> None:
    result = run_gate("Translate this quickly.")
    assert result.returncode == 2
    assert "TRANSLATE_V2_CONTRACT_GATE_STATUS=BLOCKED" in result.stdout
    assert "contract:principles-first" in result.stdout


def test_contract_blocks_stale_flat_schema() -> None:
    result = run_gate(
        """
source language and target language and task scope.
principles first / translation principles.
N-1 and N-2 previous baton.
raw capture full output.
round archive.
checkpoint wait for user.
final output user confirmation.
public spec current public entry.
scores.language scores.literary scores.cultural aggregate.
scores_14d
""",
    )
    assert result.returncode == 2
    assert "flat-score-schema-forbidden" in result.stdout


def test_contract_ok() -> None:
    result = run_gate(
        """
source language and target language and task scope.
principles first / translation principles.
N-1 and N-2 previous baton.
raw capture full output.
round archive.
checkpoint wait for user.
final output user confirmation.
public spec current public entry.
scores.language scores.literary scores.cultural aggregate.
""",
    )
    assert result.returncode == 0
    assert "TRANSLATE_V2_CONTRACT_GATE_STATUS=OK" in result.stdout


if __name__ == "__main__":
    test_contract_blocks_missing_evidence()
    test_contract_blocks_stale_flat_schema()
    test_contract_ok()
    print("contract gate tests passed")
