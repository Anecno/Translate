#!/usr/bin/env python3
"""Regression tests for the public package gate."""

from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "translate_v2_public_package_gate.py"


def run_gate(path: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), str(path)],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )


def make_good_package(root: Path) -> None:
    (root / "scripts").mkdir()
    (root / "tests").mkdir()
    (root / "SKILL.md").write_text(
        "# Public skill\n"
        "Web Relay: 哈基米, 老D, 小克, 包子, 小G.\n"
        "CLI/API Relay: 哈士奇, 小D, CC, 逗比.\n"
        "Antique Game Within Game / 《古董局中局》 context boundary.\n",
        encoding="utf-8",
    )
    (root / "README.md").write_text(
        "# Public validation gates\n"
        "This is an original-preserved public edition.\n"
        "The historical revision stream is removed.\n"
        "Antique Game Within Game / 《古董局中局》 is an authorized workflow boundary.\n",
        encoding="utf-8",
    )
    (root / "REFERENCES.md").write_text(
        "# References and Design Influences\n"
        "MQM, ISO 17100, ASTM F2575, and TREQA are reviewed references.\n"
        "maats0519/maats_mqm: GitHub API did not detect a license.\n"
        "Skytliang/Multi-Agents-Debate: GPL-3.0. Concept-only influence.\n",
        encoding="utf-8",
    )
    (root / "spec-v0.3.12.md").write_text(
        "# Spec\n"
        "Public original-preserved edition. ## 0. 顶层设计. Step 1.\n"
        "Web Relay and CLI/API rules. 哈基米. 小G. S_norm. Layer A. Layer B. Layer C.\n"
        "target-language dictionary. Antique Game Within Game / 《古董局中局》.\n"
        "Best-Worst Scaling. Translation-report.md. 句法构词分析.\n",
        encoding="utf-8",
    )
    (root / "NOTES.md").write_text(
        "# Notes\n"
        "哈基米 relay guardrails. Antique Game Within Game / 《古董局中局》 boundary.\n"
        "scores.language and scripts/translate_v2_contract_gate.py are required.\n",
        encoding="utf-8",
    )
    for rel in [
        "translate_v2_common.py",
        "translate_v2_artifact_lint.py",
        "translate_v2_contract_gate.py",
        "translate_v2_preflight_check.py",
        "translate_v2_public_package_gate.py",
    ]:
        shutil.copy(ROOT / "scripts" / rel, root / "scripts" / rel)
    for rel in [
        "test_translate_v2_artifact_lint.py",
        "test_translate_v2_contract_gate.py",
        "test_translate_v2_preflight_check.py",
        "test_translate_v2_public_package_gate.py",
    ]:
        shutil.copy(ROOT / "tests" / rel, root / "tests" / rel)


def test_package_blocks_missing_files() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "SKILL.md").write_text("# Public skill\n", encoding="utf-8")
        result = run_gate(root)
    assert result.returncode == 2
    assert "package:required-file-missing" in result.stdout


def test_package_blocks_private_marker() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        make_good_package(root)
        marker = "/Us" + "ers/example/path"
        honorific = "陛" + "下"
        with (root / "README.md").open("a", encoding="utf-8") as handle:
            handle.write(f"Do not publish {marker} or {honorific}\n")
        result = run_gate(root)
    assert result.returncode == 2
    assert "package:private-marker" in result.stdout
    assert "/Us" + "ers/" in result.stdout
    assert honorific in result.stdout


def test_package_blocks_chat_url_and_user_quote_label() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        make_good_package(root)
        url = "chatgpt.com/" + "c/abc123"
        quote_label = "原" + "话"
        with (root / "README.md").open("a", encoding="utf-8") as handle:
            handle.write(f"{url}\n用户{quote_label}: do not publish\n")
        result = run_gate(root)
    assert result.returncode == 2
    assert "package:private-marker:README.md" in result.stdout
    assert "chatgpt.com/" + "c/" in result.stdout
    assert quote_label in result.stdout


def test_package_blocks_private_memory_reference() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        make_good_package(root)
        private_memory = "feedback" + "_deepl_context_required.md"
        private_reference = "reference" + "_doubi_capacity.md"
        (root / "spec-v0.3.12.md").write_text(
            "Public original-preserved edition. ## 0. 顶层设计. Step 1.\n"
            "Web Relay and CLI/API rules. 哈基米. 小G. S_norm. Layer A. Layer B. Layer C.\n"
            "target-language dictionary. Antique Game Within Game / 《古董局中局》.\n"
            "Best-Worst Scaling. Translation-report.md. 句法构词分析.\n"
            f"Do not publish memory `{private_memory}` or {private_reference}.\n",
            encoding="utf-8",
        )
        result = run_gate(root)
    assert result.returncode == 2
    assert "package:private-reference:spec-v0.3.12.md" in result.stdout
    assert "feedback" + "_deepl_context_required.md" in result.stdout
    assert "reference" + "_doubi_capacity.md" in result.stdout


def test_package_blocks_private_script_reference() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        make_good_package(root)
        private_script = "codex" + "_skill_gate.py"
        (root / "NOTES.md").write_text(
            "# Notes\n"
            "哈基米 relay guardrails. Antique Game Within Game / 《古董局中局》 boundary.\n"
            "scores.language and scripts/translate_v2_contract_gate.py are required.\n"
            f"Do not publish {private_script}.\n",
            encoding="utf-8",
        )
        result = run_gate(root)
    assert result.returncode == 2
    assert "package:private-script-reference:NOTES.md:codex" + "_skill_gate.py" in result.stdout


def test_package_blocks_dangling_antique_companion_reference() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        make_good_package(root)
        dangling = "companion/antique-game-within-game/NOTES.md"
        with (root / "NOTES.md").open("a", encoding="utf-8") as handle:
            handle.write(f"Do not publish a dangling companion reference: {dangling}\n")
        result = run_gate(root)
    assert result.returncode == 2
    assert "package:dangling-public-reference:NOTES.md:companion/antique-game-within-game/NOTES.md" in result.stdout


def test_package_blocks_overredacted_public_content() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        make_good_package(root)
        (root / "spec-v0.3.12.md").write_text("# Thin spec\n", encoding="utf-8")
        result = run_gate(root)
    assert result.returncode == 2
    assert "package:overredacted-public-content:spec-v0.3.12.md" in result.stdout


def test_package_blocks_overredacted_notes() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        make_good_package(root)
        (root / "NOTES.md").write_text("# Notes\n", encoding="utf-8")
        result = run_gate(root)
    assert result.returncode == 2
    assert "package:overredacted-public-content:NOTES.md" in result.stdout


def test_package_blocks_platform_junk() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        make_good_package(root)
        (root / ".DS_Store").write_bytes(b"junk")
        result = run_gate(root)
    assert result.returncode == 2
    assert "package:private-metadata-present:.DS_Store" in result.stdout


def test_package_blocks_python_cache() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        make_good_package(root)
        cache = root / "scripts" / "__pycache__"
        cache.mkdir()
        (cache / "translate_v2_artifact_lint.cpython-313.pyc").write_bytes(b"cache")
        result = run_gate(root)
    assert result.returncode == 2
    assert "package:generated-cache-present" in result.stdout


def test_package_blocks_stale_license_claims() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        make_good_package(root)
        with (root / "REFERENCES.md").open("a", encoding="utf-8") as handle:
            handle.write("| **MAATS** | MIT | stale claim |\n")
            handle.write("| **Skytliang/MAD** | MIT | stale claim |\n")
        result = run_gate(root)
    assert result.returncode == 2
    assert "package:stale-license-claim:REFERENCES.md:maats-mit-unverified" in result.stdout
    assert "package:stale-license-claim:REFERENCES.md:mad-mit-stale" in result.stdout


def test_package_ok() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        make_good_package(root)
        result = run_gate(root)
    assert result.returncode == 0
    assert "TRANSLATE_V2_PUBLIC_PACKAGE_STATUS=OK" in result.stdout


if __name__ == "__main__":
    test_package_blocks_missing_files()
    test_package_blocks_private_marker()
    test_package_blocks_chat_url_and_user_quote_label()
    test_package_blocks_private_memory_reference()
    test_package_blocks_private_script_reference()
    test_package_blocks_dangling_antique_companion_reference()
    test_package_blocks_overredacted_public_content()
    test_package_blocks_overredacted_notes()
    test_package_blocks_platform_junk()
    test_package_blocks_python_cache()
    test_package_blocks_stale_license_claims()
    test_package_ok()
    print("public package gate tests passed")
