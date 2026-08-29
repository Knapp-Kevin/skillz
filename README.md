# 🛠️ skillz

![Reference Corpus](https://img.shields.io/badge/reference_corpus-500%2B-blue)
![Active Local Skills](https://img.shields.io/badge/active_local_skills-42-brightgreen)
![Engine Skills](https://img.shields.io/badge/engine_skills-7-lightgrey)
![Registered Sources](https://img.shields.io/badge/registered_sources-17-8A2BE2)
![Mode](https://img.shields.io/badge/repository-passive-blueviolet)
![License](https://img.shields.io/badge/license-MIT-green)

**Give this repository to an AI agent. It should discover which repeatable working methods would actually help you, compare the available skill ecosystem, and build the smallest dependable skill system that fits you and the environment you are using.**

You do not need to understand agent-skill formats, browse hundreds of files, clone the repository, or choose from a giant catalog yourself.

> **AI agent? Start with [`AGENT_START_HERE.md`](AGENT_START_HERE.md).** For first-visit or returning-user skill-system work, [`engine/skills/skill-bootstrap/SKILL.md`](engine/skills/skill-bootstrap/SKILL.md) is the single canonical orchestrator.

## What `skillz` is

`skillz` is a **passive instruction and reference repository**. It contains:

1. a broad reference/discovery corpus of reusable agent skills and patterns;
2. exact-version provenance and quality metadata for individually governed skills;
3. first-party user-facing skills with individual structured reviews;
4. a bootstrap instruction set that teaches an active agent how to discover, adapt, compose, create, review, and hand off a fitted skill system.

The repository itself does not run an application, observe users, schedule autonomous work, execute agents, or provide a runtime. The agent the user already has reads the repository and performs the work with capabilities it legitimately possesses.

That boundary matters. **Repository quality is evaluated semantically.** The question is whether the Markdown instructions and metadata are coherent, safe, useful, and likely to be interpreted correctly, including by a literal or weaker model. CI, executable preflights, and runtime test gates are not part of the product and are not required for completion.

## Start here

### First visit

Give your agent this repository or its URL. If you do not provide a narrower task, that is enough to begin bootstrap.

The agent should:

1. bind to its actual host, tools, authority, privacy limits, and available evidence;
2. inspect only the minimum relevant context needed to identify stable user needs;
3. translate those needs into capability requirements before searching by skill name;
4. search the local and reference corpus for whole skills and useful components;
5. distinguish governed exact-version reuse from reference/design evidence;
6. choose among `SUFFICIENT`, `ADOPT`, `ADAPT`, `SUPPLEMENT`, `COMPOSE`, `CREATE`, `CHECKLIST/HELPER`, `DYNAMIC`, or `DO NOT CREATE`;
7. extract useful mechanisms without automatically importing another author's ceremony, commands, terminology, UX, or authority model;
8. compose the smallest coherent system;
9. create the actual artifacts in the format supported by the current host;
10. adversarially review important instructions and report uncertainty honestly;
11. install when capable and authorized, or produce a complete portable handoff.

See [`BOOTSTRAP.md`](BOOTSTRAP.md) for the human-readable workflow and [`engine/skills/skill-bootstrap/SKILL.md`](engine/skills/skill-bootstrap/SKILL.md) for the canonical agent instruction contract.

### Returning visit

If you already have a fitted skill system, bootstrap starts from that system instead of pretending prior work never happened.

The agent should preserve still-valid custom behavior, identify only material drift/gaps/conflicts, re-evaluate affected capabilities, make the smallest justified change, and allow **`NO CHANGE NEEDED`** as a correct result.

## The corpus has two trust layers

### Reference and discovery corpus

The repository includes local skills plus pinned/tracked third-party corpora. Broad source material exists so an agent can discover prior art, compare methods, and extract useful patterns.

**Availability is not verification.** A skill does not become trusted merely because it exists in the repository, comes from a famous publisher, is popular, or sits next to another skill that passed review.

Material without an individual exact-version quality record is reference/design evidence only.

### Governed exact-version skills

An individually governed third-party skill has:

- exact provenance and canonical source path;
- source snapshot/version identity;
- license/attribution information;
- dependency/package characterization;
- authority and portability characterization;
- controlled metadata tags;
- exact canonical content fingerprint;
- individual structured semantic review and decisive quality state.

Those records live under:

- [`registry/skills/`](registry/skills/) for provenance;
- [`registry/verification/`](registry/verification/) for exact-version quality.

Tracked external skills can participate without copying entire upstream repositories into `vendor/`.

## First-party skills are reviewed too

The 42 active local skills under [`skills/`](skills/) do not receive a quality exemption because this repository authored them.

Their exact-version structured reviews live in [`registry/local-verification.json`](registry/local-verification.json). The manifest records a fingerprint, 20-point semantic quality score, controlled tags, authority, portability, quality state, and material review notes for each active local skill.

The closeout review found and repaired three concrete first-party defects:

- `deck-outline` no longer depends on a rejected vendored presentation skill;
- `finance-review` no longer depends on a rejected vendored spreadsheet skill;
- `agent-home-doctor` now requires explicit approval of the exact cleanup plan before destructive mutation.

First-party confidence is not evidence either.

## Quality states

The normative rubric is [`docs/skill-verification.md`](docs/skill-verification.md).

- **`verified`**: the exact version passed the structured semantic quality gate.
- **`validated`**: `verified` plus representative scenario/adversarial semantic review.
- **`unverified`**: design/reference evidence only.
- **`trusted-baseline`**: legacy schema state only, not current unchanged-selection eligibility.
- **`stale`**: prior review should not be silently inherited by changed content/evidence.
- **`rejected` / `retired`**: excluded from normal unchanged selection.

Only `verified` and `validated` are current unchanged-reuse quality states, and even those still require matching identity, acceptable provenance/license/dependencies/authority/portability, and actual user fit.

`validation_status: not-run` means only that no separate scenario-level semantic validation was recorded beyond the structured review. It is not a missing runtime test and is not, by itself, a completion blocker.

## Components can be more useful than whole skills

Bootstrap explicitly reasons below whole-skill granularity. A reference may contribute trigger logic, decision gates, evidence requirements, procedure fragments, failure handling, authority boundaries, output contracts, or useful abstractions.

Borrowing a component does **not** bypass provenance, license, dependency, rejection/staleness reasons, privacy, authority, cost, or host assumptions. The goal is to preserve the useful mechanism while leaving behind baggage that does not fit the user.

## Evaluation model

Because `skillz` is passive, the meaningful evaluation surface is textual:

- structured semantic review of each governed skill;
- adversarial reading of the bootstrap and front-door instructions;
- representative scenarios that challenge triggers, non-triggers, authority, host adaptation, component reuse, composition, returning-user refinement, and no-change outcomes;
- literal/weaker-model readings looking for ambiguity, contradictory sequencing, hidden assumptions, or opportunities to falsely claim completion.

These reviews are probabilistic. They increase confidence that an agent will interpret the instructions correctly; they do not pretend deterministic model behavior can be proven.

The current closeout review is recorded in [`docs/evals/share-ready-semantic-review.md`](docs/evals/share-ready-semantic-review.md).

## Current status: core complete, curation mode

The core repository is considered complete when:

- the passive bootstrap route is explicit and low-confusion;
- user synthesis is clearly separated from repository maintenance;
- governed skills have individual metadata and semantic review;
- broad unreviewed source material is clearly limited to reference/design use;
- first-party user-facing skills are individually reviewed;
- front-door documentation agrees on quality states and workflow boundaries;
- adversarial semantic review finds no unresolved repository-level ambiguity that materially threatens the intended process.

That is the completion boundary. Future work is **curation**:

1. discover promising new skills or sources occasionally;
2. source-vet them;
3. admit only what adds meaningful value;
4. assign provenance, metadata, score, authority, portability, and a decisive semantic quality state;
5. reject, adapt, or retain as reference anything that does not meet the unchanged-reuse bar;
6. revisit the bootstrap only when real feedback or repeated semantic review exposes an actual ambiguity.

More skills can make the ecosystem broader. They are no longer required to make the core repository function.

## Browse the library yourself

Humans can browse local skills by purpose under [`skills/categories/`](skills/categories/). The broader reference corpus is represented by [`INDEX.md`](INDEX.md), [`index.json`](index.json), `vendor/`, tracked source records, and the governed companions under `registry/`.

The source registry currently contains **17 sources**: 12 pinned vendored corpora, 3 selectively curated tracked external corpora, 1 normative Agent Skills specification source, and 1 dynamic-discovery source.

See [`registry/sources.yaml`](registry/sources.yaml), [`CURATED.md`](CURATED.md), and [`docs/curation-policy.md`](docs/curation-policy.md).

## Agent operating rules

For normal first-visit or returning-user work:

- read [`AGENT_START_HERE.md`](AGENT_START_HERE.md);
- use [`engine/skills/skill-bootstrap/SKILL.md`](engine/skills/skill-bootstrap/SKILL.md) as the canonical orchestrator;
- search capabilities before filenames;
- stop collecting evidence when more evidence is unlikely to change capability requirements;
- stop searching when all material requirements have an adequate governed/adaptation/custom path;
- do not mutate the `skillz` repository while building the user's skill system;
- do not default to repo-bound `skill-forge`, `skill-audit`, or `skill-sync` during normal user work;
- never fabricate fingerprints, review state, installation, artifacts, or inaccessible evidence;
- finish with an explicit installation/handoff state.

Repository-maintenance helpers under `engine/` and `scripts/` are optional conveniences for maintainers. They are not a runtime, not part of normal bootstrap, and not completion gates.

## No CI gate

This repository intentionally has no CI requirement. There is no application runtime here whose correctness can be established by a CI pipeline. Semantic review, metadata discipline, provenance, and adversarial instruction review are the relevant quality controls.

## Repository map

| Area | Purpose |
|---|---|
| [`AGENT_START_HERE.md`](AGENT_START_HERE.md) | Agent routing and capability floor |
| [`BOOTSTRAP.md`](BOOTSTRAP.md) | Human-readable first/returning workflow |
| [`AGENTS.md`](AGENTS.md) | Repository-wide agent contract |
| [`engine/skills/skill-bootstrap/`](engine/skills/skill-bootstrap/) | Canonical normal user-flow instructions |
| [`engine/skills/`](engine/skills/) | Optional repository-maintenance procedures, excluded from user-facing counts |
| [`skills/`](skills/) | Active local user-facing skills |
| [`registry/local-verification.json`](registry/local-verification.json) | Exact-version first-party semantic reviews |
| [`vendor/`](vendor/) | Third-party reference corpora |
| [`registry/sources.yaml`](registry/sources.yaml) | Source identity, roles, pins, licenses |
| [`registry/skills/`](registry/skills/) | Third-party per-skill provenance |
| [`registry/verification/`](registry/verification/) | Third-party exact-version semantic quality/tags/evidence |
| [`CURATED.md`](CURATED.md) | Governed third-party shelf/navigation policy |
| [`docs/evals/`](docs/evals/) | Semantic/adversarial review records |

## Licensing and attribution

First-party content is licensed under the [MIT License](LICENSE).

Third-party repositories and materially derived content retain applicable upstream obligations. The root MIT license does not relicense vendored or otherwise identified third-party material.

See [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md) and [`docs/third-party-provenance.md`](docs/third-party-provenance.md).