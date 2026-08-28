# AI-first Vibe Coding Skill

![BOOMKALAKASHA watermark](assets/brand/watermark-auto.svg)

[中文说明](README.zh-CN.md) · [Quick start](docs/quick-start.md) · [AI operation guide](docs/ai-operation-guide.md) · [Brand](docs/brand.md) · [Changelog](CHANGELOG.md) · [Contributing](CONTRIBUTING.md) · [Support](SUPPORT.md) · [Security](SECURITY.md)

> **让 AI 自主分工，把交付交给证据验收。**
>
> **Let AI divide the work; let evidence earn the release.**

Within clear boundaries, this Skill helps Codex or another coding agent break down the goal, assign bounded work, implement it, review it independently, and iterate until evidence supports the delivery decision. It is built for refactors, cross-repository delivery, and long-running engineering work—not just code generation.

Vibe coding is excellent at creating momentum. This skill keeps that momentum while adding the pieces that production work needs: repository boundaries, fact chains, testable specifications, honest evidence levels, safe Git delivery, multi-agent contracts, and iterative P0/P1 closure.

<!-- icarus-release-fact: dynamic -->
Public GitHub Releases and downloadable artifacts are available from the
[latest GitHub Release](https://github.com/boomkalakasha/ai-first-vibe-coding-skill/releases/latest)
and the [complete release history](https://github.com/boomkalakasha/ai-first-vibe-coding-skill/releases).
Use immutable tag assets for reproducible installation; a tag alone is not proof
that its Release gate passed.

## At a glance

| If you need to... | This Skill helps you... | You leave with... |
| --- | --- | --- |
| Turn a fuzzy goal into an executable plan | Map the outcome, boundaries, contracts, cases and decision points before coding | A task baseline, Spec and traceable acceptance cases |
| Split a long task across agents | Give each agent a bounded write set, role and stop condition; resize concurrency from live capacity signals | A shared execution ledger instead of scattered “done” messages |
| Know whether a change is really ready | Separate source, build, runtime, business, release and cutover evidence | A release decision with explicit `P0/P1` gates and honest unknowns |
| Ship across GitHub, GitLab or Jenkins | Select the repository's delivery profile and keep commits, reviews, tags and deployment proof separate | A reviewable branch/MR/PR path with rollback and evidence boundaries |

It is especially useful for service refactors, cross-repository changes, production-bound data flows and any task where “the tests passed” is only one part of the answer.

## 60-second path

1. Install or point your agent host at this repository's `SKILL.md`; the [AI operation guide](docs/ai-operation-guide.md) explains the smallest safe operating loop.
2. For a first task, ask for a baseline, user path, acceptance cases and the smallest safe write set.
3. For a long-running or multi-agent task, copy the [execution ledger](templates/execution-ledger.md) and [task baseline](templates/task-baseline.md), then re-check capacity at each wave boundary.
4. Run the bilingual [install, upgrade, rollback, and uninstall guide](docs/quick-start.md) and the local validation commands below. Host discovery or runtime behavior remains `DOCUMENTED_ONLY` unless observed in that host.

If the work is a one-line translation or a purely informational question, skip the full workflow and use the smallest tool that answers it.

## What you get

**Illustrative outcome — this is a format example, not a runtime or release
claim for your repository:**

| Ledger field | Example result |
| --- | --- |
| Goal | Preserve the existing API while splitting one service |
| Work packages | Contract, implementation, independent review, runtime check |
| Evidence | 42 tests passed; runtime identity still `NOT_RUN` |
| Gate | `P0: 0 open`; `P1: 0 open`; release remains `STATIC_PASS_PENDING_RUNTIME` |

The value is the decision trail: a reviewer can see what changed, which facts
were observed, what remains unknown, and why the candidate is or is not ready.

## What makes it useful

- Scales from a one-file fix to cross-repository delivery without forcing heavyweight ceremony on small tasks.
- Separates source, build, runtime, business, release, deployment, and cutover evidence.
- Preserves dirty worktrees and treats every external side effect as a distinct permission.
- Connects requirement → contract → case → implementation → evidence → release gate.
- Supports controller/implementer/reviewer agent teams without trusting delegated completion claims.
- Includes an opt-in GitHub OSS release profile while respecting project-defined GitLab, Jenkins, and private downstream rules.
- Works with any coding agent that can read Markdown instructions; compatibility claims remain explicit and evidence-based.

## Companion projects

- [Icarus AI Spring Scaffold](https://github.com/boomkalakasha/icarus-ai-spring-scaffold) — generate a safe, reviewable Java 17 service skeleton before handing implementation to collaborating agents.
- [Icarus Open-source Governance](https://github.com/boomkalakasha/icarus-open-source-governance-skill) — scan provenance and privacy risks, then package the documentation and release evidence when the project is ready to go public.

## Installation

### Codex

Clone the repository into your Codex skills directory:

```powershell
git clone --depth 1 https://github.com/boomkalakasha/ai-first-vibe-coding-skill.git "$env:USERPROFILE\.codex\skills\ai-first-vibe-coding"
```

This is the shortest supported install path. Restart or reload your Codex
session, then invoke `$ai-first-vibe-coding` or describe a matching repository
task. For other hosts, point the host's instruction loader at `SKILL.md` and
use the [AI operation guide](docs/ai-operation-guide.md) as the provider-neutral
baseline.

For a packaged candidate, use `pwsh -NoProfile -File scripts/package.ps1 -Version 1.2.3`, inspect `dist/manifest.json` and `dist/SHA256SUMS.txt`, then follow your host's documented installation path. Do not treat archive creation as proof that Codex or another host installed it.

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
pwsh -NoProfile -File scripts/package.ps1 -Version 1.2.3
```

The validator checks frontmatter, JSON, relative Markdown links, BOMs, repository-specific private patterns, and required project files. It is a safety net, not a substitute for manual legal/privacy review or a full secret-history scan.

The package stages one source tree and produces `.zip`, `.skill`, `manifest.json`, and `SHA256SUMS.txt`. Its manifest labels a source tree `clean` or `dirty`; only a clean exact-tag package can enter release review.

## Delivery profiles

The skill does not force one hosting platform:

- `project-defined`: follow the closest repository rules.
- `github-open-source`: protected `main`, PR checks, SemVer tags, GitHub Releases, checksums and optional provenance, fork-safe CI.
- `internal-gitlab`: follow the organization's supplied MR/Jenkins/customer-branch policy.

Public release and production deployment are deliberately separate proof states.

For a full public-repository readiness program, use the optional `icarus-open-source-governance` companion when the host makes it available. This is a routing name, not a claimed host installation; a GitHub Release does not prove that repository settings or production deployment were verified.

## Optional brand example

The optional BOOMKALAKASHA watermark and avatar copies are local documentation assets. Optional BOOMKALAKASHA use never asserts project ownership, support, or permission to change a personal GitHub profile. See [brand guidance](docs/brand.md).

## Status and limitations

The repository's automated checks validate structure and deterministic assertions. They do not prove that every coding-agent host follows the instructions identically. See [compatibility](compatibility.md) for the current evidence matrix and [evals](evals/README.md) for the public evaluation boundary.

## License

Apache License 2.0. By contributing, you confirm that you have the right to submit the material under this license and that it contains no confidential or customer-specific information.
