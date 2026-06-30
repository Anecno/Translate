#!/usr/bin/env python3
"""Regression tests for the public artifact linter."""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "translate_v2_artifact_lint.py"


def run_lint(artifact_type: str, text: str) -> subprocess.CompletedProcess[str]:
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "artifact.md"
        path.write_text(text, encoding="utf-8")
        return subprocess.run(
            [sys.executable, str(SCRIPT), "--type", artifact_type, str(path)],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )


def test_prompt_package_blocks_missing_contract() -> None:
    result = run_lint("prompt-package", "# Prompt\nTranslate this.")
    assert result.returncode == 2
    assert "TRANSLATE_V2_ARTIFACT_LINT_STATUS=BLOCKED" in result.stdout
    assert "prompt:baton-context" in result.stdout


def test_prompt_package_ok() -> None:
    result = run_lint(
        "prompt-package",
        """
# Relay Package
principles first / translation principles.
source language: ja. target language: en.
N-1 and N-2 previous baton context must be included.
scores.language
scores.literary
scores.cultural
aggregate
raw capture requires full output.
round archive with round summary.
checkpoint: wait for user.
final output requires user confirmation.
""",
    )
    assert result.returncode == 0
    assert "TRANSLATE_V2_ARTIFACT_LINT_STATUS=OK" in result.stdout


def test_final_report_blocks_flat_scores() -> None:
    result = run_lint(
        "final-report",
        """
# Final
user confirmation and final output approved.
source text.
final translation.
relay trajectory baton.
artifact list.
compliance self-check.
scores_14d
""",
    )
    assert result.returncode == 2
    assert "flat-score-schema-forbidden" in result.stdout


def final_report_ok_text() -> str:
    return """
# Completed Relay Report
user confirmation and final output approved.
source text.
final translation.
relay trajectory baton.
artifact list.
compliance self-check.
sentence overview with source anchor.
phrase breakdown with literal meaning.
dependency root modifiers.
lemma and morphology.
translation strategy and strategy tag.
addition omission mistranslation hallucination redline audit.
scores.language
scores.literary
scores.cultural
aggregate quality_score penalty_per_1000
"""


def test_final_report_blocks_missing_core_element() -> None:
    result = run_lint(
        "final-report",
        final_report_ok_text().replace("final translation.", ""),
    )
    assert result.returncode == 2
    assert "final:final-translation" in result.stdout


def test_final_report_blocks_missing_syntax_element() -> None:
    result = run_lint(
        "final-report",
        final_report_ok_text().replace("lemma and morphology.", ""),
    )
    assert result.returncode == 2
    assert "final:syntax-lexical-morphology" in result.stdout


def test_final_report_ok() -> None:
    result = run_lint("final-report", final_report_ok_text())
    assert result.returncode == 0
    assert "TRANSLATE_V2_ARTIFACT_LINT_STATUS=OK" in result.stdout


def test_divergence_report_blocks_missing_report_element() -> None:
    result = run_lint(
        "divergence-report",
        """
# Divergence Report
dispute and recurring issue.
root cause.
sentence overview with source anchor.
phrase breakdown with literal meaning.
dependency root modifiers.
lemma and morphology.
translation strategy and strategy tag.
addition omission mistranslation hallucination redline audit.
""",
    )
    assert result.returncode == 2
    assert "divergence:candidate-comparison" in result.stdout


if __name__ == "__main__":
    test_prompt_package_blocks_missing_contract()
    test_prompt_package_ok()
    test_final_report_blocks_flat_scores()
    test_final_report_blocks_missing_core_element()
    test_final_report_blocks_missing_syntax_element()
    test_final_report_ok()
    test_divergence_report_blocks_missing_report_element()
    print("artifact lint tests passed")
