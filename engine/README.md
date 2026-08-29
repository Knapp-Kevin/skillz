# skillz Engine

This directory contains passive procedures that explain how to use or maintain `skillz`.

**Nothing under `engine/` counts as user-facing skill-library inventory.**

## The one normal user-flow orchestrator

For FIRST_VISIT and RETURNING_USER skill-system work, use:

- [`skills/skill-bootstrap/SKILL.md`](skills/skill-bootstrap/SKILL.md)

That is the canonical instruction set for discovering user needs, translating them into capabilities, searching whole skills and reusable components, making fit decisions, composing/customizing the smallest useful system, adapting it to the active host, semantically reviewing it, and installing or handing it off.

A normal bootstrap agent should not choose among the other engine skills.

## Repository-maintenance helpers

Other engine procedures exist to help maintain or curate this repository, for example:

- `skill-forge` — scaffold a new skill into this repository's `skills/` tree;
- `skill-audit` — inspect repository skill structure;
- `skill-sync` — help move portable skills already represented here;
- `skills-pulse` — discover candidate sources for curation;
- `source-vetting` — assess external source suitability and provenance.

These are **optional maintainer conveniences**, not a runtime, not CI, and not repository-completion gates. Normal FIRST_VISIT or RETURNING_USER work must never depend on them.

## Critical boundary

During normal user work:

- do not write the user's custom skills into this repository by default;
- do not require Node/Bun, Git, shell access, initialized submodules, or CI;
- do not run repository-maintenance procedures simply because they are visible;
- create/package artifacts for the user's actual host or provide a portable handoff.

A writable `skillz` checkout is not permission to turn a user's bootstrap result into a repository change.

## Quality boundary

The meaningful quality surface is semantic: whether instructions are coherent, safe, useful, and likely to be interpreted correctly.

Exact fingerprints and metadata help identify which text was reviewed. They do not turn this passive repository into executable software or deterministic proof.

See [`../docs/skill-verification.md`](../docs/skill-verification.md) and [`../docs/evals/share-ready-semantic-review.md`](../docs/evals/share-ready-semantic-review.md).

## Placement rule

A reusable capability belongs in [`../skills/`](../skills/) when a user could reasonably install and use it independently of maintaining `skillz`.

A procedure belongs under `engine/` when its primary purpose is orchestrating bootstrap or helping maintain/curate this repository.