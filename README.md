# 🛠️ skillz

![Reference Corpus](https://img.shields.io/badge/reference_corpus-500%2B-blue)
![First-Party Skills](https://img.shields.io/badge/first--party_skills-42-brightgreen)
![Persisted Third-Party Reviews](https://img.shields.io/badge/exact--version_reviews-101-8A2BE2)
![Registered Sources](https://img.shields.io/badge/registered_sources-17-6f42c1)
![Repository](https://img.shields.io/badge/repository-passive-blueviolet)
![License](https://img.shields.io/badge/license-MIT-green)

**A large reusable AI-skill reference library plus a passive engine that helps an existing agent discover, compare, adapt, compose, create, review, and hand off the smallest dependable skill system that fits the user.**

You do not need to understand agent-skill formats or manually read hundreds of files. Give the repository to an AI agent and let it compare the relevant material against the way you actually work.

> **AI agent? Start with [`AGENT_START_HERE.md`](AGENT_START_HERE.md).** For first-visit or returning-user skill-system work, [`engine/skills/skill-bootstrap/SKILL.md`](engine/skills/skill-bootstrap/SKILL.md) is the single canonical orchestrator.
>
> **No shell, clone, Node, or writable filesystem? That is supported.** Use whatever legitimate repository, connector, API, browser, memory, history, and artifact capabilities the current host actually exposes.

## What `skillz` is

`skillz` is a **passive instruction, skill, curation, and reference repository**. It does not run an application, observe users, schedule jobs, execute agents, or act as a runtime. The host agent is the active system. `skillz` is the body of material it reads.

The repository provides four different things that should not be confused:

1. **First-party skills** maintained under [`skills/`](skills/).
2. **A 500+ pinned reference corpus** under [`vendor/`](vendor/) drawn from 12 upstream ecosystems at exact revisions.
3. **Governed third-party review records** under [`registry/skills/`](registry/skills/) and [`registry/verification/`](registry/verification/).
4. **A passive bootstrap engine** under [`engine/`](engine/) that teaches an agent how to turn user needs and prior art into a fitted skill system.

There is intentionally no CI requirement, runtime preflight, executable proof gate, or repository-owned model benchmark. The meaningful quality surface is semantic: useful instructions, complete skill packages, provenance, licensing, metadata, individual review, and adversarial reading.

## Start here

### First visit: build a fitted skill system

The easiest path is simple:

1. Give your AI this repository or its URL.
2. Ask it to help build the repeatable skills that would make it more useful and dependable for you, or provide the repository with no narrower task.
3. Bootstrap should inspect only enough legitimate history, memory, instructions, existing skills, recurring corrections, and workflows to identify durable needs.
4. It should translate those needs into capabilities **before** searching by filenames.
5. It should compare first-party skills, governed third-party records, the pinned reference corpus, relevant tracked sources, and useful components or patterns.
6. It should choose explicitly among reuse, refinement, adaptation, supplementation, composition, clean custom creation, a lightweight helper/checklist, dynamic behavior, or no new skill.
7. It should create the smallest coherent fitted system for the host actually being used.
8. It should semantically review important instructions for ambiguity, overreach, unsafe authority, missing evidence, unnecessary ceremony, and false completion claims.
9. It should install when the host supports that and the user has authorized it, otherwise provide a complete portable handoff.

See [`BOOTSTRAP.md`](BOOTSTRAP.md) for the human-readable route and [`engine/skills/skill-bootstrap/SKILL.md`](engine/skills/skill-bootstrap/SKILL.md) for the canonical agent procedure.

### Returning visit: refine instead of reset

Start from the user's existing fitted system.

A returning review should:

1. inventory the current skills and the jobs they are meant to perform;
2. preserve custom behavior that still fits;
3. identify only material drift, gaps, conflicts, or changed needs;
4. check whether better reference material or governed skills now exist where change is plausible;
5. refine, supplement, replace, retire, or add only what is justified;
6. make the smallest useful change.

**`NO CHANGE NEEDED` is a correct result.** The goal is not infinite accumulation. It is the smallest useful set that still fits.

## Browse the library yourself

You can use `skillz` as a normal skill/reference library without running bootstrap.

### First-party skills by purpose

| Category | Typical coverage |
|---|---|
| [Planning & Productivity](skills/categories/planning-productivity/) | decisions, task coordination, learning, review, recurring personal workflows |
| [Writing & Communication](skills/categories/writing-communication/) | briefs, decks, handoffs, standups, devlogs |
| [Research & Analysis](skills/categories/research-analysis/) | comparisons, deep research, fact checking, paper review |
| [Software & Repositories](skills/categories/software-repositories/) | repository health, repo monitoring, maintenance workflows |
| [Agent Operations & Security](skills/categories/agent-operations-security/) | agent environment health, postmortems, MCP vetting, permissions |
| [Monitoring & Intelligence](skills/categories/monitoring-intelligence/) | model, platform, protocol, governance, and ecosystem scans |
| [Business & Career](skills/categories/business-career/) | career scanning, finance review, small-business operations |

### Pinned external reference corpus

[`vendor/`](vendor/) contains **12 upstream corpora pinned to exact revisions**. Together with the first-party library, this restores the broad **500+ skill/reference surface** that existed before the repository cleanup.

The pinned corpus currently includes reference material from:

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

These are **reference corpora, not blanket endorsements**. Physical availability makes them discoverable. It does not make every skill safe, current, portable, or appropriate for unchanged reuse.

### Governed third-party skills

Individual third-party skills receive stronger treatment only when reviewed and recorded separately:

- [`registry/skills/`](registry/skills/) records provenance and canonical source identity.
- [`registry/verification/`](registry/verification/) records exact-version semantic quality, fingerprints, tags, authority, portability, dependencies, and disposition.

There are currently **101 persisted exact-version third-party verification companion files** across the governed shelf. Historical source-level curation also records broader review work for several corpora. Where that work is not yet represented one-for-one in current companions, the curation queue treats reconciliation as ongoing enrichment rather than pretending the evidence never existed or that the work is finished.

See [`CURATED.md`](CURATED.md) for the governed shelf and [`CURATION_QUEUE.md`](CURATION_QUEUE.md) for the living enrichment ledger.

## What counts as a skill here?

### First-party library

[`skills/`](skills/) contains **42 active first-party user-facing skills**. All 42 have individual structured semantic review records in [`registry/local-verification.json`](registry/local-verification.json).

A skill package is not required to be Markdown-only. It may legitimately include scripts, templates, references, fixtures, JSON, examples, or other supporting components. Those components belong to the skill and are part of what should be reviewed and preserved.

### Pinned reference material

The external corpora under [`vendor/`](vendor/) are available prior art. Their presence means an agent can inspect them locally when the checkout includes submodules, while connector/API/web-capable hosts can still resolve the registered upstream source directly.

### Engine machinery does not count

[`engine/skills/`](engine/skills/) contains repository/bootstrap procedures. Those do not count as user-facing library inventory.

The passive boundary applies to the **engine**, not to the contents of individual skills. The engine is Markdown instruction. User-facing skills may contain whatever legitimate components they need.

## Availability is not verification

A skill being present in the 500+ reference corpus does not automatically make it governed unchanged-reuse material.

Current quality states are defined in [`docs/skill-verification.md`](docs/skill-verification.md):

- **`verified`**: the exact version passed the structured semantic quality gate.
- **`validated`**: `verified` plus representative scenario/adversarial semantic review.
- **`unverified`**: reference/design evidence only.
- **`trusted-baseline`**: legacy characterization only, not current unchanged-reuse eligibility.
- **`stale`**: the previous review should not be silently inherited by changed material or evidence.
- **`rejected` / `retired`**: excluded from normal unchanged selection.

Even a verified skill still has to fit the user, host, dependencies, authority boundary, licensing obligations, and intended workflow.

## Components can be more useful than whole skills

Bootstrap reasons below whole-skill granularity.

A reference may contribute only one useful mechanism, such as:

- trigger or non-trigger logic;
- evidence requirements;
- decision gates;
- authority safeguards;
- procedure fragments;
- failure handling;
- output contracts;
- review heuristics;
- useful abstractions.

The correct answer may be to extract one strong component and discard the source-specific ceremony around it. Component reuse still has to respect provenance, licensing, dependencies, rejection reasons, privacy, authority, cost, and host assumptions.

## Curation mode

The repository's **core implementation is complete**. That does not mean every interesting skill on the internet has been evaluated, nor should it.

Ongoing work is enrichment:

1. reconcile prior review evidence where historical source-level results are broader than current persisted companions;
2. continue reviewing already admitted corpora;
3. discover promising new public skill sources;
4. source-vet them independently;
5. evaluate only material that adds useful coverage or distinctive mechanisms;
6. record provenance, exact identity, metadata, authority, portability, dependencies, score, and disposition;
7. preserve useful rejected material as bounded negative/adaptation evidence when appropriate.

The current queue lives in [`CURATION_QUEUE.md`](CURATION_QUEUE.md). It includes remaining admitted-source work plus active discovery candidates such as Hugging Face Skills, Selamy Labs, Hypergiant, and other promising repositories.

Future curation broadens the ecosystem. It does **not** reopen whether the passive bootstrap architecture itself is complete.

## Evaluation responsibility

`skillz` owns the quality of the material it provides, not the competence of every model that may read it.

We make a best effort to provide:

- clear, ordered instructions;
- complete skill packages;
- useful provenance and licensing context;
- disciplined metadata;
- individual semantic quality review where governed;
- adversarial review for ambiguity, overreach, contradiction, or misleading completion claims.

We do **not** require multi-model benchmarking, deterministic behavioral proof, CI, runtime tests, or arbitrary success metrics. Model behavior is probabilistic. A sufficiently weak or noncompliant model may still fail to follow clear instructions; that alone is not a repository defect.

The current repository-level semantic closeout review is recorded in [`docs/evals/share-ready-semantic-review.md`](docs/evals/share-ready-semantic-review.md).

## If you are an AI agent reading this

Read [`AGENT_START_HERE.md`](AGENT_START_HERE.md) first.

For FIRST_VISIT or RETURNING_USER work:

1. use the canonical bootstrap;
2. bind to the actual host and authority available;
3. identify capabilities before filenames;
4. search the first-party library, governed records, pinned reference corpus, and relevant tracked sources;
5. treat availability and source reputation as context, not individual proof;
6. use verified/validated unchanged only when exact identity and fit are established;
7. adapt, supplement, compose, create, or abstain when that is a better fit;
8. preserve useful skill-owned components;
9. package for the user's host, not for this repository;
10. state installation/handoff and uncertainty truthfully.

Do not mutate `skillz` merely because the checkout is writable. User work and repository maintenance are separate routes.

## Installation is part of the user result

A fitted system should end with an explicit state such as:

- `INSTALLED + VERIFIED`
- `INSTALLED, VERIFICATION PENDING`
- `READY TO UPLOAD`
- `USER ACTION REQUIRED`
- `BLOCKED: HOST DOES NOT SUPPORT SKILLS`
- `BLOCKED: INSTALLATION METHOD NOT ESTABLISHED`

See [`docs/installation-handoff.md`](docs/installation-handoff.md).

## Repository map

| Area | Purpose |
|---|---|
| [`AGENT_START_HERE.md`](AGENT_START_HERE.md) | Agent routing and capability floor |
| [`BOOTSTRAP.md`](BOOTSTRAP.md) | Human-readable first/returning workflow |
| [`AGENTS.md`](AGENTS.md) | Repository-wide agent contract |
| [`skills/`](skills/) | 42 first-party user-facing skill packages |
| [`skills/categories/`](skills/categories/) | Human browse-by-purpose navigation |
| [`vendor/`](vendor/) | 12 pinned external reference corpora, 500+ broad skill/reference surface |
| [`CURATED.md`](CURATED.md) | Governed third-party shelf and quality semantics |
| [`CURATION_QUEUE.md`](CURATION_QUEUE.md) | Ongoing source/skill discovery, reconciliation, and evaluation ledger |
| [`registry/sources.yaml`](registry/sources.yaml) | Source identity, roles, exact pins, licenses, local reference paths |
| [`registry/local-verification.json`](registry/local-verification.json) | First-party individual review records |
| [`registry/skills/`](registry/skills/) | Third-party per-skill provenance |
| [`registry/verification/`](registry/verification/) | Third-party exact-version semantic quality records |
| [`engine/skills/skill-bootstrap/`](engine/skills/skill-bootstrap/) | Canonical normal user-flow instructions |
| [`engine/skills/`](engine/skills/) | Passive repository-maintenance procedures, excluded from user-facing counts |
| [`docs/`](docs/) | Architecture, provenance, semantic evaluation, installation, and historical context |

## Licensing and attribution

First-party content is licensed under the [MIT License](LICENSE).

Third-party repositories and materially derived content retain their applicable upstream obligations. The root MIT license does not relicense pinned reference corpora or separately identified third-party material.

See [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md) and [`docs/third-party-provenance.md`](docs/third-party-provenance.md).
