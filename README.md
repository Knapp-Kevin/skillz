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

**OpenAI Web Data Visualization foundational tranche (2026-11-01).** At the registered `openai/plugins` pin, plugin `build-web-data-visualization` 0.1.21 has **18** direct front-mattered candidates; **9/18** now have terminal source-vetting decisions (**6 REFERENCE-ONLY / 3 REJECT unchanged**), leaving **9** explicit candidate gaps. The 226-entry plugin tree has 164 unique blobs and no symlinks; package references and shared foundations are not extra skills. Strong accessibility, Canvas/D3, declarative and graph-layout methods are reference prior art; persistent notifications, private schedule sync and precise-location/provider egress lack sufficient separate authority. Manifest MIT label has no controlling license text (**NOASSERTION for copying**). Official OpenAI Plugins intake is **160/169 decisions across 22 families in scope (21 complete, 1 partial; 67 REFERENCE-ONLY / 93 REJECT unchanged)**. **0** admissions, governed pairs, scans or behavioral runs; inventory **44 / 995 / 1,039**, **23** sources, **12** pinned corpora. [Exact-source receipt](docs/reviews/2026-11-01-openai-web-data-visualization-nine-candidate-vetting.md), [#595](https://github.com/Knapp-Kevin/skillz/issues/595).

**OpenAI Remotion twelve-candidate source vetting (2026-11-01).** At registered `openai/plugins` pin `0722921d5542fc593105c27bd52630babd8b8c2a`, Remotion plugin **1.0.7** has **12/12** direct first-class candidates with terminal decisions (**5 REFERENCE-ONLY / 7 REJECT unchanged**). The 251 file exposures collapse to 99 unique blobs and only 12 skills; mirrored reference files are not skills. Useful Studio, frame-timing, caption, map-stability and codec methods are separated from unapproved installs/servers, transcript/TTS disclosure, provider attribution, IAM/billing and upgrade actions. Manifest MIT label lacks controlling license text (**NOASSERTION for copying**). Official plugin finite intake is now **151/151 across 21 families (61 REFERENCE-ONLY / 90 REJECT unchanged)**. **0** admissions, semantic/provenance pairs, scans or behavioral runs; inventory stays **44 / 995 / 1,039**, **23** sources, **12** pinned corpora. [Exact-source review](docs/reviews/2026-11-01-openai-remotion-twelve-candidate-vetting.md), [#593](https://github.com/Knapp-Kevin/skillz/issues/593).


**FreeCAD four-candidate source vetting (2026-11-01).** At `sathyavikram/agent-plugins` commit `d29084314aea78989ca08f3ddd2b23238b092eef`, **4/4** FreeCAD candidate SKILL.md entries received terminal source-vetting decisions: **2 REFERENCE-ONLY / 2 REJECT unchanged**. Complete root MIT text exists, but install metadata points to an unavailable different owner and the MCP config launches a machine-specific external Python server; project and visual procedures lack action-specific execution/deletion authority. Geometry/tolerance examples remain unvalidated prior art. **No admission, copying, semantic/provenance pairs, scan or behavioral execution**. Governed inventory remains **44 first-party / 995 third-party / 1,039 total**, **23** registered sources and **12** pinned corpora. [Exact-source review](docs/reviews/2026-11-01-freecad-four-candidate-vetting.md), [#591](https://github.com/Knapp-Kevin/skillz/issues/591).

**Current static corpus (2026-10-31).** The repository records **44 first-party user-facing skills** with 44/44 provenance companions, **995 persisted third-party exact-version semantic reviews**, **1039 total verification/provenance pairs**, and **23 registered source identities**. The admitted source-family denominators below are current-standard static review counts, **not** package-security or behavioral passes. See [SYSTEM_STATE](docs/SYSTEM_STATE.md) and the [curation ledger](CURATION_QUEUE.md) for source-by-source evidence and active gates.

**Current qualifications.** The admitted source families listed below have current-standard exact-version static coverage at their registered pins. Later Microsoft Skills and Matt Pocock candidates remain **unadmitted / NO-GO for pin promotion** despite complete candidate static review. Semantic `verified` is not a security pass or behavioral validation. See the [curation ledger](CURATION_QUEUE.md), [system state](docs/SYSTEM_STATE.md), and [dated review receipts](docs/reviews/).

**Current tracked-source closure (2026-10-31).** Bhushan Modi Agent Skills **68/68**, OpenClaw Agent Skills **8/8**, and Archie Indian Superpowers **56/56** have exact-pin individual static provenance and verification companions with **zero static gaps**. These are semantic review records, not security or behavioral approvals. Archie's pinned upstream license is incomplete; [#544](https://github.com/Knapp-Kevin/skillz/issues/544) blocks redistribution clearance. All source-owned scripts remain upstream reference material.

**OpenAI Plugins discovery intake (2026-10-31).** The official `openai/plugins` repository supersedes the deprecated `openai/skills` catalog and is now registered as a **dynamic-discovery/reference surface**, not an admitted skill corpus. Its observed exact tree (`0722921d5542fc593105c27bd52630babd8b8c2a`) exposes 536 raw `SKILL.md` paths and 64 plugin manifests; these are not eligible-package denominators or reviewed skills. Terms vary per plugin, including proprietary/restricted material. No package was vendored, installed, executed, scanned, semantically verified, or behaviorally validated. [Source-vetting receipt](docs/reviews/2026-10-31-openai-plugins-discovery-vetting.md) and [#554](https://github.com/Knapp-Kevin/skillz/issues/554) record the decision.

**OpenAI Google Drive + Dropbox eleven-candidate vetting (2026-11-01).** At registered `openai/plugins` pin `0722921d5542fc593105c27bd52630babd8b8c2a`, Google Drive **5/5** and Dropbox **6/6** direct first-class packages have **11/11** terminal decisions (**5 REFERENCE-ONLY / 6 REJECT unchanged**). Google Docs/Sheets/Slides offer native structure, revision and visual-QA methods, but their workflows auto-create folders, persist private local artifacts or load source-owned helpers without sufficient independent authority; comments and file lifecycle writes also require separate authorization. Dropbox deletion, move and share confirmation is stronger, but file-request collection lacks adequate third-party privacy/retention approval. Google Drive's MIT manifest declaration lacks controlling license text; Dropbox has no declared license grant (**NOASSERTION for copying**). No copying, admission, semantic/provenance pair, scan or behavioral run. Official-plugin intake **128/128 across 18 families → 139/139 across 20 families (56 REFERENCE-ONLY / 83 REJECT unchanged)**. Governed inventory **44 / 995 / 1,039**, **23** sources, **12** pinned corpora; admitted denominator delta **0**. [Exact-source macro review](docs/reviews/2026-11-01-openai-google-drive-dropbox-eleven-candidate-vetting.md), [#586](https://github.com/Knapp-Kevin/skillz/issues/586).

**OpenAI Adobe + Airtable nine-candidate vetting (2026-11-01).** At registered `openai/plugins` pin `0722921d5542fc593105c27bd52630babd8b8c2a`, Adobe **6/6** and Airtable **3/3** direct first-class packages have **9/9** terminal candidate decisions: **2 REFERENCE-ONLY / 7 REJECT unchanged**. Adobe's preview gates are useful but do not authorize local-media upload to Creative Cloud, sensitive portrait/video disclosure, remote derivatives or Firefly board sharing; Airtable CLI confirms only destructive actions while ordinary writes and private-base reads remain unscoped. No controlling redistribution license text was found at root/plugin/child paths (**NOASSERTION for copying**); no source vendored. Official plugin intake **119/119 across 16 families → 128/128 across 18 families (51 REFERENCE-ONLY / 77 REJECT unchanged)**. Admitted denominator delta **0**, no semantic/provenance pairs, scans or behavioral runs; inventory **44 first-party / 995 third-party / 1,039 total pairs**, **23** registered sources, **12** pinned corpora. [Nine-candidate macro review](docs/reviews/2026-11-01-openai-adobe-airtable-nine-candidate-vetting.md), [#584](https://github.com/Knapp-Kevin/skillz/issues/584).

**OpenAI Temporal four-candidate vetting (2026-11-01).** The registered `openai/plugins` Temporal subtree has **4/4** first-class packages and terminal candidate decisions (**3 REFERENCE-ONLY / 1 REJECT unchanged**). Complete Temporal MIT license text exists; the source-owned 106 KB provisioner has useful locked-file token handling but its Cloud namespace/API-key flow treats tool-permission prompts as approval for billable persistent changes. Ops has stronger destructive gates yet unbounded private diagnostic reads; serverless has named-resource preapproval but no separate production cutover gate. No admission, copying, scan or behavioral execution. Official-plugin finite intake **115/115 across 15 families → 119/119 across 16 families (49 REFERENCE-ONLY / 70 REJECT unchanged)**. Governed inventory **44 first-party / 995 third-party / 1,039 exact-version pairs**, **23** registered sources, **12** pinned corpora, admitted denominator delta **0**. [Exact-source macro review](docs/reviews/2026-11-01-openai-temporal-four-candidate-vetting.md), [#582](https://github.com/Knapp-Kevin/skillz/issues/582).

**OpenAI Build iOS Apps nine-candidate vetting (2026-11-01).** At registered `openai/plugins` pin `0722921d5542fc593105c27bd52630babd8b8c2a`, the exact `build-ios-apps` tree has **9/9** direct first-class skill packages and nine terminal decisions (**4 REFERENCE-ONLY / 5 REJECT unchanged**). Plugin manifest says MIT but no controlling license text was found (**NOASSERTION for copying**). Reusable App Intents, SwiftUI composition, Liquid Glass and code-first performance methods are separated from unsafe unchanged workflows: unapproved simulator build/log capture, `npx @latest` installs and preview mirroring, ETTrace setup/destructive cleanup, sensitive memgraph capture and unapproved source refactors. No copying, admission, scans or behavioral execution. Official plugin candidate intake advances **106/106 across 14 families → 115/115 across 15 families (46 REFERENCE-ONLY / 69 REJECT unchanged)**. Governed inventory remains **44 first-party / 995 third-party / 1,039 pairs**, **23** registered sources and **12** pinned corpora; admitted denominator delta **0**. [Nine-candidate exact-source review](docs/reviews/2026-11-01-openai-build-ios-nine-candidate-vetting.md), [#580](https://github.com/Knapp-Kevin/skillz/issues/580).

**OpenAI Notion + CircleCI eight-candidate source vetting (2026-11-01).** At registered `openai/plugins` pin `0722921d5542fc593105c27bd52630babd8b8c2a`, Notion **4/4** and CircleCI **4/4** direct first-class packages have **8/8 terminal candidate decisions: 2 REFERENCE-ONLY / 6 REJECT unchanged**. Notion per-package MIT text is complete; CircleCI plugin's MIT label lacks controlling license text (**NOASSERTION for copying**). Private meeting/conversation reads, persistent Notion pages/tasks, CI/deploy edits, billable reruns, Chunk cloud tasks/credentials/scheduling lack action-specific authorization. Preserve citation/template methods, deterministic-vs-transient triage and cache/workspace/artifact design as bounded prior art. At that earlier tranche, official plugin intake was **106/106 across fourteen finite families (42 REFERENCE-ONLY / 64 REJECT unchanged)**. No admissions, source pins, admitted denominators, semantic/provenance pairs, scans or behavioral runs changed; public **44 / 995 / 1,039**, **23** sources, **12** pinned corpora. [Eight-candidate macro review](docs/reviews/2026-11-01-openai-notion-circleci-eight-candidate-vetting.md), [#578](https://github.com/Knapp-Kevin/skillz/issues/578).

**OpenAI Stripe + Supabase nine-candidate source vetting (2026-11-01).** At registered openai/plugins pin 0722921d5542fc593105c27bd52630babd8b8c2a, Stripe **7/7** and Supabase **2/2** direct first-class packages have **9/9** terminal candidate decisions: **3 REFERENCE-ONLY / 6 REJECT unchanged**. Money/resource authorization gaps include Stripe Apps uploads, Projects TOS acceptance and credential/provisioning writes, Connect auto-scanning, SDK upgrades, and Supabase live SQL iteration. Stripe copying terms **NOASSERTION**; Supabase plugin has complete MIT text. Same-pin Stripe/Supabase best-practice copies differ from Build Web Apps packages; no status inheritance. Official plugin intake is **98/98 across twelve finite families (40 REFERENCE-ONLY / 58 REJECT unchanged)**. No admission, source pin, denominator, semantic/provenance pair, security scan or behavioral run changed. Public inventory remains **44 / 995 / 1,039**, **23** registered sources and **12** pinned corpora. [Nine-candidate macro review](docs/reviews/2026-11-01-openai-stripe-supabase-nine-candidate-vetting.md), [#576](https://github.com/Knapp-Kevin/skillz/issues/576).

**OpenAI Build Web Apps six-candidate source vetting (2026-11-01).** At the registered `openai/plugins` pin, **6/6** direct first-class packages have terminal decisions: **3 REFERENCE-ONLY / 3 REJECT unchanged**, 0 admissions, 0 semantic pairs, 0 source/denominator changes, no scans or behavioral runs. Important same-pin duplication/freshness defects: the Build Web Apps Stripe copy says API `2026-02-25.clover` while the separate Stripe plugin says `2026-07-29.dahlia`; its Supabase copy says `1.1.0` while the separate Supabase plugin says `1.1.1`; React is also a different package identity. Frontend model/browser and shadcn `npx ...@latest` workflows lack independent budget, disclosure, install and action authorization. Plugin MIT label has no controlling root/plugin/child license text at the pin; no copying. [Six-candidate review](docs/reviews/2026-11-01-openai-build-web-apps-six-candidate-vetting.md), [#574](https://github.com/Knapp-Kevin/skillz/issues/574).

**Current OpenAI Plugins bounded candidate vetting (2026-11-01).** **160/169 terminal candidate decisions across 22 families in scope**: 21 complete families, one partial 9/18 Web Data Visualization family, **67 REFERENCE-ONLY / 93 REJECT unchanged**. These remain discovery-only, not admitted or semantically verified skills. [Web Data Visualization nine-candidate review](docs/reviews/2026-11-01-openai-web-data-visualization-nine-candidate-vetting.md) documents the active remainder; earlier [Remotion review](docs/reviews/2026-11-01-openai-remotion-twelve-candidate-vetting.md) remains historical evidence.

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
