# 🛠️ skillz

![Active Local Skills](https://img.shields.io/badge/active_local_skills-42-brightgreen)
![Tracked Sources](https://img.shields.io/badge/tracked_sources-17-8A2BE2)
![Repository](https://img.shields.io/badge/repository-passive-blueviolet)
![License](https://img.shields.io/badge/license-MIT-green)

**Give this repository to an AI agent. It should discover which repeatable working methods would materially help you, compare relevant prior art, and build the smallest dependable skill system that fits you and the environment you are using.**

You do not need to understand agent-skill formats, clone external repositories, or manually shop through a giant catalog.

> **AI agent? Start with [`AGENT_START_HERE.md`](AGENT_START_HERE.md).** For first-visit or returning-user skill-system work, [`engine/skills/skill-bootstrap/SKILL.md`](engine/skills/skill-bootstrap/SKILL.md) is the single canonical orchestrator.

## What `skillz` is

`skillz` is a **passive instruction and reference repository**. It contains:

1. first-party user-facing skills;
2. tracked upstream skill sources and exact-version provenance;
3. individual quality metadata for governed third-party skills;
4. structured review metadata for the first-party library;
5. bootstrap instructions that teach an active agent how to discover, adapt, compose, create, review, and hand off a fitted skill system.

The repository itself does not run an application, observe users, crawl sources, schedule work, execute agents, install anything, or provide a runtime. **The host agent is the active system. `skillz` is the resource it reads.**

There is intentionally no CI requirement, runtime preflight, test harness, or executable proof gate. The meaningful quality surface is semantic: provenance, metadata discipline, structured review, and adversarial reading of the instructions.

## Start here

### First visit

Give your agent this repository or its URL. If you provide no narrower task, that is enough to begin bootstrap.

The canonical flow is:

1. bind to the actual host, tools, authority, privacy limits, and available evidence;
2. inspect only enough relevant context to identify durable user needs;
3. translate those needs into capability requirements before searching by skill name;
4. inspect the local library, governed records, and relevant upstream references for whole skills and useful components;
5. distinguish exact-version governed reuse from reference/design evidence;
6. choose among `SUFFICIENT`, `REFINE`, `ADOPT`, `ADAPT`, `SUPPLEMENT`, `COMPOSE`, `CREATE`, `CHECKLIST/HELPER`, `DYNAMIC`, or `DO NOT CREATE`;
7. extract useful mechanisms without automatically importing another author's ceremony, terminology, commands, UX, or authority model;
8. compose the smallest coherent system;
9. create artifacts in the representation supported by the current host;
10. adversarially review the result semantically;
11. install when the host can and the user has authorized it, otherwise produce a complete portable handoff.

See [`BOOTSTRAP.md`](BOOTSTRAP.md) and the canonical [`skill-bootstrap`](engine/skills/skill-bootstrap/SKILL.md).

### Returning visit

Start from the user's existing fitted system. Preserve still-valid custom behavior, identify only material drift/gaps/conflicts, re-evaluate affected capabilities, and make the smallest justified change.

**`NO CHANGE NEEDED` is a correct outcome.**

## Library and reference model

### First-party library

The active local user-facing library lives under [`skills/`](skills/). Humans can browse it by purpose through [`skills/categories/`](skills/categories/).

All 42 active local skills have structured semantic review records in [`registry/local-verification.json`](registry/local-verification.json), including fingerprint, score, controlled tags, authority, portability, quality state, and material notes.

### Tracked upstream sources

External corpora are **not copied or mounted into this repository**. [`registry/sources.yaml`](registry/sources.yaml) records their canonical upstream locations, roles, licensing context, and pinned revisions where established.

A tracked source is a discovery/prior-art surface. Source reputation, popularity, or official branding never grants blanket skill quality.

### Governed third-party skills

When an individual external skill is deliberately reviewed, its records live under:

- [`registry/skills/`](registry/skills/) for provenance and canonical source identity;
- [`registry/verification/`](registry/verification/) for exact-version semantic quality and controlled metadata.

A governed record may establish stronger eligibility for that exact skill version. It does not promote the rest of its source repository by association.

## Quality states

The normative rubric is [`docs/skill-verification.md`](docs/skill-verification.md).

- **`verified`**: the exact version passed the structured semantic quality gate.
- **`validated`**: `verified` plus representative scenario/adversarial semantic review.
- **`unverified`**: reference/design evidence only.
- **`trusted-baseline`**: legacy schema state only, not current unchanged-selection eligibility.
- **`stale`**: prior review should not be silently inherited by changed content/evidence.
- **`rejected` / `retired`**: excluded from normal unchanged selection.

Even `verified` or `validated` material still has to fit the user, host, authority boundary, dependencies, and licensing obligations.

## Components can be more useful than whole skills

Bootstrap reasons below whole-skill granularity. A reference may contribute trigger logic, decision gates, evidence requirements, procedure fragments, safeguards, failure handling, authority boundaries, output contracts, or useful abstractions.

Borrowing a component does **not** bypass provenance, licensing, dependency, rejection/staleness reasons, privacy, authority, cost, or host assumptions. Keep the useful mechanism and discard source-specific baggage that does not fit.

## Evaluation model

Because `skillz` is passive, evaluation is textual and probabilistic:

- structured semantic review of governed skills;
- adversarial review of bootstrap/front-door instructions;
- trigger, non-trigger, and pressure scenarios;
- literal/weaker-model readings for ambiguity, contradictory sequencing, hidden assumptions, overreach, or false-completion opportunities.

The current closeout review is recorded in [`docs/evals/share-ready-semantic-review.md`](docs/evals/share-ready-semantic-review.md).

This cannot guarantee deterministic model behavior. It can make the intended path explicit enough that repeated misinterpretation is useful evidence of a documentation defect.

## Core status: complete, curation mode

Core functionality is complete when:

- one explicit bootstrap route exists;
- user synthesis is clearly separated from repository maintenance;
- first-party skills have individual review metadata;
- governed external skills have exact provenance and decisive semantic quality records;
- unreviewed upstream material is clearly reference-only;
- front-door and engine documentation agree on workflow and quality semantics;
- adversarial semantic review finds no unresolved material repository-level ambiguity.

That boundary is now satisfied. Ongoing work is **curation**:

1. occasionally discover promising new skills or sources;
2. source-vet them;
3. admit only differentiated value;
4. evaluate selected skills individually;
5. record provenance, exact version, metadata, score, authority, portability, and disposition;
6. reject, adapt, compose, or retain as reference anything that does not meet unchanged-reuse standards;
7. revisit the bootstrap only when real feedback exposes an actual ambiguity.

More skills broaden the ecosystem. They are not unfinished core implementation.

## Repository map

| Area | Purpose |
|---|---|
| [`AGENT_START_HERE.md`](AGENT_START_HERE.md) | Agent routing and capability floor |
| [`BOOTSTRAP.md`](BOOTSTRAP.md) | Human-readable first/returning workflow |
| [`AGENTS.md`](AGENTS.md) | Repository-wide agent contract |
| [`engine/skills/skill-bootstrap/`](engine/skills/skill-bootstrap/) | Canonical normal user-flow instructions |
| [`engine/skills/`](engine/skills/) | Passive repository-maintenance procedures, excluded from user-facing counts |
| [`skills/`](skills/) | Active local user-facing skills |
| [`skills/categories/`](skills/categories/) | Human browse-by-purpose navigation |
| [`registry/local-verification.json`](registry/local-verification.json) | First-party semantic review records |
| [`registry/sources.yaml`](registry/sources.yaml) | Tracked source identity, roles, pins, licenses |
| [`registry/skills/`](registry/skills/) | Third-party per-skill provenance |
| [`registry/verification/`](registry/verification/) | Third-party exact-version semantic quality records |
| [`CURATED.md`](CURATED.md) | Governed third-party navigation and curation policy |
| [`docs/evals/`](docs/evals/) | Semantic/adversarial review records |

## Licensing and attribution

First-party content is licensed under the [MIT License](LICENSE).

Third-party material retains applicable upstream obligations. Tracking a source or reviewing a skill does not relicense it.

See [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md) and [`docs/third-party-provenance.md`](docs/third-party-provenance.md).
