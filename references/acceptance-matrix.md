# Real-task acceptance matrix — recovered contract

2026-09-10 reconstruction from historical PRD/BDD and D-019. This JSON format and CLI are reconstructed, not byte-for-byte recovered originals. Generic tasks use a nonempty descriptive task_type; CRUD tasks must identify as mvp_crud. The caller remains responsible for truthful classification.

Run `python scripts/check_acceptance_matrix.py templates/acceptance-matrix.json`, or read one JSON object from stdin. Exit 0 / ACCEPTANCE_MATRIX_PASS, 1 / ACCEPTANCE_MATRIX_BLOCKED or 2 / INVALID_INPUT. The checker checks structure and declared evidence; it does not open URLs, inspect evidence files or perform the actual user journey.

Input has `task_type`, `layers`, `journey` and `cases`. Four layer names and record format follow [completion-gate.md](completion-gate.md). A passing record needs nonempty evidence references of known kinds; N/A needs a nonempty reason. Default status is NOT_RUN, never prefilled PASS.

For `mvp_crud`, journey must include login, create, list, edit and error. Every step must PASS and include UI_OBSERVED proof. HTTP 200 alone or source-only declarations cannot pass. Cases success and error must PASS with runtime/UI/business/release observation. Empty, retry, duplicate and permission must remain visible with either passing evidence or reasoned NOT_APPLICABLE. They may not silently disappear. Extra declared steps and cases are checked too.

Other tasks need at least one actually measured passing journey step, a passing success case and a visible error case (reasoned N/A allowed for error). All-N/A journeys cannot pass. All four evidence layers remain required, with matching observations for applicable layers and reasoned N/A for inapplicable layers. A local-code or documentation task with no workflow can instead use the explicit bounded completion-manifest opt-out described in [completion-gate.md](completion-gate.md), without fabricating product acceptance. Product-specific acceptance and real observations remain separate work.
