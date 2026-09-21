# 🛠️ skillz

![Reference Corpus](https://img.shields.io/badge/reference_corpus-500%2B-blue)
![First-Party Skills](https://img.shields.io/badge/first--party_skills-44-brightgreen)
![Persisted Third-Party Reviews](https://img.shields.io/badge/exact--version_reviews-598-8A2BE2)
![Registered Sources](https://img.shields.io/badge/registered_sources-20-6f42c1)
![Repository](https://img.shields.io/badge/repository-passive-blueviolet)
![License](https://img.shields.io/badge/license-MIT-green)

**A passive skill knowledge resource for AI agents.** `skillz` stores reusable skills, procedures, safeguards, anti-patterns, rejected examples, creator methods, standards, pinned source material, provenance, exact-version review evidence, controlled tags, source context, and static catalog snapshots. The external host agent is the active system.

> **AI agent? Start with [`AGENT_START_HERE.md`](AGENT_START_HERE.md).** For first-visit or returning-user skill-system work, [`engine/skills/skill-bootstrap/SKILL.md`](engine/skills/skill-bootstrap/SKILL.md) is the canonical passive procedure.

> **Normal-use boundary:** skills created, adapted, composed, or refined for a user belong in that user's active AI/agent environment or in a portable handoff. They are not written back here unless repository maintenance/curation was explicitly requested.

## What `skillz` is

`skillz` is entirely passive. The repository owns no runtime, scripts, tests, CI workflows, schedulers, monitors, crawlers, installers, synchronizers, preflight processes, generators, background services, vector databases, autonomous observers, or personalization services.

The repository provides four surfaces:

1. **44 first-party user-facing skills** under [`skills/`](skills/), all **44/44 provenance-complete**.
2. **12 intact pinned third-party corpora** under [`skills/sources/`](skills/sources/) at exact upstream revisions.
3. **Governed provenance and exact-version evidence** under [`registry/skills/`](registry/skills/) and [`registry/verification/`](registry/verification/).
4. **Passive repository-use and curation procedures** under [`engine/skills/`](engine/skills/), excluded from user-facing inventory.

Third-party packages may contain their own scripts, tests, examples, fixtures, templates, or tools. Those remain upstream package material, not repository-owned execution machinery.

## Core use

The host agent should identify durable user needs, inspect the minimum relevant evidence, compare available first-party and governed third-party material, then evaluate in this order:

**user fit → exact-version quality → operational fit → skill freshness → provenance/source context**

Valid outcomes include ADOPT, ADAPT, EXTRACT, SUPPLEMENT, COMPOSE, CREATE, CHECKLIST, DYNAMIC behavior, or NO CHANGE. The goal is the smallest coherent fitted system, not maximum reuse.

## Corpus and evidence

The registry contains **20 unique source identities**. There are currently **598 persisted exact-version third-party verification companions**. `verified` means structured static semantic review of an exact version. `validated` additionally requires representative external behavioral/adversarial evidence. `rejected` and `retired` remain useful bounded prior art but are excluded from normal unchanged selection.

Current admitted-source accounting:

| Source family | Current-standard state |
|---|---:|
| Anthropic Skills | 17 / 17 |
| Anthropic Knowledge Work Plugins | 74 / 74 |
| AWS Agent Toolkit | 72 / 72 |
| Microsoft Skills | 186 / 186 |
| Microsoft Azure Skills | 34 / 34 |
| Cole Medin Skills | 33 / 33 |
| David Ondrej Skills | 55 / 55 |
| Corey Haines Marketing Skills | **6 / 50, 44 gaps** |
| Matt Pocock Skills | 29 / 29 |
| Cloudflare Skills | 13 / 13 |
| Addy Osmani Agent Skills | 24 / 24 |
| Vercel Agent Skills | 9 / 9 |
| OpenHands Extensions | 1 / 1 |
| Google Agents CLI | 7 / 7 |
| Cline Skills (published) | 36 / 36 |

Microsoft direct-package accounting remains `.NET` **29/29**, Java **26/26**, Python **40/40**, Rust **9/9**, and TypeScript **25/25**.

### Active curation frontier

Corey Haines Marketing Skills is a tracked corpus at exact snapshot `5b2c0007766c6a1cf1d53fd8fc73e979e0821022`, with an exact eligible denominator of **50** top-level first-class skill packages. Six are individually current-standard reviewed and **44** remain.

- `ab-testing`: **rejected unchanged 13/20**; useful experiment-planning mechanisms, but materially inconsistent sample-size guidance and misleading frequentist p-value/confidence semantics.
- `ad-creative`: **rejected unchanged 15/20**; useful creative/review mechanisms, but scaled workflows lack distinct file-mutation and external-publication/user-communication authorization boundaries.
- `ads`: **rejected unchanged 15/20**; strong audit/read-only mechanisms, but operational paths do not consistently inherit explicit authorization for spend, launches, data operations, persistence, and recurring communication.
- `ai-seo`: **rejected unchanged 14/20**; useful AI-search/content mechanisms, but materially incorrect crawler-control semantics and insufficient explicit authorization boundaries around website mutation/publication and identity-bearing external activity.
- `analytics`: **rejected unchanged 15/20**; useful decision-first measurement, event-taxonomy, debugging, data-quality, consent, and minimization mechanisms, but normal GA4/GTM/site implementation paths lack distinct explicit authorization before external/persistent mutation and privacy-sensitive telemetry activation.
- `aso`: **rejected unchanged 14/20**; useful read-only ASO audit and platform-differentiation mechanisms, but volatile platform/benchmark claims are asserted too confidently and several bundled benchmarks lack claim-level traceability.

Behavioral validation is `not-run` for all six. Exact rationale, fingerprints, dependencies, authority findings, tags, and source identity live in their canonical provenance and verification companions.

Admission never grants blanket unchanged-reuse eligibility. Partner integrations, upstream source tooling, generated partner surfaces, and ordinary reference Markdown are outside the Corey denominator.

## Discovery and admission

**discovery surface → candidate issue/source → source-vetting → exact-version static evaluation → decisive admission result → repository persistence when justified → user-fit decision**

New third-party discoveries use [`docs/candidate-intake.md`](docs/candidate-intake.md). Discovery scores, popularity, official branding, creator reputation, or catalog recommendations are signals only. Restricted or unclear-license material remains reference-only unless terms justify another role.

Historically completed external corpora should be reconciled from compatible prior evidence before fresh re-review. Current lifecycle truth lives in [`CURATION_QUEUE.md`](CURATION_QUEUE.md); historical issue/PR records remain evidence only unless current governance explicitly re-establishes them.

## Repository map

| Area | Purpose |
|---|---|
| [`AGENT_START_HERE.md`](AGENT_START_HERE.md) | Agent routing and capability floor |
| [`AGENTS.md`](AGENTS.md) | Repository-wide agent contract |
| [`skills/`](skills/) | First-party user-facing corpus |
| [`skills/sources/`](skills/sources/) | Intact exact-revision external reference corpora |
| [`INDEX.md`](INDEX.md) / [`index.json`](index.json) | Hand-maintained passive catalog snapshots |
| [`CURATION_QUEUE.md`](CURATION_QUEUE.md) | Living curation and source-vetting ledger |
| [`registry/sources.yaml`](registry/sources.yaml) | Source identities, roles, pins, licenses, paths |
| [`registry/skills/`](registry/skills/) | Mandatory per-skill provenance companions |
| [`registry/verification/`](registry/verification/) | Exact-version semantic review evidence |
| [`engine/skills/`](engine/skills/) | Passive repository-use/curation procedures |
| [`docs/GOVERNANCE_INDEX.md`](docs/GOVERNANCE_INDEX.md) | Current governance precedence |
| [`docs/SYSTEM_STATE.md`](docs/SYSTEM_STATE.md) | Current live corpus and architecture snapshot |

## Licensing

First-party content is MIT-licensed. Third-party repositories and materially derived content retain their applicable upstream obligations; the root MIT license does not relicense pinned source corpora. See [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md) and [`docs/third-party-provenance.md`](docs/third-party-provenance.md).