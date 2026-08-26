---
name: ai-first-vibe-coding
description: Use when working in an existing repository on implementation, refactoring, debugging, optimization, architecture review, data or runtime flows, multi-module changes, multi-agent delivery, or iterative P0/P1 closure. Also use for 中文软件研发中的方案、实现、联调、复盘、验收与发版治理. Skip for simple translation, one-line commands, or purely informational questions.
license: Apache-2.0
metadata:
  version: "1.1.2"
  repository: https://github.com/boomkalakasha/ai-first-vibe-coding-skill
---

# AI-first Vibe Coding

Turn a user's goal into a verifiable software outcome. Preserve the speed and creativity of vibe coding while adding evidence, operational boundaries, traceability, and honest release gates.

Tool boundary: file search, editing, and shell access are required. Browser, database, logs, CI, deployment, and multi-agent capabilities are optional adapters; report unavailable evidence explicitly.

## Start here

1. Read the closest repository instructions (`AGENTS.md`, README, contribution and release rules).
2. Record the current branch, remote, base commit, dirty files, running services, and authorized side effects.
3. Classify the task and choose the smallest workflow that covers its risk.
4. Build a fact chain before changing behavior.
5. Implement within the authorized write set.
6. Verify with the strongest available evidence and state what was not verified.

## Non-negotiable principles

- Lead with the user's outcome, not a preferred technology.
- Preserve dirty worktrees and user data. Never reset, overwrite, delete, deploy, or write to production by implication.
- Treat branch creation, commit, push, PR/MR, tag, release, deployment, database writes, restarts, and cleanup as separate side effects.
- Do not invent metrics, issue numbers, runtime success, coverage, release state, or business completion.
- Fix the smallest proven cause. Do not broaden a change merely to make the design look cleaner.
- A source diff, green build, HTTP 200, visible button, and business closure are different proof states.
- When runtime or external evidence is unavailable, downgrade the claim instead of filling the gap with confidence.
- For any formal business-state change, inventory every write path and route all callers through one policy source.

## Task modes

Choose one and record its boundaries:

- `READ_ONLY_REVIEW`: inspect and report; no repository or external writes.
- `PLAN_ONLY`: produce architecture, specification, cases, risks, and plan; no implementation.
- `IMPLEMENT_AND_VERIFY`: modify only the authorized write set and run proportionate checks.
- `FULL_ITERATIVE_DELIVERY`: execute a multi-wave plan until the defined gate is met or a real blocker remains.
- `SKILL_REVIEW`: evaluate a skill, its references, templates, and evals without silently modifying target projects.

Record when relevant: `allowedWrites`, `allowedRestarts`, `allowedDatabaseWrites`, `allowedExternalSideEffects`, `requestedIterations`, and `deliveryProfile`.

## Risk levels

- `L0`: one low-risk file, no runtime or business-state impact. Use inspect → edit → focused check.
- `L1`: one component, page, endpoint, or module. Use baseline → lightweight contract → implementation → affected-path verification.
- `L2`: cross-module behavior, data state, permissions, integration, or user workflow. Read [the end-to-end workflow](references/end-to-end-workflow.md).
- `L3`: L2 plus broad audit, multiple repositories, delegated implementation, repeated iterations, or a P0/P1 closure goal. Use an execution ledger and independent review.

Do not create ceremony for L0/L1. Do not compress L2/L3 into an unverified suggestion list.

## Fact chain before change

For affected behavior, trace the smallest complete chain:

```text
user intent
→ UI or public interface
→ request/event contract
→ service/policy logic
→ persistence or external dependency
→ observable runtime result
```

Classify statements as `FACT`, `INFERENCE`, or `NOT_VERIFIED`. If history or documentation conflicts with current code/runtime, current evidence wins and the plan must be updated.

## Design and planning

For L2/L3, produce and maintain:

- system/application map and in-scope boundaries;
- detailed behavioral contract and non-goals;
- user stories and positive/negative/error/retry cases;
- business and operational review;
- P0/P1/P2 implementation plan;
- traceability from requirement to implementation and evidence.

Use [task baseline](templates/task-baseline.md), [decision log](templates/decision-log.md), [traceability matrix](templates/traceability-matrix.md), and, for L3, [execution ledger](templates/execution-ledger.md).

When the user asks for a plan only, stop at the plan. When they explicitly ask to plan and implement, document the design and continue without asking ceremonial questions.

## Implementation protocol

1. Reuse existing contracts, components, scripts, and configuration sources.
2. Add or expose the failing case before changing behavior when practical.
3. Fix data/API/state semantics before presentation details.
4. Keep one source of truth for shared state, menus, policy, and public contracts.
5. Measure before performance optimization: requests, latency, payload, queries, cache, and concurrency.
6. For migrations or backfills, record scope, identifiers, checkpoints, idempotency, audit, and rollback before writing data.
7. Update the traceability matrix as the implementation changes; do not wait until handoff.

For formal state changes, inventory user actions, background jobs, callbacks, imports, synchronization, retries, scheduled jobs, and administrative paths. Test both allowed and blocked cases for each entry point.

## Verification and claims

Read [evidence and verification](references/evidence-and-verification.md). Choose checks based on risk:

- static: syntax, types, encoding/BOM, whitespace, secrets, licenses;
- tests: unit, contract, integration, migration, negative and retry cases;
- runtime: startup, health, logs, endpoint, UI, console, network;
- data: source record, transformation, persistence, status and time semantics;
- operational: configuration, packaging, rollback, observability and recovery;
- release: exact commit, checks, artifact, checksum/provenance and target state.

Report one of:

- `RUNTIME_PASS`
- `STATIC_PASS_PENDING_RUNTIME`
- `PARTIAL_PASS`
- `OLD_RUNTIME`
- `BLOCKED`
- `NOT_RUN`
- `FAIL`

For UI claims also identify `UI_OBSERVED`, `HTTP_OBSERVED`, `SOURCE_INFERRED`, `DOCUMENTED_ONLY`, or `NOT_EVALUATED`.

## Multi-agent and iterative work

Use multiple agents only when work packages are independent enough to reduce latency or provide a genuinely separate review. Read [multi-agent orchestration](references/multi-agent-orchestration.md) for L3 work.

- The controller owns scope, shared contracts, permissions, decisions, and final verification.
- Implementers receive explicit write sets, dependencies, cases, and stop conditions.
- Parallel writers require isolated workspaces and non-overlapping ownership.
- Before spawning, take a live capacity snapshot: current-tree running agents (including the controller/root), running children, tree limit, app-visible active root tasks, independent `READY` work, review backlog, and resource pressure. An unobservable cross-window child count is `UNKNOWN`, never zero.
- Use staged fan-out: start with one child, keep controller/reviewer capacity in reserve, and grow by at most one only after a healthy wave. With other active windows, unknown global child load, review backlog, failures, or resource pressure, keep at most one child or run serially. A hard cross-window cap requires a platform scheduler or atomic leased semaphore.
- An agent's `DONE` is candidate evidence, never automatic acceptance.
- At each wave boundary, re-anchor on the baseline, plan, decision log, ledger, Git state, and runtime facts.
- If the goal is zero P0/P1, do not stop merely because the requested number of rounds or a token budget is exhausted.

## Git and delivery profiles

Before branch, commit, push, PR/MR, tag, release, or deployment work, read [Git delivery profiles](references/git-delivery-profiles.md).

Select a profile from repository rules or the user's explicit target:

- `project-defined`: repository policy is authoritative.
- `github-open-source`: use [the GitHub OSS release profile](references/github-open-source-release-profile.md).
- `internal-gitlab`: follow the organization's GitLab/MR/CI/customer-branch rules supplied by the project.

Never silently translate a customer deployment into a public GitHub Release, or a GitHub Release into production readiness. If profile selection is ambiguous and would cause an external write, pause before that write.

## Open-source governance handoff

For a broad public-repository productization request—provenance, privacy, license decision state, optional branding, community files, GitHub settings, release assets, and public-host evidence—hand off to `icarus-open-source-governance` when that companion Skill is available in the host. This is a routing name, not a claimed host installation. If it is unavailable, retain the conservative `github-open-source` profile and stop at every unresolved ownership, privacy, legal, or remote-evidence gate.

Commit messages use the project's convention. If none exists, use truthful Conventional Commits:

```text
<type>(<scope>): <summary>

- <why or observable change>
- <verification or compatibility detail>
```

Do not copy example text or invent an issue identifier.

## Final review

Review from five angles:

1. user/business outcome;
2. data and content semantics;
3. correctness, security, performance, and maintainability;
4. interaction, accessibility, and failure recovery;
5. operations, governance, rollback, and release evidence.

For L2/L3, deliver:

- outcome and remaining boundary;
- artifacts and traceability;
- side effects performed and explicitly not performed;
- commands, URLs, logs, data, or screenshots used as evidence;
- evidence level and observation source;
- P0/P1/P2 findings and the next release gate.

Read [tool adapters](references/tool-adapters.md) only when mapping this protocol to a specific environment. Tool availability changes the evidence you can collect, not the truth standard.
