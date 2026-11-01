# Cumulative exact-version discovery and license integrity audit: 65 sources

**2026-11-01. Verified from the current draft PR #590 repository files.** This is static discovery accounting, not security scanning, behavioral evaluation, skill admission, license clearance, or permission to install. No untrusted skill text was executed.

## Exact inventory and rights reconciliation

| Measured field | Value | Meaning |
|---|---:|---|
| Original repositories with indexed SKILL.md entrypoints | **65** | Original source URLs, not independently verified methods |
| Source/category inventory CSVs | **69** | Every entry has exact source commit, skill path, file SHA and package tree SHA |
| SKILL.md path records across all sources | **4,835** | Candidate references, not admitted/qualified options |
| Individually matched licensing-context records | **4,835** | Consumer rights row exists for every path and exact source identity |
| Distinct Git entrypoint file blobs | **4,807** | Exact-byte file identity only |
| Extra byte-identical occurrences / groups | **28 / 28** | Different discoverable paths to identical file content |
| Byte-identical cross-repository entrypoints | **0** | No identical bytes across distinct source repositories; method-level derivatives may still exist |
| Source repositories without observed root license | **6** | 67 candidate paths; each checked for frontmatter license |
| Individual no-root-license SKILL.md frontmatters checked | **67** | All 67 have **no `license:` claim** in the inspected entrypoint frontmatter |
| Harvard civic SKILL.md licenses read individually | **9** | 6 declared MIT; 3 declared CC0-1.0; assets/dependencies remain unqualified |
| Candidate paths under Databricks-restricted parent license | **20** | No general-purpose unchanged use inferred |
| Newly admitted packages | **0** | All indexed paths remain reference-only |
| Candidate direct-use rows cleared | **0** | All remain `HOLD_RIGHTS_AND_SECURITY` |

The 69 inventory files and 11 [per-skill rights ledgers](../RIGHTS_INDEX.md) were reconciled against the [65-source license evidence map](../SOURCE_LICENSE_EVIDENCE.csv). Verified no missing source identity, source revision mismatch, unpinned skill link or missing rights companion in the recorded 4,835 rows.

## Byte-identity duplicate breakdown

The **same 28** byte-identical occurrences documented in the earlier [46-source audit](CUMULATIVE_46_SOURCES.md) remain after adding 19 sources:
- **3**: `glotoff/freecad-skills` `skills/` and `.agents/skills/` alternate paths;
- **1**: `danmaps/gis-agent-skills` `skills/` and `.github/skills/` alternate paths;
- **23**: `haowjy/creative-writing-skills` Claude and OpenCode host copies;
- **1**: `Owl-Listener/inclusive-design-skills` two paths with the same entrypoint blob.

The newly ingested 652 entries produced **no new byte-identical repeat occurrences** relative to the existing 4,183 entries. **This is not semantic deduplication.** For example, `kalta-ai/actuarial-skills/loss-reserve-analysis/SKILL.md` at blob `a296a5074ebbac0ba804621f626a416612b071ae` and `ilkeraslan/actuarial-skills/loss-reserve-analysis/SKILL.md` at blob `191b297d6f477de3924bfc7d57fd5f1ee15a64aa` differ by exact bytes, but the latter's license text credits `kalta-ai` and shares a skill name. Investigate the source relationship before counting independent alternatives.

## What the legal data means and does not mean

**Observed root license** is linked at the exact upstream revision. It may not govern a skill, bundled media/code/data or contributor-specific material. **Individual SKILL.md frontmatter** is a claim of license, not proof the person asserting it owns all referenced work. **Unlocated root license** is not proof of public-domain or open-source status.

Every rights row displays:
`observed_parent_license`, original pinned `source_license_url` or `UNLOCATED`, `license_obligation_profile`, `source_scope_status`, `skill_license_status`, `bundled_asset_rights`, direct reuse and inspiration status, and a pinned original `skill_url`. See [rights index](../RIGHTS_INDEX.md) and [licensing disclosure policy](../../../SKILL_LICENSE_DISCLOSURE.md).

In particular: 67 no-root-license skills were individually fetched, with no explicit license in SKILL.md frontmatter; this is an **unresolved-rights finding**, not permission to use or a claim that a separate package-local grant cannot exist. The 9 Harvard skills have individual declared CC0/MIT labels but still need attached-asset/legal-scope review before any direct-use clearance. A Databricks DB-style license imposes service-linked restrictions even if source files are openly browseable. The humanities CC BY-NC content is not unrestricted for commercial adaptation.

Copying source expression, modifying a licensed package, merely referencing it, and independently developing new work inspired by unprotected techniques are distinct legal/engineering uses. None is authorized simply by appearing in an index. Preserve original author credit, license/NOTICE references and changes when actually permitted to reuse.

## Work remaining before any maturity claim

1. Inspect per-package `LICENSE`, `NOTICE`, copyright, SKILL frontmatter, child scripts/assets/data and any embedded third-party licensing for each candidate; compare apparently conflicting claims.
2. Establish method-level originality or derivation, including the actuarial-source relationship, localization, mirrors and adapted techniques. Preserve references even where unchanged reuse is blocked.
3. Map every entry to one or more of the provisional [441 explicit subdomains](../CAPABILITY_UNIVERSE.csv), with independent-option denominators and evidence of task relevance.
4. After broad collection, run authorized external security and functional evaluation, retaining per-skill evidence/grades and professional/safety boundaries. Do not misreport source-license discovery as security or quality clearance.
5. Feed observed quality gaps and underrepresented subdomains into targeted further source search, independent adaptation, or a governed first-party skill draft where actually warranted.

The preceding [46-source audit](CUMULATIVE_46_SOURCES.md) remains a historical receipt; it is not the current total. The existing first-party and third-party governed review identities remain unchanged. This repository stays entirely passive.
