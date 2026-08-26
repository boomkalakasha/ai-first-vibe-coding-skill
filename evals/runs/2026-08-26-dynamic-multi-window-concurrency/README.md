# Dynamic multi-window concurrency host run

- Date: 2026-08-26
- Evidence: `HOST_OBSERVED`
- Scenario: four active root-task windows, one controller in the current tree, tree capacity four including the controller, eight independent low-cost implementation packages, and no visibility into other windows' child-agent counts.
- Scope: one low-cost-model evaluator on the current host; no external side effects and no nested agents.

## RED — without the Skill

The evaluator chose three children immediately because the current tree had three nominally free child slots. It also admitted that other windows' child-agent counts were not observable. This demonstrated the missing rule: local free slots were treated as dispatchable even though global load was unknown.

## GREEN — first revision

The evaluator chose one initial child and treated cross-window load as `UNKNOWN`, but recorded local running agents as zero even though the controller occupied a slot, then allowed later growth to three children. The first revision fixed global uncertainty but left occupancy and reserve semantics ambiguous.

## REFACTOR — final revision

The evaluator produced the following consistent decision:

```text
activeRootTasks=4
localRunningAgentsIncludingController=1
localRunningChildren=0
treeCapacity=4
reserveSlots=1
crossWindowChildrenVisibility=UNKNOWN
localFreeAfterReserve=2
targetActiveChildren=1
spawnNow=1
```

It limited the current unknown-global-load state to one child, limited later local expansion to two active children because one extra slot stays reserved, and required a platform scheduler or atomic leased semaphore for a hard machine-wide cap.

## Boundary

This run proves one host/model scenario changed behavior. It does not prove that every host exposes app-wide task status, that a global scheduler exists, or that a cross-window semaphore has been implemented.
