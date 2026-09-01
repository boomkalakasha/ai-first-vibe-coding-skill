#!/usr/bin/env python3
"""Validate one honest no-skill / short-prompt / AI-first comparison record."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


REQUIRED_VARIANTS = ("no-skill", "short-prompt", "ai-first")
COMPLETED_STATUSES = {"PASS", "FAIL", "BLOCKED"}
ALL_STATUSES = COMPLETED_STATUSES | {"PLANNED"}
OBSERVED_SOURCES = {"HOST_OBSERVED", "HUMAN_OBSERVED"}
ALL_SOURCES = OBSERVED_SOURCES | {"DOCUMENTED_ONLY"}


def error(errors: list[str], message: str) -> None:
    errors.append(message)


def is_non_negative_integer(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool) and value >= 0


def validate_results(payload: object) -> list[str]:
    errors: list[str] = []
    if not isinstance(payload, dict):
        return ["results must be a JSON object"]
    if payload.get("schemaVersion") != 1:
        error(errors, "schemaVersion must be 1")

    task = payload.get("task")
    if not isinstance(task, dict):
        return [*errors, "task must be an object"]
    task_id = task.get("id")
    criteria = task.get("successCriteria")
    if not isinstance(task_id, str) or not task_id.strip():
        error(errors, "task.id must be a non-empty string")
    if not isinstance(criteria, list) or not criteria or not all(isinstance(item, str) and item.strip() for item in criteria):
        error(errors, "task.successCriteria must be a non-empty list of strings")
    elif len(criteria) != len(set(criteria)):
        error(errors, "task.successCriteria must not contain duplicates")

    variants = payload.get("variants")
    if not isinstance(variants, list):
        return [*errors, "variants must be a list"]
    ids = [item.get("id") for item in variants if isinstance(item, dict)]
    missing = [name for name in REQUIRED_VARIANTS if name not in ids]
    unknown = [name for name in ids if name not in REQUIRED_VARIANTS]
    if missing:
        error(errors, f"missing required variants: {', '.join(missing)}")
    if unknown:
        error(errors, f"unknown variants: {', '.join(str(name) for name in unknown)}")
    if len(ids) != len(set(ids)):
        error(errors, "variant ids must be unique")
    if len(variants) != len(REQUIRED_VARIANTS):
        error(errors, "variants must contain exactly no-skill, short-prompt, and ai-first")

    expected_criteria = set(criteria) if isinstance(criteria, list) else set()
    for variant in variants:
        if not isinstance(variant, dict):
            error(errors, "each variant must be an object")
            continue
        variant_id = variant.get("id")
        prefix = variant_id if isinstance(variant_id, str) else "<unknown>"
        if variant.get("taskId") != task_id:
            error(errors, f"{prefix}: taskId must match task.id")
        status = variant.get("status")
        source = variant.get("observationSource")
        if status not in ALL_STATUSES:
            error(errors, f"{prefix}: status must be one of {', '.join(sorted(ALL_STATUSES))}")
        if source not in ALL_SOURCES:
            error(errors, f"{prefix}: observationSource is invalid")
        if status in COMPLETED_STATUSES:
            if source not in OBSERVED_SOURCES:
                error(errors, f"{prefix}: completed status requires HOST_OBSERVED or HUMAN_OBSERVED")
            if not is_non_negative_integer(variant.get("elapsedSeconds")):
                error(errors, f"{prefix}: completed status requires non-negative elapsedSeconds")
            if not is_non_negative_integer(variant.get("reworkCount")):
                error(errors, f"{prefix}: completed status requires non-negative reworkCount")
            verified = variant.get("verifiedCriteria")
            if (
                not isinstance(verified, list)
                or not all(isinstance(item, str) and item.strip() for item in verified)
                or len(verified) != len(set(verified))
                or set(verified) != expected_criteria
            ):
                error(errors, f"{prefix}: verifiedCriteria must match task.successCriteria")
        elif source != "DOCUMENTED_ONLY":
            error(errors, f"{prefix}: PLANNED status must use DOCUMENTED_ONLY")
    return errors


def print_summary(payload: dict[str, Any]) -> None:
    task = payload["task"]
    variants = payload["variants"]
    planned = [variant["id"] for variant in variants if variant["status"] == "PLANNED"]
    if planned:
        print(f"HOLD: comparative trial ({task['id']}) is planned only: {', '.join(planned)}")
        print("DOCUMENTED_ONLY: a planned record is not evidence that any agent host was evaluated")
        return
    print(f"VALID: comparable trial record ({task['id']})")
    for variant in variants:
        print(
            "EVIDENCE: "
            f"{variant['id']}={variant['status']} "
            f"source={variant['observationSource']} "
            f"elapsedSeconds={variant['elapsedSeconds']} reworkCount={variant['reworkCount']}"
        )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--results", type=Path, required=True)
    args = parser.parse_args()
    try:
        payload = json.loads(args.results.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot read results: {exc}", file=sys.stderr)
        return 2
    errors = validate_results(payload)
    if errors:
        for item in errors:
            print(f"FAIL: {item}")
        return 1
    assert isinstance(payload, dict)
    print_summary(payload)
    return 0


if __name__ == "__main__":
    sys.exit(main())
