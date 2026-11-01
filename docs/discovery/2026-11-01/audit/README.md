# Cross-source exact file SHA audit: 29-source discovery archive

**Latest cumulative result:** [46-source, 4,183-entrypoint audit](CUMULATIVE_46_SOURCES.md) verifies **4,155 distinct Git blobs** and **28 extra byte-identical occurrences** across six SHA batches. This document retains the original 29-source four-batch historical receipt below; the latest cumulative page supersedes its totals but does not rewrite its original evidence.

**Audit date:** 2026-11-01. Passive Git object comparison only. No upstream code, scans, CI, external service, execution or installations.

## Scope and method

Inputs: [sha-batch-01.csv](sha-batch-01.csv), [sha-batch-02.csv](sha-batch-02.csv), [sha-batch-03.csv](sha-batch-03.csv), and [sha-batch-04.csv](sha-batch-04.csv). These four deterministic input partitions were built from **all 33 source-inventory CSVs** linked from [the discovery index](../INDEX.md) and [domain expansion](../DOMAIN_GAP_EXPANSION.md). Counts: **2,586 + 718 + 322 + 117 = 3,743** complete SHA rows from **29 original source repositories**.

For every record, compare the `entrypoint_blob_sha` field exactly. Every observed SHA is a 40-character lowercase Git hash. This is exact Git blob identity, **not** text normalization, similarity/semantic matching, package-tree equivalence, or security evidence. Root source commits and tree objects are preserved in the source inventory CSVs.

## Results

| Measure | Count | Qualification |
|---|---:|---|
| Pinned source repositories | 29 | Unique repository names, not independent methodologies |
| Total `SKILL.md` paths | **3,743** | Git-tree enumerated; not 3,743 distinct usable skills |
| Distinct `SKILL.md` Git blobs | **3,740** | Byte-identity at Git blob level, not semantic dedup |
| Redundant exact-blob occurrences | **3** | All within one FreeCAD source; none cross repository boundaries |
| Groups of exact duplicate blobs | **3** | Each pair has two alternate paths |
| Cross-repository exact-blob duplicate groups | **0** | No evidence of byte-identical files across sources; does not prove independent ideas |
| Behaviorally validated candidates in these discovery records | **0** | No evaluation performed in this tranche |

### Three exact duplicate entrypoint pairs

| Skill | Git blob | Equivalent paths at the same pinned commit |
|---|---|---|
| FreeCAD power user | `02348a936289477009dcb1b83f17ab5ab66444f9` | `.agents/skills/freecad-power-user/SKILL.md` and `skills/freecad-power-user/SKILL.md` |
| FreeCAD user | `1683783b80d00830e925505e58d2808e2446aa0a` | `.agents/skills/freecad-user/SKILL.md` and `skills/freecad-user/SKILL.md` |
| FreeCAD developer | `425509fe4134a7b0cfbf5e0eb0f165c67b0359de` | `.agents/skills/freecad-developer/SKILL.md` and `skills/freecad-developer/SKILL.md` |

All three pairs belong to `glotoff/freecad-skills@9fe36d37dfb1a0684b277a9d143876d45d1f6b15`. Preserve both paths for host-specific discovery, but **count one exact entrypoint blob in each pair**.

## What this audit does *not* conclude

- There may be numerous **semantic duplicates**, adapted copies, instruction translations, provider mirrors or overlapping methods with different Git blob hashes. No normalized text, semantic embeddings or package resource comparison was performed.
- `salikkhann/openmedskills` contributes both `skills/` and `dist/agent-skills/` paths, and `ellmos-ai/skills` has localization variants. They may represent the same approach even though their SHA values differ. They remain `POTENTIAL_DERIVATIVE` pending source graph and semantic review.
- No candidate is assumed safe, effective, open for unchanged redistribution, current for production use, or uniquely valuable because its file hash is unique.
- Existing **995 governed third-party exact-version review identities** are **not included in this 3,743-path exact-file comparison**; do not sum the denominators or claim review reconciliation.

**Next acceptance work:** establish a structured semantic and method-level relationship index per *subdomain*, including `independent_method`, `same_method`, `distribution_copy`, `localization_variant`, `fork`, `superset` and `specialist_alternative`. Then link receipts for task quality (Q), security (S), provenance/licensing (P), portability (T) and currency (C). For high-risk physical, clinical and legal work, require specialist review and action-safety acceptance before unchanged reuse.

The repository remains **passive reference material**.
