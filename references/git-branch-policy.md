# Git delivery policy selection

This public reference does not define an organization's internal branch,
review, CI or customer-delivery rules. Select those rules from the closest
repository guidance or an organization-supplied policy (组织提供的策略).

## Precedence

1. System and safety constraints.
2. Explicit user authorization for the current action.
3. Closest project `AGENTS.md` and repository delivery documentation.
4. An organization-supplied policy selected by the project.
5. Machine-local preferences.
6. Public Skill defaults.

A higher layer may narrow a lower layer. Machine preference cannot weaken a
project security or release gate.

## Facts to record before writing

- delivery profile and its source document;
- base/default branch and exact baseline commit;
- current branch/worktree and dirty files;
- real Issue/PR/MR requirement and commit convention;
- required checks and reviewers;
- tag, artifact and deployment mechanisms;
- whether branch, commit, push, review request, merge, tag, release, deployment
  and cleanup are individually authorized.

Never infer an internal branch format from a hosting vendor. Never invent an
issue number. If the project has no delivery policy, use `project-defined`
and stop before an external write that would require one.

## Shared safe minimum

- Preserve user work and isolate long-running changes.
- Keep commits cohesive and messages truthful.
- Do not force-push a protected or shared branch.
- Treat local tests, default-branch merge, public release and deployment as
  distinct proof states.
- Scan public candidates for secrets, private endpoints, customer identifiers,
  proprietary assets and incompatible licenses.

For public GitHub repositories, read
[GitHub open-source release profile](github-open-source-release-profile.md).
Private downstream policy stays in its private owner and is not copied into
this package.
