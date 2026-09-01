# Lite delivery

`LITE` is the smallest AI-first delivery record. It prevents a small, local,
reversible change from inheriting the ceremony intended for a cross-repository
or production-bound program.

## Use it only when every condition is true

- One cohesive local change can be described without a new interface contract.
- The change does not write business data, alter permissions, touch customer or
  regulated content, or change a security boundary.
- It does not require a restart, deployment, release, Git write, external
  service action, or another repository to be changed in lockstep.
- A focused, repeatable verification command or observable check exists.

If any condition stops being true while working, keep the card and upgrade to
the appropriate `L0`, `L1`, `L2`, or `L3` path. Do not make the user repeat
their goal just because the task became larger.

## The whole record

Copy [the Lite task card](../templates/lite-task-card.md) and fill only these
three fields before editing:

1. `goal` — the observable result to preserve or change.
2. `allowedEffects` — the exact local write set and the external effects that
   remain forbidden.
3. `verification` — the focused command or user-visible check that can prove
   the result.

Then inspect the local baseline, make the smallest change, run the stated
verification, and report the evidence level. A `LITE` card is not permission
to commit, push, release, deploy, write data, or restart a service.

## Escalation examples

| Signal found during work | Upgrade because |
| --- | --- |
| A second repository or shared API contract changes | The result is no longer locally bounded. |
| The change can write business state or affects authorization | The risk requires a write-path or permission audit. |
| A restart, rollout, tag, or CI action is needed | Local source evidence no longer proves the user outcome. |
| No focused verification exists | The result needs a case/spec and stronger evidence plan. |
