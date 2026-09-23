# Skill Curation Queue

This is the living evidence ledger for ongoing `skillz` corpus curation. The repository is entirely passive; the external host agent performs curation under explicit repository-maintenance authority. Detailed exact-version evidence belongs in canonical companions under `registry/`; this ledger tracks source-family state, active frontiers, macro findings, and lifecycle priorities rather than duplicating every companion rationale.

## Current governed depth

- **44** first-party user-facing skills, **44/44** provenance-complete.
- **12** pinned upstream reference corpora under `skills/sources/`.
- **20** unique registered source identities.
- **625** persisted exact-version third-party verification companions.
- Broad **500+** first-party + pinned external reference surface.

Historical source-level review evidence remains broader than the one-file companion shelf for some completed corpora. Recover compatible prior evidence before fresh re-review.

## Curation and admission model

**discovery surface → candidate issue/source → source-vetting → exact-version static evaluation → decisive admission result → repository persistence when justified → user-fit decision**

New third-party discoveries use `docs/candidate-intake.md`. Discovery intelligence never substitutes for canonical upstream identity, license/terms, exact version, or individual quality evidence.

### Macro-first curation cycle

For an active finite source family, recompute the whole remaining frontier before selecting work: denominator, genuine gaps, duplicate/alias exposure, shared provenance/dependency facts, authority/privacy/evidence clusters, capability overlap, and omission defects. Prefer a coherent bounded tranche when quality permits instead of defaulting to one skill per lifecycle. Shared source facts may be reviewed efficiently together, but every eligible skill still gets an individual exact-version provenance/verification record and decisive disposition. Deep-review high-authority, privacy-sensitive, evidence-heavy, unusually differentiated, or ambiguous packages. Reconcile the five public accounting surfaces once per material tranche, never by lowering the quality bar to hit a batch quota.

## Mandatory provenance status

Issue #66 is the corpus-wide provenance-completeness audit. First-party is **44/44** complete. Enforcement is documentary/evidentiary through external-agent curation, never repository-owned scripts, CI, scanners, or runtime.

## Admitted-source curation

| Source family | Pin / scope | Reviewed | Gaps | State |
|---|---|---:|---:|---|
| Anthropic Skills | `9d2f1ae187231d8199c64b5b762e1bdf2244733d` | 17 / 17 | 0 | CURRENT-STANDARD COMPLETE |
| Anthropic Knowledge Work Plugins | `ca3e3fb2c4a1d3eea73fc003998faef6daa650b8` | 74 / 74 | 0 | CURRENT-STANDARD COMPLETE |
| AWS Agent Toolkit | `ff1481a7bc1a04ee00ebf63d3a8a149aa6a2c546` | 72 / 72 | 0 | CURRENT-STANDARD COMPLETE |
| Microsoft Skills | `32cad4ee689c95c309e61aeefcbc6af356f1e6a7` | 186 / 186 | 0 | CURRENT-STANDARD COMPLETE |
| Microsoft Azure Skills | `8f8c72bb9e22aee4366e07aadfd5766ef9add8f4` | 34 / 34 | 0 | CURRENT-STANDARD COMPLETE |
| Cole Medin Skills | `fb2e876f057c5356d6603ba0c52d6b4418d893ba` | 33 / 33 | 0 | CURRENT-STANDARD COMPLETE |
| David Ondrej Skills | `7d0ef87dad1f638cab58995eead9e0e6e3fae237` | 55 / 55 | 0 | CURRENT-STANDARD COMPLETE |
| **Corey Haines Marketing Skills** | `5b2c0007766c6a1cf1d53fd8fc73e979e0821022` | **33 / 50** | **17** | **TRACKED / ADMITTED** |
| Matt Pocock Skills | `6654f6b60cd9d5be8b54c6fafe44346dabeb3b76` | 29 / 29 | 0 | CURRENT-STANDARD COMPLETE |
| Cloudflare Skills | `f96bff754e428838818017f75817f0f9428acd48` | 13 / 13 | 0 | CURRENT-STANDARD COMPLETE |
| Addy Osmani Agent Skills | `f63ec56a3cc936408d792956ae583c3c96a825bd` | 24 / 24 | 0 | CURRENT-STANDARD COMPLETE |
| Vercel Agent Skills | `f8a72b9603728bb92a217a879b7e62e43ad76c81` | 9 / 9 | 0 | CURRENT-STANDARD COMPLETE |
| OpenHands Extensions | `87959a7da3e75445647e77b2fbf5bf5b66fb037b` | 1 / 1 | 0 | CURRENT-STANDARD COMPLETE |
| Google Agents CLI | `ef7808f33fc3038112b69d4ad488ce33b72699b1` | 7 / 7 | 0 | CURRENT-STANDARD COMPLETE |
| Cline Skills | `26378461e978f2b4e2e6d67b57121b86b2a79ba5` | 36 / 36 published | 0 | CURRENT-STANDARD COMPLETE |

Microsoft direct-package accounting remains `.NET` **29/29**, Java **26/26**, Python **40/40**, Rust **9/9**, and TypeScript **25/25**. David Ondrej sub-family accounting remains agent orchestration **17/17**, ops/setup **11/11**, research/web **10/10**, skill authoring **4/4**, and thinking/docs **13/13**.

### Corey Haines Marketing Skills — active frontier

- Pin: `5b2c0007766c6a1cf1d53fd8fc73e979e0821022` (upstream v2.11.1 state).
- Admitted through issue #297 as a **tracked corpus**, not blanket trusted inventory.
- Root license: **MIT**, copyright Corey Haines (2025).
- Exact eligible denominator: **50** top-level first-class `skills/<name>/SKILL.md` packages.
- Current provenance/verification companions: **33/50**; gaps **17**.
- Out of denominator: partner/integration guides, `tools/` CLI/integration material, source-owned scripts/workflows, generated partner surfaces, and ordinary reference Markdown nested beneath skill packages.
- Behavioral validation is `not-run` for all thirty-three reviewed units.

Reviewed through tranche 01: `ab-testing`, `ad-creative`, `ads`, `ai-seo`, `analytics`, `aso`, `attribution`, `churn-prevention`, `co-marketing`, `cold-email`, `community-marketing`, `competitor-profiling`, `competitors`, `content-strategy`, `copy-editing`, `copywriting`, `cro`, `customer-research`, `directory-submissions`, `emails`, `events`, `free-tools`, `image`, `influencer-marketing`, and `launch`.

Macro tranche 02 adds: `lead-magnets`, `marketing-council`, `marketing-ideas`, `marketing-loops`, `marketing-plan`, `marketing-psychology`, `offers`, and `onboarding`.

All eight tranche-02 packages are **rejected unchanged** while retained as adaptation/extraction/reference prior art. `marketing-plan` fails the authority hard rule because ordinary procedure includes persistent file creation and optional external API/data pulls without a distinct authorization boundary. The other seven are primarily advisory/planning artifacts and do not establish an authority hard fail, but unchanged adoption is rejected for combinations of unsupported or volatile claims, privacy/consent/minimization gaps, simulated-authority concerns, planning-to-execution boundary blur, and insufficient non-deception safeguards around persuasion, scarcity, urgency, profiling, or behavioral instrumentation. Individual scores, fingerprints, dependencies, controlled tags, freshness evidence, authority findings, and exact rationale remain canonical in `registry/skills/corey-haines-marketing-skills/` and `registry/verification/corey-haines-marketing-skills/`.

**Macro finding:** Corey Haines remains consistently stronger as planning/checklist/design prior art than as unchanged operational authority. Across the first thirty-three reviews, recurring defects are fragmented action authorization, weak privacy/minimization/consent/retention boundaries, unsupported or volatile quantitative marketing/platform claims, and incomplete safeguards around persuasive or dark-pattern-adjacent tactics. Upstream evals are intended-behavior evidence, never behavioral validation. The remaining seventeen should continue in coherent tranches with deeper review reserved for high-authority, privacy-sensitive, evidence-heavy, or ambiguous packages.

## Governed discovery / source-vetting

Discovery proceeds in parallel without displacing current-standard source maintenance. Current governed surfaces and candidates include the Creator Technical Resource Catalog, Hugging Face Skills, GitHub Awesome Copilot, Agent Skills Specification, creator-methodology sources, and bounded candidate work surfaced through current issues. Discovery intelligence never substitutes for canonical source identity, terms, exact-version evidence, or individual quality review.

`ConsultingFuture4200/unusual-thoughts` (#307) and `ConsultingFuture4200/repo-readme` (#308) were resolved **REFERENCE-ONLY** and closed after canonical repository review found no redistribution license/terms sufficient for governed corpus inclusion. Their useful public prior art may still inform discovery, but neither is vendored or promoted to governed corpus material unless canonical terms materially change.

## Lifecycle hygiene

At each run: inspect every open PR and issue; merge a current authorized ready PR; close evidence-complete/duplicate/superseded bounded issues; state concrete blockers; reconcile README, `docs/SYSTEM_STATE.md`, this ledger, `INDEX.md`, and `index.json` atomically after a material tranche; preserve the passive architecture.

## Historical authority boundary

Wayfinder #35 remains canonical destination/scope evidence, but stale frontier text is historical. Source queue #27, structure ticket #41, and PR #42 are closed historical evidence. Current README and Tier-1 governance control live execution.

## Next action

Continue the Corey Haines Marketing Skills admitted-source frontier from **33/50** reviewed and **17** gaps while issue #66 tracks corpus-wide provenance completeness. Recompute the whole remaining frontier first, choose a coherent tranche when quality permits, deep-review ambiguous/high-authority/privacy/evidence-sensitive units, preserve individual exact-version decisions, synthesize macro findings, and reconcile all five public accounting surfaces once per material tranche before merge.
