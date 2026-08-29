# 🛠️ skillz

![Reference Corpus](https://img.shields.io/badge/reference_corpus-500%2B-blue)
![Active Local Skills](https://img.shields.io/badge/active_local_skills-42-brightgreen)
![Engine Skills](https://img.shields.io/badge/engine_skills-7-lightgrey)
![Registered Sources](https://img.shields.io/badge/registered_sources-17-8A2BE2)
![Agent Use](https://img.shields.io/badge/agent_use-no_local_runtime_required-blueviolet)
![License](https://img.shields.io/badge/license-MIT-green)

**Give this repository to an AI agent. It should discover which repeatable working methods would actually help you, compare the available skill ecosystem, and build the smallest dependable skill system that fits you and the environment you are using.**

You do not need to understand agent-skill formats, browse hundreds of files, clone the repository, or choose from a giant catalog yourself.

> **AI agent? Start with [`AGENT_START_HERE.md`](AGENT_START_HERE.md).** For first-visit or returning-user skill-system work, [`engine/skills/skill-bootstrap/SKILL.md`](engine/skills/skill-bootstrap/SKILL.md) is the single canonical orchestrator.
>
> **No shell, Node, Git, clone, or writable filesystem? That is supported.** Normal bootstrap can operate through repository-native, connector/API/web, or minimal read-only capability paths.

## What `skillz` is

`skillz` is a **passive repository** containing:

1. a broad reference/discovery corpus of reusable agent skills and patterns;
2. exact-version quality/provenance metadata for individually governed skills;
3. first-party user-facing skills with exact-version structured reviews;
4. a bootstrap engine that teaches an active agent how to discover, adapt, compose, create, validate, and hand off a fitted skill system.

The repository itself does not watch users, run an application, schedule autonomous work, or maintain a background runtime. The agent the user already has does the work with capabilities it legitimately possesses.

The product is therefore **not the largest possible skill catalog**. The product is the fitted-skill-system process.

## Start here

### First visit

Give your agent this repository or its URL. If you do not provide a narrower task, that is enough to begin bootstrap.

The agent should:

1. bind to its actual host, tools, authority, privacy limits, and available evidence;
2. inspect only the minimum relevant context needed to identify stable user needs;
3. translate those needs into capability requirements before searching by skill name;
4. search the local/reference corpus for whole skills and useful components;
5. distinguish governed exact-version reuse from reference/design evidence;
6. choose among `SUFFICIENT`, `ADOPT`, `ADAPT`, `SUPPLEMENT`, `COMPOSE`, `CREATE`, `CHECKLIST/HELPER`, `DYNAMIC`, or `DO NOT CREATE`;
7. extract useful mechanisms without automatically importing another author's ceremony, commands, terminology, UX, or authority model;
8. compose the smallest coherent system;
9. create the actual artifacts in the format supported by the current host;
10. adversarially review important behavior and report validation honestly;
11. install when capable and authorized, or produce a complete portable handoff.

See [`BOOTSTRAP.md`](BOOTSTRAP.md) for the human-readable workflow and [`engine/skills/skill-bootstrap/SKILL.md`](engine/skills/skill-bootstrap/SKILL.md) for the executable agent contract.

### Returning visit

If you already have a fitted skill system, bootstrap starts from that system instead of pretending prior work never happened.

The agent should preserve still-valid custom behavior, identify only material drift/gaps/conflicts, re-evaluate affected capabilities, make the smallest justified change, and allow **`NO CHANGE NEEDED`** as a correct result.

## The corpus has two different trust layers

### 1. Reference and discovery corpus

The repository includes local skills plus pinned/tracked third-party corpora. This broad material exists so an agent can discover prior art, compare methods, and extract useful patterns.

**Availability is not verification.**

A skill does not become trusted merely because:

- it exists under `vendor/`;
- its publisher is famous or official;
- its repository is popular;
- its source was admitted to the registry;
- a neighboring skill from the same source passed review.

Broad source material without an individual exact-version quality record is reference/design evidence only.

### 2. Governed exact-version skills

An individually governed third-party skill has:

- exact provenance and canonical source path;
- source snapshot/version identity;
- license/attribution information;
- dependency/package characterization;
- authority and portability characterization;
- controlled metadata tags;
- exact canonical content fingerprint;
- individual structured review and decisive quality state.

Those records live under:

- [`registry/skills/`](registry/skills/) for provenance;
- [`registry/verification/`](registry/verification/) for exact-version quality.

Tracked external skills can participate without copying entire upstream repositories into `vendor/`.

## First-party skills are reviewed too

The 42 active local skills under [`skills/`](skills/) do not receive a quality exemption because this repository authored them.

Their exact-version structured reviews live in:

[`registry/local-verification.json`](registry/local-verification.json)

That manifest records, per active local skill:

- Git blob fingerprint;
- structured 20-point rubric score;
- quality state;
- behavioral-validation status;
- controlled use-case/lifecycle/characteristic tags;
- authority and portability;
- material review notes.

`node scripts/verify-share-ready-corpus.ts` is designed to fail if an active local skill is added, removed, or changed without a matching current review.

During the current adversarial closeout, that local review found and repaired three real defects before certification:

- `deck-outline` no longer depends on a rejected vendored presentation skill;
- `finance-review` no longer depends on a rejected vendored spreadsheet skill;
- `agent-home-doctor` now requires explicit approval of the exact cleanup plan before destructive mutation.

That is the point of the process. First-party confidence is not evidence either.

## Quality states

The normative rubric is [`docs/skill-verification.md`](docs/skill-verification.md).

For exact third-party skill versions:

- **`verified`**: passed the current individual structured quality gate;
- **`validated`**: `verified` plus representative behavioral evidence;
- **`unverified`**: design/reference evidence only;
- **`trusted-baseline`**: legacy schema state only, not current unchanged-selection eligibility;
- **`stale`**: prior evidence no longer matches current content/evidence;
- **`rejected`** / **`retired`**: excluded from normal unchanged selection.

Only `verified` and `validated` are current unchanged-reuse quality states, and even those still require matching fingerprint, dependencies, license, authority, portability, and actual user fit.

`validation_status: not-run` means exactly what it says. Static quality review, upstream tests, source reputation, or a high score do not magically turn into behavioral validation.

## Components can be more useful than whole skills

Bootstrap explicitly reasons below whole-skill granularity.

A reference may contribute:

- trigger/non-trigger logic;
- decision gates;
- evidence requirements;
- procedure fragments;
- failure handling;
- authority boundaries;
- validation tests;
- output contracts;
- useful abstractions.

Borrowing a component does **not** bypass provenance, license, dependency, rejection/staleness reasons, privacy, authority, cost, or host assumptions.

The goal is to keep the useful mechanism and leave behind source-specific baggage that does not fit the user.

## Browse the library yourself

Humans can browse local skills by purpose under [`skills/categories/`](skills/categories/):

| Category | Examples |
|---|---|
| [Planning & Productivity](skills/categories/planning-productivity/) | daily work, decisions, task coordination, learning, weekly review |
| [Writing & Communication](skills/categories/writing-communication/) | briefs, deck outlines, handoffs, standups, devlogs |
| [Research & Analysis](skills/categories/research-analysis/) | comparisons, deep research, fact checking, paper review |
| [Software & Repositories](skills/categories/software-repositories/) | repository health, repo monitoring, TODO maintenance |
| [Agent Operations & Security](skills/categories/agent-operations-security/) | agent environment health, postmortems, MCP vetting, permissions |
| [Monitoring & Intelligence](skills/categories/monitoring-intelligence/) | model, platform, protocol, governance, ecosystem scans |
| [Business & Career](skills/categories/business-career/) | career scanning, finance review, small-business operations |

Generated indexes:

- [`INDEX.md`](INDEX.md): human-readable generated catalog;
- [`index.json`](index.json): machine-readable generated catalog.

These generated files must be refreshed and deterministically proven from a fully materialized checkout before the current share-ready candidate is declared complete. Connector-capable agents should not treat a stale generated index as a reason to stop normal user work; they can inspect current registry/provenance records directly.

## Registered sources

The source registry currently contains **17 sources**:

- 12 pinned vendored corpora;
- 3 selectively curated tracked external corpora;
- 1 normative Agent Skills specification source;
- 1 dynamic-discovery source.

Adding more sources is useful enrichment, not part of the definition of core completion once the fitted-skill process and governed corpus gates are proven.

See [`registry/sources.yaml`](registry/sources.yaml) and [`docs/curation-policy.md`](docs/curation-policy.md).

## Agent operating rules

For normal first-visit or returning-user work:

- read [`AGENT_START_HERE.md`](AGENT_START_HERE.md);
- use [`engine/skills/skill-bootstrap/SKILL.md`](engine/skills/skill-bootstrap/SKILL.md) as the canonical orchestrator;
- search capabilities before filenames;
- stop collecting evidence when more evidence is unlikely to change capability requirements;
- stop searching when all material requirements have an adequate governed/adaptation/custom path;
- do not mutate the `skillz` repository while building the user's skill system;
- do not default to repo-bound `skill-forge`, `skill-audit`, or `skill-sync` during normal user work;
- never fabricate fingerprints, validation, installation, artifacts, or inaccessible evidence;
- finish with an explicit installation/handoff state.

Repository-maintenance tasks are different. They may legitimately use the repo-bound engine helpers and maintainer runtime.

## Installation is part of completion

Each target host/surface finishes in one explicit state such as:

- `INSTALLED + VERIFIED`
- `INSTALLED, VERIFICATION PENDING`
- `READY TO UPLOAD`
- `USER ACTION REQUIRED`
- `BLOCKED: HOST DOES NOT SUPPORT SKILLS`
- `BLOCKED: INSTALLATION METHOD NOT ESTABLISHED`

See [`docs/installation-handoff.md`](docs/installation-handoff.md).

## Deterministic maintenance proof

Normal users do not need Node/Git/submodules. Maintainers do.

The current deterministic share-ready gate is:

```bash
git submodule update --init --recursive
node scripts/share-ready-preflight.ts
```

It checks:

1. exact-version coverage/metadata for all active first-party skills;
2. decisive metadata/provenance closure for individually governed third-party skills;
3. exact vendored source materialization/pins;
4. schema-v2 catalog generation and semantic invariants;
5. byte-identical second-pass catalog generation;
6. structural and semantic-risk audits;
7. repository contract tests;
8. strict characterization fingerprint integrity.

Passing that command means **ready for blind engine proof**, not that behavioral proof magically happened.

Automatic GitHub Actions remain manual-dispatch only to protect Actions budget.

## Adversarial / blind engine proof

The repository has already retired two earlier treatment sets as invalid blind evidence:

- v1 exposed evaluator answer-key material publicly;
- v2 used neutral IDs but those IDs were later publicly mapped to expected decision classes.

The active v3 public fixture is under [`docs/evals/fixtures/`](docs/evals/fixtures/). Active scenario IDs must not be publicly mapped to expected outcomes while the set is in use.

The remaining behavioral gate requires:

- a private evaluator bundle frozen outside the repository and bound to the exact public fixture;
- fresh isolated treatment contexts;
- at least one strong model;
- at least one materially weaker/cheaper model;
- a constrained connector/API/read-only host;
- demonstrated governed reuse/refusal, component extraction/composition, custom synthesis, host adaptation, returning-user minimal change, and returning-user no-op;
- classification of failures as repository ambiguity, broken/stale reference, host limitation, missing evidence, or model noncompliance.

Repeated failure at the same stage across models is presumed repository/design evidence until shown otherwise.

See [`docs/alpha-lock.md`](docs/alpha-lock.md), [`docs/evals/initial-alpha-matrix.md`](docs/evals/initial-alpha-matrix.md), and [`docs/evals/run-initial-alpha.md`](docs/evals/run-initial-alpha.md).

## Current completion status

The architecture and static closeout work are near completion, but the repository is **not yet honestly declared share-ready**.

Remaining evidence gates are deliberately concrete:

1. run `scripts/share-ready-preflight.ts` in a fully materialized network-capable checkout of the exact candidate commit and refresh generated catalog/counts;
2. freeze/verify the private v3 evaluator bundle outside the repository;
3. run the isolated strong-model, weaker-model, and constrained-host treatment proof with no active answer leakage.

Issue [#56](https://github.com/Knapp-Kevin/skillz/issues/56) is the share-ready completion map. Issue [#59](https://github.com/Knapp-Kevin/skillz/issues/59) is the blind engine-proof gate.

Once those are green, new skill/source intake becomes ecosystem enrichment rather than unfinished core work.

## Repository map

| Area | Purpose |
|---|---|
| [`AGENT_START_HERE.md`](AGENT_START_HERE.md) | Agent routing and capability floor |
| [`BOOTSTRAP.md`](BOOTSTRAP.md) | Human-readable first/returning workflow |
| [`AGENTS.md`](AGENTS.md) | Repository-wide agent contract |
| [`engine/skills/skill-bootstrap/`](engine/skills/skill-bootstrap/) | Canonical normal user-flow engine |
| [`engine/skills/`](engine/skills/) | Repo engine/maintenance procedures, excluded from user-facing counts |
| [`skills/`](skills/) | Active local user-facing skills |
| [`skills/categories/`](skills/categories/) | Human browse-by-purpose navigation |
| [`registry/local-verification.json`](registry/local-verification.json) | Exact-version first-party skill reviews |
| [`vendor/`](vendor/) | Pinned third-party reference corpora |
| [`registry/sources.yaml`](registry/sources.yaml) | Source identity, roles, pins, licenses |
| [`registry/skills/`](registry/skills/) | Third-party per-skill provenance |
| [`registry/verification/`](registry/verification/) | Third-party exact-version quality/tags/evidence |
| [`CURATED.md`](CURATED.md) | Governed third-party shelf/navigation policy |
| [`docs/`](docs/) | Architecture, curation, evaluation, installation, closeout docs |
| [`tests/`](tests/) | Contract/fixture tests |

## Licensing and attribution

First-party content is licensed under the [MIT License](LICENSE).

Third-party repositories and materially derived content retain applicable upstream obligations. The root MIT license does not relicense vendored or otherwise identified third-party material.

See [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md) and [`docs/third-party-provenance.md`](docs/third-party-provenance.md).