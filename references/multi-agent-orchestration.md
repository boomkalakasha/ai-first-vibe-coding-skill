# Multi-agent orchestration

## Roles, not model brands

- `Controller`: owns outcome, constraints, shared contracts, decisions, dependencies, and final release gate.
- `Researcher`: performs read-only fact finding and returns citations, unknowns, and proposed checks.
- `Implementer`: works inside an explicit, isolated write set and runs named cases.
- `Reviewer`: independently checks requirements, diff quality, security, and regressions.
- `Verifier`: reruns the result in the controller's target environment.

A capable low-cost model can implement a well-bounded task; a higher-reasoning model should own ambiguous architecture and final acceptance. Model names and reasoning settings are configuration, not proof of quality.

## Delegation contract

Every task includes:

- objective and non-goals;
- baseline and required context files;
- allowed and forbidden writes;
- stable interfaces and dependencies;
- cases and commands;
- evidence format;
- stop/escalation conditions.

Parallel writers require non-overlapping ownership, isolated branches/worktrees, and stable shared contracts. Otherwise run serially.

## Review gates

1. `SPEC_REVIEW`: did the result implement the requested behavior and only that behavior?
2. `QUALITY_REVIEW`: is it correct, secure, maintainable, and covered by meaningful tests?
3. `CONTROLLER_VERIFY`: does the integrated revision pass in the intended environment?

Reject completion claims without current evidence. Reopen the task with the exact failed case rather than vague feedback.

## Context re-anchor

Before and after each wave, read the baseline, plan, decision log, ledger, Git state, runtime state, and open P0/P1 list. If they disagree, update the recorded plan and explain the change before further writes.
