# Repository Guidelines

## Project Structure

`SKILL.md` is the public entrypoint and must stay concise enough to load as instructions. Put detailed guidance in `references/`, reusable tables in `templates/`, deterministic checks in `scripts/`, and behavioral examples in `evals/`. Public collaboration and release automation live in `.github/`. Design decisions and implementation plans live under `docs/`.

## Build and Validation

Run `python scripts/validate.py` before every commit. It validates frontmatter, JSON, Markdown links, UTF-8/BOM, required files, and known private-pattern leaks. Run `pwsh -File scripts/package.ps1` to create the release ZIP and SHA-256 under `dist/`. Both commands must work from the repository root and must not require private services.

## Writing Style

Use direct, testable language. Separate facts, inferences, and unverified claims. Do not add company policies, customer examples, internal URLs, local absolute paths, credentials, or unverifiable compatibility claims. Keep English and Chinese README behaviorally aligned. Prefer relative links and UTF-8 without BOM.

## Tests and Evals

Every behavior change needs a failing or discriminating scenario in `evals/evals.json` or `evals/trigger-evals.json`, followed by current validation evidence. Deterministic assertions belong in `scripts/validate.py`; model-quality observations must be labeled manual and retain their limitations.

## GitHub OSS Delivery Profile

Use the optional `github-open-source` profile in `references/github-open-source-release-profile.md`. Work on a short branch, link a real Issue when one exists, and merge through a reviewed PR into protected `main`. Use truthful Conventional Commits, for example `feat(workflow): add release evidence gate`. Tags follow `vMAJOR.MINOR.PATCH`; never move a published tag. GitHub Releases publish reviewed source/artifacts only and do not prove production deployment. Keep private customer branches and internal CI configuration outside this repository.
