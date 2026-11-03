# Q1 four-source, 113-package integration invariant audit (2026-11-03)

**Audit base:** main `960b3ab04da77a6ef7839d74780b95ea75f16a3f` (#657). This is an independently recomputed **ledger-integrity and cross-source identity audit** of the existing exact-pin candidate decisions, **not** a new semantic review, upstream fetch, license clearance, security scan, behavioral execution, source admission, or a replacement for source-file inspection.

## Machine-readable ledger inputs and recomputed results

| Original source / pin | Exact ledger | Records | REFERENCE-ONLY | REJECT | Cursor |
| --- | --- | ---: | ---: | ---: | --- |
| [judicialmind/legal-skills @916ec5a4](https://github.com/judicialmind/legal-skills/tree/916ec5a4328a893cc57b4e0ecb9958b761901ca1) | [Q1 legal](../../registry/discovery/q1-judicialmind-legal-skills-static-20261103.json) | 30 | 12 | 18 | complete |
| [huang-sir1/radiology-skills @aaa0fe62](https://github.com/huang-sir1/radiology-skills/tree/aaa0fe621c404d3146333e0e1a2a22ed51f415fe) | [Q1 radiology](../../registry/discovery/q1-huang-sir1-radiology-skills-static-20261103.json) | 40 | 39 | 1 | complete |
| [bladecoder/narrative-skills @c0948f79](https://github.com/bladecoder/narrative-skills/tree/c0948f7970178b72bb9561030372e75d303d37b3) | [Q1 narrative](../../registry/discovery/q1-bladecoder-narrative-skills-static-20261103.json) | 28 | 27 | 1 | complete |
| [YujxZJCN/teaching-skills @fd0c486e](https://github.com/YujxZJCN/teaching-skills/tree/fd0c486e61cb1f065b88133b599e8806dfaeac12) | [Q1 teaching](../../registry/discovery/q1-yujxzjcn-teaching-skills-static-20261103.json) | 15 | 15 | 0 | complete |
| **Totals** | | **113** | **93** | **20** | **4/4 complete at pinned revision** |

### External-host checks actually performed

Parsed each of the four published JSON ledgers and iterated **all 113 individual records**, not merely the source summary or commit message.

- **113/113** records have 10 rubric dimensions and the sum of those dimensions equals the recorded `score_20`.
- **113/113** records have syntactically valid 40-hex `skill_blob` and `package_tree` identities. **This checks field shape, not independent git hash recomputation.**
- **113/113** records contain a nonempty package-owned-file list, controlled capability domain/subdomain/specific purpose, purpose/nontrigger description, authority/privacy finding, package-rights finding, and static scope.
- **113/113** records have neither `admitted_governed_record=true` nor `unchanged_use_approved=true`.
- Across all four source ledgers, **0 duplicate SKILL.md blobs** and **0 duplicate complete package-tree hashes** occur within this 113-record tranche. This is **within-tranche** deduplication only; no claim of uniqueness against 1,039 historical governed records or other GitSkills source families.
- All 113 records state `security_scan=not-run` and `behavioral_validation=not-run`; no execution evidence was added.
- **3 hard-fail records** remain REJECT and are not marked as static threshold eligible: `skills/court-filings/SKILL.md` (unauthorized consequential legal action), `radiology-skills/skills/radiology-journal/SKILL.md` (unauthorized consequential publication action), `skills/if/ink-doc/SKILL.md` (license conflict).
- All four source ledgers reference pinned root MIT license blobs; per-package restrictions remain independent. The audit did not independently re-read upstream license text or clear sidecar content rights.
- All four source-specific `review_cursor` values state 0 remaining at their pinned source revisions. This does not imply current-upstream freshness or any global completion percentage.

### Integration boundary and remaining evidence work

This audit **does not change** the four-source 4,813 raw path denominator, the 4,809 current-standard path decisions, the historical 1,039 governed review records, the 25 registered sources, or the unknown distinct eligible denominator. These 113 packages are from four additional **discovery-only** source families. Do not add 113 to the four-source numerator or admit them automatically.

The Q1 ledger has a valid coherent integration candidate. However, **cross-corpus identity comparison against every governed record and every other discovery family remains unproven**, and no independent source-file/rights reread was performed here. Capability-directory admission and atomic reconciliation of README, SYSTEM_STATE, CURATION_QUEUE, INDEX and index.json must be done together in a later material integration, not as partial counter churn. The existing six held PRs require their own qualification gates.

**Disposition:** ledger structural integrity PASS; within-tranche identity collision check PASS; source/copyright/security/behavior/unchanged-use qualification **NOT CLAIMED**. Keep the four source families discoverable as `SOURCE_VETTED_REFERENCE_ONLY_OR_REJECT` and keep their external-action hard fails explicit. The next worker should reconcile Q1 identities against governed and G1-G3 source indices before any admission or public accounting delta.
