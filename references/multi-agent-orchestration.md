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

## Live concurrency budget across windows

Concurrency is a feedback-control decision, not a fixed team size. Capture a capacity snapshot before each dispatch wave and again when the wave finishes.

| Signal | What it proves | Boundary |
|---|---|---|
| Platform global scheduler or quota | Hard global grant/free slots | Preferred source when available |
| App-wide active root-task list | Other conversations are working | Does not reveal their child-agent count unless explicitly exposed |
| Current-tree agent list and tree limit | Local occupancy and local free slots | Cannot prove machine-wide availability |
| Independent `READY` work packages | Useful parallelism | Queued or dependent work is not dispatchable |
| Review backlog, failures, timeouts, CPU/memory/IO pressure | Whether the controller can absorb more results | Advisory signals; pressure reduces concurrency |

Record `activeRootTasks`, `localRunningAgentsIncludingController`, `localRunningChildren`, `treeCapacity`, `reserveSlots`, `crossWindowChildrenVisibility`, `readyIndependentWork`, `reviewBacklog`, `resourcePressure`, `targetActiveChildren`, `spawnNow`, timestamp, and the reason for changing the target. `localRunningAgentsIncludingController` is at least 1 while the controller is running; `targetActiveChildren` is the desired total, while `spawnNow` is only the additional children to create.

When tree capacity is known, keep one additional local slot unused for reviewer/urgent work whenever the platform permits:

`localFreeAfterReserve = max(0, treeCapacity - localRunningAgentsIncludingController - reserveSlots)`

`spawnNow` must not exceed `localFreeAfterReserve`, and `targetActiveChildren` must not exceed `localRunningChildren + localFreeAfterReserve`.

Use the following conservative policy when the platform has no global grant:

1. Treat missing cross-window child data as `UNKNOWN`, not zero.
2. Count the controller/root in local occupancy and reserve at least one additional slot for reviewer/urgent work when capacity permits; do not fill every locally available slot with implementers.
3. Start one child. Add at most one after a healthy wave only when independent `READY` work remains, review backlog is controlled, no failures/timeouts/conflicts appeared, resource pressure is normal, and app-wide active work did not increase.
4. Keep at most one child, or serialize, when another window is active and global child load is unknown. Reduce immediately on new active tasks, `needs_attention`, repeated failure, review backlog, contract instability, overlapping writes, resource pressure, or user steering.
5. Re-evaluate at wave boundaries and immediately before a spawn. Do not run a tight polling loop or keep slots busy merely because they exist.

For a hard machine-wide limit, use a platform-native global scheduler. If the platform has none, use an atomic shared lease/semaphore with owner identity, capacity, heartbeat, TTL, release, and orphan recovery. A plain unlocked JSON/text counter is not a safe global semaphore.

## Review gates

1. `SPEC_REVIEW`: did the result implement the requested behavior and only that behavior?
2. `QUALITY_REVIEW`: is it correct, secure, maintainable, and covered by meaningful tests?
3. `CONTROLLER_VERIFY`: does the integrated revision pass in the intended environment?

Reject completion claims without current evidence. Reopen the task with the exact failed case rather than vague feedback.

## Context re-anchor

Before and after each wave, read the baseline, plan, decision log, ledger, Git state, runtime state, and open P0/P1 list. If they disagree, update the recorded plan and explain the change before further writes.
