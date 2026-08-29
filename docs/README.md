# skillz Documentation

This directory contains passive documentation for corpus curation, provenance, verification, portability, behavioral evidence, and historical project records.

`skillz` does not execute documentation, scripts, tests, preflight checks, CI, or evaluation harnesses. The external agent reading the repository performs any active work.

## Current authoritative documentation

When current and historical files disagree, use these surfaces in this order:

1. [`../README.md`](../README.md) — repository identity and user-facing purpose;
2. [`../AGENT_START_HERE.md`](../AGENT_START_HERE.md) — entry instructions for an external agent;
3. [`../AGENTS.md`](../AGENTS.md) — agent operating boundaries;
4. [`../BOOTSTRAP.md`](../BOOTSTRAP.md) — first-visit and returning-user discovery method;
5. [`CONCEPT.md`](CONCEPT.md) — project concept;
6. [`ARCHITECTURE_PLAN.md`](ARCHITECTURE_PLAN.md) — passive repository architecture;
7. [`SYSTEM_STATE.md`](SYSTEM_STATE.md) — current curation state and next frontier;
8. [`../ROADMAP.md`](../ROADMAP.md) — current curation roadmap;
9. active Wayfinder issues, especially #35 and the current linked frontier ticket.

The current architecture is simple: **the repository is passive; the external agent is active.**

## Curation and quality

- [`curation-policy.md`](curation-policy.md) — availability, provenance, characterization, verification, validation, source context, and refresh policy;
- [`companion-metadata.md`](companion-metadata.md) — companion metadata contract and interpretation order;
- [`skill-verification.md`](skill-verification.md) — exact-version structured review standard;
- [`third-party-provenance.md`](third-party-provenance.md) — attribution and derived-work requirements;
- [`vendor-freshness.md`](vendor-freshness.md) — historical name for source-freshness guidance; physical third-party sources now live under `skills/sources/`.

Related passive machine-readable surfaces live under `../registry/`:

- `sources.yaml` — source identity, role, pin, license;
- `source-signals.yaml` — timestamped source visibility/maintenance context;
- `categories.yaml` — local human categories;
- `skills/` — per-skill provenance companions;
- `verification/` — exact-version quality state and tags;
- `taxonomy.yaml` — controlled characterization vocabulary.

## Portability and external behavioral evidence

- [`portable-skill-profile.md`](portable-skill-profile.md) — portable representation of a fitted user skill system;
- [`installation-handoff.md`](installation-handoff.md) — guidance for an external agent performing or handing off host installation;
- [`evaluation-framework.md`](evaluation-framework.md) — principles for behavioral evaluation performed outside `skillz`.

These files may describe actions an external agent can perform. They must not imply that this repository itself executes those actions.

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

Examples include older `alpha-lock`, `initial-implementation`, feature/backlog proof trackers, evaluation runbooks, and Qor-era records. When they mention scripts, Node/Bun, CI, test runners, runtime proof, or repository-owned execution, interpret them as historical unless a current authoritative document explicitly re-establishes the concept.

Current work is corpus curation: establish denominators, review existing skills, maintain provenance and exact-version quality state, tag and organize the corpus, reconcile passive documentation/catalog snapshots, and later store external behavioral evidence for consequential skills.

## Passive-repository invariant

Current first-party guidance must not require `skillz` itself to run, schedule, monitor, fetch, validate, test, install, synchronize, or execute anything.

Any active participation belongs to the external agent interacting with the repository.
