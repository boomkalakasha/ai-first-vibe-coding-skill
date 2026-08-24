# Compatibility

Evidence levels are intentionally conservative.

| Host | Installation route | Status | Evidence |
|---|---|---|---|
| OpenAI Codex | repository under the configured skills directory | STRUCTURE_VERIFIED | official local Skill validator and packager passed; arbitrary task behavior is not automatically graded |
| Claude Code | host-specific skill/instruction directory | DOCUMENTED_ONLY | Markdown is portable; host behavior not run in this release |
| Cursor | project/user rules integration | DOCUMENTED_ONLY | adapter not included |
| Cline | custom instructions/workflow integration | DOCUMENTED_ONLY | adapter not included |
| GitHub Copilot | repository instructions/custom agent integration | DOCUMENTED_ONLY | adapter not included |

## Requirements

- Ability to read `SKILL.md` and referenced Markdown files.
- File search and edit support for implementation tasks.
- Shell access for deterministic validation.
- Browser, database, logs, CI, deployment, and subagents are optional; unavailable observations must remain `NOT_RUN` or `BLOCKED`.

Compatibility means the content can be integrated, not that every host has identical skill discovery, permissions, or tool behavior.
