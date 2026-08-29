# Agent Entry Contract

`skillz` is a passive skill library, source registry, review corpus, and instruction set. The host agent is the active system.

**Start with [`AGENT_START_HERE.md`](AGENT_START_HERE.md).**

For normal first-visit or returning-user work, use one canonical orchestrator:

[`engine/skills/skill-bootstrap/SKILL.md`](engine/skills/skill-bootstrap/SKILL.md)

## Inventory boundary

- `skills/`: first-party user-facing skills.
- `vendor/`: pinned upstream reference corpora. These broaden discovery/prior art but do not create blanket trust.
- `engine/skills/`: bootstrap and repository-maintenance procedures. Do not count them as user-facing inventory.
- `registry/sources.yaml`: source identity, role, licensing context, and exact pins where established.
- `registry/skills/`: exact provenance for individually governed third-party skills.
- `registry/verification/`: exact-version semantic quality records.
- `registry/local-verification.json`: structured review of first-party skills.
- `CURATION_QUEUE.md`: living curation evidence ledger and active frontier.

The broad repository surface is **500+ skills/reference artifacts**, but availability and individual unchanged-reuse eligibility are separate facts.

## Route before acting

Choose one route:

- **DIRECT_LIBRARY**: browse/search/compare/use a known skill.
- **FIRST_VISIT**: build a fitted skill system.
- **RETURNING_USER**: refine an existing fitted skill system.
- **REPOSITORY_MAINTENANCE**: change or curate `skillz` itself.

FIRST_VISIT and RETURNING_USER follow `skill-bootstrap`.

## Capability routing

Never require local shell, Git, Node/Bun, writable filesystem, CI, materialized submodules, or repository scripts for normal user work.

When `vendor/` is materialized, use it as local reference material. When it is not, resolve the same registered upstream sources through whatever legitimate repository/API/web capability the host has.

## Third-party reuse rule

Source reputation does not equal individual verification.

Unchanged third-party reuse requires an individually reviewed exact version whose current state is `verified` or `validated`, plus acceptable provenance, license, dependencies, authority, portability, identity confidence, and actual user fit.

- `unverified` and legacy `trusted-baseline`: reference/design evidence only.
- `stale`: do not inherit the old review silently.
- `rejected` / `retired`: exclude from normal unchanged selection.

If exact identity cannot be established, say so and take the conservative path.

## Core doctrine

**Compare before creation. User-fit before reuse. Search capabilities before filenames. Smallest coherent system over maximum skill count.**

A reference may contribute useful components without becoming the final workflow. Preserve the useful mechanism without automatically importing source-specific terminology, ceremony, commands, UX, file layout, or authority assumptions.

A skill may legitimately own scripts, references, templates, fixtures, examples, JSON, assets, or other supporting components. Preserve and evaluate those as part of the skill package. The passive boundary applies to the repository engine, not to every file inside every user-facing skill.

## Memory, privacy, and mutation

Use relevant accessible context before asking the user to repeat it. Never reconstruct unavailable history from assumptions or mine unrelated private connectors merely because they exist.

Discovery and design are read-only by default. During normal user work, do not modify `skillz`. Create or hand off artifacts for the user's actual environment.

A writable surface is not authorization to mutate it.
