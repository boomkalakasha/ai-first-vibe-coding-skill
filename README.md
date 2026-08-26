# AI-first Vibe Coding Skill

![BOOMKALAKASHA watermark](assets/brand/watermark-dark.svg)

[中文说明](README.zh-CN.md) · [Quick start](docs/quick-start.md) · [Brand](docs/brand.md) · [Changelog](CHANGELOG.md) · [Contributing](CONTRIBUTING.md) · [Support](SUPPORT.md) · [Security](SECURITY.md)

An evidence-led workflow skill for turning fast AI-assisted coding into trustworthy software delivery.

Vibe coding is excellent at creating momentum. This skill keeps that momentum while adding the pieces that production work needs: repository boundaries, fact chains, testable specifications, honest evidence levels, safe Git delivery, multi-agent contracts, and iterative P0/P1 closure.

Release status and downloadable artifacts are tracked on [GitHub Releases](https://github.com/boomkalakasha/ai-first-vibe-coding-skill/releases). This source line targets `v1.1.1`; a tag alone is not proof that its Release gate passed.

## 60-second path

Use the bilingual [install, upgrade, rollback, and uninstall guide](docs/quick-start.md). The package commands create local artifacts and checksums; host discovery or runtime behavior remains `DOCUMENTED_ONLY` unless observed in that host.

## What makes it useful

- Scales from a one-file fix to cross-repository delivery without forcing heavyweight ceremony on small tasks.
- Separates source, build, runtime, business, release, deployment, and cutover evidence.
- Preserves dirty worktrees and treats every external side effect as a distinct permission.
- Connects requirement → contract → case → implementation → evidence → release gate.
- Supports controller/implementer/reviewer agent teams without trusting delegated completion claims.
- Includes an opt-in GitHub OSS release profile while respecting project-defined GitLab, Jenkins, and private downstream rules.
- Works with any coding agent that can read Markdown instructions; compatibility claims remain explicit and evidence-based.

## Installation

### Codex

Clone the repository into your Codex skills directory:

```powershell
git clone https://github.com/boomkalakasha/ai-first-vibe-coding-skill.git "$env:USERPROFILE\.codex\skills\ai-first-vibe-coding"
```

Restart or reload your Codex session, then invoke `$ai-first-vibe-coding` or describe a matching repository task.

For a packaged candidate, use `pwsh -NoProfile -File scripts/package.ps1 -Version 1.1.1`, inspect `dist/manifest.json` and `dist/SHA256SUMS.txt`, then follow your host's documented installation path. Do not treat archive creation as proof that Codex or another host installed it.

### Other agents

Point the agent's skill/instruction loader at this repository's `SKILL.md`. Some hosts use a different folder layout or metadata subset; see [compatibility](compatibility.md) and verify behavior in your own host before relying on it for release decisions.

## Example requests

- “Refactor this service, preserve current behavior, and prove the affected data path still works.”
- “Audit whether this feature branch can replace the current runtime 1:1; separate source and runtime evidence.”
- “Use multiple agents for implementation and independent review, and keep one P0/P1 ledger.”
- “Prepare this project for an open-source GitHub release without leaking internal GitLab/Jenkins details.”
- “复盘这次跨模块改造，补齐测试、运行态证据和发布门禁。”

## Repository layout

```text
SKILL.md                    Core routing and execution protocol
references/                 Detailed workflows and delivery profiles
templates/                  Copyable baselines, ledgers, and traceability
evals/                      Behavioral and trigger scenarios
scripts/validate.py         Dependency-free repository validation
scripts/package.ps1         Repeatable distributable archive with SHA-256
.github/                    Public contribution, CI, security, and release automation
```

## Quick validation

```powershell
python scripts/validate.py
python scripts/run_evals.py
pwsh -NoProfile -File scripts/package.ps1 -Version 1.1.1
```

The validator checks frontmatter, JSON, relative Markdown links, BOMs, repository-specific private patterns, and required project files. It is a safety net, not a substitute for manual legal/privacy review or a full secret-history scan.

The package stages one source tree and produces `.zip`, `.skill`, `manifest.json`, and `SHA256SUMS.txt`. Its manifest labels a source tree `clean` or `dirty`; only a clean exact-tag package can enter release review.

## Delivery profiles

The skill does not force one hosting platform:

- `project-defined`: follow the closest repository rules.
- `github-open-source`: protected `main`, PR checks, SemVer tags, GitHub Releases, checksums and optional provenance, fork-safe CI.
- `internal-gitlab`: follow the organization's supplied MR/Jenkins/customer-branch policy.

Public release and production deployment are deliberately separate proof states.

For a full public-repository readiness program, use the optional `icarus-open-source-governance` companion when the host makes it available. This Skill does not claim that the companion is installed or that GitHub settings have been verified.

## Optional brand example

The optional BOOMKALAKASHA watermark and avatar copies are local documentation assets. Optional BOOMKALAKASHA use never asserts project ownership, support, or permission to change a personal GitHub profile. See [brand guidance](docs/brand.md).

## Status and limitations

The repository's automated checks validate structure and deterministic assertions. They do not prove that every coding-agent host follows the instructions identically. See [compatibility](compatibility.md) for the current evidence matrix and [evals](evals/README.md) for the public evaluation boundary.

## License

Apache License 2.0. By contributing, you confirm that you have the right to submit the material under this license and that it contains no confidential or customer-specific information.
