# skillz Documentation

Use this directory for current architecture, operating policy, provenance, semantic evaluation, installation, lifecycle, and historical records.

## Current status

**Core implementation is complete. The repository is in governed curation mode.**

`skillz` is passive. Its meaningful quality surface is the clarity and likely interpretation of its instructions and metadata. There is no CI gate, application runtime, executable preflight, or deterministic model-behavior proof required for repository completion.

## Start here

- [`SYSTEM_STATE.md`](SYSTEM_STATE.md) — current architecture, inventory boundaries, and curation-mode state.
- [`initial-implementation.md`](initial-implementation.md) — core completion definition.
- [`alpha-lock.md`](alpha-lock.md) — historical alpha milestone.
- [`../ROADMAP.md`](../ROADMAP.md) — current curation-oriented roadmap.
- [`BACKLOG.md`](BACKLOG.md) — remaining curation/documentation work.
- [`GOVERNANCE_INDEX.md`](GOVERNANCE_INDEX.md) — current control surfaces.

## Semantic evaluation

- [`evals/initial-alpha-matrix.md`](evals/initial-alpha-matrix.md) — representative semantic/adversarial review dimensions.
- [`evals/run-initial-alpha.md`](evals/run-initial-alpha.md) — how to perform a literal/weaker-model semantic review.
- [`evals/share-ready-semantic-review.md`](evals/share-ready-semantic-review.md) — current closeout review and findings.

These are reading/reasoning artifacts. They are not an executable test harness.

## Library curation and quality

- [`curation-policy.md`](curation-policy.md) — availability, provenance, characterization, verification, validation, and refresh policy.
- [`skill-verification.md`](skill-verification.md) — exact-version semantic quality standard.
- [`third-party-provenance.md`](third-party-provenance.md) — attribution and derived-work requirements.
- [`vendor-freshness.md`](vendor-freshness.md) — source freshness concepts and historical source checks.

Related metadata surfaces live under `../registry/`:

- `sources.yaml` — source identity, role, pin, license;
- `categories.yaml` — canonical local human categories;
- `skills/` — per-skill provenance companions;
- `verification/` — fingerprint-bound semantic quality state and tags;
- `local-verification.json` — individual first-party reviews;
- `taxonomy.yaml` — controlled characterization vocabulary.

## Fitted skill systems and installation

- [`portable-skill-profile.md`](portable-skill-profile.md) — portable representation of a fitted skill system.
- [`installation-handoff.md`](installation-handoff.md) — installation modes, authority boundaries, and completion states.
- [`evaluation-framework.md`](evaluation-framework.md) — general review principles.

## Historical material

Older Qor-era plans, gate artifacts, ledgers, and prior evaluation experiments are historical records. They may explain how the repository evolved, but they do **not** define current completion criteria or create CI/runtime requirements.

When historical and current files disagree, follow the current README, bootstrap, verification standard, system state, and semantic closeout review.