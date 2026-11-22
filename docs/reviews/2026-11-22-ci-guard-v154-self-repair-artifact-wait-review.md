# CI Guard v1.5.4: one-pass self-repair, test-phase costing and artifact dependency waits

**Date:** 2026-11-22. **Tracker:** #857. This first-party skill review
uses only anonymous invented consumer scenarios. No real consumer
repository, account, project, or execution URL is reproduced.

## Source failure modes

1. Pathological CI can rerun a full legacy workflow on every
   half-completed repair PR. The skill needed a complete read-only
   inventory, one coordinated cheap draft change, readiness checkpoint,
   bounded expensive final proof and owner-approved rollback.
2. A superficially long-running test process is not proof of expensive
   test algorithms. A test may instead **poll for an artifact**, occupy a
   billed runner, then finish immediately after the artifact appears.
3. Recommending a simple unconditional producer→consumer `needs` edge
   may inadvertently **skip legitimate lightweight verification** when
   the artifact producer is intentionally not selected.
4. Different test IDs may have distinct fault detection even when
   repeating immutable fixture work; fresh-directory/mutating setup
   cannot be shared on guesswork.
5. Status rules and release/spec obligations must remain protected,
   independently of what a GitHub required-status setting currently
   enforces.

## Source correction

The standalone CI Guard v1.5.4 package adds
`components/ci-self-repair-and-test-cost.md`,
`scripts/ci_repair_preflight.py`, anonymous self-repair fixtures
and Python negative tests. The main SKILL.md makes this a mandatory
P0 preflight for expensive, over-fanned, self-blocking CI.

**Artifact root-cause update:** The second invented fixture models a
producer delivering one artifact after 1,800 seconds, two consumer
jobs having already started on separate runners and claiming 3,490
combined seconds of polling, 110 seconds of compilation and only
13 seconds of genuine test-case execution. The preflight groups the
polling intervals under `dependency_wait` and distinct
`DEPENDENCY_WAIT` instead of treating them as algorithm runtime
or shareable immutable setup.

The proposed full path must declare the artifact producer in each
consumer's `needs`, delay consumer runner allocation, bind producer
revision/run and custody, and propagate producer failure. The
producer-skipped lightweight path must retain its own required
consumer verification with a documented alternate route. Missing
or unconditional `needs`, stale/other-run artifacts, missing
failure propagation and accidental skip all HOLD.

**One canonical overlap auditor:** Existing `ci_overlap.py` remains
responsible for cross-workflow terminal checks and post-cutover safety.
The new `ci_repair_preflight.py` handles stage/readiness,
forecast and phase-level bottlenecks only. No duplicate cross-workflow
auditor, passive daemon or background service is added.

## Actual proof and limits

- **28/28 current local Python regression cases PASS** from
  `test_ci_repair_preflight.py` (17 original) and
  `test_ci_artifact_wait.py` (11 additional). These exercised
  ordinary first-use, coarsely repeated immutable and distinct
  assertions, draft fanout, release normative obligations, altered
  CI policy, artifact timestamps, job dependency safety, alternate
  producer-skipped path and source-graph evidence boundary.
- Claimed 3,490 runner-occupied seconds are **invented fixture inputs**.
  They are not validated billing receipts, observed provider timings,
  actual job DAG completion or measured dollar savings.
- Script sets `optimization_complete: false`,
  `host_authenticated: false`,
  `observed_runner_minutes_delta: NOT_MEASURED` and
  `observed_critical_path_delta: NOT_MEASURED` even when all
  the declared fixture rules structurally pass.
- The accompanying caller-authored artifact schedule and observed
  input fields are not independently authenticated. Actual GH runner
  allocation, same-run custody, native/release safety and
  legitimate lightweight route selection still need authorized
  consumer-specific receipts and negative controls.
- New Python source and fixture blobs are pinned by Git and verified
  on the branch. Full hosted exact-head CI Guard QA and complete
  package Git tree/index matching remain required **before merge**.

## Gate

**Skill source:** completion only once a reviewed PR merges and the
exact complete package's version, SKILL blob and tree hashes match
`main`.

**Real consumer CI repair:** NOT_VERIFIED until actual before/after
provider logs, phase timing, job allocation, released artifact custody,
failure propagation, source/spec parity, and measured runner minutes
versus critical path are observed under explicit consumer authority.
