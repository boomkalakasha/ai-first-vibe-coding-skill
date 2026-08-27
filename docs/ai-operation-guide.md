# AI Operation Guide

[中文说明](ai-operation-guide.zh-CN.md) · [AI-first Vibe Coding Skill](../README.md)

> A calm, evidence-led way to let an AI coding assistant move quickly without
> quietly expanding the task.

> **Loading note:** This is optional companion documentation. It does not
> replace or alter `SKILL.md`, is not a second Skill, and is not auto-loaded by
> an agent host. The host entry remains the repository's `SKILL.md`; read this
> guide when you want the operating rationale and practical checklists.

This is a provider-neutral operating guide distilled from a real engineering
workflow and rewritten for public collaboration. It is deliberately generic:
there are no local paths, credentials, internal addresses, customer records or
host-specific defaults here. Adapt the examples to your repository and keep
project-level rules above this guide.

## Start here

Use the smallest path that matches the request:

| Request shape | Start with | Do not assume |
| --- | --- | --- |
| Explain, compare or investigate | Read-only inspection and a factual report | That an explanation authorizes a code or data change |
| Implement or refactor locally | A baseline, bounded write set and tests | That a local green build proves runtime or business readiness |
| Commit, publish, deploy or change data | An explicit side-effect boundary and rollback path | That a previous approval covers a new external target |

## Scope before action

1. State the outcome in one sentence and name the repository, branch and
   environment that are in scope.
2. Check the current tree, recent history and existing user changes before
   editing. Preserve dirty worktrees; never use reset or cleanup as a shortcut.
3. Separate local edits from external effects. A commit, push, pull request,
   tag, release, deployment, database write, restart or cleanup is its own
   operation and should be performed only when the request authorizes it.
4. If facts are missing, keep the item `PENDING` instead of silently filling
   the gap with a plausible assumption.

## Evidence before claims

Keep these evidence streams distinct:

- **Source:** files, diff, branch and reachable history;
- **Build/test:** compiler, unit/integration tests and static checks;
- **Runtime:** process, container, endpoint, logs and UI behavior;
- **Business/data:** real state transitions, records and downstream effects;
- **Release/deployment/cutover:** reviewed commit, artifact, environment and
  traffic-switch evidence.

A passing test, build, HTTP 200 or running container proves only the narrow
claim it actually exercises. Report `RUNNING`, `PENDING`, `RECOVERING` and
`COMPLETED` separately, and say exactly what remains unobserved. If the host,
browser, service or data source is unavailable, downgrade the evidence level
instead of converting documentation into runtime proof.

## A safe implementation loop

1. Inspect and map the user path, dependencies and failure boundaries.
2. Write a compact baseline: goal, non-goals, acceptance cases and smallest
   safe write set.
3. Implement the smallest change that can satisfy one case.
4. Run the verification command that proves that case; add a regression test
   when the original behavior could regress.
5. Review the diff and generated artifacts for unintended files, secrets,
   path changes and permission expansion.
6. Record changed, verified, unknown and next-step items in one ledger.

## Parallel work without overload

Multiple Agents are useful only when the work is genuinely independent. A
practical starting rule is one worker; add another only when the write sets do
not overlap and there is spare capacity.

At each wave boundary, recalculate:

```text
effective concurrency = min(
  independent tasks,
  safe workspace slots,
  available agents across other conversations,
  model/tool/rate budget
)
```

Use short waves, one owner per write set and an independent reviewer for
high-risk changes. Pause or merge a wave when conflicts, capacity pressure or
uncertain requirements appear. A delegated `DONE` is a handoff signal, not an
acceptance result.

## Tool choice and graceful fallback

- Prefer repository-native scripts, tests and documented commands.
- Use a browser for visible UI and user-flow evidence; use CLI/API/database
  tools for machine-readable facts when authorized.
- Detect available capabilities at runtime; do not hard-code one provider,
  plugin or IDE as a universal dependency.
- If a tool cannot attach or a host is unavailable, report the downgrade and
  continue with the strongest safe evidence available.

## Privacy and public collaboration

Before sharing a guide, issue or patch:

- replace user-specific paths with `<repo>` and credentials with
  `[REDACTED_SECRET]`;
- remove internal hostnames, private IPs, customer identifiers, real data and
  organization-only rules;
- scan both the current tree and reachable history when provenance matters;
- keep private runbooks and public operating principles in separate files.

This guide is a starting point, not a universal law. Suggestions, examples and
counterexamples are welcome through issues, discussions or pull requests. A
project maintainer still decides which rules fit the repository, risk profile
and contributors.

## Copyable handoff checklist

```text
[ ] Outcome, repository, branch and environment are explicit
[ ] User changes and current history were inspected
[ ] Write set, non-goals and side effects are bounded
[ ] Independent work has a named owner and a capacity check
[ ] Verification proves the stated claim, not a wider one
[ ] Unknowns and downgraded evidence are recorded
[ ] Secrets, private paths, internal addresses and real data are absent
[ ] Commit/push/release/deploy/data-write actions are separately authorized
```
