# Cumulative exact-file deduplication audit: 46 source repositories

**2026-11-01. Reference-only audit, no execution.** Inputs: the six [source SHA batches](README.md) `sha-batch-01.csv` through `sha-batch-06.csv`, constructed from all **50** source/category inventory CSVs. These records contain original source name and immutable revision in the originating inventory, skill path, Git blob SHA, and complete package-tree fingerprint. All source tree traversals were confirmed non-truncated.

## Evidence and measured counts

| Item | Observed |
|---|---:|
| Original repository sources | **46** |
| Source/category inventory files | **50** |
| Git-tree-listed `SKILL.md` path occurrences | **4,183** |
| Distinct exact `SKILL.md` Git blobs | **4,155** |
| Byte-identical extra occurrences | **28** |
| Exact-duplicate groups | **28**, each 2 paths |
| Exact-blob duplicates across different original repositories | **0** |
| Executed package/security/behavior evaluations by this discovery | **0** |
| New admitted skill packages by this discovery | **0** |

The first four batches hold **2,586 + 718 + 322 + 117 = 3,743** entries from 29 original sources. New fifth and sixth batches add **114 + 326 = 440** entries from 17 additional sources. The complete SHA comparison found **28 duplicated-blob groups**.

## Exact-byte duplicate breakdown

| Source | Duplicate occurrences | Why the distinction matters |
|---|---:|---|
| `glotoff/freecad-skills` | 3 | Copies under `.agents/skills/` and `skills/`, functionally the same exact source text |
| `danmaps/gis-agent-skills` | 1 | Same ArcGIS Online search entrypoint under `.github/skills/` and `skills/` |
| `haowjy/creative-writing-skills` | 23 | Same entrypoint text under Claude and OpenCode plugin paths; cross-host packaging does not constitute a separate methodology |
| `Owl-Listener/inclusive-design-skills` | 1 | Cognitive accessibility entries for adaptive personalization and contextual help have the same exact file blob; verify whether this is intentional before recommending two methods |
| **Total** | **28** | Preserve every discoverable path, count only one exact file identity per group |

**Important:** A unique Git blob is not an independently developed skill, unique method, cleared license, measured performance, or admitted capability. It is only a byte-distinct entrypoint. Cross-source semantic copies, localizations, paraphrased forks, derivative packages, and unverified generated content may remain extensive. No semantic or normalized-body deduplication occurred in this audit. Treat the **4,155** distinct-blobs count as an upper bound on distinct instruction text artifacts, **not** on independent useful skill approaches.

## Evidence files

- `sha-batch-01.csv`: 2,586 entries (initial tranche).
- `sha-batch-02.csv`: 718 entries.
- `sha-batch-03.csv`: 322 entries.
- `sha-batch-04.csv`: 117 entries.
- `sha-batch-05.csv`: 114 entries (new climate, geospatial, civic, pet-health, industrial and factory sources).
- `sha-batch-06.csv`: 326 entries (new electronics, logistics, history, accessibility, media and creative writing sources).

For per-repository immutable commit IDs and whole-package directory SHA fingerprints, see the source CSVs in [the discovery directory](../INDEX.md), [professional-domain expansion](../DOMAIN_GAP_EXPANSION.md) and [latest specialist expansion](../DOMAIN_EXPANSION_3.md).

## Next step: method-level and behavioral quality, not source-count theater

1. Match the collected candidates against the **995 existing governed third-party review identities** by source, path, revision and tree fingerprint, preserving existing evidence states.
2. Map each source entrypoint to one or more of the proposed [441 capability subdomains](../CAPABILITY_UNIVERSE.csv), with evidence links and no invented qualified-option counts.
3. Distinguish `same-byte`, `distribution copy`, `localization`, `fork`, `same-method rewrite`, `independent specialist` and `complementary method`; retain all paths for discovery.
4. Evaluate with task-baseline outcomes, safety/authority, licensing, portability, freshness, and independent expert review where required. Publish separate grades and failures.
5. Feed remaining weaknesses back into additional discovery and, only where justified, original [gap-fill skill authoring](../../../CAPABILITY_DISCOVERY_REFINEMENT_LOOP.md).

The passive repository runs no scanners, searches, external services, CI jobs or background work. These results were produced by the external authorized maintainer and deposited as static evidence. **No branch merge, admission or benchmark pass is claimed.**
