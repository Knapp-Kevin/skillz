# Skill Curation Queue

**Latest Microsoft candidate qualification (2026-10-28):** [Foundry root 220-file exact-version review](docs/reviews/2026-10-28-microsoft-foundry-root-220-file-exact-static.md) completes changed-existing **75/76 → 76/76**, leaving **0** static gaps. **220/220 distinct candidate blobs read, 1,299,560 bytes**; **REJECT unchanged 11/20** for mandatory installation, cloud/RBAC authority, sensitive trace and OAuth credential handling. Third-party companions **826**, total verification YAML **870**. July **186/186**, candidate denominator **208**, source pin and security/behavioral states unchanged.

This is the living evidence ledger for ongoing `skillz` corpus curation. The repository is entirely passive even during explicitly authorized maintenance. Detailed exact-version evidence belongs in canonical companions under `registry/`; any scanners or behavioral tests are run by the external host, not by repository-owned automation. This ledger tracks source-family state, active frontiers, macro findings, and lifecycle priorities rather than duplicating every companion rationale.

## Current governed depth

- **44** first-party user-facing skills, **44/44** provenance-complete.
- **12** pinned upstream reference corpora under `skills/sources/`.
- **22** unique registered source identities.
- **826** persisted exact-version third-party verification companions.
- Broad **500+** first-party + pinned external reference surface.

Historical source-level review evidence remains broader than the one-file companion shelf for some completed corpora. Recover compatible prior evidence before fresh re-review.

## Curation and admission model

**discovery surface → candidate issue/source → source-vetting → exact-version static evaluation → exact-version package-security scan → decisive admission result → repository persistence when justified → user-fit decision**

New third-party discoveries use `docs/candidate-intake.md`. Discovery intelligence never substitutes for canonical upstream identity, license/terms, exact version, or individual quality evidence.

### Macro-first curation cycle

For an active finite source family, recompute the whole remaining frontier before selecting work: denominator, genuine gaps, duplicate/alias exposure, shared provenance/dependency facts, authority/privacy/evidence clusters, capability overlap, and omission defects. Prefer a coherent bounded tranche when quality permits instead of defaulting to one skill per lifecycle. Shared source facts may be reviewed efficiently together, but every eligible skill still gets an individual exact-version provenance/verification record and decisive disposition. Deep-review high-authority, privacy-sensitive, evidence-heavy, unusually differentiated, or ambiguous packages. Reconcile the five public accounting surfaces once per material tranche, never by lowering the quality bar to hit a batch quota.

## Mandatory provenance status

The corpus-wide provenance-completeness audit #66 is **closed completed**. First-party is **44/44** complete and every source family explicitly represented as current-standard complete below has zero package gaps. Selectively tracked corpora remain bounded to the individual units actually admitted and are not silently counted as whole-family complete. Provenance and semantic completion remain documentary/evidentiary; package-security evidence may be established by an authorized external host using the registered pinned scanner, with only passive receipts persisted here.

The bounded controlled-taxonomy conformance audit #342 is also **closed completed**. Ongoing conformance is ordinary curation hygiene against `registry/taxonomy.yaml`; do not infer current defects from historical examples without live evidence.

## Current first-party authority repair

Current-main authority debt spans **10 distinct first-party manifests across three bounded findings**, without changing the 44-skill inventory. [#478](https://github.com/Knapp-Kevin/skillz/issues/478) covers five recurring-scan procedures and [#481](https://github.com/Knapp-Kevin/skillz/issues/481) covers four additional recurring review procedures. Their former drafts #480/#482, along with #416/#485, are **closed superseded, not merged**; all 29 distinct first-party repairs now share a 44-entry fingerprint-reconciled draft [#489](https://github.com/Knapp-Kevin/skillz/pull/489). One-time read-only review does not authorize durable schedules, future private-data access, delivery or retention. Final-version external package-security reports and independent executed adversarial acceptance are still missing.

[#483](https://github.com/Knapp-Kevin/skillz/issues/483) separately records two current security-review procedures (`mcp-vetting`, `permissions-review`) that refer to obsolete permission tiers/source-trust scoring. Draft #489 selects the newer corrected variants from #485 and #482, superseding the older #416 variants. Both remain **unmerged**; all 10 affected current-main manifests remain unchanged. No package-security or behavioral approval is inherited.

## Package-security backfill

**First-party historical security evidence (reconciled 2026-10-29).** At main `713c98fa55d5`, **44/44** package trees and semantic fingerprints matched their recorded identities. The retained October 10 baseline recorded **23 exact-tree PASSED / 20 INCOMPLETE / 1 FAILED**; a separate 44-pass candidate report matches only **23/44** of those package trees, so its other 21 passes cannot transfer. Three disjoint unmerged repair drafts now revise **36 distinct existing first-party skills**: [#489](https://github.com/Knapp-Kevin/skillz/pull/489) **29** (including 8 formerly passing), [#492](https://github.com/Knapp-Kevin/skillz/pull/492) **5** (all formerly passing), and [#496](https://github.com/Knapp-Kevin/skillz/pull/496) **2** (both formerly passing). If all three merge unchanged, **15** historical matching-pass package identities will have changed and only **8** historical matching-pass identities will remain unaffected. All **36 final changed package trees** require fresh pinned external security reports and independent executed adversarial acceptance. These are pending candidate identities, not merged or newly scanned packages. The 44 first-party / 826 third-party / 870 total semantic inventory is unchanged. No new scan, behavioral validation, or unchanged-use approval is claimed. [Full historical identity matrix](docs/reviews/2026-10-29-first-party-security-exact-tree-reconciliation.md).

Issue **#402** owns the bounded backfill introduced by the SkillSpector integration. Existing `verified` / `validated` records remain valid semantic evidence but do not inherit a security pass. Backfill priority is first-party, then semantically eligible third-party packages with executable components or consequential authority, then the remaining unchanged-use candidate surface. Security evidence is persisted under `registry/security/` and must bind to the exact package and exact scanner revision.

## Matt Pocock candidate freshness (unadmitted)

**Vercel deploy authority correction (2026-10-29).** Pinned Vercel Agent Skills remains **9/9 current-standard complete**, now **5 VERIFIED semantic only / 4 REJECT unchanged**. `deploy-to-vercel` at unchanged blob `a0251ce89a7636230be9c5b989a81e1a54a52a96` was reclassified from VERIFIED to REJECT unchanged: its automatic project linking, CLI installation, no-auth source upload, and broad git staging/push do not establish separate action-specific authority. Preserve the useful deployment decision tree for ADAPT/EXTRACT, not unchanged execution. No new security scan, behavioral pass, source-pin change, or inventory delta. [Exact review](docs/reviews/2026-10-29-vercel-deploy-authority-reclassification.md).

**Matt Pocock candidate freshness (2026-10-29).** Registered pin remains **29/29** at `6654f6b60cd9d5be8b54c6fafe44346dabeb3b76`. Candidate `a496f5513d4a4cf889bc48e189e579f4b0bdf6aa` has **31 eligible** manifests: 12 unchanged, 16 changed-existing, 3 newly eligible; one pinned package is **retired from candidate exposure only**, with old pinned reference retained. All **19/19 changed/new candidate-only static reviews** are decisive: **6 VERIFIED semantic only / 13 REJECT unchanged**, **0 static gaps**. Source-pin promotion **NO-GO** due authority hard fails and absent security/behavioral acceptance. Published inventory unchanged. [Initial ten](docs/reviews/2026-10-29-mattpocock-upstream-freshness-ten-exact-static.md) and [final nine](docs/reviews/2026-10-29-mattpocock-upstream-freshness-final-nine-exact-static.md).

**Matt Pocock pinned path hygiene (2026-10-29).** The registered 29-skill source remains unchanged at its exact pin. A live audit of 58 pinned provenance/verification companions found **25 stale provenance** and **11 stale verification** `local_path` values pointing at removed `vendor/mattpocock-skills/`. All 36 were corrected to `skills/sources/mattpocock-skills/`, without changing upstream identities, fingerprints, dispositions, scores, counts or security/behavioral states. [Exact-path audit](docs/reviews/2026-10-29-mattpocock-pinned-path-hygiene.md).

**Cline pinned path hygiene (2026-10-29).** Audited all **74** provenance/verification companions for **37** governed Cline records (36 published + one separately characterized internal). Found and corrected **7 stale provenance + 7 stale verification** `local_path` values from removed top-level `vendor/cline-skills/` to `skills/sources/cline-skills/`. The registered source gitlink and the nested `cline-sdk` upstream gitlink were checked against exact manifest fingerprints. **0 stale Cline companion paths remain**. No source pin, review disposition, score, security state, behavioral state, or inventory count changed. [Exact-path review](docs/reviews/2026-10-29-cline-pinned-path-hygiene.md).

## Admitted-source curation

| Source family | Pin / scope | Reviewed | Gaps | State |
|---|---|---:|---:|---|
| Anthropic Skills | `8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4` | 19 / 19 | 0 | CURRENT-STANDARD COMPLETE |
| Anthropic Knowledge Work Plugins | `ca3e3fb2c4a1d3eea73fc003998faef6daa650b8` | 74 / 74 | 0 | CURRENT-STANDARD COMPLETE |
| AWS Agent Toolkit | `ff1481a7bc1a04ee00ebf63d3a8a149aa6a2c546` | 72 / 72 | 0 | CURRENT-STANDARD COMPLETE |
| Microsoft Skills | `32cad4ee689c95c309e61aeefcbc6af356f1e6a7` | 186 / 186 | 0 | CURRENT-STANDARD COMPLETE |
| Microsoft Azure Skills | `8f8c72bb9e22aee4366e07aadfd5766ef9add8f4` | 34 / 34 | 0 | CURRENT-STANDARD COMPLETE |
| Cole Medin Skills | `fb2e876f057c5356d6603ba0c52d6b4418d893ba` | 33 / 33 | 0 | CURRENT-STANDARD COMPLETE |
| David Ondrej Skills | `7d0ef87dad1f638cab58995eead9e0e6e3fae237` | 55 / 55 | 0 | CURRENT-STANDARD COMPLETE |
| Corey Haines Marketing Skills | `5b2c0007766c6a1cf1d53fd8fc73e979e0821022` | **50 / 50** | **0** | **CURRENT-STANDARD COMPLETE** |
| Dan Dewhurst Story Skills | `b113a8298ae5deb37929a5b1d0cc1536d98a508c` | **23 / 23** | **0** | **CURRENT-STANDARD COMPLETE** |
| Matt Pocock Skills | `6654f6b60cd9d5be8b54c6fafe44346dabeb3b76` | 29 / 29 | 0 | CURRENT-STANDARD COMPLETE |
| Cloudflare Skills | `f96bff754e428838818017f75817f0f9428acd48` | 13 / 13 | 0 | CURRENT-STANDARD COMPLETE |
| Addy Osmani Agent Skills | `f63ec56a3cc936408d792956ae583c3c96a825bd` | 24 / 24 | 0 | CURRENT-STANDARD COMPLETE |
| Vercel Agent Skills | `f8a72b9603728bb92a217a879b7e62e43ad76c81` | 9 / 9 | 0 | CURRENT-STANDARD COMPLETE |
| OpenHands Extensions | `87959a7da3e75445647e77b2fbf5bf5b66fb037b` | 1 / 1 | 0 | CURRENT-STANDARD COMPLETE |
| Google Agents CLI | `ef7808f33fc3038112b69d4ad488ce33b72699b1` | 7 / 7 | 0 | CURRENT-STANDARD COMPLETE |
| Cline Skills | `26378461e978f2b4e2e6d67b57121b86b2a79ba5` | 36 / 36 published | 0 | CURRENT-STANDARD COMPLETE |

Microsoft direct-package accounting remains `.NET` **29/29**, Java **26/26**, Python **40/40**, Rust **9/9**, and TypeScript **25/25**. David Ondrej sub-family accounting remains agent orchestration **17/17**, ops/setup **11/11**, research/web **10/10**, skill authoring **4/4**, and thinking/docs **13/13**.

### Jwynia Agent Skills — fiction denominator complete

- Source pin: `e02ec7e226a6e4f8419fd3b88a1d8e472d421b32`.
- Source scope: **112** skills, including **57** creative/narrative skills; exact fiction denominator under #388: **54** first-class packages.
- Source role: **tracked-corpus**, selective individual curation only; not vendored and not blanket trusted.
- License state: **MIXED/per-skill**; no root `LICENSE` was found at the evaluated pin.
- Governed fiction units: **54 / 54**; remaining **0**.
- Current disposition: **39 VERIFIED**, **15 REJECTED unchanged**; behavioral validation `not-run` for all fifty-four.
- Tranche 1 under #388 added seven VERIFIED and four REJECTED unchanged core/craft/character units.
- Tranche 2 added nine VERIFIED structure units and rejected `reverse-outliner` unchanged at **12/20** because its semantic-looking analysis rests largely on regex/common-name/fixed-position heuristics with broad Deno runtime requirements.
- Tranche 3 added nine VERIFIED worldbuilding units and rejected `conlang` unchanged at **13/20** for unsupported cross-linguistic frequency/provenance claims.
- Final tranche VERIFIED `book-marketing` **15/20**, `dna-extraction` **15/20**, `flash-fiction` **16/20**, `interactive-fiction` **16/20**, `media-adaptation` **15/20**, `paradox-fables` **15/20**, and `table-tone` **16/20**.
- Final tranche REJECTED unchanged `adaptation-synthesis` **13/20**, `game-facilitator` **13/20**, `list-builder` **12/20**, `multi-order-evolution` **13/20**, `sensitivity-check` **13/20**, `shared-world` **14/20**, `sleep-story` **13/20**, and `chapter-drafter` **13/20**.
- Key Celestara finding: `shared-world`, `game-facilitator`, and `chapter-drafter` contain unusually valuable concepts but require adaptation because their unchanged runtime/authority/oracle behavior is not governable enough. `systemic-worldbuilding`, `interactive-fiction`, `table-tone`, and proposal-only `world-fates` provide strong governed reference behavior.
- `story-zoom` remains REJECTED unchanged because its persistent watcher lacks an action-appropriate authorization gate; its cross-level synchronization concept remains useful prior art.
- Source-owned scripts remain upstream evidence and never become repository-owned runtime.

### Dan Dewhurst Story Skills — completed frontier

- Pin: `b113a8298ae5deb37929a5b1d0cc1536d98a508c`.
- Root license: **MIT**, Copyright (c) 2026 Daniel Dewhurst.
- Exact eligible denominator: **23** first-class `skills/<name>/SKILL.md` packages.
- Current provenance/verification companions: **23/23**; gaps **0**.
- All 23 are **VERIFIED semantic exact-version references**, with static rubric scores **16/20–18/20**. New unchanged-reuse eligibility additionally depends on package-security backfill under #402.
- Behavioral validation is `not-run` for all 23; upstream tests/evals remain source evidence only.
- Main portability caveat: the corpus assumes the upstream Markdown/YAML Story Skills project schema and often an optional upstream `story` CLI.
- `story-maintenance` packages a local Node fallback with explicit validate/reindex/rename/move/remove/repair operations. That runtime remains upstream-only and is not adopted by `skillz`.
- Submission/publishing/editorial procedures prepare artifacts and plans but leave actual sending, uploads, purchases, contracts, account operations, pushes, and publication to the author.

Individual fingerprints, package trees, freshness evidence, dependencies, controlled tags, authority findings, and exact rationale live in `registry/skills/danjdewhurst-story-skills/` and `registry/verification/danjdewhurst-story-skills/`.

### Corey Haines Marketing Skills — completed frontier

- Pin: `5b2c0007766c6a1cf1d53fd8fc73e979e0821022` (upstream v2.11.1 state).
- Admitted through issue #297 as a **tracked corpus**, not blanket trusted inventory.
- Root license: **MIT**, copyright Corey Haines (2025).
- Exact eligible denominator: **50** top-level first-class `skills/<name>/SKILL.md` packages.
- Current provenance/verification companions: **50/50**; gaps **0**.
- Out of denominator: partner/integration guides, `tools/` CLI/integration material, source-owned scripts/workflows, generated partner surfaces, and ordinary reference Markdown nested beneath skill packages.
- Behavioral validation is `not-run` for reviewed units unless a companion explicitly records otherwise.

Final macro tranche: `revops` **13/20 REJECTED unchanged**, `sales-enablement` **17/20 VERIFIED**, `schema` **17/20 VERIFIED**, `seo-audit` **17/20 VERIFIED**, `signup` **15/20 REJECTED unchanged**, `site-architecture` **17/20 VERIFIED**, `sms` **13/20 REJECTED unchanged**, `social` **14/20 REJECTED unchanged**, and `video` **13/20 REJECTED unchanged**. `VERIFIED` denotes successful exact-version static semantic review, not behavioral validation or automatic unchanged-use eligibility.

**Macro finding:** across all fifty reviews, Corey Haines is consistently stronger as planning/checklist/design prior art than as unchanged operational authority, while still containing meaningful bounded semantic candidates for unchanged use pending applicable package-security evidence. Recurring defects are fragmented action authorization, weak privacy/minimization/consent/retention boundaries, unsupported or volatile quantitative marketing/platform claims, and incomplete safeguards around persuasive or external-action workflows. Upstream evals are intended-behavior evidence, never behavioral validation.

Individual fingerprints, dependencies, controlled tags, freshness evidence, authority findings, and exact rationale remain canonical in `registry/skills/corey-haines-marketing-skills/` and `registry/verification/corey-haines-marketing-skills/`.

**Candidate full-package static reviews (2026-10-28):** New/ungoverned candidates **26/26** fully reviewed (4 VERIFIED semantic only, 22 REJECT unchanged); changed-existing **76/76** fully reviewed (**70 REJECT unchanged, 6 VERIFIED semantic only**). Candidate current-version static frontier **102/102 complete**, **0** gaps. Latest [Foundry root 220-file review](docs/reviews/2026-10-28-microsoft-foundry-root-220-file-exact-static.md) adds one REJECT unchanged companion (11/20), all 220 distinct source blobs read. Third-party companions **826**, total YAML **870**. July pin **186/186**, candidate denominator **208**, no security scan, behavioral validation, source admission or pin movement.

**Changed-existing Rust qualification (2026-10-28):** [Eight complete single-file Rust reviews](docs/reviews/2026-10-28-microsoft-rust-eight-changed-exact-static.md) finished **8/76** changed-existing Microsoft candidates, leaving **68**. All eight are **REJECT unchanged** (8–11/20) for authorization and sensitive-data failures; Key Vault Keys also contains a four-byte DEK example. Exact candidate provenance and static verification are recorded; security and behavioral states `not-run`. Third-party companions **758 at this Rust checkpoint**. Registered July **186/186** and source pin unchanged.

**Changed-existing Python Azure AI qualification (2026-10-28):** [Eight complete three-file exact-version reviews](docs/reviews/2026-10-28-microsoft-python-ai-multimodal-eight-exact-static.md) finished **16/76** changed-existing Microsoft candidates, leaving **60** (29 Python, 30 Azure operations, one skill-creator). All eight are **REJECT unchanged** (9–13/20) for unapproved external data transmission, persistent service effects and privacy/retention failures; document translation also exposes SAS-bearing URL patterns. Exact provenance, all 24 blob identities and individual semantic dispositions are recorded. Security and behavioral states remain `not-run`; third-party companions **766**, total verification YAML **810** (44 first-party + 766 third-party). Registered July **186/186** and source pin unchanged.
**Changed-existing Python data/storage/events qualification (2026-10-28):** [Eight complete three-file exact-version static reviews](docs/reviews/2026-10-28-microsoft-python-data-storage-events-eight-exact-static.md) advance **16/76 → 24/76** changed-existing Microsoft packages, leaving **52** (21 Python, 30 Azure operations, one skill-creator). All eight are **REJECT unchanged** (10–12/20) for unapproved production mutations, tenant/sensitive-data disclosure, destructive storage/queue effects and event publication. All 24 exact blobs and individual companions are recorded. Security and behavioral states remain `not-run`; third-party verification companions **774**, total verification YAML **818** (44 first-party + 774 third-party). Registered July **186/186** and source pin unchanged.

**Changed-existing Python identity/telemetry qualification (2026-10-28):** [Six complete three-file exact-version static reviews](docs/reviews/2026-10-28-microsoft-python-identity-telemetry-six-exact-static.md) advance **24/76 → 30/76**, leaving **46** (15 Python, 30 Azure operations, one skill-creator). All six are **REJECT unchanged** (10–12/20) for authority/privacy hard fails. All 18 source blobs and individual companions are recorded. Security and behavioral states `not-run`; third-party companions **780**, total YAML verification **824**. July pin **186/186** unchanged.

**Changed-existing Python services/management qualification (2026-10-28):** [Eight complete exact-version static reviews](docs/reviews/2026-10-28-microsoft-python-services-management-eight-exact-static.md) advance **30/76 → 38/76**, leaving **38** (7 Python, 30 Azure operations, one skill-creator). Deep nine-file Cosmos service-layer review plus seven management/messaging/agent packages; **29 source blobs**, eight individual provenance/verification pairs, all **REJECT unchanged** (10–12/20) for authorization, credential/PII disclosure, destructive resource changes and billable capacity operations. Cosmos additionally has a potential untrusted SQL-fragment sink and substring-based emulator TLS bypass. Security and behavioral states remain `not-run`; third-party companions **788**, total YAML verification **832**. July pin **186/186** unchanged.

**Changed-existing Python final seven qualification (2026-10-28):** [Seven complete exact-version package reviews](docs/reviews/2026-10-28-microsoft-python-final-seven-exact-static.md) advance **38/76 → 45/76**, leaving **31** (30 Azure operations, one skill-creator); Python changed-existing **37/37** complete. **32 source blobs**, seven individual provenance/verification pairs, **six REJECT unchanged (10–11/20)** for cloud agent/ML/data/audio authority or FastAPI resource-ownership failures and **one Pydantic VERIFIED semantic only (17/20)**. All package-security and behavioral states remain `not-run`; third-party companions **795**, total verification YAML **839**. Registered July **186/186** and source pin unchanged.

**Changed-existing Azure operations qualification (2026-10-28):** [Eight complete exact-version static reviews](docs/reviews/2026-10-28-microsoft-azure-ops-discovery-eight-exact-static.md) advance **45/76 → 53/76**, leaving **23** (22 Azure operations, one skill-creator). **56 exact source blobs**, eight individual provenance/verification pairs, **two VERIFIED semantic only (16/20)** for bounded resource lookup/visualization and **six REJECT unchanged (10–12/20)** for live remediation, sensitive-data disclosure, quota/storage mutation, credential access and telemetry. Security and behavioral states `not-run`; third-party companions **803**, total YAML **847**. Registered July **186/186** and source pin unchanged.

**Changed-existing Azure AI/gateway/deployment qualification (2026-10-28):** [Five complete exact-version static reviews](docs/reviews/2026-10-28-microsoft-azure-ai-deployment-five-exact-static.md) advance **53/76 → 58/76**, leaving **18** (17 Azure operations, one skill-creator). **63 package-file exposures (60 distinct blobs)**, five individual provenance/verification pairs, **five REJECT unchanged** (9–13/20) for APIM key/RBAC changes, private AI data transmission, AKS token TEMP files, unapproved billable App Service creation and storage connection-string disclosure. Security and behavioral states `not-run`; third-party companions **808**, total YAML **852**. July pin **186/186** unchanged.

**Changed-existing Foundry deployment qualification (2026-10-28):** [Four exact-version parent/nested reviews](docs/reviews/2026-10-28-microsoft-foundry-deploy-four-exact-static.md) advance **62/76 → 66/76**, leaving **10** (eight large Azure operations, Foundry root and finetuning). **30 file exposures / 17 distinct blobs**, four provenance/verification pairs, **two VERIFIED semantic only** (router/customize, 16/20) and **two REJECT unchanged** (capacity 11/20, preset 10/20). Security/behavioral `not-run`; third-party **816**, total YAML **860**. July **186/186** and source pin unchanged.

**Changed-existing Azure infrastructure/migration qualification (2026-10-28):** [Three complete exact-version static reviews](docs/reviews/2026-10-28-microsoft-azure-infra-migration-three-exact-static.md) advance **66/76 → 69/76**, leaving **7**. Azure operations **20/30 → 23/30**; **113 distinct source blobs**, three individual provenance/verification pairs, all REJECT unchanged (Compute 11/20, Cloud Migrate 11/20, Enterprise Infra Planner 15/20). Third-party **819**, total YAML **863**. Security and behavioral not-run; July pin and 208 denominator unchanged.

**Changed-existing Azure Deploy/Foundry Finetuning qualification (2026-10-28):** [Two complete exact-version static reviews](docs/reviews/2026-10-28-microsoft-azure-deploy-foundry-finetuning-two-exact-static.md) advance **69/76 → 71/76**, leaving **5**. Azure operations **23/30 → 24/30**; **75 distinct source blobs**, two provenance/verification pairs, both REJECT unchanged (12/20) for action authorization, billable operations, sensitive training data and CLI credentials. Third-party **821**, total YAML **865**. Security and behavioral not-run; July pin and 208 denominator unchanged.

## Microsoft freshness reconciliation: static frontier closed (issue #400, 2026-10-28)

Registered July remains **186/186** at its own pin. The [canonical denominator review](docs/reviews/2026-10-27-microsoft-canonical-denominator-and-ungoverned-exposures.md) establishes **208 structurally eligible packages** at `61fe0305ea70389ed8705eec6026a786f57865cf`: 106 carry-forwards + 76 changed + 26 new/ungoverned. Changed screening **76/76** is not requalification. **26/26 new candidates** now have full static companions (4 VERIFIED semantic only / 22 REJECT unchanged), with **76/76 changed-existing** full current-version reviews complete (0 gaps). All four removed-path candidate retirement/no-proven-successor decisions are [recorded](docs/reviews/2026-10-27-microsoft-four-removed-path-candidate-retirements.md); July pin evidence remains unchanged. No admission, pin, security or behavioral promotion; PRs #412/#413/#489 remain external qualification holds.

**Microsoft candidate pin decision (2026-10-28): NO-GO for promotion.** [Decision record](docs/reviews/2026-10-28-microsoft-candidate-pin-no-go-decision.md) closes the bounded 102/102 static-review frontier without changing the registered July source pin. Of 102 changed/new packages, **10 are VERIFIED semantic only** and **92 are REJECT unchanged**; none has qualifying candidate-version package-security or behavioral evidence. Four removed paths have candidate-only dispositions. The 106 exact-tree carry-forwards preserve their existing evidence, not inherited new-version security approval. Re-entry requires scoped external exact-package security evidence, independent acceptance, and a fresh explicit pin decision. Counts stay **44 first-party / 826 third-party / 870 total**, candidate denominator **208**, July **186/186**.

## Governed discovery / source-vetting

Discovery proceeds in parallel without displacing current-standard source maintenance. Current governed surfaces and candidates include the Creator Technical Resource Catalog, Hugging Face Skills, GitHub Awesome Copilot, Agent Skills Specification, creator-methodology sources, and bounded candidate work surfaced through current issues. Discovery intelligence never substitutes for canonical source identity, terms, exact-version evidence, or individual quality review.

`jwynia/agent-skills` is an admitted **tracked corpus for selective curation**, with the exact **54/54 fiction denominator complete** at the registered snapshot. Missing root licensing still prevents blanket source-wide license inference outside the individually governed packages.

`danjdewhurst/story-skills` is an admitted **tracked corpus with a complete 23/23 exact-version review** at the registered snapshot. Its source-owned runtime remains upstream-only.

`ConsultingFuture4200/unusual-thoughts` (#307) and `ConsultingFuture4200/repo-readme` (#308) were resolved **REFERENCE-ONLY** and closed after canonical repository review found no redistribution license/terms sufficient for governed corpus inclusion.

## Lifecycle hygiene

At each run: inspect every open PR and issue; merge a current authorized ready PR; close evidence-complete/duplicate/superseded bounded issues; state concrete blockers; reconcile README, `docs/SYSTEM_STATE.md`, this ledger, `INDEX.md`, and `index.json` atomically after a material tranche; preserve the entirely passive architecture.

## Historical authority boundary

Wayfinder #35 remains canonical destination/scope evidence, but stale frontier text is historical. Source queue #27, structure ticket #41, PR #42, completed provenance audit #66, and completed taxonomy audit #342 are historical evidence. Current README and Tier-1 governance control live execution.

## Next action

The admitted corpus has no known current-standard gaps in the explicitly complete families, and the narrative capability program is complete. Continue with source freshness and high-salience omission detection, bounded candidate/source evaluation, lifecycle hygiene, and selective behavioral/adversarial evidence produced only by authorized external environments. Preserve decisive prior evidence and do not invent repository runtime or architecture to keep the queue busy.
