# CI Guard v1.5.3: execution-graph cross-workflow cutover adversarial review

**Date:** 2026-11-22. **Priority:** P0. **Canonical repository:** `Knapp-Kevin/skillz`.
This is a first-party authored skill release, not a live consumer CI
optimization. Anonymous fixtures are intentionally unrelated to any
consumer repository.

## Concurrent baseline and design choice

CI Guard v1.5.2 was concurrently published via **merged PR #854** while
a separate v1.6 proposal was being prepared. The latter prototype's
standalone checker passed 26/26 local Python tests, but contained a
**second overlapping execution auditor**. The pending v1.6 PR #855
was therefore **not merged**: avoid two nearly identical tools
for detecting redundancy.

Instead, this v1.5.3 integration makes the shipped v1.5.2
`scripts/ci_overlap.py` **the single canonical auditor** and
extends that exact implementation with an independent strict
post-cutover decision, preserving its pre-cutover/--enforce CLI,
existing 12 tests and all classifier/plan tests. The main
SKILL decision procedure now requires complete source-to-terminal
execution inventory at step **2**, before classification and
optimization are implemented.

## Concrete delta

- Each nested call path is explicitly returned from the same
  recursive graph expansion as the original overlap classifier.
  The normalized class is EXACT_DUPLICATE / PARTIAL_OVERLAP /
  JUSTIFIED_REPETITION / UNPROVEN; historical candidate names
  remain as compatible source-classification output.
- `--enforce` still checks documented overlap dispositions.
  A documented intent to VERIFY/CONSOLIDATE is NOT actual
  consolidation. The new `--verify-cutover` mode adds a strict
  separate check, returning code **3** if old active duplicate
  paths remain, even if they have proposed dispositions.
- To accept a retired old path, the inventory retains it as
  inactive with revision-bound `retirement_proof`; missing
  evidence fails.
- Both candidate and release required obligations must appear
  in effective terminal executions and have matching exactly
  bound success receipts. Missing/failed/skipped/stale/reduced
  release verification fails, including removed signing.
- Draft path must be cheap and explicitly non-qualifying;
  ready and release retain their own current exact-revision
  obligations. Unexpanded matrices, unknown conditions/events,
  unknown inventory or missing policy are blockers.
- All results remain `host_authenticated:false` or
  `optimization_complete:false`; runner-minute and
  critical-path deltas remain `NOT_MEASURED`.
- File input requires non-symlinked path/ancestors, bounded
  1 MiB JSON and rejects duplicate keys.
- Two original anonymous JSON files show a nested duplicate
  and a modeled cutover, with standalone CLI commands.
  No third-party skill code, external rights or access,
  installation dependency, live service or obligatory
  independent model was added.

## Adversarial acceptance

The original 12 cross-workflow candidate-finder tests remain.
The additional **16 current Python regression tests** cover
nested composite/standalone aliases, co-triggered push/PR,
same effective command behind distinct recipes, false-positive
platform repetition and unproven differences, stale active
standalone workflow, revision-bound path retirement, missing
release signing, absent/failed/stale authoritative receipts,
draft expensive work, incomplete inventory/unknown matrix,
runnable before/after JSON and symlink/duplicate-key input.

A source-graph structural PASS on the synthetic corrected fixture
must **not** be called CI adoption or measured runner savings.

## Genuine GitHub CI evidence vs host outcomes

On PR #856, source-bound Actions job `offline-contracts`
was observed passing on branch commit
`89e708891117e46e2a6525347dce46ed7ea9e00a`,
run **45006875321**, job **137160321648**:
- 12/12 original nested-overlap regressions PASS
- 15/15 new cutover/qualification regressions PASS
- 28/28 classification regressions PASS
- 26/26 plan/qualification regressions PASS
- run comparator script invoked successfully

An additional co-trigger push/PR regression was added after
that run, changing this test suite to **16** cases. This
later commit and the registry/evidence update require a fresh
exact-head GitHub QA run before claiming all current tests passed.

**External consumer source inventory, true provider event coverage,
real branch protection, release gate actual receipt identity, full
before/after failure-detection parity, runner minutes and observed
critical path:** NOT_VERIFIED / NOT_MEASURED. An authored
graph contains untrusted caller assertions; only independent
host evidence can establish actual savings.

## Disposition

**GO for source publication** only after the integration PR
is merged and full current package source/tree/index pins verify
on main, with current exact-head GitHub QA green.

**NO-GO for real CI cost-benefit claims** until the consumer's
authorized workflow revisions, actual nested invocation graph,
release qualification, baseline/after job receipts, planted
failure controls, and comparable measured costs are independently
observed. Zero unmerged PRs is the repository hygiene target;
do not leave the incompatible superseded v1.6 PR #855 open.
