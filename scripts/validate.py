#!/usr/bin/env python3
"""Dependency-free structural validation for the public Skill repository."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "SKILL.md",
    "README.md",
    "README.zh-CN.md",
    "LICENSE",
    "AGENTS.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    "SUPPORT.md",
    "CHANGELOG.md",
    "references/github-open-source-release-profile.md",
    "evals/evals.json",
    "evals/trigger-evals.json",
    "evals/rubric.json",
    "scripts/run_evals.py",
    "docs/quick-start.md",
    "docs/quick-start.zh-CN.md",
    "docs/brand.md",
    "assets/brand/brand-mark.svg",
    "assets/brand/avatar.png",
    "assets/brand/watermark-dark.svg",
    "assets/brand/watermark-light.svg",
    "assets/brand/watermark-auto.svg",
    "docs/assets/brand/brand-mark.svg",
    "docs/assets/brand/avatar.png",
    "docs/assets/brand/watermark-dark.svg",
    "docs/assets/brand/watermark-light.svg",
    "docs/assets/brand/watermark-auto.svg",
]
TEXT_SUFFIXES = {".md", ".json", ".py", ".ps1", ".yml", ".yaml", ".txt", ".svg"}
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
PRIVATE_PATTERNS = {
    "Windows user path": re.compile(r"[A-Za-z]:\\Users\\[^\\\s]+", re.IGNORECASE),
    "private IPv4 range": re.compile(r"https?://10\.\d{1,3}\.\d{1,3}\.\d{1,3}", re.IGNORECASE),
    "GitHub token": re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b"),
    "private key": re.compile(r"BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY"),
    "legacy private marker": re.compile(r"\b(?:ysstech|metateam|yss-ai|biggroup)\b", re.IGNORECASE),
}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def text_files() -> list[Path]:
    excluded = {".git", "dist", "__pycache__"}
    return [
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and path.suffix.lower() in TEXT_SUFFIXES
        and not excluded.intersection(path.relative_to(ROOT).parts)
    ]


def validate_frontmatter(errors: list[str]) -> None:
    content = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    if not content.startswith("---\n"):
        fail(errors, "SKILL.md must start with YAML frontmatter")
        return
    parts = content.split("---", 2)
    if len(parts) != 3:
        fail(errors, "SKILL.md frontmatter is not closed")
        return
    frontmatter = parts[1]
    for key in ("name:", "description:", "license:"):
        if not re.search(rf"(?m)^{re.escape(key)}\s*\S", frontmatter):
            fail(errors, f"SKILL.md frontmatter is missing {key[:-1]}")
    if not re.search(r"(?m)^name:\s*ai-first-vibe-coding\s*$", frontmatter):
        fail(errors, "Skill name must be ai-first-vibe-coding")


def validate_json(errors: list[str]) -> None:
    for relative in ("evals/evals.json", "evals/trigger-evals.json", "evals/rubric.json"):
        path = ROOT / relative
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
            fail(errors, f"{relative}: invalid JSON: {exc}")
            continue
        cases = data.get("cases")
        if not isinstance(cases, list) or not cases:
            fail(errors, f"{relative}: cases must be a non-empty list")
        ids = [case.get("id") for case in cases if isinstance(case, dict)]
        if len(ids) != len(set(ids)):
            fail(errors, f"{relative}: case ids must be unique")
    behavior = json.loads((ROOT / "evals/evals.json").read_text(encoding="utf-8"))
    github_case = next((case for case in behavior["cases"] if case.get("id") == "github-open-source-profile"), None)
    if not github_case:
        fail(errors, "evals/evals.json must cover the GitHub open-source profile")
    rubric = json.loads((ROOT / "evals/rubric.json").read_text(encoding="utf-8"))
    if rubric.get("evaluation_mode") != "DOCUMENTED_ONLY":
        fail(errors, "evals/rubric.json must retain DOCUMENTED_ONLY host evidence")
    behavior_ids = {case.get("id") for case in behavior.get("cases", []) if isinstance(case, dict)}
    rubric_ids = {case.get("id") for case in rubric.get("cases", []) if isinstance(case, dict)}
    if behavior_ids != rubric_ids:
        fail(errors, "evals/rubric.json case ids must match evals/evals.json")


def validate_release_contract(errors: list[str]) -> None:
    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    if 'version: "1.1.3"' not in skill:
        fail(errors, "SKILL.md must declare the v1.1.3 patch version")
    if "icarus-open-source-governance" not in skill or "not a claimed host installation" not in skill:
        fail(errors, "SKILL.md must provide a truthful optional governance-skill handoff")
    english = (ROOT / "README.md").read_text(encoding="utf-8")
    chinese = (ROOT / "README.zh-CN.md").read_text(encoding="utf-8")
    for source, heading, release_boundary in (
        (english, "## 60-second path", "a tag alone is not proof"),
        (chinese, "## 60 秒路径", "仅创建标签不能证明"),
    ):
        if heading not in source or release_boundary not in source or "GitHub Releases" not in source:
            fail(errors, "README language pair must expose the v1.1.3 release-evidence boundary")
    security = (ROOT / "SECURITY.md").read_text(encoding="utf-8").lower()
    if "seven days" in security or "does not promise" not in security:
        fail(errors, "SECURITY.md must not invent a response SLA")
    for path in (ROOT / "docs" / "quick-start.md", ROOT / "docs" / "quick-start.zh-CN.md"):
        if "DOCUMENTED_ONLY" not in path.read_text(encoding="utf-8"):
            fail(errors, f"{path.relative_to(ROOT)} must state the host-evidence boundary")
    for workflow in (ROOT / ".github" / "workflows").glob("*.yml"):
        source = workflow.read_text(encoding="utf-8")
        if "pull_request_target" in source:
            fail(errors, f"{workflow.relative_to(ROOT)}: pull_request_target is forbidden")
        for line in source.splitlines():
            if "uses:" in line and not re.search(r"uses:\s*[^@\s]+@[0-9a-f]{40}\b", line):
                fail(errors, f"{workflow.relative_to(ROOT)}: action references must use reviewed commit SHAs")


def validate_files(errors: list[str]) -> None:
    for relative in REQUIRED:
        if not (ROOT / relative).is_file():
            fail(errors, f"missing required file: {relative}")

    for path in text_files():
        relative = path.relative_to(ROOT).as_posix()
        raw = path.read_bytes()
        if raw.startswith(b"\xef\xbb\xbf"):
            fail(errors, f"{relative}: UTF-8 BOM is not allowed")
        try:
            content = raw.decode("utf-8")
        except UnicodeDecodeError as exc:
            fail(errors, f"{relative}: not valid UTF-8: {exc}")
            continue
        if path.name != "validate.py":
            for label, pattern in PRIVATE_PATTERNS.items():
                if pattern.search(content):
                    fail(errors, f"{relative}: matched {label}")
        if path.suffix.lower() == ".md":
            for target in MARKDOWN_LINK.findall(content):
                target = target.strip().split(maxsplit=1)[0].strip("<>")
                if target.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                target_path = (path.parent / target.split("#", 1)[0]).resolve()
                if not target_path.exists():
                    fail(errors, f"{relative}: broken relative link {target}")


def main() -> int:
    errors: list[str] = []
    validate_files(errors)
    if (ROOT / "SKILL.md").is_file():
        validate_frontmatter(errors)
    if all((ROOT / relative).is_file() for relative in ("evals/evals.json", "evals/trigger-evals.json", "evals/rubric.json")):
        validate_json(errors)
    if all((ROOT / relative).is_file() for relative in REQUIRED):
        validate_release_contract(errors)
    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("PASS: v1.1 package, bilingual lifecycle, optional governance handoff, and host-evidence boundary")
    print(f"Validation passed: {len(text_files())} text files checked")
    return 0


if __name__ == "__main__":
    sys.exit(main())
