# Matt Pocock registered-pin local-path reconciliation (2026-10-29)

Current registered pin: `6654f6b60cd9d5be8b54c6fafe44346dabeb3b76`; upstream recursive tree nontruncated, **29 eligible SKILL.md packages** under the registered inclusion/exclusion rules.
## Audit result
- Inspected all **29 provenance** and **29 verification** companions under the registered `mattpocock-skills` namespaces.
- Found **25 provenance** and **11 verification** `local_path` entries still pointing to the removed top-level `vendor/mattpocock-skills/` root. This was a current metadata navigation defect, not historical source identity.
- Changed exactly **36 `local_path` lines** to `skills/sources/mattpocock-skills/` and left every source revision, SKILL.md blob, package fingerprint, review score, status, license, evidence statement and behavioral state unchanged.
- The other **22** companion paths were already correct. The target canonical root is the intact pinned third-party gitlink under `skills/sources/`, not a new repository runtime or vendor copy.
- No package-security scanner or behavioral validation was executed, no source pin promoted, and no user-facing/admitted-source denominator changed.
## Scope and systemic finding
Historical structural migration had left current provenance/verification references pointing at an absent path. That can cause external hosts to miss governed evidence even though semantic review records exist. Correcting the path, not regenerating reviews or re-vendoring source, is the minimal remedy.
Current Tier-1 passive governance and source registry control. Historical `vendor/` references outside live `local_path` fields remain history unless independently shown to be active routing defects.
## Accounting
Registered Matt Pocock 29/29 unchanged; first-party 44 unchanged; third-party exact-version reviews 826 unchanged; total verification 870 unchanged; candidate freshness 19/19 unchanged. All five public accounting surfaces were reconciled in this lifecycle.
