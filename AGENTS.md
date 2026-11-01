# Agent Entry Contract

`skillz` is an entirely passive skill library, source registry, review corpus, and instruction set. The external host agent performs all active work; it may deposit authorized review evidence here without introducing repository-owned automation.

**Start with [`AGENT_START_HERE.md`](AGENT_START_HERE.md).** A generic “look at this repository” request uses [agent value discovery](docs/agent-value-discovery.md) before deciding whether a full personal bootstrap is warranted. Public repository access does not grant permission to mine private task history or install skills.

For normal first-visit or returning-user work, use one canonical orchestrator:

[`engine/skills/skill-bootstrap/SKILL.md`](engine/skills/skill-bootstrap/SKILL.md)

## Non-negotiable destination boundary

During normal use, **`skillz` is a read-only knowledge source, not the destination for skills derived for a user.**

Unless the user explicitly asks to maintain, curate, or change this repository itself and the request is routed as `REPOSITORY_MAINTENANCE`:

- never create, adapt, compose, refine, install, or save a user-derived skill anywhere inside this repository;
- never treat `skills/`, `engine/skills/`, `registry/`, or any other repository path as the target location for a fitted user skill;
- interpret `CREATE`, `ADAPT`, `COMPOSE`, `REFINE`, and similar bootstrap dispositions as actions on the **user's active host/environment or a portable handoff artifact**, not on `skillz`;
- if the host can write to this repository, that capability is not authorization to do so;
- if the user says “create this skill” while using `skillz` normally, create it for the user's agent/environment or provide a portable package. Do not submit it to this repository by default.

Repository admission is a separate governed maintainer activity. A useful skill discovered or generated during normal use does not become a `skillz` repository candidate merely because it exists.

## Index-first discovery and recommendation rule

The **open-ended indexed corpus**, including governed third-party records and tracked/pinned external references, is the primary discovery surface. Use [the capability directory](registry/capability-directory.json) to navigate, but treat its currently sparse skill links as unknown coverage, not negative search results. Expand by capability terms across all accessible record/source families; see [the consumer lifecycle contract](docs/consumer-discovery-and-installation.md). First-party skills are ordinary source-family members. Do not prefer, rank, or recommend them because their metadata is locally convenient or they are authored here. For all discovery routes, search by capability across available source families; preserve source ownership only as provenance. Report inaccessible source families and avoid claiming a first-party-only result represents the corpus. Eligibility remains subject to exact-version license, security, authority, privacy, and behavioral evidence.

## Inventory boundary

- `skills/`: first-party user-facing **reference/corpus material maintained by this repository**, not a destination for host-generated user skills.
- `skills/sources/<source-id>/`: intact pinned upstream reference corpora. These broaden discovery/prior art but do not create blanket trust.
- `engine/skills/`: bootstrap and repository-maintenance procedures. Do not count them as user-facing inventory.
- `registry/sources.yaml`: source identity, role, licensing context, and exact pins where established.
- `registry/skills/`: exact provenance for individually governed third-party skills.
- `registry/verification/`: exact-version semantic quality records.
- `registry/local-verification.json`: structured review of first-party skills.
- `CURATION_QUEUE.md`: living curation evidence ledger and active frontier.

The discovery ecosystem is **open-ended**. Registered/persisted review counts are snapshots rather than a ceiling, and availability and individual unchanged-reuse eligibility are separate facts.

## Route before acting

Choose one route:

- **REPOSITORY_ORIENTATION**: assess whether the library can improve this agent's work for its user; inspect relevant authorized user context only, identify direct and adjacent opportunities, deliver a short value brief without installing.
- **DIRECT_LIBRARY**: browse/search/compare/use a known skill.
- **FIRST_VISIT**: build a fitted skill system.
- **RETURNING_USER**: refine an existing fitted skill system.
- **REPOSITORY_MAINTENANCE**: change or curate `skillz` itself.

FIRST_VISIT and RETURNING_USER follow `skill-bootstrap`.

Only `REPOSITORY_MAINTENANCE` may target repository files for mutation. Every other route treats the repository as read-only unless an explicit, separate maintainer instruction changes the route.

## Capability routing

Never require local shell, Git, Node/Bun, writable filesystem, CI, materialized source corpora, repository scanners, or repository scripts for normal user work. During explicit `REPOSITORY_MAINTENANCE`, the external host may use its authorized tools to assess source material and commit passive evidence; this repository owns no scanners, scripts, tests, or CI workflows.

When `skills/sources/<source-id>/` is available in the host, use the applicable pinned corpus as local reference material. When a pinned corpus is not locally materialized or accessible through the current host, resolve the same registered upstream source through whatever legitimate repository/API/web capability the host has, preserving the registered source identity and exact pin when the task depends on exact-version evidence.

## Third-party reuse rule

Source reputation does not equal individual verification.

Unchanged third-party reuse requires an individually reviewed exact version whose current semantic state is `verified` or `validated`, acceptable exact-version package-security evidence when the package is scanner-compatible, plus acceptable provenance, license, dependencies, authority, portability, identity confidence, and actual user fit.

- semantic `verified` / `validated` does not imply a security pass; security state is governed separately by `docs/security-scanning.md`.
- security `not-run`, `failed`, `incomplete`, or `stale`: not eligible for new unchanged admission/refresh where a qualifying package scan is applicable.
- `unverified` and legacy `trusted-baseline`: reference/design evidence only.
- `stale`: do not inherit the old review silently.
- `rejected` / `retired`: exclude from normal unchanged selection.

If exact identity cannot be established, say so and take the conservative path. Root `skillz` MIT licensing applies only to first-party material; inspect controlling third-party package/child license text and preserve required notices before any copying, adaptation, packaging or redistribution. A valid license is not authority to execute, install, disclose information or access user accounts.

## Core doctrine

**Compare before creation. User-fit before reuse. Search capabilities before filenames. Smallest coherent system over maximum skill count.**

A reference may contribute useful components without becoming the final workflow. Preserve the useful mechanism without automatically importing source-specific terminology, ceremony, commands, UX, file layout, or authority assumptions.

A skill may legitimately own scripts, references, templates, fixtures, examples, JSON, assets, or other supporting components. Preserve and evaluate those as part of the skill package. The passive boundary applies to repository-owned infrastructure, not intact source-authored bundled components used by an authorized external host.

## Memory, privacy, and mutation

Use relevant accessible context before asking the user to repeat it. On a user-requested personalized skill fit assessment, prioritize observed recurring requests, friction and quality gaps over topic frequency; treat memories as summaries, not complete activity logs. A generic repository link only authorizes public orientation, not an unrestricted search of private conversations, emails or connected services. Never reconstruct unavailable history from assumptions or mine unrelated private connectors merely because they exist.

Discovery and design are read-only by default. During normal user work, do not modify `skillz`. Create or hand off artifacts for the user's actual environment.

A writable surface is not authorization to mutate it.
