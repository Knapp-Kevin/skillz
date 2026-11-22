# CI Guard v1.5.4: one-pass CI_SELF_REPAIR and nested test-phase cost

Date: 2026-11-22. Source feature for external-trial feedback #857,
integrated *after* canonical CI Guard v1.5.3 overlap/cutover auditor
was merged. No consumer repository, source path, workflow or identity
is identified or modified.

## Material failing behavior under assessment

A partial CI optimization can inadvertently trigger a still-active,
large legacy ready-PR matrix for each subsequent correction. Job-level
dedup is insufficient when tests spend far more time in case execution
than in a brief compilation step, yet share mutable or immutable setup
with different correctness obligations.

The v1.5.4 skill now requires read-only **DISCOVER** of every candidate
event and nested invocation, **PREPARE** one complete change set on a
cheap draft, **PROVE** a single owner-authorized exact-head qualification
with preserved native/release evidence, **CUT OVER** all old workflows
and required/status/spec contracts, **OBSERVE** actual provider costs
and latency, and **ROLL BACK** under explicit owner authority. This
does not grant permission to change host branch protection.

## Exact portable source and evidence

- Bundled independent MIT skill directory: **29 files**.
- Complete Git package tree: `66cd22ccd873d26e7ac419fc029c51438837ccbb`.
- SKILL.md Git blob: `d4ad020828d1175625d3478646165b813bb48d69`.
- New read-only preflight: `scripts/ci_self_repair.py`;
  Git blob `33dd8e989a9bec64aefa1e2d4fee0c28a295f2e8`.
- Fourteen new Python adversarial cases:
  `examples/test_ci_self_repair.py`;
  Git blob `035ed67e12561b9e140f119401ffdd31ecea957a`.
- Source, registry, verification and file count: **14/14 current
  structural invariants passed** at the proposed package tree.
- Fixture: `examples/ci-self-repair-fixture.json`, entirely invented
  and local, forecast 0 draft / 3 planned ready jobs; old 48-job
  ready workflow, when reactivated, should trigger HOLD.
- The original `ci_overlap.py` is unchanged: it remains the
  *only* cross-workflow nested-verifier and release-cutover auditor.
- QA workflow invokes the new test file **along with** original overlap,
  strict cutover, change classification, plan/qualification and
  observed-run comparator suites, on exact PR HEAD.

## Adversarial safety matrix

| Failure mode | Required bounded detection or safeguard |
| --- | --- |
| Trivial correction inherits legacy 48-job matrix | Forecast all matching ready jobs before first expensive PR |
| Draft also triggers legacy full bootstrap | HOLD, no expensive draft allocation |
| Multiple partial fixes each trigger full verification | Detect qualification cycles above owner cap |
| Test cases 25–26m, compile phase 2m | Test bodies dominate source-reported phase workload |
| Shared immutable fixture appears reusable | Only candidate class; do not authorize reuse without parity |
| Mutation or fresh directory demands isolation | JUSTIFIED_ISOLATION, unique assertions retained |
| Two test names appear equal but detect different defects | UNIQUE_DETECTION or UNPROVEN; do not consolidate blindly |
| Fewer runners, longer sequential wall time | No claim of improvement from job-count reductions |
| Prior green draft with identical SHA becomes ready | New source-bound required checks and cheap readiness checkpoint |
| Branch rule reduced but release spec still requires signing | HOLD, no merge qualification |
| Old unconditional workflow survives cutover | Existing strict `--verify-cutover` rejects active overlap |
| CI policy/classifier edit changes own obligations | HOLD until full source graph and scope mapped |
| Missing/malicious/unbounded JSON/symlink input | Refuse; no script/network/consumer action |
| Only estimated phase p90 provided | Treat as per-test reported estimate; sums aren't observed cohort percentiles |

## Qualification distinction

New v1.5.4 Python tests were *authored* but had **not been executed**
when this review was written. Older v1.5.3 QA results cannot transfer
to changed source bytes. A real exact-head GitHub Actions result is
required before source publication. Structural source checks do not
prove the consumer's workflows were actually inventoried, all provider
events respected GitHub semantics, branch protections were migrated,
or any person saved money. The optional preflight uses declared records,
does not parse YAML and never says `optimization_complete:true`.
Cost comparison remains `NOT_MEASURED` until comparable observed
provider receipts independently establish job-runtime, *billed*
minutes and critical-path changes.

Source publication completes **only on merge verified on main**.
The external consumer and cost-effectiveness acceptance belongs to
the separately authorized issue #840 and remains unverified here.
