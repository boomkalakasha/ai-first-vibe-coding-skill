#!/usr/bin/env python3
"""Fail on new internal-policy markers while recording known public legacy history."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUNTIME_PATHS = ("SKILL.md", "references", "templates")
MARKERS = (
    "feat-#<Issue",
    "bug_fix-#<Issue",
    "proj_main-",
    "前后端分支管理规范.docx",
)
KNOWN_LEGACY_CHANGE_COMMITS = {
    "582c0c8578fea0e94d6440cd16a7584b280f9b88",
    "69e14841b16ea610eb4890742948e62fed08db92",
}


def git(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args], cwd=ROOT, capture_output=True, text=True, check=False
    )


def current_runtime_has_marker() -> bool:
    candidates = [ROOT / "SKILL.md", *(ROOT / "references").glob("*.md"), *(ROOT / "templates").glob("*.md")]
    source = "\n".join(path.read_text(encoding="utf-8") for path in candidates)
    return any(marker in source for marker in MARKERS)


def commit_tree_has_marker(commit: str, expression: str) -> bool:
    result = git("grep", "-q", "-E", expression, commit, "--", *RUNTIME_PATHS)
    if result.returncode not in (0, 1):
        raise RuntimeError(result.stderr.strip() or "git grep failed")
    return result.returncode == 0


def remote_heads_with_marker(expression: str) -> list[str]:
    refs = git(
        "for-each-ref", "--format=%(refname)", "refs/remotes/origin"
    )
    if refs.returncode != 0:
        raise RuntimeError(refs.stderr.strip() or "git for-each-ref failed")
    exposed: list[str] = []
    for ref in (line.strip() for line in refs.stdout.splitlines() if line.strip()):
        if ref.endswith("/HEAD"):
            continue
        if commit_tree_has_marker(ref, expression):
            exposed.append(ref.removeprefix("refs/remotes/"))
    return exposed


def main() -> int:
    if current_runtime_has_marker():
        print("FAIL: current public runtime contains an organization-policy marker")
        return 1
    top_level = git("rev-parse", "--show-toplevel")
    if (
        top_level.returncode != 0
        or Path(top_level.stdout.strip()).resolve() != ROOT.resolve()
    ):
        print("NOT_RUN: Git history is unavailable in this package checkout")
        return 0

    expression = "|".join(re.escape(marker) for marker in MARKERS)
    changed = git(
        "log", "--all", "--format=%H", "-G", expression, "--", *RUNTIME_PATHS
    )
    if changed.returncode != 0:
        print("FAIL: could not inspect reachable Git history")
        return 1
    commits = [line.strip() for line in changed.stdout.splitlines() if line.strip()]
    unexpected: list[str] = []
    remediation: list[str] = []
    for commit in commits:
        if commit in KNOWN_LEGACY_CHANGE_COMMITS:
            continue
        try:
            still_present = commit_tree_has_marker(commit, expression)
        except RuntimeError as exc:
            print(f"FAIL: {exc}")
            return 1
        if still_present:
            unexpected.append(commit)
        else:
            remediation.append(commit)
    if unexpected:
        for commit in unexpected:
            print(f"FAIL: unexpected history marker change remains present at {commit}")
        return 1
    print("PASS: current public runtime is free of organization-policy markers")
    print(
        "ACCEPTED_LEGACY: "
        f"{len(KNOWN_LEGACY_CHANGE_COMMITS)} already-public marker-change commits are recorded"
    )
    try:
        exposed_heads = remote_heads_with_marker(expression)
    except RuntimeError as exc:
        print(f"FAIL: {exc}")
        return 1
    if exposed_heads:
        print(
            "ACCEPTED_LEGACY: remote heads still exposing the recorded history: "
            + ", ".join(exposed_heads)
        )
    if remediation:
        print(f"PASS: {len(remediation)} remediation commit(s) remove the markers")
    return 0


if __name__ == "__main__":
    sys.exit(main())
