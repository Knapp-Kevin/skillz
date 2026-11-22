# CI Guard v1.6.0: host run/job receipt reconciliation

**Date:** 2026-11-22. **Scope:** Source milestone in issue #861, one standalone authored CI Guard skill, no consuming repository touched.

## Material capability implemented

The existing normalized v3 simulator represents a caller-supplied workflow/job model. Passing its tests cannot show which workflow/job instances actually executed on GitHub. New `scripts/ci_host_reconcile.py` is a bounded read-only evidence adapter that compares one complete simulated design/scenario to exact hosted workflow run attempts and their job receipts.

It enforces expected normalized job coverage, single mapping of each scheduled job to an exact provider job name, exact repository/source HEAD, workflow file and API event, distinct attempt job endpoints, completed workflow-level outcome, per-job conclusion, timestamps, duplicate/unmapped job exclusion, and no silent mixing of retry job receipts.

Two explicit modes:
1. `--observations` reads caller-supplied offline JSON and marks all observations `OBSERVED_AS_SUPPLIED_NOT_AUTHENTICATED`. An attacker can write fake JSON; it is not host verification.
2. `--live` performs owner-authorized, read-only GitHub API GET requests under TLS via fixed `api.github.com` routes, with redirect refusal, bounded paging, no credential output and optional `GH_TOKEN` `actions:read`. Only a direct live read may declare `OBSERVED_GITHUB_API_DIRECT`, and it still does not authenticate upstream dispatcher causality or policy.

A matching observed job list yields only `HOST_JOB_RECONCILED`, not proof of old-workflow absence, effective branch rules, positive/negative conformance tests, actual release/tag/forward side effects, artifact custody, latency causality, billable savings or suitability for production cutover.

**Planted synthetic acceptance:** `examples/test_ci_host_reconcile.py` adds **26** methods with isolated fake API calls, missing and duplicated jobs, source/event/path drift, stale run attempts, false-green workflow-level outcome, skipped/canceled behavior, invalid timestamps, finite bounded API receipts, and CLI negative controls. Bundled fictional `ci-host-reconcile-map.json` and `ci-host-reconcile-observations.json` demonstrate offline invocation without any consumer access. Existing 184 tests retained; target is **210** hosted tests. Source exact-head CI and security checks PENDING as of this record.

## Remaining open #861 acceptance

The adapter cannot derive the normalized source graph from actual GitHub workflow YAML or compiled repo conformance tests. GitHub provider dispatch cause/effect, token exceptions, permissions, run lineage, accurate protected branch policy, negative-control host qualification, end-to-end artifact custody and actual consumer provider billing/performance are still independently required. Do not close issue #861 based only on this feature. Issue #840 remains the external adoption/ROI ledger.

**Integration standard:** only an exact-head passing reviewed PR merged into `main` counts as source completion. No source-only report may claim authenticated consumer savings.
