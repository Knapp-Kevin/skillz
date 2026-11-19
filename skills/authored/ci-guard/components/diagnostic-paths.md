# CI Guard: targeted diagnostic scaffolding

**Load only when needed.** This component helps an agent distinguish
misleading CI outcomes, find a failing boundary, or select a defensible
optimization. It is not mandatory for a well-grounded direct execution.
Read the [repository-wide capability-adaptive standard](../../../../docs/capability-adaptive-skill-execution.md)
when the Skillz repository is available; the rules below remain independently
usable when the package is installed alone.

## Minimal evidence card

`repo@sha | requested outcome | failed or suspect claim | evidence/logs |
candidate mechanisms | smallest check that distinguishes them |
unique control at risk | action | verification | unknown`

Only populate observed fields; absence is `UNKNOWN`, not a guessed pass.
Do not spend a round making a card if evidence already supports an authorized
fix and its verification.

## Junction A: a green gate may not have actually compared data

**Input:** a benchmark comparison job reports SUCCESS.

1. Inspect the actual comparator program, baseline producer, artifact/cache
   materialization, and relevant log for the **same run and SHA**.
2. Branch: baseline absent, empty or unrelated? Mark `NO_BASELINE`, not
   `COMPARED_PASS`. If zero matching measured cases, mark `NO_MATCHES`.
3. Branch: comparison exists but normalizes away a global slowdown?
   Distinguish hardware-class shift from systemic product regression
   by a stable comparable runner, control workload or credible historical
   performance record; if impossible, mark the systemic claim UNPROVEN.
4. Branch: positive and negative controls demonstrably exercise the tested
   threshold? Keep useful detection and REPAIR only the misleading case.
5. Act directly within authorized scope when an exact patch and safe
   regression can be implemented. Otherwise provide the precise change,
   proof required and rollback trigger.

**Wrong shortcut:** delete all performance checks because they are expensive.
**Wrong shortcut:** a green exit means a valid statistical comparison happened.

**Worked counterexample:** baseline of [10, 10, 10] units, current [30, 30,
30], threshold 2x; a gate that divides every ratio by a global 3x shift
may report PASS. It is not evidence of unchanged shipping performance.

## Junction B: a job fails on one platform

1. Capture failure step, actual revision, installed/runner environment and
   whether the same assertion passes on other platforms.
2. Distinguish product defect, host constraint, runner-image regression,
   flaky ordering, dependent service, and broken fixture by selecting the
   smallest discriminating test. Repetition alone cannot prove "flaky".
3. Fix the demonstrated root cause and add a regression for that failure
   mode. Do not suppress native platform testing merely to clear a PR.
4. If the failing job is itself being repaired and protection blocks it,
   use only the owner's authorized narrow substitute qualification and
   restoration, not a silent check-name bypass.

**Worked counterexample:** a Windows-native cancellation test crashes
while Linux unit tests pass; Linux PASS does not qualify installed Windows
memory safety. Preserve the platform gate and isolate the native repro.

## Junction C: optimize cost without losing protection

1. Confirm the true critical path and measured job-minutes separately.
2. Identify the job's unique failure detection and whether the proposed
   new gate runs **before the irreversible consequence** (merge/release).
3. Compare representative patch classes and include a seeded relevant
   failure. Inspect conditional skips and required-status reporting.
4. If detection and revision binding survive, apply the smallest authorized
   change and compare results; otherwise KEEP or VERIFY before relocation.

**Worked counterexample:** a ten-minute benchmark and an eleven-minute
CodeQL job run in parallel; removing the benchmark might save runner
minutes without materially reducing total PR latency.

## Adaptive use

- If the root cause is already proved, skip the card and fix/verify it.
- If evidence conflicts, follow the smallest branch that resolves the
  conflict, not the entire handbook.
- If a host supports a more reliable equivalent analysis or safe
  deterministic tool, use it.
- If no branch/protection access exists, document that narrow unknown;
  do not infer the ruleset is absent.
- Escalate only a real external permission or owner decision; continue safe
  implementation and diagnosis otherwise.
