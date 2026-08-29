# Historical Initial-Implementation Boundary

> **Status: SUPERSEDED AS CURRENT GOVERNANCE**
>
> This document previously defined an execution-oriented alpha finish line with repository-owned proof, preflight, and evaluation machinery. That architecture is no longer current.

`skillz` is an entirely passive repository. The external AI agent reading it performs discovery, reasoning, curation, evaluation, installation, browsing, editing, or other active work through capabilities supplied by its host.

The historical implementation discussion remains recoverable in Git history. Do not treat removed scripts, tests, CI, runtime proof, catalog generators, or evaluator harnesses as current requirements.

## Current foundation

The useful foundation is the passive contract:

1. a human can understand what `skillz` is from `README.md`;
2. an external agent can enter through `AGENT_START_HERE.md` and `BOOTSTRAP.md`;
3. the agent can inspect legitimately available user context and identify durable repeatable methods;
4. all user-facing reference material lives under `skills/`, including pinned source corpora under `skills/sources/`;
5. source provenance and individual skill quality are distinct;
6. exact-version review state, tags, freshness, dependencies, authority, portability, and source context are available to inform selection where established;
7. the agent can choose reuse, adaptation, extraction, supplementation, composition, custom creation, checklist, dynamic behavior, or no change;
8. returning-user refinement starts from the existing fitted set rather than rebuilding from zero;
9. any external behavioral evaluation or installation is performed by the host agent and reported truthfully;
10. the repository itself remains passive.

## Current finish line

Current production-readiness work is corpus-centered rather than runtime-centered:

- finish the unified `skills/` tree and passive documentation cleanup;
- establish full eligible denominators source by source;
- provide adequate provenance companions for eligible skills;
- characterize dependencies, authority, portability, freshness, and intended use;
- apply controlled tags consistently;
- give every eligible skill a decisive current static state;
- reconcile passive catalog/count snapshots with the live corpus;
- keep source reputation/adoption signals contextual rather than using them as quality proof;
- only after static corpus completion, behaviorally validate consequential/high-use skills through an external evaluation environment.

## Behavioral evidence

Representative behavioral evidence remains valuable. It simply does not require or justify an execution harness inside `skillz`.

An external evaluator may test questions such as:

- Does an eligible reference get reused or minimally adapted when it genuinely fits?
- Does the agent refuse unsafe/unproven unchanged reuse?
- Does a poor fit lead to custom creation rather than forced reuse?
- Does a returning-user review make only justified changes?
- Can the agent correctly conclude `NO CHANGE NEEDED`?

When actual evidence exists, store it passively and distinguish it from static review.

## Current authority

Use `README.md`, `AGENT_START_HERE.md`, `AGENTS.md`, `BOOTSTRAP.md`, `docs/CONCEPT.md`, `docs/ARCHITECTURE_PLAN.md`, `docs/SYSTEM_STATE.md`, `ROADMAP.md`, `docs/GOVERNANCE_INDEX.md`, and Wayfinder Issue #35 for current direction.
