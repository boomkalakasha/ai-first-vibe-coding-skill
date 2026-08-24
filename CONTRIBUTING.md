# Contributing

Thank you for improving the workflow.

1. Search existing issues and open one for non-trivial behavior changes.
2. Fork the repository and create a short branch from current `main`.
3. Add or update a discriminating eval before changing the instruction.
4. Keep examples generic and remove internal, customer, machine, or credential data.
5. Run `python scripts/validate.py` and `pwsh -File scripts/package.ps1`.
6. Open a PR with scope, rationale, compatibility impact, evidence, and release-note impact.

Use truthful Conventional Commits such as `fix(evidence): distinguish runtime and build claims`. Do not invent issue identifiers or copy an example message unchanged.

By submitting a contribution, you confirm that you have the right to license it under Apache-2.0 and that it contains no confidential or personal data.
