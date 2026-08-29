# skillz Documentation

## Current status

**Core implementation is complete. The repository is in governed curation mode.**

`skillz` is passive. Its quality surface is semantic: instruction clarity, complete skill packages, provenance, metadata, authority/dependency characterization, and best-effort adversarial review.

There is no CI gate, application runtime, executable preflight, model benchmark, or deterministic behavioral proof required for repository completion.

The repository still intentionally carries a large reference surface: 42 first-party skills plus 12 pinned external corpora contributing to a 500+ skill/reference library. The breadth is visible prior art; individual unchanged-reuse trust is narrower and governed separately.

## Current architecture and workflow

- [`SYSTEM_STATE.md`](SYSTEM_STATE.md) — current architecture, inventory boundaries, and curation-mode state.
- [`initial-implementation.md`](initial-implementation.md) — core completion boundary and responsibility model.
- [`../AGENT_START_HERE.md`](../AGENT_START_HERE.md) — agent routing.
- [`../BOOTSTRAP.md`](../BOOTSTRAP.md) — first-visit and returning-user workflow.
- [`../engine/skills/skill-bootstrap/SKILL.md`](../engine/skills/skill-bootstrap/SKILL.md) — canonical normal-user orchestrator.
- [`../ROADMAP.md`](../ROADMAP.md) — intentionally quiet curation-oriented roadmap.
- [`BACKLOG.md`](BACKLOG.md) — core implementation backlog state.

## Curation and quality

- [`../CURATION_QUEUE.md`](../CURATION_QUEUE.md) — **living public evidence ledger** for completed source-level review depth, current companion coverage, reconciliation work, admitted sources still under evaluation, and discovery candidates.
- [`../CURATED.md`](../CURATED.md) — governed third-party shelf and quality semantics.
- [`curation-policy.md`](curation-policy.md) — availability/reference versus individual governance policy.
- [`skill-verification.md`](skill-verification.md) — normative exact-version semantic quality standard.
- [`evaluation-framework.md`](evaluation-framework.md) — passive semantic evaluation model.
- [`third-party-provenance.md`](third-party-provenance.md) — attribution and derived-work requirements.
- [`companion-metadata.md`](companion-metadata.md) — governed metadata concepts.

Related corpus/registry surfaces:

- `../vendor/` — 12 exact-revision external reference corpora;
- `../registry/sources.yaml` — source identity, role, pin, license, and local reference path;
- `../registry/skills/` — governed third-party provenance;
- `../registry/verification/` — governed third-party semantic quality records;
- `../registry/local-verification.json` — first-party review records;
- `../registry/taxonomy.yaml` — controlled characterization vocabulary.

A skill package may include its own scripts, references, templates, fixtures, JSON, examples, assets, or other supporting components. Those are part of the skill and should be preserved/evaluated accordingly. The **engine** is passive; that does not mean all user-facing skills must be Markdown-only.

## Semantic review evidence

- [`evals/share-ready-semantic-review.md`](evals/share-ready-semantic-review.md) — current repository-level closeout review.
- [`evals/README.md`](evals/README.md) — distinction between current and historical evaluation records.

Repository-level semantic review answers whether the architecture and instructions are coherent enough to share. Ongoing skill/source curation is tracked in `CURATION_QUEUE.md` and is intentionally not a core-completion gate.

## Installation and fitted systems

- [`portable-skill-profile.md`](portable-skill-profile.md) — portable representation of a fitted skill system.
- [`installation-handoff.md`](installation-handoff.md) — installation/handoff modes and authority boundaries.

## Historical material

Older alpha, Qor-era, model-specific, feature-index, ledger, and prior evaluation documents explain how the repository evolved. They do not define current completion criteria.

When historical and current material disagree, follow the root README, `AGENT_START_HERE.md`, `BOOTSTRAP.md`, `AGENTS.md`, the canonical bootstrap skill, `skill-verification.md`, `SYSTEM_STATE.md`, `CURATED.md`, and `CURATION_QUEUE.md`.
