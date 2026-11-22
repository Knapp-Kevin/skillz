# Results proof: before/after ROI and assurance-parity acceptance

## Outcome: proof of results is separate from proof of work

The existing [strict receipt comparator](../scripts/compare_ci_runs.py) retains its
same-source, same-scenario, same-runner-profile and same-cache matching. The
[results-proof generator](../scripts/ci_results_proof.py) consumes those
receipts when supplied and emits **two linked artifacts**:
`ci-results-proof.json` and `CI-BEFORE-AFTER.md`.

Use this phase **after** the full CI Guard DISCOVER → JUSTIFY → SIMULATE →
OPTIMIZE → PREPARE → PROVE → CUT OVER process for substantial CI repair.
A passed PR and merged workflow prove code integration, not performance
improvement or retained failure detection. For small repairs, document
`NOT_MEASURED` proportionately rather than inventing an ROI project.

Run from this independently downloadable skill package:

```sh
mkdir -p /tmp/ci-proof-out
python3 scripts/ci_results_proof.py \
  --input examples/ci-results-proof-fixture.json \
  --output-dir /tmp/ci-proof-out
python3 -m unittest discover -s examples -p 'test_ci_results_proof.py' -v
```

**All bundled examples are fictional and cannot demonstrate provider savings.**
The command has no network access or host mutation and refuses to overwrite
existing proof filenames. The caller owns the observation files, provider
authorization and output storage. Never copy consumer-private receipts or
identifying project data into the public Skillz source repository.

## Input contract (schema_version 1)

- `comparison_mode`: `strict`, `longitudinal` or `estimate`.
- `evidence`: `OBSERVED_AS_SUPPLIED_NOT_AUTHENTICATED`, `SIMULATED`,
  `ESTIMATED`, or `NOT_MEASURED`. The standalone generator **cannot**
  assert `OBSERVED_PROVIDER`. A separate trusted host/provider adapter
  must authenticate actual run IDs, source revisions, rulesets, native
  controls, billing and provider dispatch before promoting claims.
- `pairs`: zero to 40 `{baseline, optimized}` objects using the existing
  comparator's exact run/job schema. Job records include run attempt,
  source HEAD, scenario, runner profile, cache class, protected status,
  dependency edges, UTC timestamps, outcome and provider-billed minutes.
  If billing is unavailable, supply `null` and retain raw executed
  job-minute and elapsed-time reports. The strict comparator's original
  mandatory-billing API is **not relaxed**.
- `assurance`: separate expected/executed before/after terminal detector
  identities, required context sets, seeded-fault detection in both
  variants, retained release guards, old-workflow retirement and cutover
  verification. A `QUALIFIED` result is **as supplied**, not independently
  authenticated. Missing unique detection, stale/ghost successes,
  surviving unconditional legacy runs or missing failure controls must
  result in `NOT_QUALIFIED`.
- `scope`: source-workload equivalence, event/PR stage, host OS/
  architecture, matrix size, toolchain and confounders. Source HEAD,
  cache, runner and scenario are additionally checked in every pair.
- `source_refs`: workflow versions, source trees and receipt IDs/links
  retained by the consumer. Never invent source URLs or quote private
  evidence in the skill package.
- `change`: improvement description, observed waste mechanisms,
  retired workflows and optional **forecast** percent, clearly separated
  from actual observations.
- Optional `failure_feedback` has source-observed baseline/optimized
  seconds. Missing timing is `NOT_MEASURED`, not an inferred improvement.

## Comparison and verdict logic

**Strict**: identical source HEAD, scenario, runner profile and cache class
plus matched scope, distinct attempts, successful required jobs and known
billing produce a machine-computed comparison through
`compare_ci_runs.compare()`. Partial billing falls back to its strict
`summarize_run(allow_missing_billing=True)` raw-time lens without pretending
a strict monetary comparison passed.

**Longitudinal**: before/after source revisions frequently differ. Report
each run separately, with a source/host/scope reconciliation and directional
deltas only. `DIRECTIONAL_ONLY` and `NOT_COMPARABLE` must never be
reworded as a same-source causal result. Workloads, matrix obligations,
stage (release versus PR), platform, cache and toolchain must be reconciled.
A 78-job release run against a 4-job PR does not establish optimization ROI.

**Estimated**: forecasts never become observed savings. Missing provider
billing cannot yield dollar savings. A single sample has no p90; three
or more samples report median and nearest-rank p90, along with sample count,
baseline denominators and raw/percentage deltas.

The generated decision has two independent dimensions:
`decision.verdict` (economic/latency integrity) and
`assurance_parity.verdict` (failure-detection and cutover parity).
`NOT_CUT_OVER` means the actual replacement/retirement is incomplete;
`REGRESSION` detects lost controls or a negative cost/latency/feedback
trade-off; `NOT_COMPARABLE` refuses mismatched pair conclusions; and
`NOT_MEASURED` refuses unobserved or unauthenticated proof. The generator
**never emits certified `PROVED_IMPROVEMENT` or `PROVED_NO_GAIN` from
caller-declared inputs**. A consuming host can adopt these final outcomes
only with independently verified provider, security and pricing receipts.

Monitor separate **executed job minutes**, **provider-billed runner minutes**,
**dependency critical path** and **end-to-end observed qualification envelope**.
Record queue/setup/wait/checkout subphases only from reliable instrumented
traces. A smaller sum of job minutes can increase the critical path and
delay the first useful failure. Do not add overlapping test and dependency
wait periods twice; do not infer actual billed cost from CPU duration.

## Planted acceptance tests

The included 16 executable tests cover all eight RP-01..RP-08 classes:
exact-source success with planted-fault parity, incomparable release-vs-PR,
runner-minute improvement with no latency gain, estimate without receipts,
still-active legacy or dropped unique detector, source mismatch with separate
longitudinal mode, no provider billing, worse critical path/earlier-feedback
regression. Additional controls validate repeated samples, failed/skipped
jobs, schema discipline, report generation, absence of provider authentication
and the strict comparator's existing guarantees.

Real adoption remains separately required under the consuming project's own
governed ledger: final merge and cutover, actual job allocations, protected
required contexts, seeded failing paths, signing/publication boundaries,
provider-invoiced billing and same-scope before/after receipts. Only those
can establish genuine production impact.