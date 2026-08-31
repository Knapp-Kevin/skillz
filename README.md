# 🛠️ skillz

![Reference Corpus](https://img.shields.io/badge/reference_corpus-500%2B-blue)
![First-Party Skills](https://img.shields.io/badge/first--party_skills-43-brightgreen)
![Persisted Third-Party Reviews](https://img.shields.io/badge/exact--version_reviews-181-8A2BE2)
![Registered Sources](https://img.shields.io/badge/registered_sources-19-6f42c1)
![Repository](https://img.shields.io/badge/repository-passive-blueviolet)
![License](https://img.shields.io/badge/license-MIT-green)

**A passive skill knowledge resource for AI agents.** `skillz` accumulates reusable skills, procedures, safeguards, anti-patterns, rejected examples, creator methods, standards, pinned source material, provenance, exact-version review evidence, tags, source context, catalog snapshots, and instructions so an external host agent can construct the smallest useful skill set for the user.

> **AI agent? Start with [`AGENT_START_HERE.md`](AGENT_START_HERE.md).** For first-visit or returning-user skill-system work, [`engine/skills/skill-bootstrap/SKILL.md`](engine/skills/skill-bootstrap/SKILL.md) is the canonical passive procedure.

> **Normal-use boundary:** skills created, adapted, composed, or refined for a user belong in that user's active AI/agent environment or in a portable handoff. They are **not written back into this repository** unless the user explicitly requested repository maintenance/curation.

## What `skillz` is

`skillz` is entirely passive. The external host agent is the active system.

The repository owns no runtime, scripts, tests, CI workflows, schedulers, monitors, crawlers, installers, synchronizers, preflight processes, generators, background services, vector databases, autonomous observers, or personalization services. Browsing, evaluation, installation, file mutation, external action, and behavioral validation are performed by the host agent using capabilities and authority it already possesses.

The repository provides four distinct surfaces:

1. **43 first-party user-facing skills** under [`skills/`](skills/) as maintained corpus/reference material.
2. **12 intact pinned third-party corpora** under [`skills/sources/`](skills/sources/) at exact upstream revisions.
3. **Governed provenance and exact-version evidence** under [`registry/skills/`](registry/skills/) and [`registry/verification/`](registry/verification/).
4. **Passive repository-use and curation procedures** under [`engine/skills/`](engine/skills/), excluded from user-facing inventory.

Third-party skill packages may contain their own scripts, tests, examples, fixtures, templates, or tools. Those belong to the upstream package. Preserve intact pinned sources and do not treat their tooling as repository-owned execution machinery.

## Core use

Give the repository to an AI agent and ask it to help build or refine repeatable capabilities. The agent should:

1. identify durable user needs before searching by filenames;
2. inspect only the evidence needed to understand those needs and the current host;
3. compare first-party skills, exact-version reviewed material, pinned prior art, tracked sources, and relevant standards;
4. evaluate in this order: **user fit → exact-version quality → operational fit → skill freshness → provenance/source context**;
5. choose explicitly among ADOPT, ADAPT, EXTRACT, SUPPLEMENT, COMPOSE, CREATE, CHECKLIST, DYNAMIC behavior, or NO CHANGE;
6. preserve authority, privacy, dependency, portability, and licensing boundaries;
7. produce the smallest coherent fitted system rather than maximizing reuse;
8. create/install fitted artifacts in the user's active host when supported and authorized, otherwise provide a complete portable handoff.

`NO CHANGE NEEDED` is a correct result. The corpus is accumulated knowledge and design material, not a reuse quota.

## Corpus layout

### First-party skills

[`skills/`](skills/) contains **43 active first-party user-facing skills**. Structured semantic review evidence lives in [`registry/local-verification.json`](registry/local-verification.json), and mandatory first-party provenance companions live under [`registry/skills/local-skills/`](registry/skills/local-skills/).

The first-party family is currently **43/43 provenance-complete** after the `automation-receipts` admission through issue #72. Category navigation is governed by [`registry/categories.yaml`](registry/categories.yaml) and surfaced under [`skills/categories/`](skills/categories/).

### Pinned source corpora

[`skills/sources/`](skills/sources/) contains **12 pinned upstream corpora** at exact revisions:

- Anthropic Skills
- Anthropic Knowledge Work Plugins
- Vercel Agent Skills
- Microsoft Skills
- Microsoft Azure Skills
- AWS Agent Toolkit
- Matt Pocock Skills
- Addy Osmani Agent Skills
- OpenHands Extensions
- Cline Skills
- Cloudflare Skills
- Google Agents CLI

These corpora are available prior art, not blanket endorsements. Physical presence, official branding, stars, forks, or repository age do not prove individual skill quality.

Exact source identity, role, license/terms, and pins live in [`registry/sources.yaml`](registry/sources.yaml). The registry currently contains **19 unique source identities** across pinned-reference, tracked-corpus, normative-spec, and dynamic-discovery roles. Volatile source-level signals belong separately in [`registry/source-signals.yaml`](registry/source-signals.yaml).

### Governed third-party evidence

- [`registry/skills/`](registry/skills/) records per-skill provenance and canonical source identity.
- [`registry/verification/`](registry/verification/) records exact-version semantic quality, fingerprints, tags, authority, portability, dependencies, and disposition.

There are currently **181 persisted exact-version third-party verification companions**. Historical source-level review work is broader than the current one-file companion shelf for some admitted corpora, so reconciliation remains ongoing rather than being silently treated as either complete or lost.

## Quality states

Current quality semantics are defined in [`docs/skill-verification.md`](docs/skill-verification.md):

- **`verified`**: the exact version passed structured semantic review.
- **`validated`**: verified plus representative external scenario/adversarial evidence.
- **`unverified`**: reference/design evidence only.
- **`trusted-baseline`**: legacy characterization only, not current unchanged-reuse eligibility.
- **`stale`**: prior review cannot be silently inherited by changed material.
- **`rejected` / `retired`**: excluded from normal unchanged selection, while remaining useful bounded prior art when appropriate.

A composable admitted source is statically complete only when its exact eligible denominator is established and every in-scope skill has current provenance, exact identity/fingerprint when establishable, freshness, license/terms, dependency/authority/portability characterization, controlled tags, structured review evidence, and a decisive current disposition.

Static completion comes before broad behavioral validation. `skillz` does not own an evaluator, benchmark, test harness, scenario runner, or behavioral runtime. External agents/environments may later produce behavioral evidence for consequential or high-use skills, and that evidence may be stored passively here.

## Discovery and admission

Discovery is intentionally separate from admission and quality.

**discovery surface → candidate issue/source → source-vetting → exact-version static evaluation → decisive admission result → repository persistence when justified → user-fit decision**

New third-party discoveries use the issue-first workflow in [`docs/candidate-intake.md`](docs/candidate-intake.md). Intentional discovery inputs are documented in [`docs/discovery-surfaces.md`](docs/discovery-surfaces.md), including the connected Creator Technical Resource Catalog. Discovery-surface scores, labels, recommendations, or creator attributions are intelligence only and must be resolved independently to canonical upstream evidence before admission.

## Current curation state

Core passive architecture is complete. Ongoing work is corpus enrichment and evidence reconciliation.

Current priorities:

1. complete Microsoft Skills;
2. complete Microsoft Azure Skills;
3. reconcile historically completed external corpora to one-file current companions where still incomplete;
4. continue remaining admitted creator/registered-source curation;
5. continue governed discovery/source-vetting through issue-first intake;
6. keep current governance, source registry, category navigation, and passive catalog snapshots aligned with live corpus truth.

AWS Agent Toolkit is **72/72 historically inspected and 72/72 reconciled to the current mandatory per-skill provenance + verification companion standard** at registered pin `ff1481a7bc1a04ee00ebf63d3a8a149aa6a2c546`. No AWS current-standard companion gaps remain. Negative dispositions remain preserved where unchanged upstream procedures fail the current authority or secret-handling standard; completion therefore means decisive current evidence, not universal endorsement.

Microsoft Skills curation is active at registered pin `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`: **9/189 exact-version provenance + verification companion pairs are persisted**, leaving **180 current-standard gaps**. The denominator is derived from independently front-mattered `SKILL.md` entry points in the exact pinned Git topology, not from the upstream README's inconsistent 174/175 headline counts. It includes language SDK plugin entries, real canonical `.github/skills` packages, Azure plugin packages, Deep Wiki, Microsoft 365 Agents Toolkit, and independently front-mattered nested sub-skills; duplicate exposure paths and symlink mirrors are de-duplicated, while ordinary workflow/reference `.md` files remain part of their parent package rather than separate review units.

`applicationinsights-web-ts` is rejected unchanged under the privacy/authorization rule; `skill-creator`, `cloud-solution-architect`, `copilot-sdk`, and nested plugin package `azure-identity-dotnet` are verified by structured static review; nested `azure-ai-document-intelligence-dotnet` is rejected unchanged because custom model/classifier creation and model deletion lack a distinct affirmative authorization gate and sensitive document transmission lacks a mandatory data-governance precondition; nested `azure-ai-agents-persistent-dotnet` is rejected unchanged because its primary flow creates/deletes remote agent resources and invokes tool/external-service paths without a distinct affirmative authorization boundary; nested `azure-ai-openai-dotnet` is rejected unchanged because its normal examples directly invoke metered external AI services and transmit prompts, search-derived content, audio, image-generation requests, and other application/user data without a distinct affirmative cost/data-transmission gate or mandatory approved-data-handling prerequisite; nested `azure-ai-projects-dotnet` is rejected unchanged because its normal workflows create/delete agents and other remote project resources, upload/delete datasets, create/update/delete indexes, run evaluations, invoke metered AI/search services, and allow credential-bearing connection retrieval without distinct resource/cost/data/credential authorization gates.

The Tier-4 passive catalog surfaces are present as [`INDEX.md`](INDEX.md) and [`index.json`](index.json). They are hand-maintained snapshots of current governed corpus truth and carry no generator, preflight, or executable refresh contract.

## Repository map

| Area | Purpose |
|---|---|
| [`AGENT_START_HERE.md`](AGENT_START_HERE.md) | Agent routing and capability floor |
| [`BOOTSTRAP.md`](BOOTSTRAP.md) | Human-readable first/returning workflow |
| [`AGENTS.md`](AGENTS.md) | Repository-wide agent contract |
| [`skills/`](skills/) | 43 first-party user-facing skill packages |
| [`skills/categories/`](skills/categories/) | Human browse-by-purpose navigation |
| [`skills/sources/`](skills/sources/) | 12 intact exact-revision external reference corpora |
| [`INDEX.md`](INDEX.md) | Hand-maintained human catalog snapshot |
| [`index.json`](index.json) | Hand-maintained machine catalog snapshot |
| [`CURATED.md`](CURATED.md) | Governed third-party shelf and quality semantics |
| [`CURATION_QUEUE.md`](CURATION_QUEUE.md) | Admitted-source and discovery/source-vetting ledger |
| [`registry/sources.yaml`](registry/sources.yaml) | 19 unique source identities, roles, pins, licenses, and canonical paths |
| [`registry/source-signals.yaml`](registry/source-signals.yaml) | Timestamped volatile source-level context |
| [`registry/local-verification.json`](registry/local-verification.json) | First-party individual structured semantic review records |
| [`registry/skills/`](registry/skills/) | Mandatory per-skill provenance companions |
| [`registry/verification/`](registry/verification/) | Third-party exact-version semantic review evidence |
| [`engine/skills/`](engine/skills/) | Passive repository-use/curation procedures, excluded from user-facing counts |
| [`docs/GOVERNANCE_INDEX.md`](docs/GOVERNANCE_INDEX.md) | Current governance precedence and control-surface map |
| [`docs/SYSTEM_STATE.md`](docs/SYSTEM_STATE.md) | Current live corpus and architecture snapshot |

## Licensing and attribution

First-party content is licensed under the [MIT License](LICENSE).

Third-party repositories and materially derived content retain their applicable upstream obligations. The root MIT license does not relicense pinned source corpora or separately identified third-party material.

See [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md) and [`docs/third-party-provenance.md`](docs/third-party-provenance.md).