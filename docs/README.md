# skillz Documentation

Use this directory for current architecture, operating policy, provenance, evaluation, installation, lifecycle, and historical records.

## Current status

The initial implementation foundation is complete. **Alpha is not locked yet.** Remaining blockers are materialized catalog proof plus the five isolated first-visit/returning-user journey results.

Broad corpus expansion and deeper curation are post-alpha enrichment unless they expose a defect in the core experience.

## Start here

- [`SYSTEM_STATE.md`](SYSTEM_STATE.md) — current architecture, inventory boundaries, proof status, and exact next action.
- [`initial-implementation.md`](initial-implementation.md) — where the initial implementation ends and post-alpha enrichment begins.
- [`alpha-lock.md`](alpha-lock.md) — live evidence checklist for alpha lock.
- [`../ROADMAP.md`](../ROADMAP.md) — current milestone followed by post-alpha roadmap.
- [`BACKLOG.md`](BACKLOG.md) — active execution blockers versus post-alpha work.
- [`FEATURE_INDEX.md`](FEATURE_INDEX.md) — feature-to-implementation-to-proof-state mapping.
- [`GOVERNANCE_INDEX.md`](GOVERNANCE_INDEX.md) — current control surfaces and freshness contracts.

## Run the initial alpha proof

- [`evals/initial-alpha-matrix.md`](evals/initial-alpha-matrix.md) — the five required journey classes.
- [`evals/fixtures/initial-alpha-scenarios.json`](evals/fixtures/initial-alpha-scenarios.json) — frozen synthetic inputs and evaluator-only criteria.
- [`evals/run-initial-alpha.md`](evals/run-initial-alpha.md) — materialization, preflight, isolation, scoring, and evidence procedure.
- [`evals/results/`](evals/results/) — actual behavioral evidence only after execution.

Do not give the raw fixture answer key to the treatment agent. Use `scripts/render-alpha-scenario.ts` as documented in the runbook.

## Library curation and quality

- [`curation-policy.md`](curation-policy.md) — availability, provenance, characterization, verification, validation, and refresh policy.
- [`skill-verification.md`](skill-verification.md) — exact-version quality verification standard.
- [`third-party-provenance.md`](third-party-provenance.md) — attribution and derived-work requirements.
- [`vendor-freshness.md`](vendor-freshness.md) — source freshness concepts and historical source checks.

Related machine-readable surfaces live under `../registry/`:

- `sources.yaml` — source identity, role, pin, license;
- `categories.yaml` — canonical local human categories;
- `skills/` — per-skill provenance companions;
- `verification/` — fingerprint-bound quality state and tags;
- `taxonomy.yaml` — controlled characterization vocabulary.

## Fitted skill systems and installation

- [`portable-skill-profile.md`](portable-skill-profile.md) — portable representation of a fitted execution system.
- [`installation-handoff.md`](installation-handoff.md) — installation modes, authority boundaries, and required completion states.
- [`evaluation-framework.md`](evaluation-framework.md) — skill-level behavioral evaluation principles.

## Historical material

The repository contains older Qor-era plans, gate artifacts, ledger entries, and evaluation reports. They are preserved as historical evidence and may explain how earlier features were built.

They do **not** override the current state surfaces listed above. When historical and current files disagree about present counts, architecture, workflow, or release status, follow the current governance index and system state.
