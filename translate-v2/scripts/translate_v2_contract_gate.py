#!/usr/bin/env python3
"""Check a public translate-v2 prompt/handoff contract."""

from __future__ import annotations

import argparse

from translate_v2_common import flat_scores_missing, has_any, has_layered_scores


def contract_missing(text: str) -> list[str]:
    checks = [
        ("contract:scope", ["source language", "target language", "task scope"]),
        ("contract:principles-first", ["principles first", "translation principles"]),
        ("contract:baton-context", ["n-1", "n-2", "previous baton"]),
        ("contract:raw-capture", ["raw capture", "full output"]),
        ("contract:round-archive", ["round archive"]),
        ("contract:checkpoint", ["checkpoint", "wait for user"]),
        ("contract:final-output-confirmation", ["final output", "user confirmation"]),
        ("contract:stale-source-boundary", ["public spec", "current public entry"]),
    ]
    missing = [name for name, needles in checks if not has_any(text, needles)]
    if not has_layered_scores(text):
        missing.append("contract:layered-scoring")
    missing.extend(flat_scores_missing(text, "contract:"))
    stale_markers = [
        "scores_14d",
        "six-dimension score",
        "fixed critic",
        "parallel blind review",
        "skip raw capture",
        "no checkpoint needed",
    ]
    for marker in stale_markers:
        if marker in text.lower():
            missing.append(f"contract:stale-marker:{marker.replace(' ', '-')}")
    return missing


def main() -> int:
    parser = argparse.ArgumentParser(description="Check a translate-v2 public contract text.")
    parser.add_argument("path")
    args = parser.parse_args()
    with open(args.path, "r", encoding="utf-8") as handle:
        text = handle.read()
    missing = contract_missing(text)
    if missing:
        print("TRANSLATE_V2_CONTRACT_GATE_STATUS=BLOCKED")
        print("MISSING_POLICY_ITEMS=" + ",".join(missing))
        return 2
    print("TRANSLATE_V2_CONTRACT_GATE_STATUS=OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
