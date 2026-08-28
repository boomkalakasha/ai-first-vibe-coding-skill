# Changelog

All notable changes are documented here. The project follows Semantic Versioning.

## [1.2.1] - 2026-08-28

> Candidate notes for the next release; this version is not public until its
> tag, CI, packaged assets and release gates are independently verified.

### Changed

- Reframed the bilingual first-glance description around autonomous goal
  decomposition, bounded agent work, implementation, independent review and
  repeated evidence-led acceptance.
- Replaced hard-coded latest-version claims with dynamic GitHub Release facts
  and added an illustrative execution-ledger outcome before the detailed guide.
- Added deterministic documentation checks for the user-facing outcome example
  and current packaging instructions.
- Added the reusable Governance release-documentation gate, pinned to the
  reviewed `main` commit SHA, before release packaging.
- Aligned the public Release workflow with that gate by accepting stable
  `vMAJOR.MINOR.PATCH` tags only; local candidate packaging may still use a
  prerelease version without publishing it through this workflow.

## [1.2.0] - 2026-08-26

> Local candidate notes; this version is not public until its tag, CI,
> packaged assets and release gates are independently verified.

### Added

- Added a capability-based multi-model orchestration reference with Controller,
  Implementer, evidence, review and release-audit roles.
- Added a single execution-ledger lifecycle, context re-anchoring, staged
  concurrency control and explicit P0/P1 stop gates.
- Added reusable handoff, iteration, business-write-path and branch-policy
  templates, plus red/green evidence for tiered-model closure and dynamic
  multi-window concurrency.
- Reworked both READMEs around a first-glance feature table, user scenarios and
  a four-step first-task path so a new maintainer can choose a safe starting point.
- Added a sanitized bilingual AI operation guide covering scope, evidence,
  safe parallel work, tool fallbacks, privacy and community discussion.

### Fixed

- Clarified that a delegated `DONE`, a green build or a published Release is
  not by itself proof of runtime or business completion.

## [1.1.3] - 2026-08-26

### Added

- Added a first-glance bilingual value proposition that explains autonomous agent delegation, independent review, iterative acceptance, and release evidence.
- Added companion links and short usage scenarios for Icarus Scaffold and Icarus Open-source Governance.

## [1.1.2] - 2026-08-26

### Fixed

- Added a theme-compatible BOOMKALAKASHA watermark with explicit light/dark fallbacks, and documented the asset choice for current `main` users.

## [1.1.1] - 2026-08-26

### Added

- Canonical staged-tree `.zip` and `.skill` package artifacts with manifest and SHA-256 checksums.
- Bilingual install/upgrade/rollback/uninstall guidance with explicit host-runtime limits.
- Runnable documented-only eval rubric, optional brand documentation, and a governed OSS handoff route.

### Fixed

- Restricted GitHub Release uploads to the four reviewed files so the local `dist/stage` directory cannot break publication.
- Added dynamic cross-window sub-agent concurrency governance and evidence-led controller/reviewer handoff guidance.

`v1.1.0` is retained as the immutable tag that exposed the failed release-upload contract; no GitHub Release was published for that tag.

## [1.0.0] - 2026-08-24

### Added

- General evidence-led AI software delivery workflow.
- L0-L3 task routing and explicit side-effect boundaries.
- Fact-chain, traceability, runtime, business, and release evidence model.
- Multi-agent controller/implementer/reviewer protocol with context re-anchoring.
- Optional GitHub open-source iteration and release profile.
- Bilingual documentation, public governance files, validation, packaging, and CI.

[1.2.1]: https://github.com/boomkalakasha/ai-first-vibe-coding-skill/releases/tag/v1.2.1
[1.2.0]: https://github.com/boomkalakasha/ai-first-vibe-coding-skill/releases/tag/v1.2.0
[1.1.3]: https://github.com/boomkalakasha/ai-first-vibe-coding-skill/releases/tag/v1.1.3
[1.1.2]: https://github.com/boomkalakasha/ai-first-vibe-coding-skill/releases/tag/v1.1.2
[1.1.1]: https://github.com/boomkalakasha/ai-first-vibe-coding-skill/releases/tag/v1.1.1
[1.0.0]: https://github.com/boomkalakasha/ai-first-vibe-coding-skill/releases/tag/v1.0.0
