#!/usr/bin/env python3
"""Validate a staged public translate-v2 skill package."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


PRIVATE_MARKERS = [
    "/Us" + "ers/",
    "~/.co" + "dex",
    "~/.cl" + "aude",
    "Desk" + "top/",
    "HISTORICAL " + "REFERENCE ONLY",
    "陛" + "下",
    "原" + "话",
    "chatgpt.com/" + "c/",
    "claude.ai/" + "chat/",
    "deep" + "seek.com/",
]

PRIVATE_REFERENCE_RE = re.compile(r"\b(?:memory\s+`)?(?:feedback|project|reference)_[a-z0-9_]+\.md`?", re.I)
PRIVATE_SCRIPT_RE = re.compile(r"\b(?:codex_skill_gate|codex_translate_v2_artifact_lint)\.py\b")
FORBIDDEN_PUBLIC_REFERENCES = [
    "companion/antique-game-within-game/NOTES.md",
]

REQUIRED_FILES = [
    "SKILL.md",
    "README.md",
    "REFERENCES.md",
    "NOTES.md",
    "spec-v0.3.12.md",
    "scripts/translate_v2_common.py",
    "scripts/translate_v2_artifact_lint.py",
    "scripts/translate_v2_contract_gate.py",
    "scripts/translate_v2_preflight_check.py",
    "scripts/translate_v2_public_package_gate.py",
    "tests/test_translate_v2_artifact_lint.py",
    "tests/test_translate_v2_contract_gate.py",
    "tests/test_translate_v2_preflight_check.py",
    "tests/test_translate_v2_public_package_gate.py",
]

FORBIDDEN_NAMES = {
    ".DS_Store",
    "HANDOVER.md",
    "SOURCE",
    "LAST_SYNC",
    "LOCALIZED",
}

FORBIDDEN_PARTS = {
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
}

FORBIDDEN_SUFFIXES = {
    ".pyc",
    ".pyo",
}

REQUIRED_PUBLIC_MARKERS = {
    "SKILL.md": [
        "哈基米",
        "老D",
        "小克",
        "包子",
        "小G",
        "哈士奇",
        "小D",
        "CC",
        "逗比",
        "Antique Game Within Game",
        "《古董局中局》",
    ],
    "spec-v0.3.12.md": [
        "Public original-preserved edition",
        "## 0. 顶层设计",
        "Step 1",
        "Web Relay",
        "CLI/API",
        "哈基米",
        "小G",
        "S_norm",
        "Layer A",
        "Layer B",
        "Layer C",
        "target-language dictionary",
        "Antique Game Within Game",
        "《古董局中局》",
        "Best-Worst Scaling",
        "Translation-report.md",
        "句法构词分析",
    ],
    "README.md": [
        "original-preserved public edition",
        "historical revision stream",
        "Antique Game",
        "《古董局中局》",
    ],
    "REFERENCES.md": [
        "References and Design Influences",
        "MQM",
        "ISO 17100",
        "ASTM F2575",
        "TREQA",
        "maats0519/maats_mqm",
        "GitHub API did not detect a license",
        "Skytliang/Multi-Agents-Debate",
        "GPL-3.0",
        "Concept-only influence",
    ],
    "NOTES.md": [
        "哈基米",
        "Antique Game Within Game",
        "《古董局中局》",
        "scores.language",
        "scripts/translate_v2_contract_gate.py",
        "relay",
    ],
}

STALE_LICENSE_CLAIMS = [
    (
        "maats-mit-unverified",
        re.compile(r"\|\s*(?:\*\*)?MAATS(?:\*\*)?\s*\|\s*MIT\s*\|", re.I),
    ),
    (
        "mad-mit-stale",
        re.compile(
            r"\|\s*(?:\*\*)?(?:Skytliang/)?(?:MAD|Multi-Agents-Debate)(?:\*\*)?\s*\|\s*MIT\s*\|",
            re.I,
        ),
    ),
]


def iter_files(root: Path) -> list[Path]:
    return sorted(path for path in root.rglob("*") if path.is_file())


def read_small(path: Path, limit: int = 300_000) -> str:
    if path.stat().st_size > limit:
        return ""
    return path.read_text(encoding="utf-8", errors="replace")


def package_missing(root: Path) -> list[str]:
    missing: list[str] = []
    files = iter_files(root)
    rels = [path.relative_to(root).as_posix() for path in files]
    for rel in REQUIRED_FILES:
        if rel not in rels:
            missing.append(f"package:required-file-missing:{rel}")
    forbidden = [rel for rel in rels if Path(rel).name in FORBIDDEN_NAMES]
    if forbidden:
        missing.append("package:private-metadata-present:" + ",".join(forbidden))
    generated = [
        rel
        for rel in rels
        if any(part in FORBIDDEN_PARTS for part in Path(rel).parts)
        or Path(rel).suffix.lower() in FORBIDDEN_SUFFIXES
    ]
    if generated:
        missing.append("package:generated-cache-present:" + ",".join(generated))
    for path in files:
        rel = path.relative_to(root).as_posix()
        if path.suffix.lower() not in {".md", ".py", ".txt", ".json", ".yml", ".yaml"}:
            continue
        text = read_small(path)
        if path.suffix.lower() in {".md", ".txt"}:
            for claim_id, pattern in STALE_LICENSE_CLAIMS:
                if pattern.search(text):
                    missing.append(f"package:stale-license-claim:{rel}:{claim_id}")
        for marker in PRIVATE_MARKERS:
            if marker in text:
                missing.append(f"package:private-marker:{rel}:{marker}")
        if path.suffix.lower() in {".md", ".txt"}:
            for ref in FORBIDDEN_PUBLIC_REFERENCES:
                if ref in text:
                    missing.append(f"package:dangling-public-reference:{rel}:{ref}")
            for match in PRIVATE_REFERENCE_RE.finditer(text):
                missing.append(f"package:private-reference:{rel}:{match.group(0).strip('`')}")
            for match in PRIVATE_SCRIPT_RE.finditer(text):
                missing.append(f"package:private-script-reference:{rel}:{match.group(0)}")
        if re.search(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", text, flags=re.I):
            missing.append(f"package:email-marker:{rel}")
    for rel, markers in REQUIRED_PUBLIC_MARKERS.items():
        path = root / rel
        if not path.is_file():
            continue
        text = read_small(path)
        absent = [marker for marker in markers if marker not in text]
        if absent:
            missing.append(f"package:overredacted-public-content:{rel}:" + "|".join(absent))
    return missing


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a staged public translate-v2 package.")
    parser.add_argument("package_dir")
    args = parser.parse_args()
    root = Path(args.package_dir).resolve()
    if not root.is_dir():
        print("TRANSLATE_V2_PUBLIC_PACKAGE_STATUS=BLOCKED")
        print("MISSING_POLICY_ITEMS=package:directory-missing")
        return 2
    missing = package_missing(root)
    if missing:
        print("TRANSLATE_V2_PUBLIC_PACKAGE_STATUS=BLOCKED")
        print("MISSING_POLICY_ITEMS=" + ",".join(missing))
        return 2
    print("TRANSLATE_V2_PUBLIC_PACKAGE_STATUS=OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
