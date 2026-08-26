# Public evals

`evals.json` contains behavior scenarios. `trigger-evals.json` contains prompts that should and should not activate the Skill. They are public, generic, and contain no customer or internal environment data.

`python scripts/validate.py` performs deterministic structure and assertion checks. Model responses still require repeated runs and human or rubric-based grading; deterministic validation is not a model-quality benchmark.

Run `python scripts/run_evals.py` to check that the documented-only rubric covers every behavior scenario. It does not call a coding-agent host or invent a host result; capture a separate transcript, host/version, date, prompt and score whenever a real host evaluation is authorized.

## GitHub profile RED/GREEN record

The pre-release internal Skill did not define a named GitHub OSS profile. In a read-only baseline run on 2026-08-24, the evaluator proposed GitHub rules but correctly classified them as inference and explicitly reported that the profile was absent. The current Skill adds an opt-in profile with fork-safe CI, SemVer, release artifacts, private downstream separation, and repository-setting verification.

This record is `MANUAL / DOCUMENTED_ONLY`; raw private-session transcripts and machine paths are intentionally not published.

## Dynamic concurrency RED/GREEN/REFACTOR record

The [2026-08-26 host run](runs/2026-08-26-dynamic-multi-window-concurrency/README.md) records a pressure scenario for multiple active Codex windows, unknown cross-window child load, staged fan-out, reserve slots, and the boundary between conservative observation and a real global scheduler.
