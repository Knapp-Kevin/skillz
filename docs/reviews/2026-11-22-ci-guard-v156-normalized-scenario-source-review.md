# CI Guard v1.5.6: bounded whole-workflow scenario simulator

**Date:** 2026-11-22. **Scope:** first concrete #861 implementation
slice. **Source prior to change:** CI Guard v1.5.5 30-file package tree
`7c06e7057310e9fc4819e2d892d4bf4390cf40f8`. The
single public entry remains `skills/authored/ci-guard/SKILL.md`.
No real consumer organization, project, PR, run or account is cited.

## Implemented, not just proposed

- New [scenario-simulation component]
  (../../skills/authored/ci-guard/components/scenario-simulation.md),
  [read-only standard-library scenario checker]
  (../../skills/authored/ci-guard/scripts/ci_scenario.py),
  [fully fictional 8-workflow/2-graph/10-scenario fixture]
  (../../skills/authored/ci-guard/examples/ci-scenario-fixture.json),
  and [executable tests]
  (../../skills/authored/ci-guard/examples/test_ci_scenario.py).
- The checker takes a bounded, explicitly source-derived
  NORMALIZED_SUBSET_V1. **It is not a GitHub Actions parser/interpreter**.
  It rejects arbitrary expressions, generic GitHub minimatch globs,
  cross-workflow `needs`, unknown input fields, cycles, unknown matrix
  sources and unsupported trigger chains rather than making up
  provider behavior.
- Current-source conformance-oracle guard/needs comparison is
  mandatory in the normal form, and missing actual oracle inspection
  produces HOLD. This is only evidence of *caller-declared agreement*;
  the host must still read and run actual repository Rust/shell/YAML
  conformance tests against the new graph.
- A CI-only independent lane must declare its export fail-fast guard;
  injecting an indirect artifact-export request into that lane
  makes the scenario fail. This tests the source contract, **not
  runtime instrumentation in any live consumer**.
- The fixture's complete source/revision/status matrix includes
  draft and ready, source-stale green, producer failed/skipped, one
  failed proof shard, hidden independent export, postmerge push,
  release lacking proof and cancellation. Each obligation is
  distinct by verifier + platform + trust + explicit matrix shard.
  Full/limited routes have separate same-workflow qualification
  prerequisites, and both retain independent security/native
  checks from other workflows as required status obligations.
- The two candidate full-run forecasts preserve all required
  detectors but intentionally have different dependency schedules:
  **blanket producer barrier:** 1,926 synthetic runner-seconds,
  1,820 synthetic critical-path seconds; **split independent
  check:** 1,926 synthetic runner-seconds, 1,808 synthetic
  critical-path seconds. Those are invented duration inputs,
  not actual billed savings or measured GH latency.
- The optional simulator **does not** reimplement canonical
  `ci_overlap.py` or the existing one-pass `ci_self_repair.py`.
  It is the bounded SIMULATE phase after DISCOVER and JUSTIFY.

## Actual executable qualification

On the first local Python 3.13 run, 35/35 synthetic
adversarial tests passed. An additional adversarial pass caught
two source-shape hazards before committing:
1. Python `fnmatch` treats a wildcard differently from GitHub
   workflow path filter syntax, so the supported normal form
   now permits only exact paths, `**` (all), and
   `prefix/**` (descendants). All other path glob syntax
   requires trusted host normalization or is rejected.
2. A policy gate must not appear to succeed at time zero
   before its real same-workflow prerequisites; the full/light
   fixture gates now have explicit `needs` and the checker
   rejects a zero-prerequisite qualifying job.

**Result:** **37/37 local Python negative controls passed**
against the corrected source and fixture. The full established
CI Guard suites (105 earlier methods) must still run
**on this exact v1.5.6 PR head** before integration.

The host/consumer side remains **not qualified**:
- Real GitHub Actions `if`, dynamic outputs, reusable workflows,
  queued jobs, token-trigger constraints, branch rules and
  workflow-run dispatch semantics are not authenticated by the
  normalized model. Unknown source behavior is HOLD.
- A caller may falsify `inventory.complete`,
  `conformance_condition`, `status_checks`,
  `runtime_guard`, source attribution or timing. The script
  does not independently inspect a repository, obtain GH
  receipts, execute actual test or artifact-export code,
  or apply policy/ruleset mutations.
- Real runner allocation, protected status acceptance,
  downstream publication behavior, live independent-lane
  export negative controls, and billed runner-minute/critical
  path deltas all remain NOT_RUN/NOT_MEASURED.

**#861 remains open** for full event-chain/dispatch semantic
coverage, provider/test-oracle integration and live normalized
model versus true workflow validation. A merged 1.5.6 source
slice is not the entire consumer's CI optimization.
