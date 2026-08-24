# GitHub open-source profile RED/GREEN

Date: 2026-08-24

Scenario: sanitize an internal GitLab/Jenkins Java scaffold, publish a public GitHub upstream, and define branch, PR, CI, SemVer, release artifact, security, and customer-downstream rules.

## Baseline

The pre-change Skill correctly preserved dirty work and separated internal deployment from public release, but explicitly reported that no named GitHub OSS profile existed. GitHub Flow, SemVer, fork safety, public security policy, and release artifacts were therefore only proposed inference.

Status: `RED / DOCUMENTED_ONLY`.

## Updated Skill

An independent read-only evaluator:

- selected `github-open-source` only because the user explicitly requested GitHub publication;
- retained `internal-gitlab` for private downstream delivery;
- required protected `main`, PR evidence, fork-safe CI, SemVer, exact-tag artifacts, checksums, and release gates;
- kept customer configuration, `proj_main`-style branches, Jenkins topology, credentials, and private assets out of the public repository;
- refused to equate GitHub Release with deployment or cutover;
- identified repository-host settings as `NOT_VERIFIED` until observed in GitHub.

Status: `GREEN / DOCUMENTED_ONLY`.

## Limitations

This is one paired manual scenario, not a statistically meaningful model benchmark. Private transcripts and machine-specific paths are intentionally omitted. Repository validation verifies the scenario and reference files exist; it does not grade arbitrary model output.
