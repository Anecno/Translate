#!/usr/bin/env python3
"""End-to-end consistency checks for the public relay validation flow."""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTRACT_GATE = ROOT / "scripts" / "translate_v2_contract_gate.py"
ARTIFACT_LINT = ROOT / "scripts" / "translate_v2_artifact_lint.py"
PREFLIGHT = ROOT / "scripts" / "translate_v2_preflight_check.py"


PROMPT = """
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


RAW_CAPTURE = """
# Baton Raw Capture
source surface: web relay.
captured from: local test fixture.
source language: ja
target language: en
relay stage: R1 baton 1.
principles first / translation principles
N-1 and N-2 previous baton context included
candidate translation: sample candidate.
review reason: sample review explaining the candidate.
convergence: pending.
scores.language
scores.literary
scores.cultural
aggregate
raw capture full output
round archive
checkpoint wait for user
final output user confirmation
"""


def run_script(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, *args],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )


def test_public_flow_contract_preflight_raw_lint_consistency() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        prompt_path = Path(tmp) / "prompt.md"
        raw_path = Path(tmp) / "raw.md"
        prompt_path.write_text(PROMPT, encoding="utf-8")
        raw_path.write_text(RAW_CAPTURE, encoding="utf-8")

        contract = run_script(str(CONTRACT_GATE), str(prompt_path))
        before_send = run_script(
            str(PREFLIGHT),
            "before-send",
            "--operator",
            "local",
            "--surface",
            "web-relay",
            "--prompt-file",
            str(prompt_path),
            "--raw-capture-plan",
            "capture full prompt and full output",
            "--contract-status",
            "TRANSLATE_V2_CONTRACT_GATE_STATUS=OK",
        )
        lint = run_script(str(ARTIFACT_LINT), "--type", "baton-raw", str(raw_path))
        after_result = run_script(
            str(PREFLIGHT),
            "after-result",
            "--surface",
            "web-relay",
            "--raw-capture-file",
            str(raw_path),
            "--artifact-lint-status",
            "TRANSLATE_V2_ARTIFACT_LINT_STATUS=OK",
            "--output-captured",
            "full output captured",
        )

    assert contract.returncode == 0, contract.stdout
    assert before_send.returncode == 0, before_send.stdout
    assert lint.returncode == 0, lint.stdout
    assert after_result.returncode == 0, after_result.stdout


if __name__ == "__main__":
    test_public_flow_contract_preflight_raw_lint_consistency()
    print("flow consistency tests passed")
