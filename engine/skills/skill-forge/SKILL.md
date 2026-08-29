---
name: skill-forge
description: >-
  Guide an external agent in authoring a minimal convention-clean skill for
  this repository. Use when the user asks to create, scaffold, forge, or add
  a skill after comparison shows that a new or adapted skill is warranted.
metadata:
  author: frostwulf.zo.computer
  category: Meta
  display-name: Skill Forge
  emoji: "⚒️"
  version: 1.1.0
  repo-bound: true
---

# Skill Forge

Guide the external host agent in creating or adapting a skill artifact in this repository. This file is passive instruction material: it does not scaffold files, run audits, regenerate catalogs, schedule work, or deploy anything by itself.

Prefer the smallest useful fitted behavior. Before creating a new skill, inspect relevant user context the host may legitimately access and compare existing first-party and reference-corpus material. An existing skill may be adopted, adapted, mined for one useful procedure, supplemented, composed with another skill, or rejected in favor of a custom artifact. Creation is not the default merely because no exact title match exists.

## Authoring flow

1. **Establish the need.** State the durable repeatable method being preserved and why ordinary context, a project-local rule, or a lightweight checklist is insufficient.
2. **Compare before creation.** Inspect relevant existing skills and evidence. Record whether the result is `ADOPT`, `ADAPT`, `EXTRACT`, `SUPPLEMENT`, `COMPOSE`, `CREATE`, `CHECKLIST`, `DYNAMIC`, or `NO CHANGE`.
3. **Define the artifact.** For a new or materially adapted skill, establish a non-colliding kebab-case name, realistic triggers, intended use, dependencies, host capabilities, authority assumptions, portability boundaries, safe fallbacks, and truthful completion expectations.
4. **Author minimally.** Use `docs/skill-template.md` as guidance when it remains consistent with current governance. Put user-facing first-party skill material under `skills/`. Keep repository-maintenance instructions under `engine/skills/` only when they are genuinely repository mechanics.
5. **Review statically.** The external agent checks the artifact against current README/governance, `docs/curation-policy.md`, `docs/skill-verification.md`, and relevant controlled taxonomy. Resolve unsupported authority, unsafe side effects, hidden host assumptions, stale paths, and unnecessary complexity before treating the artifact as ready.
6. **Maintain evidence and navigation.** When the artifact belongs to the governed corpus, update appropriate provenance/verification companions, navigation surfaces, and passive catalog snapshots directly as needed. Preserve truthful unknowns rather than inventing provenance, fingerprints, behavioral evidence, or source history.

## Passive boundary

- Do not require or introduce repository-owned scripts, generators, CI, tests, schedulers, installers, synchronizers, preflight processes, runtimes, or background services.
- Do not describe `skillz` as executing, auditing, deploying, validating, or regenerating anything. The external host agent performs any authorized action.
- Do not modify intact third-party material under `skills/sources/` in place. Treat it as pinned reference/source evidence; create first-party adaptations separately when needed.
- Do not manufacture behavioral validation. `verified` is structured static review of an exact version; `validated` requires representative behavioral evidence actually produced in an external environment.
- Do not create a skill merely to increase corpus size. A smaller, clearer instruction or no change is preferable when it fits the need.

## Completion report

Report the decision (`ADOPT` / `ADAPT` / `EXTRACT` / `SUPPLEMENT` / `COMPOSE` / `CREATE` / `CHECKLIST` / `DYNAMIC` / `NO CHANGE`), files changed, provenance or verification evidence added or updated, portability/authority caveats, and remaining evidence gaps. Never claim an audit, execution, installation, deployment, or behavioral result that did not actually occur through the external host.