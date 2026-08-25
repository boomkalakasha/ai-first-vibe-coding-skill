"""Validate the documented-only evaluation rubric without inventing host runs."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    behavior = json.loads((ROOT / "evals" / "evals.json").read_text(encoding="utf-8"))
    rubric = json.loads((ROOT / "evals" / "rubric.json").read_text(encoding="utf-8"))
    behavior_ids = {case.get("id") for case in behavior.get("cases", []) if isinstance(case, dict)}
    rubric_cases = rubric.get("cases", [])
    rubric_ids = {case.get("id") for case in rubric_cases if isinstance(case, dict)}
    errors: list[str] = []
    if rubric.get("evaluation_mode") != "DOCUMENTED_ONLY":
        errors.append("rubric evaluation_mode must be DOCUMENTED_ONLY without a host execution")
    if behavior_ids != rubric_ids:
        errors.append("rubric case ids must match evals/evals.json")
    for case in rubric_cases:
        if not isinstance(case, dict) or not isinstance(case.get("criteria"), list) or not case["criteria"]:
            errors.append(f"rubric case {case.get('id', '<unknown>')!r} needs non-empty criteria")
    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1
    print(f"PASS: rubric covers {len(behavior_ids)} evaluation scenario(s)")
    print("DOCUMENTED_ONLY: no coding-agent host was invoked; use this rubric for a separately recorded host run")
    return 0


if __name__ == "__main__":
    sys.exit(main())
