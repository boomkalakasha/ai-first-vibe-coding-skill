# Tool adapters

Map available tools to the protocol without weakening evidence standards.

| Need | Preferred capability | Fallback | Claim limit |
|---|---|---|---|
| code/file discovery | fast indexed search | repository-native search | source only |
| isolated implementation | native workspace/worktree | Git worktree | no isolation claim without verification |
| UI interaction | signed-in browser automation | HTTP/DOM/source inspection | no `UI_OBSERVED` without real interaction |
| database facts | read-only database client | application API/logs | no database-state claim |
| runtime verification | health, logs, process/container evidence | build/test | `STATIC_PASS_PENDING_RUNTIME` at most |
| external release | provider API/CLI/browser | documented manual checklist | `DOCUMENTED_ONLY` until observed |

Prefer repository scripts over retyping long commands. Keep secrets out of command output and evidence. If a tool fails repeatedly, capture the failure, use the safest in-scope fallback, and downgrade the result.
