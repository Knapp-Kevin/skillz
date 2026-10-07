# System State

## Snapshot

| Attribute | Value |
|---|---|
| **Last updated** | 2026-10-06 |
| **Milestone** | Runtime-passive architecture + maintainer security gate |
| **State** | Governed curation mode |
| **Repository type** | Runtime-passive, maintenance-active skill knowledge resource |
| **Reference surface** | 500+ first-party + pinned external skill/reference artifacts |
| **First-party skills** | 44 |
| **First-party provenance complete** | 44 / 44 |
| **Persisted third-party review companions** | **721** |
| **Pinned external corpora** | 12 |
| **Registered source identities** | 22 |
| **Jwynia Agent Skills selectively reviewed units** | **54 / 54 fiction** |
| **Dan Dewhurst Story Skills current-standard companions** | **23 / 23** |
| **Dan Dewhurst Story Skills current-standard gaps** | **0** |
| **Corey Haines Marketing Skills tracked denominator** | 50 |
| **Corey Haines Marketing Skills current-standard companions** | **50 / 50** |
| **Corey Haines Marketing Skills current-standard gaps** | **0** |
| **Evaluation model** | Static semantic review + separate exact-version package-security evidence; optional later external behavioral evidence |
| **Normal-use runtime/CI requirement** | None |
| **Maintenance security automation** | Pinned NVIDIA SkillSpector static gate; no scheduled full-corpus scan |

## Current architecture

The canonical boundary is stable: user-facing material lives under `skills/`; intact pinned upstream corpora live under `skills/sources/<source-id>/`; passive repository-use/curation procedures live under `engine/skills/` and are excluded from user-facing counts; provenance, semantic verification, security evidence, and exact-version tool identity live under `registry/`.

`skillz` owns no **normal-use** runtime, installer, scheduler, monitor, crawler, synchronizer, background service, vector database, autonomous observer, or personalization service. Explicit repository maintenance may use bounded CI/scanner/test tooling to establish corpus evidence. The current security gate invokes exact-pinned NVIDIA SkillSpector externally; it does not become user-facing runtime. Tooling inside pinned third-party repositories remains upstream package material.

Normal DIRECT_LIBRARY, FIRST_VISIT, and RETURNING_USER work treats this repository as read-only reference material. User-derived skills target the user's active host/environment or a portable handoff. Only explicit REPOSITORY_MAINTENANCE authority permits repository mutation.

## Current admitted-source accounting

| Source family | Reviewed / denominator | Gaps |
|---|---:|---:|
| Anthropic Skills | 19 / 19 | 0 |
| Anthropic Knowledge Work Plugins | 74 / 74 | 0 |
| AWS Agent Toolkit | 72 / 72 | 0 |
| Microsoft Skills | 186 / 186 | 0 |
| Microsoft Azure Skills | 34 / 34 | 0 |
| Cole Medin Skills | 33 / 33 | 0 |
| David Ondrej Skills | 55 / 55 | 0 |
| **Corey Haines Marketing Skills** | **50 / 50** | **0** |
| **Dan Dewhurst Story Skills** | **23 / 23** | **0** |
| Matt Pocock Skills | 29 / 29 | 0 |
| Cloudflare Skills | 13 / 13 | 0 |
| Addy Osmani Agent Skills | 24 / 24 | 0 |
| Vercel Agent Skills | 9 / 9 | 0 |
| OpenHands Extensions | 1 / 1 | 0 |
| Google Agents CLI | 7 / 7 | 0 |
| Cline Skills (published) | 36 / 36 | 0 |

Microsoft direct-package accounting remains `.NET` **29/29**, Java **26/26**, Python **40/40**, Rust **9/9**, and TypeScript **25/25**.

Completion means decisive current evidence for every eligible package in the explicitly complete families above, not universal approval. Selectively tracked corpora may intentionally have only bounded individually governed units. Rejected and retired material remains useful bounded prior art.

## Jwynia Agent Skills — fiction denominator complete

Registered snapshot: `e02ec7e226a6e4f8419fd3b88a1d8e472d421b32`. Source scope: 112 skills, including 57 creative/narrative skills. Source-wide license state is **MIXED/per-skill** because no root `LICENSE` was found at the evaluated revision; individual declarations control.

The exact fiction denominator is now **54/54 governed**: **39 VERIFIED** exact-version static references and **15 REJECTED unchanged** references retained as bounded prior art. Behavioral validation remains `not-run` for all fifty-four. The four review phases under #388 covered core/craft/character, structure, worldbuilding, and application/orchestrator packages without inheriting trust between siblings.

The final application/orchestrator phase VERIFIED `book-marketing` (15/20), `dna-extraction` (15/20), `flash-fiction` (16/20), `interactive-fiction` (16/20), `media-adaptation` (15/20), `paradox-fables` (15/20), and `table-tone` (16/20). It REJECTED unchanged `adaptation-synthesis` (13/20), `game-facilitator` (13/20), `list-builder` (12/20), `multi-order-evolution` (13/20), `sensitivity-check` (13/20), `shared-world` (14/20), `sleep-story` (13/20), and `chapter-drafter` (13/20).

**Celestara synthesis finding:** the unchanged disposition is not the same as compositional value. `shared-world` contributes the strongest explicit canon-state/source/role/conflict model but its helper can establish canon without authority. `game-facilitator` contributes high-value player-agency/session practice but auto-promotes improvised facts to canon. `chapter-drafter` contributes valuable orchestration but uses arbitrary weighted literary thresholds as an autonomous acceptance oracle. Those three should be adapted, not imported. Verified `systemic-worldbuilding`, `interactive-fiction`, `table-tone`, and proposal-only `world-fates` provide stronger governed references for causal consequence, player-driven narrative, table experience, and long-range state.

The source remains tracked rather than vendored or blanket trusted. Source-owned scripts remain upstream package evidence and do not become repository-owned runtime. Exact fingerprints, dependencies, tags, authority findings, semantic scenarios, and rationale live in the canonical Jwynia provenance/verification companions and issue #388.

## Dan Dewhurst Story Skills — current-standard complete

Registered snapshot: `b113a8298ae5deb37929a5b1d0cc1536d98a508c`. Root license: MIT, Copyright (c) 2026 Daniel Dewhurst. Exact eligible denominator: **23** first-class packages under `skills/`.

All 23 packages now have exact-version provenance and verification companions and are **VERIFIED unchanged references** after complete package review, with static rubric scores ranging from **16/20 to 18/20**. Behavioral validation remains `not-run` for all 23. Source-authored tests/evals are upstream evidence, not claimed as repository behavioral validation.

**Family synthesis:** Dewhurst provides a coherent end-to-end fiction workflow spanning premise, project initialization, character/world/plot/theme/genre design, research, drafting, scene/voice/verse craft, line editing, continuity, simulated readers, feedback/editorial review, submission, publishing, adaptation, and maintenance. Its main limitation is portability: most units assume the upstream Markdown/YAML Story Skills schema and optional `story` CLI. `story-maintenance` additionally packages a local Node fallback with explicit rename/move/remove/repair operations. These runtime assets remain upstream dependencies and are not adopted as `skillz` runtime. Submission/publishing/editorial procedures keep external sending, contracts, purchases, account actions, uploads, pushes, and publication under author control.

Exact fingerprints, package trees, dependencies, freshness evidence, controlled tags, rubric detail, and rationale live under `registry/skills/danjdewhurst-story-skills/` and `registry/verification/danjdewhurst-story-skills/`.

## Corey Haines Marketing Skills — current-standard complete

Registered snapshot: `5b2c0007766c6a1cf1d53fd8fc73e979e0821022`. Root license: MIT. Exact eligible denominator: **50** top-level first-class `skills/<name>/SKILL.md` packages. Partner/integration guides, source-owned tooling, generated partner surfaces, and ordinary reference Markdown are outside the denominator.

All fifty packages now have current-standard provenance and exact-version verification companions. The final macro tranche adds `revops` **13/20 REJECTED unchanged**, `sales-enablement` **17/20 VERIFIED**, `schema` **17/20 VERIFIED**, `seo-audit` **17/20 VERIFIED**, `signup` **15/20 REJECTED unchanged**, `site-architecture` **17/20 VERIFIED**, `sms` **13/20 REJECTED unchanged**, `social` **14/20 REJECTED unchanged**, and `video` **13/20 REJECTED unchanged**. `VERIFIED` means exact-version structured static semantic review, not behavioral validation or automatic unchanged-use eligibility. Behavioral validation remains `not-run`.

**Macro synthesis:** Corey Haines is materially stronger as planning/checklist/design prior art than as unchanged operational authority, but the family contains meaningful bounded unchanged-use candidates. Recurring defects cluster around fragmented action authorization, privacy/minimization/consent/retention, unsupported or volatile quantitative marketing/platform claims, and incomplete safeguards around persuasive or external-action workflows. `seo-audit` is notable for an explicit untrusted-content boundary; `site-architecture` remains generate-only. `revops`, `sms`, `social`, and `video` cross into consequential external-action surfaces and require stronger authority boundaries; `signup` needs stronger identity/tracking/data-inference boundaries.

Exact fingerprints, package boundaries, dependencies, controlled tags, freshness evidence, authority findings, scores, and detailed rationale live in the canonical companions under `registry/skills/corey-haines-marketing-skills/` and `registry/verification/corey-haines-marketing-skills/`.

## Provenance and quality state

The corpus-wide provenance-completeness audit #66 is **closed completed**. First-party is **44/44 provenance-complete**, and every explicitly current-standard-complete third-party family in public accounting has zero package gaps. Selective tracked corpora remain bounded by the individual units actually admitted; they are not counted as whole-family complete. Every governed third-party unit must continue to retain truthful provenance and exact-version verification evidence; unknown facts remain unknown rather than inferred.

Static verification is not package-security validation or behavioral validation. `verified` means the exact bound material passed structured semantic review. `validated` requires representative external behavioral/adversarial evidence that actually exists. Package-security state is separate under `docs/security-scanning.md`; no historical record inherits a security pass merely because it is `verified`. `rejected` and `retired` remain prior art but are excluded from normal unchanged selection.

The authority hard fail remains controlling: procedures that can mutate or materially affect infrastructure, external state, production traffic, money-bearing resources, credentials, subscriptions, DNS/routing, security controls, user communications, notifications, identity/access, persistent cloud resources, destructive lifecycle state, or sensitive-data disclosure require a real authorization boundary appropriate to the action.

The bounded controlled-taxonomy conformance audit #342 is **closed completed**. Ongoing conformance is ordinary curation hygiene against `registry/taxonomy.yaml`; historical examples and audit comments remain evidence only and do not establish current defects without live verification.

## Discovery and source vetting

Discovery runs in parallel with admitted-source maintenance but never grants quality, trust, installation authority, redistribution rights, or automatic admission. New third-party discoveries use the issue-first lifecycle in `docs/candidate-intake.md`.

Current governed discovery surfaces include the Creator Technical Resource Catalog, Hugging Face Skills, GitHub Awesome Copilot, Agent Skills Specification, canonical creator/source repositories, and candidate work recorded in the living curation ledger. Restricted or unclear-license material remains reference-only unless terms justify another role.

`jwynia/agent-skills` was admitted through issue #382 as a tracked corpus for selective individual curation. The source's missing root license prevents blanket license inference; per-skill declarations remain controlling. Its exact 54-package fiction denominator is complete under #388.

`danjdewhurst/story-skills` was admitted through issue #387 as a tracked corpus after a complete 23-package exact-version review. Source-owned Story Skills runtime remains upstream-only.

`ConsultingFuture4200/unusual-thoughts` (#307) and `ConsultingFuture4200/repo-readme` (#308) are closed REFERENCE-ONLY candidates because canonical redistribution terms sufficient for governed corpus inclusion were not established.

## Current authority and lifecycle surfaces

- Wayfinder #35 remains canonical destination/scope evidence. Its stale frontier text is historical.
- Source queue #27, structure ticket #41, and PR #42 are closed historical evidence, not live execution authority.
- Provenance audit #66 and taxonomy-conformance audit #342 are closed completed; ongoing provenance and taxonomy conformance are ordinary curation hygiene.
- Current README, AGENTS, Governance Index, this file, CURATION_QUEUE, INDEX, index.json, source registry, and taxonomy control live repository truth.
- Open PRs and issues must be triaged before new curation. Ready authorized work should move through merge/closure rather than becoming permanent lifecycle furniture.

## Accounting contract

After every material corpus tranche, reconcile these five public surfaces atomically: `README.md`, `docs/SYSTEM_STATE.md`, `CURATION_QUEUE.md`, `INDEX.md`, and `index.json`. Recompute counts from live evidence. Do not increment stale counters. Do not merge a material tranche while these surfaces disagree.

## Next action

The narrative capability program is complete. Continue in post-completion maintenance mode: verify source freshness and high-salience omission risk, resolve bounded candidate/source evaluations decisively, backfill exact-version package-security evidence in risk order, keep issue/PR lifecycle debt at zero where actionable, and add selective behavioral/adversarial evidence only when an authorized external environment can produce truthful evidence. Do not invent user-facing repository runtime merely to create work; bounded governed maintenance automation is permitted.
