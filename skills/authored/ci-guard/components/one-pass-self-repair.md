# P0: bounded, one-pass CI self-repair and test-internal cost diagnosis

## Activation

When CI is expensive, self-blocking, over-fanned-out or repeatedly triggered
during its own repair, use **CI_SELF_REPAIR**. This is a *mandatory planning
constraint* for such tasks, not another always-running system. A normal
user-authorized CI optimization must not enter expensive host qualification
before the read-only whole-system preflight. A draft branch is the default
preparation stage; skip expensive draft jobs at dispatch.

Do not optimize jobs as independent names. First inventory and record the
complete trigger-to-terminal execution graph in
[cross-workflow deduplication](cross-workflow-deduplication.md), including
all workflows, reusable jobs, composite actions, scripts, task runners,
native-platform and release controls. Then expand further **inside** each
expensive terminal test to identify actual repeated phase work.

## State transitions and authority

1. **DISCOVER (no mutation):** pin the target revision, inspect all workflows
   and their event/matrix expansion, required-status rules *and normative
   repository specifications*, actual nested verification commands, and
   previous job/run receipts. Read representative slow-job traces before
   blaming compilation. Report unknown or inaccessible coverage.
2. **PREPARE (draft, cheap):** design a *single coordinated* source, tests,
   workflow, classifier, bootstrap, release/spec, protection and rollback
   change set. Predict how **every planned commit, push, draft, ready,
   dispatch and release event** fans out through old and proposed workflows.
   Do not open/ready a PR that would launch unexpected inherited heavy CI.
   Run source-level, static and offline tests; keep expensive draft work off.
   If an owner specifies a legitimate extra CI cycle, document its explicit
   cost cap and authorization. Avoid serial half-repairs that each trigger
   the original full gate.
3. **PROVE (one scoped expensive head):** establish a visible readiness
   checkpoint: source, fixtures, verifier, spec, classification, required
   checks, negative controls, fallback and precise rollback are **all present
   and cheap validations green**. Then authorize the minimum complete
   exact-head real qualification allowed by the existing threat model.
   Old receipts can help diagnosis but cannot qualify a new head. A required
   full ready-PR gate remains mandatory until an explicitly owner-authorized,
   evidenced change to its normative protection has been completed.
4. **CUT OVER:** preserve real unique failure detection across release,
   native, signing, generated-source freshness and security boundaries,
   as well as blocked/skipped/stale negative cases. Rewire required
   statuses, workflow dependencies, specification references, branch rules
   and the old standalone workflows together. Use
   [strict post-cutover assessment](cross-workflow-deduplication.md);
   declaring CONSOLIDATE does not stop an active duplicate.
5. **OBSERVE:** on comparable current-head runs, collect per-step/phase
   and job receipts, total runner-job execution minutes, actual billed
   runner minutes, and critical-path wall time as **separate** measures.
   A smaller matrix may raise serial critical path even as job minutes fall.
   Report confidence, warm/cold cache and source/environment differences.
6. **ROLL BACK:** maintain a reversible, owner-authorized recovery path
   with an independent minimal smoke/release protection gate. A failed
   new graph must not create an unprotected green merge.

The source skill grants **no** authority to disable required checks,
change branch protections, edit or deploy a consumer repository,
schedule an action or spend money. Owner-approved gate migration
cannot quietly abandon a repo-spec assurance obligation.

## P0 SIMULATE before PREPARE for complex inherited CI

The first pass through DISCOVER must also inventory every repository
conformance test or validator that asserts hard-coded workflow guards,
`needs`, check names and matrix conditions. JUSTIFY maps those
assumptions to actual policy and semantics; a stale allowlist is
**VALIDATOR_DRIFT**, not authority to remove a good draft/dispatch guard.

Before beginning expensive PREPARE/PROVE on a multi-workflow repair,
run the [normalized scenario simulator](scenario-simulation.md)
against a complete trusted source-derived graph, at least two
candidate schedules, current and planned status contexts, fail/skip
and producer-skipped negative controls. Any unmodeled provider
expression or token-trigger chain returns HOLD; this script cannot
substitute for live GitHub acceptance. Source-specific static
artifact partitioning must be paired with a runtime CI-only
fail-fast export negative control.

## Test-internal cost and unique detection ledger

For each expensive test, record: exact source SHA, test ID, **unique
failure-detection assertion**, phase (compile/setup/fixture/project-check/
generation/test/oracle/mutation/cleanup), data and immutable-input digest,
platform/toolchain, runner/host isolation, fixture mutability, process/
fresh-directory requirement, p50/p90 observed duration and sample count,
execution source, and per-phase critical-path contribution **when traced**.

Use these classifications:

- `REPEATED_IMMUTABLE_SETUP`: same source digest/environment and
  verified immutable setup repeated. *Candidate* for shared read-only
  fixtures, prebuilt binaries or process-local reuse. **Not proof reuse
  is safe or actually performed.**
- `JUSTIFIED_ISOLATION`: separate mutation, fresh-directory determinism,
  seed, trust boundary, or process state is materially required.
  Keep separate execution unless equivalent failure controls prove safe.
- `UNIQUE_DETECTION`: a distinct assertion or failure seed matters
  even if the setup/entry function resembles another.
- `REDUNDANT_SAME_REVISION`: identical already-proven verifier and
  inputs under the same trusted execution context with no distinct
  detection. Requires actual overlap and negative-control evidence;
  the example local profiler does not authenticate this category.
- `UNPROVEN`: missing trace, digest, or isolation equivalence.
  Never consolidate on a guess.

Test-label similarity is not a duplication claim. Reuse must not convert
different unique tests into one lost detector. Reject a proposed
improvement if it reduces command invocations but leaves the dominant
test body untouched. Summed per-test p50 or p90 phase values are rough workload summaries,
**not valid portfolio percentiles** or critical-path timings. Do not infer
a p90 from one sample, infer billed
runner minutes from elapsed seconds, or sum test durations as the
critical path.

## Artifact waits hidden inside long-running test processes

When the test reports many minutes but the actual assertion finishes
immediately after a shared artifact arrives, record **dependency wait**,
not test algorithm runtime. Require per-consumer request/arrival/finish
timestamps from actual job logs, whether a billed runner was allocated
during that wait, the producing job/run/artifact identity, and distinct
test assertions. Do not assume that longer tests are redundant when
they merely wait for one shared producer.

Use an explicit producer-job dependency **only after** verifying:
the consumers do not start paid runners before the producer completes,
the artifact is authenticated from the same intended run/revision,
failed/absent producers fail closed, and a producer intentionally
skipped on the non-full path **does not skip the legitimate alternate
consumer verification**. In GitHub Actions, `needs` can propagate
skipped results, so design and test the alternate conditional route
separately. Avoid a blanket `always()` workaround that makes missing
artifact or failed producer look qualified.

Input `artifact_waits` is a required list (possibly empty), with
`controls.artifact_wait_inventory_complete=true` asserting inventory.
Each record identifies `producer_job`, `consumer_job`,
`artifact_id`, UTC `requested_at_utc`, `arrived_at_utc`,
`completed_at_utc`, `producer_outcome`, `evidence`,
`consumer_runner_allocated_during_wait`, `same_run_custody`,
`scheduling_remedy`, `runner_deferral_verified`,
`producer_failure_propagates`, and
`producer_skipped_alternate_preserved`.

The optional scanner emits `DEPENDENCY_WAIT_ON_PAID_RUNNER` and
`PAID_ARTIFACT_WAIT_REQUIRES_SAFE_JOB_DEPENDENCY`, and holds on
missing same-run custody, failure propagation, producer-skipped
alternate safety or unobserved timing. It **never** authenticates
caller assertions, verifies actual post-cutover runner allocation,
or claims verified savings. Test durations and dependency-wait spans
may overlap, so the sum is a diagnosis aid, not a measured critical
path or an additive billing result.

## Offline executable preflight

The optional standard-library-only, read-only
[`ci_self_repair.py`](../scripts/ci_self_repair.py) consumes a small,
**manually completed, source-pinned** JSON record:

```sh
python3 scripts/ci_self_repair.py --input preflight.json --require-ready
# exit 0: structurally ready to request an authorized exact-head proof
# exit 3: HOLD, incomplete, unsafe or excessive predicted fanout
# exit 2: malformed or unsafe input
```

`revision` pins the source. `inventory_complete` and
`controls` are caller assertions, not verified provider receipts.
`workflows` enumerate all relevant existing/retired jobs, with
`id`, `events`, `paths`, `active`, `expensive`,
`matrix_jobs`, `matrix_expanded`, `invocations_expanded`.
`repair_events` specify planned event `id`, `stage`, changed paths.
`budget` specifies approved preparation-job and expensive-cycle
limits. `phases` contain per-test `p50_minutes`, `p90_minutes`,
`revision`, `environment`, optional `shared_key`, immutable/mutability
and unique-detection hints. Inputs are restricted to 1 MiB, duplicate
JSON keys and symlinked source paths are rejected. No code from
the examined repository is executed. The separate overlap auditor
must still verify workflow-to-terminal equivalence; this script does
**not** parse full GitHub glob/event logic or authenticate the graph.

The output intentionally says `optimization_complete:false`,
`provider_receipts_authenticated:false`, and
`observed_*_delta: NOT_MEASURED`. A source-only preflight PASS
is **not** successful real CI, merge acceptance, saved money or a
verified release. Source changes must be merged and revalidated
on main before counted as published.

## Adversarial requirements

Run the in-package `test_ci_self_repair.py` cases,
including the planted 30-minute producer, two early-started paid
consumers, post-arrival seconds-long completion, intact unique
assertions, success/failure/skipped producer outcomes, and a
regression in which `needs` incorrectly suppresses a valid
non-full verification path:
format-only change inheriting 48 jobs; old unconditional draft/ready
workflows; short compile vs long test bodies; immutable setup versus
mutating/fresh-directory isolation; unique oracle detection; extra
expensive qualification cycles; unmapped required status/release
normative specification; draft-to-ready same SHA; unknown event/matrix;
fewer jobs but longer critical path; rejected malicious JSON input.
Pair with the bundled nested-verifier overlap tests and strict
release cutover tests.

**Completion gate:** one coherent source diff and negative controls
present; read-only forecast catches inherited fanout; exactly scoped
owner-approved qualification runs against current source; no
independent assurance lost; old unconditional paths absent; real
billed-runner and critical-path comparisons observed. Without actual
consumer receipts mark `IMPLEMENTED_NOT_ADOPTED`, never `SAVED`.
