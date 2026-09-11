# Five-minute model health — recovered contract

2026-09-10 restoration reconstruction, not recovered original source. Policy comes from the preserved September 3-4 PRD, BDD and decisions D-017–D-019. The JSON names, default minimum sample count (5), epoch timestamp format and CLI below are new compatibility decisions; historical exact schemas were not found.

Run `python scripts/model_health.py templates/model-health.json`, or pipe one JSON object to stdin. Exit 0 means ROUTE_HEALTHY, 1 means degraded/insufficient/not run, 2 means invalid input. Output is one JSON object. No host configuration changes, model calls, continuous collection or scheduler are performed.

Input: `now` (Unix seconds, required), `minimum_samples` (positive integer, default 5), `events` array and optional `fallback` (already configured route name). Every event has only `timestamp` (Unix seconds), `ok` (boolean), and `latency_ms` (finite nonnegative number). Prompt, credentials, tool arguments and other event fields are rejected. Supply a single route's samples per invocation; route partitioning belongs to the caller.

The inclusive window is `[now - 300, now]`; future and older samples are excluded. No samples returns NOT_RUN; fewer than the minimum returns NOT_ENOUGH_SAMPLES. Neither changes a route. P95 uses nearest rank `ceil(n * 0.95)`. Error rate strictly greater than 0.20 or P95 strictly greater than 90000 ms returns ROUTE_DEGRADED and QUALITY_DEGRADED. If fallback is supplied, action is USE_CONFIGURED_FALLBACK; otherwise FALLBACK_NOT_CONFIGURED. This is a recommendation only, never an actual route switch. Healthy samples do not prove quality equivalence or sustained SLA.

The default template is deliberately empty and exits 1. Example sample: `{"timestamp": 1788998400, "ok": true, "latency_ms": 1000}`. Continuous event ingestion and live scheduler remain separately NOT_RUN/HYBRID until validated against a real host adapter.
