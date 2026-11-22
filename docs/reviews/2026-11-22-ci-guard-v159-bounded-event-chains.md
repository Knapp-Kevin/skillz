# CI Guard v1.5.9: bounded workflow event-chain scheduling

**Date:** 2026-11-22. **Issue:** #861. **Prior:** merged v1.5.8 38-file package. **Source checkout:** current exact PR branch (package sha pinned in registry).

## Concrete defect

The v1.5.8 simulator accepted a destination workflow declaring `trigger_from` with a nominally verified token label, but **never actually activated that workflow from the source emitter**. A declaration could therefore be mistaken for modeled event behavior, hiding missing or incorrectly allocated downstream work.

## Implemented fix

Normalized subset v3 retains one CI Guard entry point and upgrades the existing `ci_scenario.py` only. A `role:other` source job with `dispatch_target` and `emitted_event:dispatch` can activate a target workflow with a matching `trigger_from`, dispatch-only event, and `EXTERNAL_DISPATCH_DECLARED`. The bounded virtual event edge orders downstream runner simulation after successful source completion, **not** using unsupported cross-workflow GitHub `needs`. Failed, skipped or canceled emitters allocate no downstream runner. Unknown source/target, contradictory trigger contract, invalid event, unknown token semantics and dependency cycles fail closed.

The source model returns explicit `modeled_dispatch_edges` with `provider_authenticated:false` and a global `event_chains_provider_authenticated:false`. It does not authenticate GitHub token exceptions, branch workflows, permissions, dispatch APIs, provider-run custody, billing, protected contexts or production publication. No consumer repository is named, read or altered. Real event-chain behavior must still be independently proven on an authorized host, and v3's source dependency model assumes zero dispatch transport delay as a counterfactual only.

Ten new executable negative methods in existing `test_ci_scenario.py` cover actual downstream scheduling after a deliberately reverse-ordered fixture, failed and canceled source suppression, independent direct dispatch, unsupported token events, orphan source/target, invalid role and receiver event, and forbidden cross-workflow `needs`. Existing 45 scenario methods remain. Total expected hosted Python methods if no other package changes: **184** (12+16+23+55+28+26+8+16), subject to actual CI receipts.

**Status at creation:** Source candidate staged, hosted exact-head CI PENDING, PR integration NOT COMPLETE. Issue #861 stays open for actual provider and conformance-oracle validation and live consumer acceptance. Observed cost/latency and host run lineage remain NOT_RUN/NOT_MEASURED.
