# Aviation + GIS: bounded exact-package and rights recovery (2026-11-02)

**Source:** held [PR #590](https://github.com/Knapp-Kevin/skillz/pull/590) archive at `f9567bc4f7489621c1597fa5bed58ac9f101a24b`. This is a deliberately **disjoint source-family recovery** from Claude's current four-source j4flmao/OpenAI frontier. The upstream source revisions were pinned and the exact files independently fetched through the connected GitHub API. No source admitted, skill installed, provider queried, script run, external communication sent, security scanner executed or behavioral test claimed.

## Evidence and exact identity

| Source | Pinned revision | Archive paths | Reverified SKILL.md blobs | Complete package tree evidence | Decision stage |
|---|---|---:|---:|---|---|
| `alexbrooker/aviation-skills` | `68b8856323d60bd6fb135c665acc16156cff350f` | 4 | **4/4 matched** | **4/4** single-file Git tree object SHA-1s independently reconstructed from exact Git blobs and matched to archive; no bundled files | **4** individual current-standard static source-vetting decisions |
| `danmaps/gis-agent-skills` | `7b53423036342d917392dd9d7bd350e33ecd3f59` | 21 | **21/21 matched** | Historical package-tree hashes and support counts preserved, **not independently reverified** | **0** static scores; identity and rights preflight only |

- [Aviation individual rubric ledger](../../registry/discovery/aviation-four-pinned-static-20261102.json) has each package's pin, exact SKILL blob, computed complete package-tree match, source license, triggers and nontriggers, 10 separate 0–2 dimension grades with rationale, capability mapping, authority/privacy findings, hard-fail flags and distinct security/behavioral NOT-RUN states.
- [GIS 21-path ledger](../../registry/discovery/gis-operations-21-identity-rights-20261102.csv) retains the source pin, original tree and supporting-file observations, confirmed exact SKILL blobs, alias relationship and unresolved rights. The GIS paths **must not be given scores** until complete packages and per-file rights are inspected.
- [Bounded source cursor and accounting](../../registry/discovery/aviation-gis-source-recovery-frontier-20261102.json) · [Capability-first candidate routes](../../registry/discovery/aviation-gis-capability-routes-20261102.json). These are discovery evidence links, not new approved directory candidates.

**Tree verification method:** for each aviation directory, the historical package tree claimed only `SKILL.md` (zero supporting blobs). The host independently computed the Git tree object from `100644 SKILL.md\0<20-byte Git blob id>`, hashed with Git's `tree <length>\0` prefix, and matched all four recorded tree SHAs. This verifies the exact single-file package contents at the archived tree identity, not current upstream freshness. GIS package trees were **not** reconstructed.

## Four aviation packages: individual static results

| Exact package | Grade | Static candidate disposition | Main limitation |
|---|---:|---|---|
| `aviation-ai-assurance` | **17/20** | REFERENCE-ONLY | Provisional EASA framework, safety-critical classification limits, and provider-supplied regulatory citations require current official verification |
| `aviation-data-story` | **18/20** | REFERENCE-ONLY | Dated Airside Labs observations are not live or representative of industry; provider data/quotation rights are separate from skill MIT |
| `aviation-identity-check` | **18/20** | REFERENCE-ONLY | Historical `as_of` logic is strong, but live provider data/schema and sensitive identifier-query egress remain unverified |
| `aviation-opportunity-map` | **14/20** | **REJECT unchanged** | Instructs external `report_unmet_need` submissions without action-specific approval, offers `submit_suggestion`, and lacks a bounded private-business-context egress gate; paid-key service calls also unqualified |

**Hard authority finding:** `aviation-opportunity-map` cannot be used unchanged to send suggestions or unmet-needs reports. A tool being keyless, accessible or rate-limited does **not** authorize communications. No external service was contacted in this review. All four require `mcp.airsidelabs.com/mcp` for their intended function; the connector and data were not behaviorally tested. The source `LICENSE` was fetched at the pin, blob `6e3ead51136b2ef64631d06fb7bbecb7d4d76306`, MIT copyright 2026 Airside Labs Ltd. No `NOTICE` file was located. That source license does not relicense proprietary MCP-served catalogue records, external data, EASA publications, provider trademarks or paid services. **Four static source-vetting decisions are not four governed exact-version reviews.**

## GIS: duplicate exposure and licensing conflict

- The archive has **21 raw paths**, **20** under `skills/*/SKILL.md` and one `.github/skills/agol-search/SKILL.md` agent-configuration path. Both `agol-search` entrypoints share the exact Git blob `484aee224b51aa0fb58abf30bc0ee89fcaa4df6b`, but their **package trees differ** (`52aabddc...` vs `1e8887d7...`) and the archive lists 0 vs 1 supporting file. Preserve the configuration alias, but do **not** call the two packages complete-package duplicates on blob identity alone.
- The pinned README calls the project **MIT** and advertises **19 GIS skills**; its `packs/public-core.yaml` at blob `708a04d2fc4e285dd377879f582bdc7b588d3a94` lists **20** `skills/*` entries, including `sample-qa-skill`. The README marketing count does not define eligible skill inventory. The 20 distinct source-skill entrypoints still require complete package inspection.
- **Rights blocker:** `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING`, `COPYING.md`, `NOTICE`, and `NOTICE.md` were not found at the pinned revision; the earlier source-license ledger correctly recorded `NOASSERTION` / `NO_ROOT_LICENSE_OBSERVED`. A README's one-word “MIT” assertion is useful evidence of intent but is not the complete permission and notice text needed for unchanged redistribution. Keep `HOLD_RIGHTS_AND_SECURITY` and **do not copy skill expressions** into `skillz` without resolving the actual grant and bundled asset terms.
- **Authority risk for future review:** `static-map` describes an execute mode and ArcGIS Online publication/replacement; `safety` describes production write receipts and approval. A checklist or `execute=true` parameter is not an action-specific host/user authorization. Other GIS procedures touch ArcPy exports, local files, shared geodatabases and ArcGIS Online services. Every complete package needs individual side-effect and credential checks.

## Accounting and integration boundary

These are **25 recovered path occurrences across two external discovery sources**, not additions to the **4,813 raw paths** of the four-source snapshot. The four aviation packages are complete, individually source-vetted, and source-role **discovered-only**; the 21 GIS paths have identity evidence only. **No global deduplicated eligible denominator** is established, no new `registry/verification/` governed record is claimed, and the governed total remains **1,039**.

**Why no five-surface public counter rewrite here:** README, SYSTEM_STATE, CURATION_QUEUE, INDEX and index.json already describe the separate four-source progress and are under active Claude integration. This bounded archival recovery does not change their source-snapshot denominator or approved corpus. The source cursor, individual ledger and capability route are committed together; a later source-admission or consolidated catalog tranche can reconcile the shared five surfaces atomically from latest main, without inventing extra reviewed skills or racing Claude.

## Next qualified actions

1. Resolve the GIS license grant and inspect all 20 complete source-skill package trees, supporting files, host dependencies, and authority gates; then grade the packages individually if rights and evidence permit.
2. Revalidate the aviation provider's terms and official current EASA references before any governed unchanged-use consideration; retain the four static dispositions and security/behavioral NOT-RUN.
3. Continue extracting **other unique source-family evidence** from held #590 without importing stale shared governance files or double-counting its 65-source raw path claims.

No Actions budget was intentionally consumed; verify commit-associated runs after integration. Historical PR #590 remains HOLD because its 123-file draft has unresolved overlapping accounting and rights evidence.
