#!/usr/bin/env python3
"""Shared helpers for public translate-v2 validators."""

from __future__ import annotations

import re


def has_any(text: str, needles: list[str]) -> bool:
    lowered = text.lower()
    return any(needle.lower() in lowered for needle in needles)


def contains_cjk(text: str) -> bool:
    return bool(re.search(r"[\u3400-\u9fff]", text))


def non_code_lines(text: str):
    in_fence = False
    for line_no, line in enumerate(text.splitlines(), start=1):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if not in_fence:
            yield line_no, line


FLAT_SCORE_MARKERS = [
    "scores_14d",
    "flat 14",
    "flat-score",
    "flat score",
]


FLAT_SCORE_INVALIDATION_MARKERS = [
    "scores_14d is invalid",
    "do not use scores_14d",
    "quoted failure example",
]


def flat_scores_missing(text: str, prefix: str = "") -> list[str]:
    lowered = text.lower()
    if not has_any(lowered, FLAT_SCORE_MARKERS):
        return []
    if has_any(lowered, FLAT_SCORE_INVALIDATION_MARKERS):
        return []
    return [f"{prefix}flat-score-schema-forbidden"]


def has_layered_scores(text: str) -> bool:
    return all(
        has_any(text, needles)
        for needles in [
            ["scores.language", "layer a", "language layer"],
            ["scores.literary", "layer b", "literary layer"],
            ["scores.cultural", "layer c", "cultural layer"],
            ["aggregate", "quality_score", "penalty_per_1000"],
        ]
    )
