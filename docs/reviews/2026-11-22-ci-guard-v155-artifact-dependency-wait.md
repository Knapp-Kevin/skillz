# CI Guard v1.5.5: artifact-dependent runner wait

**Date:** 2026-11-22. **Origin:** anonymous late refinement
[issue #857 comment](https://github.com/Knapp-Kevin/skillz/issues/857#issuecomment-7077123601).
No external consuming repository is identified or changed.

## Corrected failure model

Long-running test process does **not** imply long test computation.
Two independently useful tests each allocate a runner before a shared
artifact exists, wait 30 minutes in the process and complete in seven
and nine seconds after the producer's artifact arrives. The
source-backed conclusion is **dependency wait on paid runners**,
not inherently duplicate assertions, repeated compilation or expensive
algorithm work.

A proposed remedy is an explicit artifact producer job and
scheduling-level prerequisite so consumer runners start after the
same-run artifact is ready. GitHub Actions `needs` propagates skipped
prerequisites: an intentionally skipped producer can unintentionally
skip legitimate narrow verification. Therefore both producer **failure
propagation** and deliberately **skipped producer alternate paths**
require negative testing; a blanket `always()` does not qualify
missing artifacts.

## Portable skill source and acceptance

- Portable CI Guard **v1.5.5**: 30-file Git package tree
  `7c06e7057310e9fc4819e2d892d4bf4390cf40f8`.
- Entrypoint SHA `d1fefd68405080070db557f97d9d511176aefc66`.
- Additional input `artifact_waits` with UTC request/arrival/finish
  timestamps, paid runner classification, exact producer/consumer,
  artifact scope, failure/skip routes and declared schedule remedy.
  `controls.artifact_wait_inventory_complete` must be true.
- Outputs `DEPENDENCY_WAIT_ON_PAID_RUNNER`, reported paid-wait minutes,
  source-reported cause, explicit UNKNOWN/hold cases and
  `optimization_complete:false`/cost `NOT_MEASURED`.
- Existing self-repair 14 tests plus **nine additional** negative
  methods and new two-consumer JSON fixture, all executed by the
  already existing scoped CI Guard QA workflow.
- Original nested verification overlap/cutover auditor left untouched.
- The source-defined wait durations can overlap reported total test
  times; summed waiting spans are **not** independently measured
  billed savings or critical-path improvements.
- Real same-run artifact custody, post-migration runner scheduling and
  branch conditional semantics **cannot be authenticated by these
  fixture assertions**. Actual consumer acceptance remains held.
- 10/10 structural source/tree/registry/guard checks passed on PR
  candidate before current-version QA. Python current-version result
  must be evidenced by exact-head GitHub Actions run, not inferred.

## Adversarial controls

1. Two consumers wait 30 minutes each; actual computations finish
   seconds after artifact availability. Source analysis identifies
   paid dependency wait as the dominant explained cause.
2. A proposed producer-job `needs` without verified runner deferral,
   same-run artifact custody, failure propagation and alternate
   producer-skipped branch must HOLD.
3. Producer fails: an unconditional alternate success must not
   qualify. Producer intentionally skips: required narrow tests must
   still run through an independently safe route.
4. Cross-run/stale artifact reuse is refused, and unknown/estimated
   timestamps cannot count as independently observed time.
5. Total billed runner minutes and wall-clock critical path must
   be measured separately using real provider receipts. No
   assertion that removing waiting runners shortens critical path.

A merged source improvement does not demonstrate actual consumer cost
reduction. Keep issue #857 as the external consumer acceptance tracker
or close only the bounded source-delivery component with an explicit
follow-up in #840. Historical GitHub Actions checks are version-bound.
