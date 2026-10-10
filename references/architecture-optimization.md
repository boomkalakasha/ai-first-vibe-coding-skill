# Architecture optimization and engineering harness

Read this reference when changing architecture, project guidance, documentation
ownership, or the environment in which coding agents work. Keep domain rules,
commands and runtime values in their project owners. A small local correction
still uses [Lite delivery](lite-delivery.md).

## What the harness owns

An engineering harness is the observable environment around coding work:
scoped instructions, available execution tools, reproducible checks, current
task records and evidence, and boundaries on effects. A scaffold can provide
these entrypoints alongside generated code. Identify what is executable, what
is only documented, and what the host has actually loaded or observed.

Use [context and intent](workspace-records.md) for the necessary baseline,
trusted reuse, re-anchoring and unresolved goals. Use [capability routing](skill-routing.md)
for optional tools and [completion gates](completion-gate.md) for evidence.
Neither a prompt collection nor a domain agent runtime establishes that this
engineering environment exists or works. Do not claim a control loop, monitor,
sandbox or automatic enforcement that has not been implemented and observed.

## One owner, references at every other layer

Before adding documents, reuse the existing overview, map and change record.
Choose an owner for each fact and let the other layers link to it:

| Layer | Owns | References |
| --- | --- | --- |
| README | Human orientation and supported entrypoints | Current guides, maps and commands |
| AGENTS or equivalent | Scoped operating conventions | Contract owners and verification entrypoints |
| System/module map | Responsibilities, dependency direction and navigation | Specs, decisions, code symbols and cases |
| Spec | Expected behavior and invariants | Applicable changes and acceptance cases |
| Design/ADR | Implementation design or lasting choices and reasons | Contracts and relevant implementation |
| Change/task record | Approved scope, steps, progress and unresolved decisions | Canonical facts and current evidence |
| Code/tests/evidence | Implementation, executable checks and observed results | Requirement clauses and exact versions |

A useful map reference names the repository, relative path, clause or symbol,
and applicable version when the conclusion depends on one. Summaries are
navigation, not substitutes for relevant contract bodies. Preserve expected
behavior separately from implementation gaps; do not rewrite a spec to bless a
defect. When a link, version or owner is uncertain, record the gap and continue
only work that does not depend on it.

Assess documentation coverage independently of
[the decision to add a module guide](project-ai-guidance.md). A necessary module
must have reachable specification, design/decision, code, verification and
change/source entrypoints. Local explanation plus valid references is enough;
an existing full spec may make a new spec unnecessary. A contract module can
need its own coverage without distinct AGENTS; an ordinary utilities folder
usually needs navigation to its shared owners rather than a copied suite.
Update only references affected by a changed structure, command or contract.

## Thin, path-selected host entrypoints

Keep shared operating rules in one scoped guide. Host-specific entrypoints may
import or link that guide according to the host's supported mechanism. Select
guidance by the target path; multiple visible guides do not all govern every
repository. A Markdown link does not load its body. A Meta entrypoint does not
prove a child repository's guide has been read, and an isolated clone must not
assume its parent exists. Read required bodies explicitly when discovery has
not supplied them. Disk updates do not replace an old session's context.

Record host loading as documented until a current host trial observes it; do
not turn a successful file/link check into compatibility evidence.

## Golden path, incremental enablement, complete approved scope

1. Prove one actual entrypoint-to-result path in a bounded environment, with
   the relevant contracts and failure guards. Reuse the
   [first-value guide](vibe-coding.md); the bounded environment itself needs
   authorization and does not permit resetting existing services or data.
2. Enable additional entrypoints incrementally through the same policy owners.
   Check relevant authorization, isolation, idempotency and failure recovery.
   Keep unsupported unsafe actions rejected at the enforced boundary rather
   than relying on a hidden button.
3. Integrate and verify the entire currently approved scope. If that scope is
   P0 plus P1, one slice or P0 alone is an intermediate result. Record remaining
   entries and evidence gaps; do not stop at a milestone and call it complete.

Scale documentation and checks to actual impact. Reuse durable records for
nontrivial work; keep local fixes focused. Do not repeat passed checks without
new changes, failures or uncertainty. Keep iteration count, task complexity
and action risk distinct; none grants new effects or proves completion.

At corrections, repeated failures and natural closure, use
[the learning loop](skill-promotion-and-feedback.md). Route reusable methods to
their authorized owner, and keep private examples and process evidence out of
public packages. Select a readable report through capability routing when its
size or traceability warrants it; the report remains a view over canonical
facts, not another active spec.
