# 🛠️ skillz

![Reference Corpus](https://img.shields.io/badge/reference_corpus-500%2B-blue)
![First-Party Skills](https://img.shields.io/badge/first--party_skills-44-brightgreen)
![Persisted Third-Party Reviews](https://img.shields.io/badge/exact--version_reviews-995-8A2BE2)
![Registered Sources](https://img.shields.io/badge/registered_sources-23-6f42c1)
![Repository](https://img.shields.io/badge/repository-entirely--passive-blueviolet)
![License](https://img.shields.io/badge/license-MIT-green)

**An entirely passive skill knowledge resource for AI agents.** `skillz` stores reusable skills, procedures, safeguards, anti-patterns, rejected examples, creator methods, standards, pinned source material, provenance, exact-version review evidence, security evidence, controlled tags, source context, and static catalog snapshots. The external host agent remains the active user-facing system.

> **AI agent? Start with [`AGENT_START_HERE.md`](AGENT_START_HERE.md).** For first-visit or returning-user skill-system work, [`engine/skills/skill-bootstrap/SKILL.md`](engine/skills/skill-bootstrap/SKILL.md) is the canonical passive procedure. The [first-contact discovery walkthrough](docs/first-contact-discovery.md) provides a capability-aware checklist and example handoff; direct skill lookup stays lightweight.

> **Normal-use boundary:** skills created, adapted, composed, or refined for a user belong in that user's active AI/agent environment or in a portable handoff. They are not written back here unless repository maintenance/curation was explicitly requested.

## What `skillz` is

`skillz` is **entirely passive**. It owns no runtime, scripts, tests, CI workflows, schedulers, monitors, crawlers, installers, synchronizers, preflight processes, generators, background services, vector databases, autonomous observers, or personalization services. An authorized external host may run assessments elsewhere and deposit exact-version evidence here; pinned upstream package tooling stays source-owned reference material.

The repository provides five surfaces:

1. **44 first-party user-facing skills** under [`skills/`](skills/), all **44/44 provenance-complete**.
2. **12 intact pinned third-party corpora** under [`skills/sources/`](skills/sources/) at exact upstream revisions.
3. **Governed provenance and exact-version evidence** under [`registry/skills/`](registry/skills/) and [`registry/verification/`](registry/verification/).
4. **Passive repository-use and curation procedures** under [`engine/skills/`](engine/skills/), excluded from user-facing inventory.
5. **Exact-version package-security policy and evidence** under [`docs/security-scanning.md`](docs/security-scanning.md) and [`registry/security/`](registry/security/), with scanning performed only in an authorized external host environment.

Third-party packages may contain their own scripts, tests, examples, fixtures, templates, or tools. Those remain upstream package material, not repository-owned execution machinery.

## Core use

The host agent should identify durable user needs, inspect the minimum relevant evidence, compare available first-party and governed third-party material, then evaluate in this order:

**user fit → exact-version quality → operational fit → skill freshness → provenance/source context**

Valid outcomes include ADOPT, ADAPT, EXTRACT, SUPPLEMENT, COMPOSE, CREATE, CHECKLIST, DYNAMIC behavior, or NO CHANGE. The goal is the smallest coherent fitted system, not maximum reuse.

## Corpus and evidence

**Current static corpus (2026-10-31).** The repository records **44 first-party user-facing skills** with 44/44 provenance companions, **995 persisted third-party exact-version semantic reviews**, **1039 total verification/provenance pairs**, and **23 registered source identities**. The admitted source-family denominators below are current-standard static review counts, **not** package-security or behavioral passes. See [SYSTEM_STATE](docs/SYSTEM_STATE.md) and the [curation ledger](CURATION_QUEUE.md) for source-by-source evidence and active gates.

**Current qualifications.** The admitted source families listed below have current-standard exact-version static coverage at their registered pins. Later Microsoft Skills and Matt Pocock candidates remain **unadmitted / NO-GO for pin promotion** despite complete candidate static review. Semantic `verified` is not a security pass or behavioral validation. See the [curation ledger](CURATION_QUEUE.md), [system state](docs/SYSTEM_STATE.md), and [dated review receipts](docs/reviews/).

**Current tracked-source closure (2026-10-31).** Bhushan Modi Agent Skills **68/68**, OpenClaw Agent Skills **8/8**, and Archie Indian Superpowers **56/56** have exact-pin individual static provenance and verification companions with **zero static gaps**. These are semantic review records, not security or behavioral approvals. Archie's pinned upstream license is incomplete; [#544](https://github.com/Knapp-Kevin/skillz/issues/544) blocks redistribution clearance. All source-owned scripts remain upstream reference material.

**OpenAI Plugins discovery intake (2026-10-31).** The official `openai/plugins` repository supersedes the deprecated `openai/skills` catalog and is now registered as a **dynamic-discovery/reference surface**, not an admitted skill corpus. Its observed exact tree (`0722921d5542fc593105c27bd52630babd8b8c2a`) exposes 536 raw `SKILL.md` paths and 64 plugin manifests; these are not eligible-package denominators or reviewed skills. Terms vary per plugin, including proprietary/restricted material. No package was vendored, installed, executed, scanned, semantically verified, or behaviorally validated. [Source-vetting receipt](docs/reviews/2026-10-31-openai-plugins-discovery-vetting.md) and [#554](https://github.com/Knapp-Kevin/skillz/issues/554) record the decision.

**Bounded OpenAI Developers candidate vetting (2026-10-31).** All five first-class skills in the proprietary-parent `openai-developers` plugin were reconciled at the observed source revision: **4 REFERENCE-ONLY / 1 REJECT unchanged**, with no source admission, vendoring, semantic verification, security scan or behavioral validation. The plugin declares Proprietary terms while two child folders include Apache-2.0 license text; scope is unresolved for copying. The API troubleshooting skill's unapproved escalated retry of a real API request is an authority hard fail. [Five-candidate review](docs/reviews/2026-10-31-openai-developers-five-candidate-vetting.md), [bounded issue #556](https://github.com/Knapp-Kevin/skillz/issues/556).

**OpenAI Product Design bounded source vetting (2026-10-31).** All **10/10** front-mattered first-class skills under `plugins/product-design/skills/` at registered official `openai/plugins` revision have terminal candidate decisions: **2 REFERENCE-ONLY / 8 REJECT unchanged**. Proprietary plugin terms prohibit assumed redistribution; cross-workflow private-context preflight and image disclosure, unscoped connector reads, live-site asset copying, local dependency/write operations, and deployment authorization are material risks. The source's same-state design QA and visual selection discipline remain valuable reference methods. **0 admissions, 0 new semantic pairs, 0 denominator change, 0 scans/behavioral runs**. Public **44 / 995 / 1039**, sources **23** unchanged. [Ten-candidate review](docs/reviews/2026-10-31-openai-product-design-ten-candidate-vetting.md), [#560](https://github.com/Knapp-Kevin/skillz/issues/560).

**OpenAI Plugin Eval candidate vetting (2026-10-31).** The official `plugin-eval` slice has **5/5 terminal source-vetting decisions: 1 REFERENCE-ONLY / 4 REJECT unchanged**. Its structured evaluation schema and improvement-prioritization methods are useful prior art; unchanged use is held for executable metric packs inheriting host credentials, live Codex benchmark authorization/retention, automatic benchmark-config writes, broken `--dry-run` guidance and unestablished redistribution terms. This is **not** five new semantic reviews or source admissions. [Bounded review](docs/reviews/2026-10-31-openai-plugin-eval-five-candidate-vetting.md), [#558](https://github.com/Knapp-Kevin/skillz/issues/558).

**OpenAI Superpowers bounded candidate vetting (2026-10-31).** All **14/14** first-class skills at the registered `openai/plugins` snapshot received terminal source-vetting decisions: **5 REFERENCE-ONLY / 9 REJECT unchanged**. The Jesse Vincent/`obra/superpowers` MIT-licensed plugin has useful review, planning and evidence methods, but unapproved third-party image egress, raw environment logging, dependency installs, destructive TDD restart and unscoped subagent disclosure block unchanged use. **0 admissions / 0 new review pairs / 0 scans or behavioral runs**. [Review](docs/reviews/2026-10-31-openai-superpowers-fourteen-candidate-vetting.md), [issue #562](https://github.com/Knapp-Kevin/skillz/issues/562).

**Review history and macro findings:** The dated tranche receipts, individual dispositions, authority/privacy findings, and earlier count checkpoints remain in [CURATION_QUEUE.md](CURATION_QUEUE.md) and [docs/reviews/](docs/reviews/). Historical counts are evidence of progress, not current catalog totals.

**Evidence is deliberately separated.** `verified` means exact-version structured semantic review; `validated` requires actual representative external behavioral/adversarial evidence. Applicable unchanged-use eligibility also depends on complete exact-package security evidence and user fit. An upstream package's scripts or tests remain source-owned reference material, not repository runtime. Historical Microsoft tranche receipts and interim counts are preserved in [review records](docs/reviews/) and the [curation ledger](CURATION_QUEUE.md), rather than being presented here as current work remaining.

| Source family | Current-standard state |
|---|---:|
| Anthropic Skills | 19 / 19 |
| Anthropic Knowledge Work Plugins | 74 / 74 |
| AWS Agent Toolkit | **94 / 94** |
| Microsoft Skills | 186 / 186 |
| Microsoft Azure Skills | 34 / 34 |
| Cole Medin Skills | 33 / 33 |
| David Ondrej Skills | 55 / 55 |
| Corey Haines Marketing Skills | **50 / 50** |
| Dan Dewhurst Story Skills | **23 / 23** |
| Matt Pocock Skills | 29 / 29 |
| Cloudflare Skills | 13 / 13 |
| Addy Osmani Agent Skills | 24 / 24 |
| Vercel Agent Skills | 9 / 9 |
| OpenHands Extensions | 1 / 1 |
| Google Agents CLI | 7 / 7 |
| Cline Skills (published) | 36 / 36 |
| Bhushan Modi Agent Skills (tracked) | 68 / 68 |
| OpenClaw Agent Skills (tracked) | 8 / 8 |
| Archie Indian Superpowers (tracked; license #544 held) | 56 / 56 |

An [Anthropic Skills private-source and MCP evaluation authority review](docs/reviews/2026-10-30-anthropic-comms-mcp-private-data-authority-macro.md) corrected two unchanged-use approvals. The family remains **19/19** static-reviewed, now **8 VERIFIED semantic only / 11 REJECT unchanged**. Broad connected-company reads and model-backed evaluation of private MCP tool outputs require separate source, disclosure, budget and retention authority; no scanner or behavioral validation was executed.

A [Matt Pocock ten-package delegated-authority recheck](docs/reviews/2026-10-30-mattpocock-ten-delegated-authority-macro.md) corrected five unchanged-use approvals. The registered family remains **29/29** static-reviewed, now **17 VERIFIED semantic only / 12 REJECT unchanged**; its Wayfinder decision-map discipline remains useful for adapted planning, not blanket authorization for tracker writes or AFK provisioning.

An [Addy Osmani delegated-authority and RUM review](docs/reviews/2026-10-30-addyosmani-delegation-rum-24-macro.md) corrected two unchanged-use approvals. The family remains **24/24** static-reviewed, now **8 VERIFIED / 16 REJECT unchanged**; behavioral validation remains separate.

An [AWS ten-package authority recheck](docs/reviews/2026-10-30-aws-ten-authority-and-private-data-macro.md) corrected six unchanged-use approvals while preserving **94/94** exact-version static coverage and all upstream packages. Static coverage does not grant permission to create cloud resources or transmit private telemetry.

Microsoft direct-package accounting remains `.NET` **29/29**, Java **26/26**, Python **40/40**, Rust **9/9**, and TypeScript **25/25**.

### Jwynia Agent Skills selective intake

`jwynia/agent-skills` is tracked at exact snapshot `e02ec7e226a6e4f8419fd3b88a1d8e472d421b32` for selective individual curation, not blanket trust or vendoring. The source contains 112 skills, including 57 creative/narrative skills. Source-wide licensing is recorded as **MIXED/per-skill** because no root `LICENSE` was found at the evaluated pin.

The exact fiction denominator is now **54/54 governed**: **39 VERIFIED** exact-version static references and **15 REJECTED unchanged** references retained as adaptation/extraction prior art. The original governed set remains `story-collaborator`, `story-sense`, `story-zoom`, `worldbuilding`, `character-arc`, `dialogue`, `scene-sequencing`, and `prose-style`. Issue #388 tranche 1 added seven VERIFIED and four REJECTED unchanged core/craft/character units. Tranche 2 added nine VERIFIED structure units and rejected `reverse-outliner` unchanged. Tranche 3 added nine VERIFIED worldbuilding units and rejected `conlang` unchanged. The final application/orchestrator tranche VERIFIED `book-marketing`, `dna-extraction`, `flash-fiction`, `interactive-fiction`, `media-adaptation`, `paradox-fables`, and `table-tone`; it REJECTED unchanged `adaptation-synthesis`, `game-facilitator`, `list-builder`, `multi-order-evolution`, `sensitivity-check`, `shared-world`, `sleep-story`, and `chapter-drafter` for concrete oracle, evidence, package-integrity, or authority defects. Behavioral validation remains `not-run` for all fifty-four.

For Celestara, rejected does not mean useless. `shared-world`, `game-facilitator`, and `chapter-drafter` are especially strong adaptation prior art once canon authority and pseudo-oracle defects are removed. `systemic-worldbuilding`, `interactive-fiction`, `table-tone`, and `world-fates` provide clean governed concepts for causal consequence, player agency, table experience, and proposal-only long-range state. Rejected sibling behavior never inherits trust through a verified workflow.

### Dan Dewhurst Story Skills complete intake

`danjdewhurst/story-skills` is tracked at exact snapshot `b113a8298ae5deb37929a5b1d0cc1536d98a508c`. The MIT-licensed corpus has an exact denominator of **23** first-class skills, and **all 23 have individual provenance and exact-version static-review companions**: **21 VERIFIED semantic only** and **2 REJECT unchanged** (`feedback-triage`, `reader-panel`) after the 2026-10-30 authority recheck. Scores range from **14/20 to 18/20**; behavioral validation remains `not-run` for all 23.

The family is unusually coherent as an end-to-end fiction workflow, but it is not universally portable unchanged. Most skills assume the upstream Markdown/YAML Story Skills project model, and several can invoke the optional `story` CLI. `story-maintenance` also packages a local Node fallback with explicit rename/move/remove operations. Those source-owned runtime assets remain upstream evidence and dependencies rather than repository-owned `skillz` runtime. Submission, publishing, and editorial workflows keep consequential real-world sends, purchases, contracts, account actions, and publication under author control.

### Corey Haines corpus completion

Corey Haines Marketing Skills is a tracked corpus at exact snapshot `5b2c0007766c6a1cf1d53fd8fc73e979e0821022`, with an exact eligible denominator of **50** top-level first-class skill packages. **All 50 now have individual current-standard provenance and exact-version verification companions.**

The final macro tranche reviewed `revops`, `sales-enablement`, `schema`, `seo-audit`, `signup`, `site-architecture`, `sms`, `social`, and `video`. `sales-enablement`, `schema`, `seo-audit`, and `site-architecture` passed **VERIFIED exact-version static review**. The other five are **REJECTED unchanged** while retained as adaptation/extraction/reference prior art. Behavioral validation remains `not-run` for all reviewed Corey units.

The family-level pattern is stable but not absolute: Corey Haines is stronger as planning/checklist/design prior art than as unchanged operational authority. Recurring defects cluster around action authorization, privacy/minimization/consent/retention, unsupported or volatile quantitative marketing/platform claims, and safeguards around persuasive or dark-pattern-adjacent tactics. Exact dispositions, scores, fingerprints, dependencies, controlled tags, freshness evidence, authority findings, and rationale live in the canonical companions under `registry/` rather than being duplicated here.

The bounded controlled-taxonomy conformance audit in #342 is **closed completed**. Ongoing tag conformance is ordinary curation hygiene against `registry/taxonomy.yaml`; historical invalid-tag examples remain evidence only and must not be assumed to describe current records.

## Discovery and admission

**discovery surface → candidate issue/source → source-vetting → exact-version static evaluation → exact-version security scan → decisive admission result → repository persistence when justified → user-fit decision**

New third-party discoveries use [`docs/candidate-intake.md`](docs/candidate-intake.md). Discovery scores, popularity, official branding, creator reputation, or catalog recommendations are signals only. Restricted or unclear-license material remains reference-only unless terms justify another role.

## Repository map

| Area | Purpose |
|---|---|
| [`AGENT_START_HERE.md`](AGENT_START_HERE.md) | Agent routing and capability floor |
| [`docs/first-contact-discovery.md`](docs/first-contact-discovery.md) | Capability-aware first-visit walkthrough and portable receipt |
| [`CHANGES.md`](CHANGES.md) | Dated material repository changes; no adoption claims inferred |
| [`AGENTS.md`](AGENTS.md) | Repository-wide agent contract |
| [`skills/`](skills/) | First-party user-facing corpus |
| [`skills/sources/`](skills/sources/) | Intact exact-revision external reference corpora |
| [`INDEX.md`](INDEX.md) / [`index.json`](index.json) | Hand-maintained passive catalog snapshots |
| [`CURATION_QUEUE.md`](CURATION_QUEUE.md) | Living curation and source-vetting ledger |
| [`registry/sources.yaml`](registry/sources.yaml) | Source identities, roles, pins, licenses, paths |
| [`registry/skills/`](registry/skills/) | Mandatory per-skill provenance companions |
| [`registry/verification/`](registry/verification/) | Exact-version semantic review evidence |
| [`registry/security/`](registry/security/) | Exact-version package-security evidence |
| [`registry/security-tools.yaml`](registry/security-tools.yaml) | Pinned maintainer security-tool identity and policy |
| [`docs/security-scanning.md`](docs/security-scanning.md) | External security-evidence, licensing, and backfill contract |
| [`engine/skills/`](engine/skills/) | Passive repository-use/curation procedures |
| [`docs/GOVERNANCE_INDEX.md`](docs/GOVERNANCE_INDEX.md) | Current governance precedence |
| [`docs/SYSTEM_STATE.md`](docs/SYSTEM_STATE.md) | Current live corpus and architecture snapshot |

## Licensing

First-party content is MIT-licensed. Third-party repositories and materially derived content retain their applicable upstream obligations; the root MIT license does not relicense pinned source corpora. NVIDIA SkillSpector is used as a pinned external Apache-2.0 maintenance dependency and is not vendored or relicensed here. See [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md), [`docs/third-party-provenance.md`](docs/third-party-provenance.md), and [`docs/security-scanning.md`](docs/security-scanning.md).
