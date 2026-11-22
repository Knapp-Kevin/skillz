# CI Guard v1.5.8: results proof and source acceptance

**Tracking:** #867. **Date:** 2026-11-22. **Scope:** one portable first-party CI Guard package, no consumer identity or repository touched.

## Implemented

- New `scripts/ci_results_proof.py` creates linked `ci-results-proof.json` and `CI-BEFORE-AFTER.md` from supplied evidence. Includes before/after raw executed job minutes, provider-billed minutes where present, DAG critical path, wall-clock envelope, optional first-failure feedback, count, median and p90 where supported, percentage denominators, assurance detector and context parity, seeded negatives, release continuity, old-path cutover, source references, limitation statements and separate economic/assurance verdicts.
- The canonical strict `compare_ci_runs.py` remains authoritative for exact same-source revision, scenario, runner profile, cache and separate run IDs. Its default mandatory billing control remains intact. Its optional `allow_missing_billing=True` **summary-only** path reports raw job time without fabricating billing or using relaxed strict comparison.
- Longitudinal source-changing comparisons are explicitly weaker and never imply a same-source causal proof. All offline results are `OBSERVED_AS_SUPPLIED_NOT_AUTHENTICATED`, `SIMULATED`, `ESTIMATED`, or `NOT_MEASURED`; the generator cannot authenticate provider reports or certify PROVED outcomes.
- The full synthetic sample and 16 planted adverse tests cover RP-01..RP-08, provider-missing billing, lost unique detectors, still-running legacy paths, repeated samples, unsupported schema, output-file safety, critical path and first-failure tradeoffs.
- The existing CI Guard QA workflow **previously invoked `test_compare_ci_runs.py` as a plain script**, which only defined unittest classes and did not execute them. It now discovers/runs all existing comparator tests as well as the new proof tests. No repository or consumer CI controls were relaxed.

## Evidence boundary

**Hosted source evidence:** PR #869 source head `f2c28fe8f7d5d0a1eaf9b0eff284ac2321a9fb6b` passed [Actions #45079498442](https://github.com/Knapp-Kevin/skillz/actions/runs/45079498442): **174/174 tests** (12 overlap + 16 cutover + 23 self-repair + 45 scenario + 28 classifier + 26 plan + 8 comparator + 16 proof). All three PR checks succeeded. Final metadata reconciliation HEAD still requires an exact-head rerun before merge. Real consumer billing receipts, exact branch protection, host-side seeded faults, release publication, job allocation, engineering cost, commercial ROI and actual production savings are **NOT_RUN/NOT_MEASURED**. #840 stays the real-consumer acceptance record, while #867 is only complete when source and planted contract checks are merged and verified.

The two generated documents report `NOT_MEASURED` or `NOT_COMPARABLE` rather than asserting proved savings from unauthenticated supplied data. The standalone tool is not a GitHub Actions interpreter or host-attestation mechanism.
