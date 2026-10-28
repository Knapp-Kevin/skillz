# 🛠️ skillz

![Reference Corpus](https://img.shields.io/badge/reference_corpus-500%2B-blue)
![First-Party Skills](https://img.shields.io/badge/first--party_skills-44-brightgreen)
![Persisted Third-Party Reviews](https://img.shields.io/badge/exact--version_reviews-788-8A2BE2)
![Registered Sources](https://img.shields.io/badge/registered_sources-22-6f42c1)
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
5. **Exact-version package-security policy and evidence** under [`docs/security-scanning.md`](docs/security-scanning.md) and [`registry/security/`](registry/security/), backed by pinned maintainer-side scanning.

Third-party packages may contain their own scripts, tests, examples, fixtures, templates, or tools. Those remain upstream package material, not repository-owned execution machinery.

## Core use

The host agent should identify durable user needs, inspect the minimum relevant evidence, compare available first-party and governed third-party material, then evaluate in this order:

**user fit → exact-version quality → operational fit → skill freshness → provenance/source context**

Valid outcomes include ADOPT, ADAPT, EXTRACT, SUPPLEMENT, COMPOSE, CREATE, CHECKLIST, DYNAMIC behavior, or NO CHANGE. The goal is the smallest coherent fitted system, not maximum reuse.

## Corpus and evidence

**Microsoft freshness (2026-10-28):** The [canonical denominator review](docs/reviews/2026-10-27-microsoft-canonical-denominator-and-ungoverned-exposures.md) establishes **208 structurally eligible** packages at candidate `61fe0305ea70389ed8705eec6026a786f57865cf` (212 physical manifests minus 3 non-first-class references and 1 exact mirror): **106 exact-tree carry-forwards + 76 changed-existing + 26 new/previously ungoverned**. Changed-existing screening **76/76** is not full requalification. **26/26 new candidates** now have complete exact-version static companions (**4 VERIFIED semantic only, 22 REJECT unchanged**); **38 changed-existing** full current-version reviews remain (38/76 fully requalified). Four removed paths have candidate-only [retirement/no-proven-successor decisions](docs/reviews/2026-10-27-microsoft-four-removed-path-candidate-retirements.md). Registered July remains **186/186** at unchanged pin; no candidate security scan, behavioral validation, source-pin movement or admission was claimed.

**Candidate full-package static reviews (2026-10-28):** Kusto (3), AKS/Advisor/Cost (8), authority/privacy (8), AKS/prereq/Entra (3), AKS app-deploy (1), Azure App Onboard (1), Slack-to-Teams (1), and [Foundry IQ 85-skill-file + 17-plugin-file review](docs/reviews/2026-10-28-microsoft-foundry-iq-102-blob-exact-static.md) (1). **26/26** new candidates have full exact-version static companions (4 semantic VERIFIED only / 22 REJECT unchanged); **38 changed-existing** packages still require full candidate-version requalification (38/76 complete). Persisted third-party verification companions: **788** after Rust (8), Python Azure AI (8), Python data/storage/events (8), Python identity/telemetry (6), and Python services/management (8) changed-existing tranches. Foundry IQ's default-on plugin telemetry/native installer is an unchanged-use privacy/authority hard fail despite strong core approval controls. No admission, scanner execution, behavioral evidence or pin changes.

**Changed-existing Rust qualification (2026-10-28):** [Eight complete single-file Rust reviews](docs/reviews/2026-10-28-microsoft-rust-eight-changed-exact-static.md) finished **8/76** changed-existing Microsoft candidates, leaving **68**. All eight are **REJECT unchanged** (8–11/20) for authorization and sensitive-data failures; Key Vault Keys also contains a four-byte DEK example. Exact candidate provenance and static verification are recorded; security and behavioral states `not-run`. Third-party companions **758 at this Rust checkpoint**. Registered July **186/186** and source pin unchanged.

**Changed-existing Python Azure AI qualification (2026-10-28):** [Eight complete three-file exact-version reviews](docs/reviews/2026-10-28-microsoft-python-ai-multimodal-eight-exact-static.md) finished **16/76** changed-existing Microsoft candidates, leaving **60** (29 Python, 30 Azure operations, one skill-creator). All eight are **REJECT unchanged** (9–13/20) for unapproved external data transmission, persistent service effects and privacy/retention failures; document translation also exposes SAS-bearing URL patterns. Exact provenance, all 24 blob identities and individual semantic dispositions are recorded. Security and behavioral states remain `not-run`; third-party companions **766**, total verification YAML **810** (44 first-party + 766 third-party). Registered July **186/186** and source pin unchanged.
**Changed-existing Python data/storage/events qualification (2026-10-28):** [Eight complete three-file exact-version static reviews](docs/reviews/2026-10-28-microsoft-python-data-storage-events-eight-exact-static.md) advance **16/76 → 24/76** changed-existing Microsoft packages, leaving **52** (21 Python, 30 Azure operations, one skill-creator). All eight are **REJECT unchanged** (10–12/20) for unapproved production mutations, tenant/sensitive-data disclosure, destructive storage/queue effects and event publication. All 24 exact blobs and individual companions are recorded. Security and behavioral states remain `not-run`; third-party verification companions **774**, total verification YAML **818** (44 first-party + 774 third-party). Registered July **186/186** and source pin unchanged.


**Changed-existing Python identity/telemetry qualification (2026-10-28):** [Six complete three-file exact-version static reviews](docs/reviews/2026-10-28-microsoft-python-identity-telemetry-six-exact-static.md) advance **24/76 → 30/76**, leaving **46** (15 Python, 30 Azure operations, one skill-creator). All six are **REJECT unchanged** (10–12/20) for authority/privacy hard fails. All 18 source blobs and individual companions are recorded. Security and behavioral states `not-run`; third-party companions **780**, total YAML verification **824**. July pin **186/186** unchanged.

**Changed-existing Python services/management qualification (2026-10-28):** [Eight complete exact-version static reviews](docs/reviews/2026-10-28-microsoft-python-services-management-eight-exact-static.md) advance **30/76 → 38/76**, leaving **38** (7 Python, 30 Azure operations, one skill-creator). Deep nine-file Cosmos service-layer review plus seven management/messaging/agent packages; **29 source blobs**, eight individual provenance/verification pairs, all **REJECT unchanged** (10–12/20) for authorization, credential/PII disclosure, destructive resource changes and billable capacity operations. Cosmos additionally has a potential untrusted SQL-fragment sink and substring-based emulator TLS bypass. Security and behavioral states remain `not-run`; third-party companions **788**, total YAML verification **832**. July pin **186/186** unchanged.

The registry contains **22 unique source identities** and **788 persisted exact-version third-party verification companions**. `verified` means structured static semantic review of an exact version. It does **not** imply a package-security pass, behavioral validation, or automatic unchanged-use eligibility. `validated` additionally requires representative external behavioral/adversarial evidence. Security state is recorded separately; for SkillSpector-compatible packages, new unchanged admission or refresh eligibility requires `passed` or explicitly `findings-reviewed` security evidence. `rejected` and `retired` remain useful bounded prior art but are excluded from normal unchanged selection.

| Source family | Current-standard state |
|---|---:|
| Anthropic Skills | 19 / 19 |
| Anthropic Knowledge Work Plugins | 74 / 74 |
| AWS Agent Toolkit | 72 / 72 |
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

Microsoft direct-package accounting remains `.NET` **29/29**, Java **26/26**, Python **40/40**, Rust **9/9**, and TypeScript **25/25**.

### Jwynia Agent Skills selective intake

`jwynia/agent-skills` is tracked at exact snapshot `e02ec7e226a6e4f8419fd3b88a1d8e472d421b32` for selective individual curation, not blanket trust or vendoring. The source contains 112 skills, including 57 creative/narrative skills. Source-wide licensing is recorded as **MIXED/per-skill** because no root `LICENSE` was found at the evaluated pin.

The exact fiction denominator is now **54/54 governed**: **39 VERIFIED** exact-version static references and **15 REJECTED unchanged** references retained as adaptation/extraction prior art. The original governed set remains `story-collaborator`, `story-sense`, `story-zoom`, `worldbuilding`, `character-arc`, `dialogue`, `scene-sequencing`, and `prose-style`. Issue #388 tranche 1 added seven VERIFIED and four REJECTED unchanged core/craft/character units. Tranche 2 added nine VERIFIED structure units and rejected `reverse-outliner` unchanged. Tranche 3 added nine VERIFIED worldbuilding units and rejected `conlang` unchanged. The final application/orchestrator tranche VERIFIED `book-marketing`, `dna-extraction`, `flash-fiction`, `interactive-fiction`, `media-adaptation`, `paradox-fables`, and `table-tone`; it REJECTED unchanged `adaptation-synthesis`, `game-facilitator`, `list-builder`, `multi-order-evolution`, `sensitivity-check`, `shared-world`, `sleep-story`, and `chapter-drafter` for concrete oracle, evidence, package-integrity, or authority defects. Behavioral validation remains `not-run` for all fifty-four.

For Celestara, rejected does not mean useless. `shared-world`, `game-facilitator`, and `chapter-drafter` are especially strong adaptation prior art once canon authority and pseudo-oracle defects are removed. `systemic-worldbuilding`, `interactive-fiction`, `table-tone`, and `world-fates` provide clean governed concepts for causal consequence, player agency, table experience, and proposal-only long-range state. Rejected sibling behavior never inherits trust through a verified workflow.

### Dan Dewhurst Story Skills complete intake

`danjdewhurst/story-skills` is tracked at exact snapshot `b113a8298ae5deb37929a5b1d0cc1536d98a508c`. The MIT-licensed corpus has an exact denominator of **23** first-class skills, and **all 23 now have individual provenance and exact-version VERIFIED static-review companions**. Scores range from **16/20 to 18/20**; behavioral validation remains `not-run` for all 23.

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
