# End-to-end workflow

## 1. Baseline

Record objective, non-goals, repositories, closest instructions, Git state, dirty files, running processes, external systems, authorized writes, and known unknowns. Build an application map that names owners and boundaries instead of only directories.

## 2. Contract

Write the behavior in observable terms:

- actor and starting state;
- action or event;
- input validation and permissions;
- expected state transition and output;
- idempotency, concurrency, retry, timeout, and rollback;
- logging, metrics, audit, and privacy;
- compatibility and migration.

## 3. Cases and traceability

Create positive, negative, empty, duplicate, retry, failure, permission, concurrency, and recovery cases as applicable. Link each case to the contract, implementation location, and evidence.

## 4. Business review

Before implementing, challenge object identity, state names, time fields, aggregation semantics, automation boundaries, reversibility, and the user's next step. Mark disagreements and decisions rather than hiding them in code.

## 5. Prioritized plan

- `P0`: data loss, security, incorrect formal state, unavailable critical path, irreversible migration, or release blocker.
- `P1`: wrong common-path behavior, incomplete replacement scope, broken recovery, major observability or usability gap.
- `P2`: maintainability, optimization, polish, or non-blocking follow-up.

Each task must name its write set, prerequisites, cases, verification, rollback, and stop condition.

## 6. Implement in small vertical slices

Prefer a slice that can be verified from public interface to persistence over broad layer-by-layer edits. Keep shared contracts stable before parallel work. Stop and revise the plan when live facts invalidate it.

## 7. Verify and review

Run the smallest complete regression set plus every previously failing case. Review user value, semantics, technical quality, interaction, operations, and release safety. Update status using evidence rather than percentages.

## 8. Iterate

At each new wave:

1. re-read objective, non-goals, decisions, ledger, Git and runtime state;
2. carry forward every open P0/P1 and failed case;
3. add newly discovered work with evidence and impact;
4. implement only the agreed next slice;
5. rerun old failures and new cases;
6. record why the release gate moved or remained closed.

Completion means the outcome and release gate are satisfied, not merely that a planned number of iterations ran.
