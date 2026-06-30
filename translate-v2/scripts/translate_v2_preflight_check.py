#!/usr/bin/env python3
"""Preflight checks for public translate-v2 relay operations."""

from __future__ import annotations

import argparse


def before_send_missing(args: argparse.Namespace) -> list[str]:
    missing: list[str] = []
    required = {
        "operator": args.operator,
        "surface": args.surface,
        "prompt_file": args.prompt_file,
        "raw_capture_plan": args.raw_capture_plan,
        "contract_status": args.contract_status,
    }
    for name, value in required.items():
        if not value:
            missing.append(f"before-send:{name}-missing")
    if args.contract_status and "OK" not in args.contract_status:
        missing.append("before-send:contract-not-ok")
    if args.prompt_file and not args.prompt_file.endswith((".md", ".txt")):
        missing.append("before-send:prompt-file-extension")
    return missing


def after_result_missing(args: argparse.Namespace) -> list[str]:
    missing: list[str] = []
    required = {
        "surface": args.surface,
        "raw_capture_file": args.raw_capture_file,
        "artifact_lint_status": args.artifact_lint_status,
        "output_captured": args.output_captured,
    }
    for name, value in required.items():
        if not value:
            missing.append(f"after-result:{name}-missing")
    if args.artifact_lint_status and "OK" not in args.artifact_lint_status:
        missing.append("after-result:artifact-lint-not-ok")
    if args.raw_capture_file and not args.raw_capture_file.endswith(".md"):
        missing.append("after-result:raw-capture-extension")
    return missing


def main() -> int:
    parser = argparse.ArgumentParser(description="Check translate-v2 relay preflight evidence.")
    sub = parser.add_subparsers(dest="command", required=True)

    before = sub.add_parser("before-send")
    before.add_argument("--operator")
    before.add_argument("--surface")
    before.add_argument("--prompt-file")
    before.add_argument("--raw-capture-plan")
    before.add_argument("--contract-status")

    after = sub.add_parser("after-result")
    after.add_argument("--surface")
    after.add_argument("--raw-capture-file")
    after.add_argument("--artifact-lint-status")
    after.add_argument("--output-captured")

    args = parser.parse_args()
    missing = before_send_missing(args) if args.command == "before-send" else after_result_missing(args)
    if missing:
        print("TRANSLATE_V2_PREFLIGHT_STATUS=BLOCKED")
        print("MISSING_POLICY_ITEMS=" + ",".join(missing))
        return 2
    print("TRANSLATE_V2_PREFLIGHT_STATUS=OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
