# PR #698: evidence-only merge acceptance

**Date:** 2026-11-04  
**Scope:** Static research-review documentation and immutable, source-pinned observations only. This review **does not approve any third-party skill for unchanged use**, run a scanner, run a host agent, or clear the security backfill in issue #402.

## What has been independently checked

1. The branch contains only `docs/` and `registry/` paths after remediation. It adds no executable skill, host automation, workflow, installer, active generator or source-code package. It changes no README or governed catalog publication totals.
2. The original Q11 reporting SVG, CSV, Node generator source and 45-reference JSON were each copied to `docs/archive/q11/` with **identical Git blob SHA to their former path** (4/4); their old active locations were removed. The archival README says they are historical and must not drive the live README charts.
3. The Q12 machine ledger contains **50 unique selected-method IDs**. A separate CSV parser found **50 data rows plus header**, each exactly **12 columns**, with **10 passed / 7 failed / 33 incomplete** static scanner results. All 50 records are explicitly *study-only*, and unchanged-use approvals and recorded behaviorally validated methods are zero. These are dated exact-tree observations, **not** fresh security scanning.
4. All **seven** Q12 declared source-ledger Git blob SHA values were fetched at Q8 pinned head `d3aaaa29f84b81e1905b295adb3657348551b9d8` and matched exactly (7/7). The Q12 review's obsolete `45-record` and arithmetic claims were fixed; its Q8-only links now point to the pinned commit rather than missing files on current main.
5. Q9 ledger records **eight** source entrypoints from seven publishers. Q10 historical ledger records **eight** of those reviewed, with four promising but held and four other held, **zero** featured promotions and **zero** executed security/behavior tests. The ROS2 portable-bundle manifest records **118** selected files with source-identity claims; this review verified the manifest's structural counts but did **not** independently fetch all external ROS2 files or authorize installing or running the package.
6. All **eight JSON files** under `registry/discovery/q10-*`, plus Q7, Q9, Q11 historical and Q12 ledger JSONs in this PR, are parseable. Source and license/rights holds remain visible in their original review files.
7. The merged-main README's November 4 security and curation graphic remains owned by main and unaffected by this PR. The Q8 proposed 50/33 shelf remains **draft** rather than silently becoming a merged recommendation.

## Narrow acceptance decision

**Accept these historical research receipts and reproducible source identity observations into main as archival/curation evidence.** This is a review of the **documentation**, not an acceptance of the researched candidates or source packages. The draft source Q8 ledger remains pinned to its exact commit and requires regeneration before publishing any new current Q8 numbers.

## Explicitly not accepted

- No new promoted `Recommended for Use` or unchanged-use candidate.
- No `findings-reviewed` acceptance of a SkillSpector failure, no bypass of incomplete scans.
- No new package scan, dependency/rights clearance, credential access, automated host runtime or observed adversarial behavioral evidence.
- No closure of issue #402, #589, #588 or other ongoing corpus qualification issues merely because dated research evidence was merged.

**Post-merge readback:** Confirm PR merged, all archived source blobs and Q12 CSV/JSON available on main, main README unchanged, and open PR count decreased by one.
