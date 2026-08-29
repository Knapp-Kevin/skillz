# User-Facing Skill Library

This directory is the single physical home for the user-facing `skillz` corpus.

It contains two governed populations:

1. **Local/directly maintained skills** — first-party or deliberately imported skills maintained directly under `skills/`.
2. **Pinned source corpora** — intact third-party repositories mounted as git submodules under [`sources/`](sources/).

Repository-maintenance procedures remain under [`../engine/skills/`](../engine/skills/) and do **not** count as user-facing library inventory.

## Browse by purpose

Start with [`categories/`](categories/) if you are browsing the locally maintained skills as a human.

- [Planning & Productivity](categories/planning-productivity/)
- [Writing & Communication](categories/writing-communication/)
- [Research & Analysis](categories/research-analysis/)
- [Software & Repositories](categories/software-repositories/)
- [Agent Operations & Security](categories/agent-operations-security/)
- [Monitoring & Intelligence](categories/monitoring-intelligence/)
- [Business & Career](categories/business-career/)

The category folders are a human navigation layer for locally maintained skills. Canonical local skill directories remain directly under `skills/` while source corpora remain intact under `skills/sources/`.

## Pinned source corpora

[`sources/`](sources/) contains the complete pinned third-party repositories used as governed reference material. They remain intact so shared references, scripts, templates, assets, licensing, and exact upstream history are not silently discarded by copying isolated `SKILL.md` files.

A source skill can be discovered, compared, mined for useful components, adapted, composed, or reused unchanged when its individual evidence supports that decision. Merely living under `skills/` does not make a third-party skill trusted.

Source identity and pins are recorded in [`../registry/sources.yaml`](../registry/sources.yaml). Per-skill provenance lives under [`../registry/skills/`](../registry/skills/) and exact-version quality evidence under [`../registry/verification/`](../registry/verification/).

## Counting rule

**Every indexed user-facing skill is represented through the `skills/` tree.**

- Local/direct skills under `skills/` count.
- Approved indexed skills inside `skills/sources/` count.
- Repository machinery under `engine/skills/` does not count.
- Normative specifications or discovery-only sources that are not installable skill corpora do not inflate the skill count.

Generated counts come from [`../INDEX.md`](../INDEX.md) and [`../index.json`](../index.json); do not infer the total by counting only immediate child directories.

## What belongs here

A capability belongs in the user-facing tree when it makes sense for a user or host agent to use it independently of maintaining `skillz` itself.

Third-party source material remains pinned and attributed. Directly imported or materially adapted third-party skills must preserve applicable licensing and provenance.

## Availability is not verification

Physical inclusion and quality are intentionally separate.

- **local/imported**: maintained directly under `skills/`;
- **pinned source reference**: available from an approved source under `skills/sources/`;
- **characterized**: has source provenance plus controlled tags/fingerprint;
- **verified**: the exact version passed the structured quality rubric;
- **validated**: representative behavioral evidence also passed;
- **unverified**: available as reference/design evidence, not trusted unchanged by default;
- **stale**: prior characterization no longer matches the current skill content/evidence;
- **rejected/retired**: excluded from normal unchanged selection;
- **engine**: repository machinery under `engine/skills/`, outside the user-facing corpus.

See [`../docs/skill-verification.md`](../docs/skill-verification.md) and [`../registry/verification/README.md`](../registry/verification/README.md).
