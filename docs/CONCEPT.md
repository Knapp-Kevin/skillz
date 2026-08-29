# Project Concept

## Why

Make reusable AI-agent skills easy to discover and use without forcing people to become skill-library experts, while giving agents a governed way to build and later refine the smallest skill set that actually fits a user.

## Product shape

`skillz` has two first-class surfaces:

1. **A large reusable skill library.** Humans and agents can browse, search, compare, inspect, install, adapt, or reference user-facing skills directly.
2. **A bootstrap/refinement engine.** A user can hand the repository to an AI on a first visit, or return later with an existing fitted set, and let the agent perform the comparison, creation, verification, and installation/handoff work.

The library is the asset. Bootstrap and refinement are the accessibility and synthesis layer built on top of it.

## Human experience

A person should not need to understand repository internals.

- First visit: provide the repository, let the agent discover durable needs from legitimately accessible context, compare against the governed corpus, and build the smallest useful fitted set.
- Returning visit: review the current fitted set, detect meaningful drift/gaps/overlap, preserve still-valid custom behavior, and make only justified changes.
- Direct browse: use categories, the generated catalog, provenance, and quality metadata without running bootstrap.

`NO CHANGE NEEDED` is a successful returning-user outcome.

## AI-agent experience

An agent should have an unmistakable entry route and deterministic boundaries:

- route direct-library, first-visit, returning-user, and repository-maintenance requests differently;
- compare before creation;
- prefer user fit over reuse for its own sake;
- use exact-version quality/fingerprint metadata when considering unchanged third-party reuse;
- treat unverified material as design evidence unless deliberately verified;
- create custom skills when existing material preserves the wrong assumptions, authority model, workflow, terminology, or UX;
- finish with truthful installation or portable-handoff state;
- never treat access to unrelated private connectors as permission to profile them.

## Inventory boundary

- `skills/`: local/imported user-facing library skills.
- approved indexed skills in `skills/sources/`: referenced user-facing library skills.
- `engine/skills/`: repository-operating machinery; excluded from library inventory.
- `registry/`: source, provenance, category, characterization, and exact-version quality metadata.

The library can contain hundreds of available skills while only a smaller subset has individual characterization, verification, or behavioral validation.

## Quality model

Availability and quality are separate.

- provenance establishes where a skill came from;
- characterization describes what it is useful for and its operating traits;
- verification establishes structured exact-version quality evidence;
- validation requires representative behavioral evidence;
- fingerprint drift invalidates prior characterization until refreshed.

Source reputation is discovery context, not automatic individual-skill proof.

## Scope

### In scope

- reusable user-facing skills across domains;
- pinned and attributed third-party source corpora;
- human browse/category surfaces;
- generated human/machine catalogs;
- provenance and exact-version quality metadata;
- first-visit skill discovery/synthesis;
- returning-user review/refinement;
- custom skill creation, evaluation, audit, and installation/handoff machinery;
- governed curation and ongoing corpus enrichment.

### Out of scope for initial alpha

- exhaustive verification of every available third-party skill;
- exhaustive corpus growth;
- proving every possible host installation adapter;
- replacing the execution/runtime responsibilities of the user's chosen agent host;
- using unrelated private data merely because a connector exists.

Those boundaries may evolve after alpha, but they are not prerequisites for a useful initial product.

## Success criteria

The initial product succeeds when:

1. a new user can give the repository to an AI and receive a dependable fitted skill set without shopping manually through hundreds of files;
2. governed selection refuses stale or unverified material for silent trusted unchanged reuse;
3. the agent can choose reuse, adaptation, composition, supplementation, or custom creation based on actual fit;
4. installation or a precise portable handoff is part of completion;
5. a returning user can improve an existing set without restarting from zero;
6. the system can correctly preserve a working set when no change is justified;
7. humans can still use the repository as a normal browsable skill library;
8. third-party attribution, provenance, freshness, and quality evidence remain auditable.
