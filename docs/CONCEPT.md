# Project Concept

## Why

People teach AI systems how they work through repeated instructions, corrections, workflows, preferences, safeguards, and definitions of done. Those useful working methods are often trapped in one agent, one conversation history, or one product.

`skillz` helps an external agent identify the durable repeatable parts of that collaboration and express them as portable skills.

## What `skillz` is

`skillz` is an entirely passive repository containing:

1. a large reusable user-facing skill corpus;
2. instructions that teach an external agent how to discover durable user workflows;
3. provenance, verification, tagging, freshness, and source-context evidence that helps the agent reason about reference material;
4. passive guidance for adapting, extracting, composing, creating, curating, and transferring skills.

The AI agent reading the repository performs the reasoning and any requested actions. `skillz` itself executes nothing.

## What `skillz` is not

It is not:

- an application or service;
- an agent runtime or framework;
- a background observer;
- a memory database or user-model service;
- a scheduler or monitor;
- an installer or synchronization daemon;
- a CI/test system;
- a vector database;
- a self-modifying learning loop.

Any active behavior belongs to the external host agent.

## Core flow

```text
current agent experience
        ↓
inspect legitimately available user context
        ↓
identify durable repeatable methods
        ↓
compare with governed reference skills
        ↓
ADOPT / ADAPT / EXTRACT / SUPPLEMENT / COMPOSE / CREATE / NO CHANGE
        ↓
produce the smallest useful portable skill set
```

The corpus is design material, not a reuse quota.

## Human experience

A person should not need to understand repository internals.

- **First visit:** give the repository to an AI. The agent identifies durable methods from legitimate context, compares them with the corpus, and creates the smallest useful fitted set.
- **Returning visit:** the agent inventories the existing fitted set, detects meaningful drift/gaps/overlap, preserves still-valid custom behavior, and makes only justified changes.
- **Direct browse:** a human or agent may inspect skills, categories, provenance, and review evidence directly.

`NO CHANGE NEEDED` is a successful returning-user outcome.

## Agent experience

An agent should:

- distinguish direct-library, first-visit, returning-user, and repository-curation requests;
- compare before creating;
- prefer user fit over reuse for its own sake;
- distinguish preferences and project rules from reusable methods;
- inspect exact-version quality/fingerprint evidence when considering unchanged third-party reuse;
- treat unverified material as design evidence by default;
- create custom skills when existing material preserves the wrong assumptions, authority model, workflow, terminology, or UX;
- preserve provenance and licensing when third-party material materially contributes;
- never treat unrelated private connector access as permission to profile the user;
- never claim execution, validation, installation, or evidence that did not occur through the external host.

## Inventory boundary

- `skills/`: complete user-facing skill tree.
- `skills/sources/`: intact pinned third-party reference corpora within the user-facing tree.
- `engine/skills/`: passive repository-curation instructions, excluded from user-facing corpus inventory.
- `registry/`: passive source, provenance, characterization, and exact-version quality metadata.
- `docs/`: passive explanatory, curation, portability, validation, and historical documentation.

## Quality model

Availability and quality are separate.

- provenance establishes origin and obligations;
- characterization describes purpose and operating traits;
- verification establishes structured exact-version static evidence;
- validation records representative behavioral evidence produced externally;
- fingerprint or material assumption drift requires reconsideration;
- source reputation is context, not automatic skill proof.

For selection use:

**user fit → exact-version quality → operational fit → skill freshness → provenance/source context**

## Success criteria

The repository succeeds when:

1. an external agent can understand the repository without mistaking it for software that must run;
2. a new user can receive a fitted portable skill set without manually shopping through hundreds of files;
3. the agent can correctly choose reuse, adaptation, extraction, supplementation, composition, custom creation, or no change;
4. source provenance, licensing, freshness, dependencies, authority, portability, and quality evidence are legible enough to inform those choices;
5. a returning user can refine an existing set without restarting from zero;
6. the repository can be curated source by source until every eligible skill has a decisive static state;
7. any behavioral validation or installation is performed externally and reported truthfully;
8. the repository remains entirely passive.
