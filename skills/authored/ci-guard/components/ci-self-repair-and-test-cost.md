# CI_SELF_REPAIR: one-pass pathological CI recovery and test-internal cost

**P0 binding when:** a CI pipeline is already abnormally slow, runs a large
matrix for each minor correction, blocks its own repair, repeatedly launches
legacy workflows, or when the actual expensive phase is unknown. This
component is part of the standalone CI Guard package. It is a *method for
a host*; it does not operate repository jobs or govern a consumer.

## 1. Discover the complete execution and expense boundary first

Before making **any substantive expensive CI edit**, pin the exact source
revision and enumerate **every workflow/event**: draft, ready, synchronize,
push, merge queue, dispatch, workflow-run, release and publication. Traverse
job conditions, needs, matrix expansion, reusable workflows, composite
actions and all nested task-runner/scripts to effective terminal verifiers.
The normative repository spec/branch rules, downstream status consumers,
release requirements and trust boundaries are separate evidence sources.

Use the existing mandatory
[cross-workflow execution deduplication method](cross-workflow-deduplication.md)
and its [single canonical auditor](../scripts/ci_overlap.py). This
**self-repair component does not implement another overlap auditor.**
Resolve shared verifier command paths before inserting a selective
classifier or draft skip, and preserve uniquely effective checks.
If even one relevant path cannot be inspected, label it UNPROVEN,
expand to full qualification or HOLD. Do not treat job names as
verification identities.

For the **slowest jobs**, inspect actual provider step logs and, where
authorized, add bounded local timing for within-test phases:
`compile/setup | fixture construction | source copy/check | generation |
case execution | differential/oracle | mutation | export | cleanup`.
Report observed phase durations *by test ID* with exact run/head, OS,
toolchain, environment, input closure, p50/p90 where supported, and
runner-minute and actual qualification critical-path contribution.
Do **not** declare repeated compilation the bottleneck simply because
build logs contain compiler invocations. Nor conclude that a process
spending 30 minutes inside a test harness was computing for 30 minutes.
Inspect blocking/polling intervals, requested-artifact timestamps, artifact
arrival timestamps, producer run/job identity and post-arrival completion.
If several consumers finish seconds after the **same upstream artifact**
arrives, classify the evidenced waiting interval as `DEPENDENCY_WAIT`,
not test algorithm execution, redundant compilation or shareable setup.

**Job scheduling remedy:** If the producer supplies required same-run
artifacts, consider explicit producer→consumer job `needs` and
same-run artifact custody, delaying consumer runner allocation until
producer success. Reject a proposed graph where consumers still occupy
runners waiting, where a producer fails but consumers claim success, or
where an artifact from another run/revision is silently accepted.
**Do not make the producer an unconditional dependency on all paths.**
When the producer is intentionally skipped in a legitimate lightweight
or non-full path, keep that path's required consumer verification running
via a separately demonstrated conditional route and valid fallback.
A skipped producer must not make all downstream tests disappear.

For cost, distinguish *potential runner-occupied wait seconds* inferred
from source-bound timestamps from **actual billed runner-minute savings**
and **observed qualification critical-path changes** after deployment.
Dependency scheduling may save runner time without reducing the wall-clock
critical path, and can make some paths slower. These outcomes require
provider receipts; synthetic evidence never establishes a dollar saving.

For repeated operations, distinguish:
- `REPEATED_IMMUTABLE_SETUP`: same proven immutable input closure,
  platform/trust and safe read-only setup, possibly reusable. Source
  equivalence alone does not authorize sharing.
- `JUSTIFIED_ISOLATION`: fresh-directory, mutation, process/OS boundary,
  deterministic-reproducibility or independent attestation demands separate
  setup. KEEP the repetition until discriminating tests prove otherwise.
- `UNIQUE_DETECTION`: individual tests have distinct assertions/fault
  detection, even if their fixtures look alike. KEEP the assertions and
  negative cases even when improving common immutable setup.
- `REDUNDANT_SAME_REVISION`: positive equivalence receipts match effective
  work and failure detection at exact inputs/platform/trust. Candidate for
  consolidation only after independent negative-control parity.
- `UNPROVEN`: unknown mutation/semantics, source, environment, trust or
  fault coverage. VERIFY, not a shortcut to removing expensive tests.

A test refactor which only reduces process launches but preserves
unchanged expensive case bodies is **not measured savings**.
Always separate **total billed runner minutes** from **actual
qualification critical-path wall time**. A serial batch may reduce
runner setup bills yet worsen time-to-green; do not label it faster CI.

## 2. Prepare ONE coordinated bounded change without triggering old CI

Use `CI_SELF_REPAIR` with sequential phases:

1. **DISCOVER:** read-only whole-graph and bottleneck inventory. Obtain
   prior receipts, never discard observed failure evidence, and never
   treat a stale SHA as fresh qualification.
2. **PREPARE:** assemble source, workflow, classifier/policy, tests,
   negative controls, required-status migration, exact release/packaging
   dependencies and rollback in **one coordinated proposed change**.
   Keep PR a draft or work in a cheap authorized local branch. A draft
   defaults to **zero expensive CI runner allocation**, including
   *independently triggered* workflows. Use offline lint/static/source
   tests and quick targeted checks, not repeated incomplete full runs.
3. **PROVE:** before leaving draft, show readiness receipts for **all**
   edits, policy, tests, negative-control coverage and rollback at the
   same revision; cheap formatting/integrity validation must pass.
   Forecast fanout by event and matrix, including the legacy workflow.
   Select a **bounded number** of expensive final exact-head
   qualification cycles, normally one, only when the full coherent
   candidate is ready. If the old repository rules insist on full
   qualification, either honor them, or obtain owner-approved equivalent
   governed migration with shadow/negative-control parity. Never assume
   disabling a required GitHub check deletes repository-spec obligations.
4. **CUTOVER:** retain each unique detector, native-platform/security/
   signing/release obligation and exact-head status; migrate old required
   names and downstream publication dependencies under authority.
   Test that **missing/skipped/failed/stale** selected evidence fails
   the final gate. Re-inventory all events to prove old unconditional
   verifiers no longer run. An incomplete migration is HOLD, not DONE.
5. **OBSERVE:** compare actual before/after triggered jobs and billed
   runner-minute totals across all workflows *separately* from
   wall-time critical path, queue/setup, variance and negative-control
   parity. If observed runs are missing, report NOT_MEASURED, not 50%
   saved because one job disappeared.
6. **ROLLBACK:** preserve a bounded owner-authorized recovery path.
   If the change breaks unique detection, restore original required
   qualification before claiming repair. Document residual risk.

**Do not create a repository-owned service or new scheduled evaluator.**
This method belongs in the downloaded standalone skill and is invoked by
the host only when explicitly authorized. It must not automatically edit
a consumer's branch rules or disable existing workflows.

## 3. P0 fanout and readiness contract

Before opening or converting the consumer PR to ready, produce a
forecast row for **every relevant event**:

`event | source revision | triggering workflows | matching path filters |
expanded matrix jobs | expensive? | compulsory protected/spec obligations |
expected setup + test phases | estimated total runner minutes |
estimated critical-path impact | uncertainty | authority`

A one-line formatting fix in a test file may be a genuine source change
to the verifier and need real qualification, but **it should not trigger
the old full matrix repeatedly while preparing an incomplete repair**.
If the existing spec demands full on all ready PRs, do not pretend the
work is safely skippable; choose (a) governed migration with evidence,
(b) one necessary full qualification after ready, or (c) HOLD.
Classification of CI/policy/spec/unknown edits always expands to full
qualification unless a separately accepted equivalent migration proves
the same detection coverage.

Readiness requires frozen exact source/head, all intended edits, current
source-bound negative cases, selected obligations, provider trust
boundary, owner-approved status/ruleset plan, successful cheap checks,
fanout estimate, final qualification budget and rollback. If any is
absent, **do not start a full costly proof cycle yet**.

## 4. Portable executable self-repair preflight

The Python standard-library
[read-only self-repair preflight](../scripts/ci_repair_preflight.py)
inspects a *caller-authored* JSON record of inventory completeness,
phase observations, fanout forecast, proposed stage sequencing and
normative required versus selected checks. It complements the canonical
cross-workflow checker; it does not discover workflow YAML, execute
tests, change GitHub settings, verify external receipts or guarantee
cost reduction. A local fixture is bundled:

```sh
python3 scripts/ci_repair_preflight.py --input examples/ci-self-repair-fixture.json
python3 -B -m unittest discover -s examples -p 'test_ci_repair_preflight.py' -v
python3 scripts/ci_repair_preflight.py --input examples/ci-artifact-wait-fixture.json
python3 -B -m unittest discover -s examples -p 'test_ci_artifact_wait.py' -v
```

The fictional fixture models 110 seconds total compile but 4,500
seconds case execution. A separate fictional
[shared-artifact wait fixture](../examples/ci-artifact-wait-fixture.json)
models a 30-minute producer and two consumers claiming a combined
3,490 runner-occupied seconds waiting on that artifact while performing
only 13 seconds of case execution. These are synthetic timings and
do not demonstrate real runner billing or critical-path savings.
The wait classifier requires claimed artifact request, availability,
producer identity and same-run revision data; without that evidence,
long-lived processes remain unproven compute-versus-blocking causes. It flags repeated immutable setup separately
from mutated fresh-directory work and individual unique assertions.
The fields `phase_observations[].run_id`, environment, revision,
`on_critical_path`, p50/p90 and cost are **analyst supplied**;
an actual provider log and proof of critical-path timing are required
to label any value OBSERVED. This prototype reports
`host_authenticated:false`, `optimization_complete:false`
and `NOT_MEASURED` observed cost deltas **even when source-graph
structure passes**. A claimed `inventory.complete:true` is not
verified by the local program.

Mechanical negative cases include the 10 required adversarial
situations: pathological draft fanout, nested verifier duplication
(covered by canonical overlap checker), test-body bottlenecks,
safe immutable vs mutating setup, batching misrepresented as faster,
old unconditional runner, normative spec ignored after ruleset edit,
draft-to-ready stale status, second formatting correction while not
ready, and CI/policy edits improperly labeled passive. These are
separate from live host qualification.

**Optimization assessment fails** if an unnecessary unconditional
duplicate remains undisclosed, an expensive repair branch triggers
old full validation before readiness, a large conformance test is
incorrectly diagnosed as compilation, unique failure coverage is
removed, protected status migration omits normative requirements,
or source-bound observed cost/critical-path improvements are claimed
without independently comparable receipts.
