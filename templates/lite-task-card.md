# Lite task card

Use this card only after the [Lite delivery conditions](../references/lite-delivery.md)
are true. Keep it with the task note or final handoff; it does not need a full
execution ledger.

```text
goal: <one observable local outcome>
allowedEffects: <exact files/components that may change; external effects that remain forbidden>
verification: <one focused command or observable check and its expected result>
```

If the work crosses a repository, business-state, permission, restart,
deployment, release, or untestable boundary, preserve this card and upgrade
the task instead of stretching Lite past its safe limits.
