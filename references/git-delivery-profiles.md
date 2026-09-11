# Git delivery profiles

## Select before writing

Determine the profile from, in order:

1. closest repository instructions;
2. explicit user release target;
3. remote host and existing CI/release files;
4. otherwise `project-defined` and pause before external writes.

Record `deliveryProfile`, base branch, remote, baseline commit, dirty state, issue/PR requirement, commit convention, checks, release mechanism, and protected targets.

An explicit user or organization commit convention is binding for the task. Do
not silently replace it with the public default; derive the title and body from
the actual diff, and split changes that do not share one goal and rollback
boundary.

## Shared rules

- Preserve uncommitted user work; use an isolated branch/worktree for risky or long-running changes.
- Never invent issue numbers or copy sample commit text.
- Keep commits cohesive and messages truthful.
- When one commit covers several related changes, enumerate each change and its
  verification in the body; split unrelated goals.
- Branch, commit, push, PR/MR, tag, release, deploy, and cleanup are separately observable actions.
- Do not force-push a protected or shared branch.
- A feature branch passing locally is not the same as the default branch being released.
- Before publishing, scan the current tree and repository history for secrets, private URLs, customer identifiers, proprietary assets, generated binaries, and incompatible licenses.

## Organization-supplied profile

Use only the exact rules supplied by the organization or repository. An
organization-supplied policy (组织提供的策略) owns any private branch, reviewer,
CI, customer-delivery and deployment details. They must not be inferred from a
hosting vendor or copied into this public repository.

## GitHub OSS profile

Read [GitHub open-source release profile](github-open-source-release-profile.md). It is opt-in and does not replace internal delivery rules.
