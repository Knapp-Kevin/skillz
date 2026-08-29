# User-Facing Skill Library

This directory is the single physical home for the **user-facing** `skillz` corpus.

It contains two governed populations:

1. **Local/directly maintained skills**: first-party or deliberately imported reusable skills maintained directly under `skills/`.
2. **Pinned source corpora**: intact third-party repositories mounted as git submodules under [`sources/`](sources/).

The only allowed exception is repository-maintenance skills under [`../engine/skills/`](../engine/skills/). Those skills exist to help an external agent maintain `skillz` itself and do **not** count as user-facing inventory. Future repository-maintenance skills may also live under `engine/skills/` when they genuinely serve that maintenance role.

No `SKILL.md` should exist under any third root.

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

[`sources/`](sources/) contains complete pinned third-party repositories used as governed reference material. They remain intact so shared references, scripts, templates, assets, licensing, and exact upstream history are not silently discarded by copying isolated `SKILL.md` files.

A composable source skill can be discovered, compared, adapted, extracted from, composed, or reused unchanged when its individual evidence supports that decision. Merely living under `skills/` does not make a third-party skill trusted.

Not every tracked source is composable. Integrated subsystem references such as Qor-logic are intentionally tracked outside the reusable skill tree and should be recommended as whole systems when appropriate rather than mined for independent skill fragments.

Source identity and pins are recorded in [`../registry/sources.yaml`](../registry/sources.yaml). Per-skill provenance lives under [`../registry/skills/`](../registry/skills/) and exact-version quality evidence under [`../registry/verification/`](../registry/verification/).

## Counting rule

**Every user-facing skill physically owned by this repository is represented through the `skills/` tree.**

- Local/direct skills under `skills/` count.
- Eligible skills inside admitted `skills/sources/` corpora count according to their established source denominator.
- Repository-maintenance skills under `engine/skills/` do not count as user-facing inventory.
- Normative specifications, discovery-only sources, restricted references, and integrated external systems do not inflate the composable skill count.

[`../INDEX.md`](../INDEX.md) and [`../index.json`](../index.json) are **passive hand-maintained snapshots**, not generated artifacts. The live tree and current registry companions control when a snapshot drifts.

## What belongs here

A capability belongs in the user-facing tree when it makes sense for a user or host agent to use it independently of maintaining `skillz` itself.

A capability belongs under `engine/skills/` only when its purpose is maintaining, curating, reviewing, or operating on this repository as a repository-maintenance procedure.

Third-party source material remains pinned and attributed. Directly imported or materially adapted third-party skills must preserve applicable licensing and provenance.

## Availability is not verification

Physical inclusion and quality are intentionally separate.

- **local/imported**: maintained directly under `skills/`;
- **pinned source reference**: available from an admitted source under `skills/sources/`;
- **characterized**: has source provenance plus controlled tags/fingerprint;
- **verified**: the exact version passed the structured quality rubric;
- **validated**: representative external behavioral evidence also passed;
- **unverified**: available as reference/design evidence, not trusted unchanged by default;
- **stale**: prior characterization no longer matches the current skill content/evidence;
- **rejected/retired**: excluded from normal unchanged selection;
- **engine maintenance**: repository-maintenance skill under `engine/skills/`, outside user-facing corpus counts.

See [`../docs/skill-verification.md`](../docs/skill-verification.md) and [`../registry/verification/README.md`](../registry/verification/README.md).
