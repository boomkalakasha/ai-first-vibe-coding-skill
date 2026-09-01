# Repository Guidelines

## Project Structure

`SKILL.md` is the public entrypoint and must stay concise enough to load as instructions. Put detailed guidance in `references/`, reusable tables in `templates/`, deterministic checks in `scripts/`, and behavioral examples in `evals/`. Public collaboration and release automation live in `.github/`. Design decisions and implementation plans live under `docs/`.

## Build and Validation

Run the complete local gate from the repository root before opening a pull request:

```text
python scripts/validate.py
python scripts/check_history_boundaries.py
python -m unittest discover -s scripts -p "test_*.py"
python scripts/run_evals.py
pwsh -NoProfile -File scripts/package.ps1
```

The validator covers frontmatter, JSON, Markdown links, UTF-8/BOM, required
files, and known private-pattern leaks. The history boundary check reports
documented legacy exposure separately from new leakage; never rewrite public
history merely to silence it. Packaging creates the release ZIP and SHA-256
under `dist/`. These commands must work without private services.

## Writing Style

Use direct, testable language. Separate facts, inferences, and unverified claims. Do not add company policies, customer examples, internal URLs, local absolute paths, credentials, or unverifiable compatibility claims. Keep English and Chinese README behaviorally aligned. Prefer relative links and UTF-8 without BOM.

## Tests and Evals

Every behavior change needs a failing or discriminating scenario in `evals/evals.json` or `evals/trigger-evals.json`, followed by current validation evidence. Deterministic assertions belong in `scripts/validate.py`; model-quality observations must be labeled manual and retain their limitations.

## Project/module AI guidance coverage

This root `AGENTS.md` is the project-level guide for the public Skill. Its
runtime is intentionally organized by content type rather than independently
released application modules, so the current module-level status is
`NOT_NEEDED`. Do not create duplicate instructions just because a folder exists.
Reassess this decision when a subarea gains distinct build/run commands,
privileged data or external contracts, a separate release/ownership lifecycle,
or a dependency direction that the root guide cannot explain. Keep any needed
nearest-scope guide short, link it back here, and keep project or organization
facts out of the public runtime.

## GitHub OSS Delivery Profile

Use the optional `github-open-source` profile in `references/github-open-source-release-profile.md`. Work on a short branch, link a real Issue when one exists, and merge through a reviewed PR into protected `main`. Use truthful Conventional Commits, for example `feat(workflow): add release evidence gate`. Tags follow `vMAJOR.MINOR.PATCH`; never move a published tag. GitHub Releases publish reviewed source/artifacts only and do not prove production deployment. Keep private customer branches and internal CI configuration outside this repository.
