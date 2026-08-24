# Evidence and verification

## Claim ladder

Keep these claims separate:

1. `SOURCE_READY`: intended code/config exists and static checks pass.
2. `BUILD_PASS`: the exact source revision compiles or packages.
3. `TEST_PASS`: named automated cases pass for the exact revision.
4. `RUNTIME_PASS`: the intended process is running that revision and affected paths were observed.
5. `BUSINESS_PASS`: state, permissions, data semantics, retries, and user outcome close correctly.
6. `RELEASE_READY`: version, artifact, rollback, security, configuration, and operator checks are complete.
7. `DEPLOYED`: the named environment runs the named artifact.
8. `CUTOVER_ACCEPTED`: replacement traffic and rollback criteria were explicitly accepted.

A higher claim requires evidence for the lower claims it depends on. An HTTP 200 does not prove business correctness; a deployment record does not prove cutover acceptance.

## Evidence record

For every material check, capture:

- timestamp and environment;
- exact branch/commit/tag or artifact digest;
- command, URL, case, or query;
- expected and observed result;
- status and remaining ambiguity.

Use secrets-safe summaries. Never paste credentials, cookies, tokens, private keys, or customer data into evidence.

## Negative evidence

Failed, blocked, and not-run checks are first-class results. Preserve:

- the exact failure;
- whether it predates the change;
- the smallest reproducible path;
- what was tried;
- why further work requires a new decision, permission, dependency, or environment change.

Do not relabel an inaccessible environment as passed based on source inspection.

## UI and data chains

For UI work, connect the user action to network, response, state update, and rendered result. Check loading, empty, error, retry, permission, and responsive behavior where affected.

For data work, connect the source record to parsing/transformation, association rationale, persisted state, time semantics, and displayed result. Candidate, linked, approved, and formal states must remain distinct.
