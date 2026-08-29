# skillz Documentation

This directory contains passive documentation for corpus curation, provenance, verification, portability, external behavioral evidence, and historical project records.

**`skillz` does not run. The external agent reading `skillz` performs any active work.**

No current governance document should require repository-owned scripts, tests, CI, runtimes, schedulers, monitors, installers, generators, preflight commands, or autonomous services.

## Start with governance

- [`GOVERNANCE_INDEX.md`](GOVERNANCE_INDEX.md) — authoritative governance map, precedence rules, and passive-repository invariant.
- [`curation-policy.md`](curation-policy.md) — what it means for corpus material to be available, characterized, verified, validated, and contextually understood.
- [`companion-metadata.md`](companion-metadata.md) — provenance, verification, and source-context companion contract.
- [`skill-verification.md`](skill-verification.md) — structured static review performed by an external reviewing agent.
- [`third-party-provenance.md`](third-party-provenance.md) — source inclusion, attribution, copying/adaptation, and licensing rules.
- [`vendor-freshness.md`](vendor-freshness.md) — passive pinned-source freshness policy; despite the historical filename, current third-party corpora live under `skills/sources/`.

## Current identity and state

When current and historical files disagree, use the precedence defined in [`GOVERNANCE_INDEX.md`](GOVERNANCE_INDEX.md).

Primary current surfaces are:

1. [`../README.md`](../README.md) — repository identity and purpose;
2. [`../AGENT_START_HERE.md`](../AGENT_START_HERE.md) — entry instructions for an external agent;
3. [`../AGENTS.md`](../AGENTS.md) — agent operating boundaries;
4. [`../BOOTSTRAP.md`](../BOOTSTRAP.md) — first-visit and returning-user discovery method;
5. [`CONCEPT.md`](CONCEPT.md) — project concept;
6. [`ARCHITECTURE_PLAN.md`](ARCHITECTURE_PLAN.md) — passive repository architecture;
7. [`SYSTEM_STATE.md`](SYSTEM_STATE.md) — current curation state and next frontier;
8. [`../ROADMAP.md`](../ROADMAP.md) — current curation roadmap;
9. active Wayfinder decisions, especially Issue #35 and the current linked frontier ticket.

The architecture is intentionally simple: **the repository is passive; the external agent is active.**

## Passive evidence surfaces

Related machine-readable evidence lives under `../registry/`:

- `sources.yaml` — source identity, role, revision/pin, and license context;
- `source-signals.yaml` — timestamped source visibility/maintenance context;
- `categories.yaml` — local human categories;
- `skills/` — per-skill provenance companions;
- `verification/` — exact-version quality state and tags;
- `taxonomy.yaml` — controlled characterization vocabulary.

These files store evidence. They do not cause anything to execute.

## Portability and external behavioral evidence

- [`portable-skill-profile.md`](portable-skill-profile.md) — passive representation of a fitted user skill system;
- [`installation-handoff.md`](installation-handoff.md) — guidance for an external agent performing or handing off host installation;
- [`evaluation-framework.md`](evaluation-framework.md) — principles for behavioral evaluation performed outside `skillz`.

A skill may instruct an external agent to use tools available in its host. That does not give `skillz` its own runtime.

## Historical execution-oriented material

Older files may describe prior experiments with:

- alpha locks;
- local runtimes;
- preflight scripts;
- CI/test workflows;
- generated catalogs;
- treatment/evaluator harnesses;
- Qor gates and ledgers.

Those records may remain useful history, but they are **not current repository architecture or required workflow**.

Examples include older alpha-lock, initial-implementation, feature/backlog proof trackers, evaluation runbooks, and Qor-era records. When they mention scripts, Node/Bun, CI, test runners, runtime proof, or repository-owned execution, interpret them as historical unless higher-precedence current governance explicitly says otherwise.

Current work is primarily corpus curation: establish denominators, review existing skills, maintain provenance and exact-version quality state, tag and organize the corpus, reconcile passive documentation/catalog snapshots, and later store external behavioral evidence for consequential skills.

## Passive-repository invariant

Current first-party guidance must not require `skillz` itself to run, schedule, monitor, fetch, validate, test, install, synchronize, generate, or execute anything.

Any active participation belongs to the external agent interacting with the repository.
