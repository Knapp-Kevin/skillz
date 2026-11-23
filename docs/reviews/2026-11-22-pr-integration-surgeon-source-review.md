# First-party PR Integration Surgeon: executable source assessment

**Date:** 2026-11-22. **Origin:** #880. **Package:** skills/authored/pr-integration-surgeon.
**Identity:** initial `0.1.0`, not recurring version inflation; 7 original MIT files.

## Gap and differentiation

Repository Delivery Assessor diagnoses delivery readiness and owner actions,
CI Guard handles verification workflow semantics, and Source Debt Triage
handles code annotations. None independently produces a dependency-ordered,
head-bound conservative PR integration queue. Existing third-party GitHub
triage/review tooling covers generic backlog discovery; this skill focuses
on verified **integration progression** rather than copying those methods.

## Functional prototype

The offline stdlib `scripts/plan.py` accepts only a supplied normalized,
bounded source-stage PR inventory. It orders declared dependency edges,
refuses cycles/duplicate identities, separates draft/conflict/check failure
from unknown merger/review/ruleset/queue/parent state, and compares required
check name plus app identity to exact PR HEAD. Stale reviews/CI are HELD;
unknown mergeability and incomplete changed path inventories are HELD.
Same-file edits produce advisories, not conflict verdicts. A candidate
always requires actual current GitHub review/ruleset/CI and merge-queue
verification, followed by provider receipt and issue outcome confirmation.

The six-PR example demonstrates one candidate for live recheck, one
dependent hold, two blocked changes and two evidence holds. It is entirely
fictional. **No actual repository was integrated.**

## Evidence boundaries

The 49 Python planted methods passed in a local container test run
prior to upload (not independent GitHub provider qualification).
Hosted exact-HEAD QA is pending. No live GitHub ruleset, merge event,
customer outcome, or user-authorized source mutation was performed.
Static success must not be upgraded to host behavior or real PR-closure ROI.

Current GitHub REST and merge-queue/stacked PR documentation used only as
factual background:
https://docs.github.com/en/rest/pulls/pulls
https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue
https://docs.github.com/en/pull-requests/get-started/about-stacked-prs

**Next:** verify final source SHA with hosted 49-test run and authored-wide
provenance/security gates. Merge only after CI success; preserve true status
under issue #880 for eventual authorized live paired trial.
