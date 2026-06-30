#!/usr/bin/env python3
"""Integration checks between prompt contracts and artifact linting."""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTRACT_GATE = ROOT / "scripts" / "translate_v2_contract_gate.py"
ARTIFACT_LINT = ROOT / "scripts" / "translate_v2_artifact_lint.py"


def run_script(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, *args],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )


def test_contract_gate_and_artifact_lint_agree_on_prompt_requirements() -> None:
    prompt = """
source language and target language and task scope.
principles first / translation principles.
N-1 and N-2 previous baton.
raw capture full output.
round archive.
checkpoint wait for user.
final output user confirmation.
public spec current public entry.
scores.language scores.literary scores.cultural aggregate.
"""
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "prompt.md"
        path.write_text(prompt, encoding="utf-8")
        contract = run_script(str(CONTRACT_GATE), str(path))
        lint = run_script(str(ARTIFACT_LINT), "--type", "prompt-package", str(path))

    assert contract.returncode == 0, contract.stdout
    assert "TRANSLATE_V2_CONTRACT_GATE_STATUS=OK" in contract.stdout
    assert lint.returncode == 0, lint.stdout
    assert "TRANSLATE_V2_ARTIFACT_LINT_STATUS=OK" in lint.stdout


def test_contract_gate_and_artifact_lint_block_flat_score_schema() -> None:
    prompt = """
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
"""
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "prompt.md"
        path.write_text(prompt, encoding="utf-8")
        contract = run_script(str(CONTRACT_GATE), str(path))
        lint = run_script(str(ARTIFACT_LINT), "--type", "prompt-package", str(path))

    assert contract.returncode == 2
    assert "flat-score-schema-forbidden" in contract.stdout
    assert lint.returncode == 2
    assert "flat-score-schema-forbidden" in lint.stdout


if __name__ == "__main__":
    test_contract_gate_and_artifact_lint_agree_on_prompt_requirements()
    test_contract_gate_and_artifact_lint_block_flat_score_schema()
    print("gate/lint integration tests passed")
