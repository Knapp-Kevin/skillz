# 🛠️ skillz

![Reference Corpus](https://img.shields.io/badge/reference_corpus-500%2B-blue)
![First-Party Skills](https://img.shields.io/badge/first--party_skills-42-brightgreen)
![Persisted Third-Party Reviews](https://img.shields.io/badge/exact--version_reviews-109-8A2BE2)
![Registered Sources](https://img.shields.io/badge/registered_sources-17-6f42c1)
![Repository](https://img.shields.io/badge/repository-passive-blueviolet)
![License](https://img.shields.io/badge/license-MIT-green)

**A passive skill knowledge resource for AI agents.** `skillz` accumulates reusable skills, procedures, safeguards, anti-patterns, rejected examples, creator methods, standards, pinned source material, provenance, exact-version review evidence, tags, source context, and catalog snapshots so an external host agent can construct the smallest useful skill set for the user.

> **AI agent? Start with [`AGENT_START_HERE.md`](AGENT_START_HERE.md).** For first-visit or returning-user skill-system work, [`engine/skills/skill-bootstrap/SKILL.md`](engine/skills/skill-bootstrap/SKILL.md) is the canonical passive procedure.

## What `skillz` is

`skillz` is entirely passive. The external host agent is the active system.

The repository owns no runtime, scripts, tests, CI workflows, schedulers, monitors, crawlers, installers, synchronizers, preflight processes, generators, background services, vector databases, autonomous observers, or personalization services. Any browsing, evaluation, installation, file mutation, external action, or behavioral validation is performed by the host agent using capabilities and authority it already possesses.

The repository provides four distinct surfaces:

1. **42 first-party user-facing skills** under [`skills/`](skills/).
2. **12 intact pinned third-party corpora** under [`skills/sources/`](skills/sources/) at exact upstream revisions.
3. **Governed third-party evidence** under [`registry/skills/`](registry/skills/) and [`registry/verification/`](registry/verification/).
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
8. install only when the host supports it and the user has authorized it, otherwise provide a complete handoff.

`NO CHANGE NEEDED` is a correct result. The corpus is accumulated knowledge and design material, not a reuse quota.

See [`BOOTSTRAP.md`](BOOTSTRAP.md) for the human-readable route and [`engine/skills/skill-bootstrap/SKILL.md`](engine/skills/skill-bootstrap/SKILL.md) for the canonical agent procedure.

## Corpus layout

### First-party skills

[`skills/`](skills/) contains **42 active first-party user-facing skills**, each with structured semantic review evidence in [`registry/local-verification.json`](registry/local-verification.json).

Browse by purpose through [`skills/categories/`](skills/categories/):

| Category | Typical coverage |
|---|---|
| Planning & Productivity | decisions, coordination, learning, recurring workflows |
| Writing & Communication | briefs, decks, handoffs, standups, devlogs |
| Research & Analysis | comparisons, deep research, fact checking, paper review |
| Software & Repositories | repository health and maintenance workflows |
| Agent Operations & Security | environment health, postmortems, permissions, MCP vetting |
| Monitoring & Intelligence | model, platform, protocol, governance, and ecosystem research |
| Business & Career | career, finance, and small-business workflows |

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

Exact source identity, role, license/terms, and pins live in [`registry/sources.yaml`](registry/sources.yaml). Volatile source-level signals belong separately in [`registry/source-signals.yaml`](registry/source-signals.yaml).

### Governed third-party evidence

- [`registry/skills/`](registry/skills/) records per-skill provenance and canonical source identity.
- [`registry/verification/`](registry/verification/) records exact-version semantic quality, fingerprints, tags, authority, portability, dependencies, and disposition.

There are currently **109 persisted exact-version third-party verification companions**. Historical source-level review work is broader than the current one-file companion shelf for some admitted corpora, so reconciliation remains ongoing rather than being silently treated as either complete or lost.

## Quality states

Current quality semantics are defined in [`docs/skill-verification.md`](docs/skill-verification.md):

- **`verified`**: the exact version passed structured semantic review.
- **`validated`**: verified plus representative external scenario/adversarial evidence.
- **`unverified`**: reference/design evidence only.
- **`trusted-baseline`**: legacy characterization only, not current unchanged-reuse eligibility.
- **`stale`**: prior review cannot be silently inherited by changed material.
- **`rejected` / `retired`**: excluded from normal unchanged selection, but may remain useful bounded prior art.

A composable admitted source is statically complete only when its exact eligible denominator is established and every in-scope skill has current provenance, exact identity/fingerprint when establishable, freshness, license/terms, dependency/authority/portability characterization, controlled tags, structured review evidence, and a decisive current disposition.

Static completion comes before broad behavioral validation. `skillz` does not own an evaluator, benchmark, test harness, scenario runner, or behavioral runtime. External agents/environments may later produce behavioral evidence for consequential or high-use skills, and that evidence may be stored passively here.

## Current curation state

Core passive architecture is complete. Ongoing work is corpus enrichment and reconciliation.

Current admitted-source priority:

1. finish AWS Agent Toolkit exact-version companion closure;
2. complete Microsoft Skills;
3. complete Microsoft Azure Skills;
4. continue remaining admitted creator/registered-source curation.

Governed discovery/source-vetting may proceed in parallel. Discovery never grants quality, trust, redistribution authority, installation authority, or automatic admission.

See [`CURATION_QUEUE.md`](CURATION_QUEUE.md) for the living curation ledger and [`CURATED.md`](CURATED.md) for the governed shelf.

## Repository map

| Area | Purpose |
|---|---|
| [`AGENT_START_HERE.md`](AGENT_START_HERE.md) | Agent routing and capability floor |
| [`BOOTSTRAP.md`](BOOTSTRAP.md) | Human-readable first/returning workflow |
| [`AGENTS.md`](AGENTS.md) | Repository-wide agent contract |
| [`skills/`](skills/) | 42 first-party user-facing skill packages |
| [`skills/categories/`](skills/categories/) | Human browse-by-purpose navigation |
| [`skills/sources/`](skills/sources/) | 12 intact exact-revision external reference corpora |
| [`CURATED.md`](CURATED.md) | Governed third-party shelf and quality semantics |
| [`CURATION_QUEUE.md`](CURATION_QUEUE.md) | Admitted-source and discovery/source-vetting ledger |
| [`registry/sources.yaml`](registry/sources.yaml) | Source identity, roles, exact pins, licenses, canonical paths |
| [`registry/source-signals.yaml`](registry/source-signals.yaml) | Timestamped volatile source-level context |
| [`registry/local-verification.json`](registry/local-verification.json) | First-party individual review records |
| [`registry/skills/`](registry/skills/) | Third-party per-skill provenance |
| [`registry/verification/`](registry/verification/) | Third-party exact-version semantic review evidence |
| [`engine/skills/`](engine/skills/) | Passive repository-use/curation procedures, excluded from user-facing counts |
| [`docs/`](docs/) | Architecture, provenance, curation, evaluation evidence, and historical context |
| [`docs/GOVERNANCE_INDEX.md`](docs/GOVERNANCE_INDEX.md) | Current governance precedence and control-surface map |
| [`docs/SYSTEM_STATE.md`](docs/SYSTEM_STATE.md) | Current live corpus and architecture snapshot |

## Licensing and attribution

First-party content is licensed under the [MIT License](LICENSE).

Third-party repositories and materially derived content retain their applicable upstream obligations. The root MIT license does not relicense pinned source corpora or separately identified third-party material.

See [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md) and [`docs/third-party-provenance.md`](docs/third-party-provenance.md).
