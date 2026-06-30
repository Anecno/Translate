#!/usr/bin/env python3
"""Lint public translate-v2 Markdown artifacts."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from translate_v2_common import flat_scores_missing, has_any, has_layered_scores, non_code_lines


ARTIFACT_TYPES = {
    "prompt-package",
    "baton-raw",
    "round-archive",
    "checkpoint",
    "divergence-report",
    "final-report",
}


def missing_required(text: str, checks: list[tuple[str, list[str]]]) -> list[str]:
    return [name for name, needles in checks if not has_any(text, needles)]


def english_only_surface_missing(text: str, prefix: str) -> list[str]:
    missing: list[str] = []
    for line_no, line in non_code_lines(text):
        stripped = line.strip()
        if stripped.startswith("#"):
            heading = stripped.lstrip("#").strip()
            if len(heading.split()) >= 2 and heading.isascii() and not any(ch.isdigit() for ch in heading):
                # Public artifacts may use English, but this catches placeholder-only
                # headings that usually indicate an unlocalized template leak.
                if heading.lower() in {"prompt package", "raw capture", "final report"}:
                    missing.append(f"{prefix}:placeholder-heading:L{line_no}")
    return missing


def syntax_morphology_missing(text: str, prefix: str) -> list[str]:
    checks = [
        (f"{prefix}:syntax-sentence-overview", ["sentence overview", "source anchor"]),
        (f"{prefix}:syntax-phrase-breakdown", ["phrase breakdown", "literal meaning"]),
        (f"{prefix}:syntax-dependency", ["dependency", "root", "modifiers"]),
        (f"{prefix}:syntax-lexical-morphology", ["lemma", "morphology"]),
        (f"{prefix}:syntax-strategy-tags", ["translation strategy", "strategy tag"]),
        (f"{prefix}:syntax-redline-audit", ["addition", "omission", "mistranslation", "hallucination"]),
    ]
    return missing_required(text, checks)


def prompt_package_missing(text: str) -> list[str]:
    checks = [
        ("prompt:baton-context", ["n-1", "n-2", "previous baton"]),
        ("prompt:principles-first", ["translation principles", "principles first"]),
        ("prompt:layered-scoring", ["scores.language", "scores.literary", "scores.cultural", "aggregate"]),
        ("prompt:raw-capture", ["raw capture", "full output"]),
        ("prompt:round-archive", ["round archive", "round summary"]),
        ("prompt:checkpoint", ["checkpoint", "wait for user"]),
        ("prompt:final-output-confirmation", ["final output", "user confirmation"]),
    ]
    missing = missing_required(text, checks)
    missing.extend(flat_scores_missing(text, "prompt:"))
    missing.extend(english_only_surface_missing(text, "prompt"))
    return missing


def baton_raw_missing(text: str) -> list[str]:
    checks = [
        ("baton:source-surface", ["source surface", "captured from"]),
        ("baton:relay-stage", ["relay stage", "baton"]),
        ("baton:full-output", ["full output"]),
        ("baton:candidate", ["candidate translation", "candidate"]),
        ("baton:review", ["review", "reason"]),
        ("baton:convergence", ["convergence", "satisfaction"]),
    ]
    missing = missing_required(text, checks)
    missing.extend(flat_scores_missing(text, "baton:"))
    missing.extend(english_only_surface_missing(text, "baton"))
    return missing


def round_archive_missing(text: str) -> list[str]:
    checks = [
        ("round:metadata", ["round", "source language", "target language"]),
        ("round:baton-table", ["baton", "candidate", "review"]),
        ("round:n-1-n-2", ["n-1", "n-2"]),
        ("round:checkpoint", ["checkpoint", "next step"]),
        ("round:raw-links", ["raw capture"]),
    ]
    missing = missing_required(text, checks)
    missing.extend(flat_scores_missing(text, "round:"))
    return missing


def checkpoint_missing(text: str) -> list[str]:
    checks = [
        ("checkpoint:user-stop", ["wait for user", "user decision"]),
        ("checkpoint:convergence-state", ["convergence", "remaining issue"]),
        ("checkpoint:next-options", ["continue", "revise", "finalize"]),
    ]
    return missing_required(text, checks)


def divergence_missing(text: str) -> list[str]:
    checks = [
        ("divergence:disputes", ["dispute", "recurring issue"]),
        ("divergence:root-causes", ["root cause"]),
        ("divergence:candidate-comparison", ["candidate comparison"]),
    ]
    missing = missing_required(text, checks)
    missing.extend(syntax_morphology_missing(text, "divergence"))
    missing.extend(flat_scores_missing(text, "divergence:"))
    return missing


def final_report_missing(text: str) -> list[str]:
    checks = [
        ("final:user-confirmation", ["user confirmation", "final output approved"]),
        ("final:source-text", ["source text"]),
        ("final:final-translation", ["final translation"]),
        ("final:relay-trajectory", ["relay trajectory", "baton"]),
        ("final:artifact-list", ["artifact list"]),
        ("final:compliance-check", ["compliance", "self-check"]),
    ]
    missing = missing_required(text, checks)
    missing.extend(syntax_morphology_missing(text, "final"))
    if not has_layered_scores(text):
        missing.append("final:layered-scoring")
    missing.extend(flat_scores_missing(text, "final:"))
    return missing


def lint_text(artifact_type: str, text: str) -> list[str]:
    if artifact_type == "prompt-package":
        return prompt_package_missing(text)
    if artifact_type == "baton-raw":
        return baton_raw_missing(text)
    if artifact_type == "round-archive":
        return round_archive_missing(text)
    if artifact_type == "checkpoint":
        return checkpoint_missing(text)
    if artifact_type == "divergence-report":
        return divergence_missing(text)
    if artifact_type == "final-report":
        return final_report_missing(text)
    raise ValueError(f"unknown artifact type: {artifact_type}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Lint a public translate-v2 Markdown artifact.")
    parser.add_argument("--type", required=True, choices=sorted(ARTIFACT_TYPES))
    parser.add_argument("path")
    args = parser.parse_args()

    path = Path(args.path)
    text = path.read_text(encoding="utf-8")
    missing = lint_text(args.type, text)
    if missing:
        print("TRANSLATE_V2_ARTIFACT_LINT_STATUS=BLOCKED")
        print("MISSING_POLICY_ITEMS=" + ",".join(missing))
        return 2
    print("TRANSLATE_V2_ARTIFACT_LINT_STATUS=OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
