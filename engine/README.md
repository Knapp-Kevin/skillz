# skillz Engine

This directory contains the passive procedures that explain how to use or maintain `skillz`.

**Nothing under `engine/` counts as user-facing skill-library inventory.**

## The one normal user-flow orchestrator

For FIRST_VISIT and RETURNING_USER skill-system work, use:

- [`skills/skill-bootstrap/SKILL.md`](skills/skill-bootstrap/SKILL.md)

That is the canonical procedure for discovering user needs, translating them into capabilities, searching whole skills and reusable components, making fit decisions, composing/customizing the smallest useful system, adapting it to the active host, validating it, and installing or handing it off.

A normal bootstrap agent should not choose among the other engine skills.

## Repository-maintenance helpers

These operate the `skillz` repository or its curation/deployment lifecycle:

- `skill-forge` — scaffold a new skill **into this repository's `skills/` tree**;
- `skill-audit` — mechanically validate this repository;
- `skill-sync` — deploy portable skills that already live in this repository;
- `skills-pulse` — monitor/discover candidate sources for repository curation;
- `source-vetting` — evaluate external source suitability and characterization integrity.

Use those only when the active task is `REPOSITORY_MAINTENANCE` or when a maintainer explicitly needs their evidence.

`skill-eval` describes controlled behavioral evaluation mechanics. `skill-bootstrap` may apply the same evaluation principles when appropriate, but normal user bootstrap must not fail merely because the repo-bound evaluation machinery cannot execute.

## Critical boundary

During normal FIRST_VISIT or RETURNING_USER work:

- do not write the user's custom skills into this repository by default;
- do not require Node/Bun, Git, shell access, initialized submodules, or GitHub Actions;
- do not run repository audit/sync/forge procedures simply because they are visible;
- create/package artifacts for the user's actual host or provide a portable handoff.

A writable `skillz` checkout is not permission to turn a user's bootstrap result into a repository change.

## Verification integrity

Third-party characterization is bound to exact canonical skill content. Maintainers can run the offline drift checker at:

```text
engine/skills/source-vetting/scripts/verify-characterization-integrity.ts
```

with:

```text
node engine/skills/source-vetting/scripts/verify-characterization-integrity.ts
```

It performs no network calls. A real hash mismatch reports `STALE / REVERIFY REQUIRED`; missing uninitialized submodules are unavailable evidence rather than content drift.

## Placement rule

A reusable capability belongs in [`../skills/`](../skills/) when a user could reasonably install and use it independently of maintaining `skillz`.

A procedure belongs under `engine/` when its primary purpose is orchestrating `skillz` bootstrap or maintaining, curating, verifying, generating, validating, or deploying this repository.
