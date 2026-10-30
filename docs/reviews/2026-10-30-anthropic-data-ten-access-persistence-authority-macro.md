# Anthropic Knowledge Work Plugins: data-access and persistence authority macro review

Date: 2026-10-30. Source: `anthropics/knowledge-work-plugins`, registered Apache-2.0 pin `ca3e3fb2c4a1d3eea73fc003998faef6daa650b8`. This is a **ten-package exact-version static recheck**, not a new source admission or executed security/behavioral qualification.

## Whole-family map and bounded tranche

The admitted, separately governed denominator remains **74/74** first-class skills, with 74 existing provenance and 74 verification companions and **zero static gaps**. Pinned source identity and upstream package trees were compared against the current companions. The source contains additional non-governed nested/partner exposure paths that do not automatically enlarge the 74-skill admitted denominator. The data sub-family has ten individually governed skills, all already reviewed; no new eligible identity or duplicate package is added.

| Data skill | Pinned SKILL.md blob | Current disposition | Rationale |
|---|---|---|---|
| `analyze` | `31ce9c58dd4de3038643750373de5b71a2494fa2` | **VERIFIED 18 → REJECT 14/20** | Connected warehouse SQL executes without approved private-data/query-cost scope |
| `build-dashboard` | `030c8aad751c289898cef092a67d340712ecccb9` | REJECT 12/20 retained | Offline/CDN contradiction; shareable HTML embeds sensitive query results |
| `create-viz` | `54840e6742d5bf4adf27f8fef02c6dc4dd7d76c0` | **VERIFIED 17 → REJECT 14/20** | Auto-query and persistent PNG output without scope, cost and destination approval |
| `data-context-extractor` | `1e065695c4f896f542c641ebeac3a80ccad952b6` | **VERIFIED 18 → REJECT 13/20** | Broad schema reads and company-sensitive persistent skill/ZIP generation lack scope and content approval |
| `data-visualization` | `409cce60f59b463a8386c83cde03dc7e70be93f3` | VERIFIED 18/20 retained | Advisory chart selection/uncertainty and accessibility methods |
| `explore-data` | `f1e7032d0abee77903fc3abbfdc7646e383d4993` | **VERIFIED 16 → REJECT 13/20** | All-column live profiling can disclose rare/identity-bearing values and incur unbounded query costs |
| `sql-queries` | `f92e232c67054b078fcc1ee558101163ebdbb87d` | VERIFIED 16/20 retained | Generate-only SQL reference; no autonomous execution authorized |
| `statistical-analysis` | `59cc87de24a0c1b2b5b1d7ba2d8d10eb314a6557` | REJECT 13/20 retained | Overgeneralized statistical defaults and significance interpretation |
| `validate-data` | `30a1bac41bf9679dc7d96b7ec59a116f03ec0575` | VERIFIED 18/20 retained | Pre-delivery QA of supplied analyses, not automatic source-system access |
| `write-query` | `ae8333dd4ea9c8baafc242ad8410c1823cbdf792` | VERIFIED 16/20 retained | Schema-aware drafting; execution is offered, not automatically performed |

## Individual corrected package identity and hard-fail authority evidence

1. **`analyze`**: `data/skills/analyze/` tree `7572805313d85c22d2d0a3e25101fdb1ed187af2`. The connected-warehouse path says explore schema, write SQL, execute, retrieve, debug/retry, then present raw query evidence. No separate account, table, column, time, query-budget or sensitive-output boundary. A request for a metric is not blanket approval for unrestricted warehouse exploration.
2. **`create-viz`**: `data/skills/create-viz/` tree `a1d964650cb9d2439af30254e88d45ad494ec05d`. It directly executes a connected warehouse query and saves a PNG in the current directory. Neither query scope/cost nor destination/retention is approved separately. Ordinary pasted-data visualization remains useful.
3. **`data-context-extractor`**: `data/skills/data-context-extractor/` tree `63e9e6585eed590b6af3ee98665500dd5664beba`. It enumerates schemas, extracts company-specific identifiers/metrics and writes a durable skill plus ZIP without an explicit host destination and sensitivity review. Its **upstream-owned** `scripts/package_data_skill.py` recursively packages non-hidden files under the generated skill and defaults output to cwd. The script and four bundled references are preserved intact as source evidence, never recast as repository-owned execution.
4. **`explore-data`**: `data/skills/explore-data/` tree `bee4c8c0603859fd60c3622dd41e7a093476fcbf`. Its default live profile queries every column's common and rare values, including text fields. No PII/identity exclusions, safe aggregation threshold, bounded time/row scope, or warehouse cost approval precedes the reads. A generated summary can itself disclose sensitive data.

Every corrected exact-version companion now records individual source/fingerprint, source-level dependencies, controlled authority tags, score/rationale and explicit `validation_status: not-run`. Scores do not override an action-authorization hard fail. No actual private-data exposure or unauthorized execution was observed.

## Macro synthesis and retained value

The key systemic defect is **connected tool availability being mistaken for read authority**. The data family has three different risk clusters: (a) broad warehouse query/financial cost, (b) rare-value and identity-bearing data exposure, and (c) persistent derivative artifacts that carry private company schema and business definitions. `analyze` overlaps `write-query` for SQL drafting, `explore-data` overlaps `validate-data` for quality checks, and `create-viz` overlaps `data-visualization` for presentation. These are complementary mechanisms, not a reason to create a new skill or source. Prefer ADAPT/EXTRACT/CHECKLIST with minimum-necessary scope, privacy-safe aggregation, cost limits and destination approval. Four simpler advisory/generate-only verified procedures retain their existing static status.

After this tranche: Anthropic Knowledge Work Plugins **74/74**, **30 VERIFIED semantic only / 44 REJECT unchanged**, zero gaps. Denominator delta **0**. Corpus accounting **44 first-party / 867 third-party persisted reviews / 911 total** unchanged. No source pin, license, package bytes, external scanner, behavioral validation, first-party skill, or repository-owned runtime changed.

Open first-party repair PRs #489/#492/#496 remain blocked on 36 complete pinned SkillSpector final-tree reports and independently executed adversarial acceptance; admissions #412/#413 have separate holds. This tranche touches none of those PRs' manifests or the shared first-party registry. Current Tier-1 governance and Wayfinder #35 control; historical #27/#41/#42 do not reinstate execution machinery.
