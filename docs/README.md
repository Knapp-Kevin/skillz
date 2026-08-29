# skillz Documentation

## Current status

**Core implementation is complete. The repository is in governed curation mode.**

`skillz` is passive. Its quality surface is semantic: instruction clarity, complete skill packages, provenance, metadata, authority/dependency characterization, and best-effort adversarial review.

There is no CI gate, application runtime, executable preflight, model benchmark, or deterministic behavioral proof required for repository completion.

## Current architecture and workflow

- [`SYSTEM_STATE.md`](SYSTEM_STATE.md) — current architecture and curation-mode state.
- [`initial-implementation.md`](initial-implementation.md) — core completion boundary and responsibility model.
- [`../AGENT_START_HERE.md`](../AGENT_START_HERE.md) — agent routing.
- [`../BOOTSTRAP.md`](../BOOTSTRAP.md) — first-visit and returning-user workflow.
- [`../engine/skills/skill-bootstrap/SKILL.md`](../engine/skills/skill-bootstrap/SKILL.md) — canonical normal-user orchestrator.
- [`../ROADMAP.md`](../ROADMAP.md) — intentionally quiet curation-oriented roadmap.
- [`BACKLOG.md`](BACKLOG.md) — currently empty implementation backlog.

## Curation and quality

- [`curation-policy.md`](curation-policy.md) — curation policy.
- [`skill-verification.md`](skill-verification.md) — normative exact-version semantic quality standard.
- [`evaluation-framework.md`](evaluation-framework.md) — current passive semantic evaluation model.
- [`third-party-provenance.md`](third-party-provenance.md) — attribution and derived-work requirements.
- [`companion-metadata.md`](companion-metadata.md) — governed metadata concepts.

Related registry surfaces:

- `../registry/sources.yaml` — tracked upstream source identity, role, pin, and license context;
- `../registry/skills/` — governed third-party provenance;
- `../registry/verification/` — governed third-party semantic quality records;
- `../registry/local-verification.json` — first-party review records;
- `../registry/taxonomy.yaml` — controlled characterization vocabulary.

## Semantic review evidence

- [`evals/share-ready-semantic-review.md`](evals/share-ready-semantic-review.md) — current repository closeout review.
- [`evals/README.md`](evals/README.md) — distinction between current and historical evaluation records.

A skill package may include its own scripts, references, templates, fixtures, JSON, examples, or other supporting components. Those are part of the skill and should be preserved/evaluated accordingly. The **engine** is passive; that does not mean all user-facing skills must be Markdown-only.

## Installation and fitted systems

- [`portable-skill-profile.md`](portable-skill-profile.md) — portable representation of a fitted skill system.
- [`installation-handoff.md`](installation-handoff.md) — installation/handoff modes and authority boundaries.

## Historical material

Older alpha, Qor-era, model-specific, feature-index, ledger, and prior evaluation documents explain how the repository evolved. They do not define current completion criteria.

When historical and current material disagree, follow the root README, `AGENT_START_HERE.md`, `BOOTSTRAP.md`, the canonical bootstrap skill, `skill-verification.md`, `SYSTEM_STATE.md`, and the current semantic closeout review.
