# Changelog

All notable changes are documented here. The project follows Semantic Versioning.

## [1.2.5] - 2026-09-01

### Changed

- Added a provider-neutral project-guidance drift check that distinguishes stale
  documentation, implementation drift, old runtime, and uncertain version identity.
- Required independent judgment and explicit clarification when missing evidence
  would materially change business, data, permission, or release decisions.
- Removed Java, Vue, JRebel, PostgreSQL, and Snowflake-specific operating notes
  from the generic Skill so project-specific rules remain in each repository.

### Evals

- Added a discriminating project-guidance drift and evidence-gap scenario.

## [1.2.4] - 2026-08-28

### Fixed

- Made draft identity independent of the differing GitHub CLI and REST URL
  representations by enforcing zero pre-existing drafts and exactly one new
  `draft=true` release for the expected tag.
- Added bounded retries for GitHub's post-create consistency window until the
  expected draft and all four reviewed assets are visible, then compare their
  exact names.
- Reissued the complete package after the `v1.2.3` workflow correctly created
  its draft but failed closed while matching the draft by URL.

## [1.2.3] - 2026-08-28

> The tag exists and its workflow created a private draft with all four custom
> assets, but the post-create guard failed because GitHub CLI and REST expose
> different URL forms for the same draft. No `v1.2.3` Release was published;
> use `v1.2.4`.

### Fixed

- Kept the exact-draft verification command inside valid GitHub Actions YAML
  while preserving the fail-closed draft, tag and asset checks.
- Added a regression test for the release step's block-scalar indentation so a
  workflow parse failure is caught before another tag is created.
- Prepared the complete packaged assets after the `v1.2.2` YAML failure; the
  later URL-identity mismatch prevented them from becoming a public
  `v1.2.3` Release.

## [1.2.2] - 2026-08-28

> The tag exists, but GitHub rejected the Release workflow before execution
> because the embedded Python command escaped the YAML block indentation. No
> `v1.2.2` GitHub Release was published; use `v1.2.4`.

### Fixed

- Added a fail-closed post-create check for the exact four draft Release assets.
- Captured the CI-created `untagged-*` draft URL directly, verified that exact
  draft and its assets through the GitHub API, and exposed the URL in the
  workflow summary so a maintainer does not accidentally publish a second,
  empty Release form for the same tag.
- Prepared a reissue of the packaged assets missing from the immutable
  `v1.2.1` Release; the workflow parse failure prevented that reissue from
  becoming a `v1.2.2` Release.

## [1.2.1] - 2026-08-28

> The source release is public. Its custom packaged assets were not retained
> when a second empty Release form was published for the same tag; use
> `v1.2.4` for the complete downloadable package and checksums.

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

[1.2.5]: https://github.com/boomkalakasha/ai-first-vibe-coding-skill/releases/tag/v1.2.5
[1.2.4]: https://github.com/boomkalakasha/ai-first-vibe-coding-skill/releases/tag/v1.2.4
[1.2.3]: https://github.com/boomkalakasha/ai-first-vibe-coding-skill/releases/tag/v1.2.3
[1.2.2]: https://github.com/boomkalakasha/ai-first-vibe-coding-skill/releases/tag/v1.2.2
[1.2.1]: https://github.com/boomkalakasha/ai-first-vibe-coding-skill/releases/tag/v1.2.1
[1.2.0]: https://github.com/boomkalakasha/ai-first-vibe-coding-skill/releases/tag/v1.2.0
[1.1.3]: https://github.com/boomkalakasha/ai-first-vibe-coding-skill/releases/tag/v1.1.3
[1.1.2]: https://github.com/boomkalakasha/ai-first-vibe-coding-skill/releases/tag/v1.1.2
[1.1.1]: https://github.com/boomkalakasha/ai-first-vibe-coding-skill/releases/tag/v1.1.1
[1.0.0]: https://github.com/boomkalakasha/ai-first-vibe-coding-skill/releases/tag/v1.0.0
