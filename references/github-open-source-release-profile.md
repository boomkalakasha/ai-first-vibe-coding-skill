# GitHub open-source release profile

Use this profile only when repository instructions or the user explicitly choose public GitHub collaboration/release.

## Branch and PR

- Protect `main`; merge changes through pull requests.
- Create short descriptive branches from current `main`. If an issue exists, include its real number; do not fabricate one.
- Recommended names: `feat/123-short-description`, `fix/123-short-description`, `docs/short-description`, or a repository-defined equivalent.
- PRs include scope, linked issue, compatibility/security impact, evidence, screenshots when relevant, and release-note impact.
- Require unique status-check job names, resolved conversations, and code-owner review for sensitive paths where repository settings support them.

## Safe CI for forks

- Use `pull_request` with read-only permissions for untrusted fork code.
- Do not expose repository/environment secrets or privileged self-hosted runners to fork PRs.
- Do not combine `pull_request_target` with checkout/execution of untrusted PR code.
- Pin third-party actions to reviewed commit SHAs for release/security-sensitive workflows; let Dependabot propose updates.

## Version and release

- Use SemVer tags: `vMAJOR.MINOR.PATCH`; use `-rc.N` or `-beta.N` for prereleases.
- A public tag points to a reviewed default-branch commit and is never moved or reused.
- Build release artifacts from the exact tag. Publish checksums and, where supported, SBOM and provenance attestations.
- Keep `CHANGELOG.md` useful offline and GitHub Release notes authoritative for the published release event.
- Treat a GitHub Release as source/artifact publication, not proof of deployment or production acceptance.

## Backports and private downstreams

- Maintain supported lines on `release/X.Y` only when needed.
- Fix on `main` first, then create an auditable backport PR using `cherry-pick -x` where appropriate.
- Keep customer-specific branches, configuration, deployment scripts, and identifiers in private downstream repositories. Public upstream changes should contain only generalizable code.

## Release gate

- exact commit/tag recorded;
- clean required checks and independent review;
- version, changelog, docs, examples, and compatibility aligned;
- current-tree and history secret/privacy/license scans complete;
- artifacts can be rebuilt from the exact tag and include checksums;
- security reporting instructions present;
- release draft reviewed before publication;
- rollback/deprecation/migration notes included where applicable.

Repository-host settings such as branch protection, private vulnerability reporting, immutable releases, and tag rulesets must be verified in GitHub; files in the repository cannot prove those settings are enabled.
