# Legacy public-history boundary

Earlier published revisions contained organization-specific branch and
customer-delivery examples. Version 1.3.0 removes those details from the
current public runtime and gives them a private organization-policy owner.

The older commits and immutable release tags remain public provenance. They
contained workflow formats, not credentials, customer identities or runtime
secrets. Rewriting shared history would invalidate existing release identity,
so this project records the already-public low-sensitivity disclosure and
fails CI if a new history change leaves those markers in a commit tree.

As of 2026-09-01, the pre-migration public `main` and several stale remote
heads still point to trees containing that same accepted history, including
`feat/multi-model-orchestration-v1.2.0`, `feat/project-guidance-drift-checks`,
`docs/release-evidence-v1.2.1`, and multiple `fix/release-*` heads. The gate
inspects all fetched refs and reports every exposed remote head. Merging 1.3.0
will clean `main`; deleting or rebasing stale public heads is a separate,
destructive remote-maintenance decision and does not erase immutable tag or
commit history.

The recorded marker-change commits are
`582c0c8578fea0e94d6440cd16a7584b280f9b88` and
`69e14841b16ea610eb4890742948e62fed08db92`. The second is the tip of the
stale `feat/multi-model-orchestration-v1.2.0` branch and expanded the already
public policy examples. Any additional marker-changing commit fails the gate.

This is not permission to add private policy back to the public core. A new
clean lineage would require an explicit repository-ownership and migration
decision outside an ordinary feature release.
