# Agent Entry Contract

`skillz` is an entirely passive repository of skills, instructions, provenance, verification evidence, tags, and reference material.

The external AI agent reading the repository is the active system. `skillz` owns no runtime, scheduler, validator, installer, monitor, test runner, CI process, or executable maintenance layer.

Read [`AGENT_START_HERE.md`](AGENT_START_HERE.md) first.

## Inventory boundary

- `skills/`: the complete user-facing skill tree. Count user-facing skills here, including pinned source corpora under `skills/sources/`.
- `engine/skills/`: passive repository-maintenance instructions for an external agent. Do **not** count them as user-facing corpus inventory.
- `registry/skills/`: provenance companions for individually characterized third-party skills.
- `registry/verification/`: exact-version quality state and controlled tags.
- `registry/sources.yaml`: source identity, role, license, and pin.

Availability and quality are separate. Presence in a source corpus does not establish individual skill quality.

## Route the request

### Direct library mode

If the user asks to browse, compare, inspect, adapt, or use a known skill, work directly with the relevant corpus material. Do not force full bootstrap.

### First-visit bootstrap mode

If the user gives you this repository or its URL without a narrower task and does not present an existing fitted skill set, begin first-visit discovery.

1. Read [`BOOTSTRAP.md`](BOOTSTRAP.md) and [`engine/skills/skill-bootstrap/SKILL.md`](engine/skills/skill-bootstrap/SKILL.md).
2. Inspect only relevant history, memory, workspace context, instructions, existing skills, recurring corrections, and workflow evidence the host legitimately exposes.
3. Identify stable repeatable methods rather than simple preferences or one-off facts.
4. Compare those methods against relevant material under `skills/`.
5. For third-party candidates, inspect provenance, verification status, exact version/fingerprint when establishable, dependencies, authority, portability, and freshness.
6. Treat weakly evidenced or unverified material as design evidence rather than silently trusted unchanged material.
7. Reuse, adapt, extract, supplement, compose, create, or deliberately make no skill change based on actual fit.
8. Adversarially review consequential new or adapted behavior.
9. Return the smallest useful fitted set.
10. Any installation or external action, if requested, is performed only by the host agent using its own capabilities and authority rules.

### Returning-user refinement mode

If the user already has a fitted set, do not restart from zero.

1. Inventory the current skills and intended jobs.
2. Compare them with current working patterns and available evidence.
3. Identify meaningful drift, overlap, conflict, stale assumptions, or gaps.
4. Preserve still-valid custom behavior.
5. Search the corpus for materially better references only where a real need exists.
6. Make the smallest justified change.
7. Permit **NO CHANGE NEEDED** as a successful result.

### Repository-curation mode

If the user asks to improve `skillz` itself, curate the passive repository using the external host agent's tools.

- inspect current files and pinned sources;
- review existing skills source by source;
- reconcile source denominators;
- update provenance, verification, tags, source context, and documentation;
- improve static `SKILL.md` instructions;
- preserve third-party source integrity and licensing;
- remove stale or misleading references;
- do not create repository-owned scripts, CI, runtimes, preflight commands, background monitors, or other execution machinery.

The agent may use GitHub, web, filesystem, search, or other tools supplied by its host while doing this work. Those tools are external to `skillz`.

## Third-party quality rule

Source reputation does not equal individual skill verification.

- Characterization applies to the recorded exact skill version.
- If content or supporting assumptions materially change, reconsider the prior conclusion.
- `verified` means the recorded exact version passed structured static review.
- `validated` requires actual representative behavioral evidence in addition to static review.
- `unverified` material is design/reference evidence by default.
- `stale`, `rejected`, and `retired` material is excluded from normal unchanged selection.

When exact identity cannot be established, lower confidence rather than fabricating a match.

Use source reputation, stars, forks, maintenance activity, and official status as context only. They never upgrade an individual skill automatically.

## Core doctrine

**Compare before creation. User fit before reuse. Smallest useful set over maximum skill count.**

A reference may contribute triggers, safeguards, procedures, abstractions, decision rules, or failure handling without becoming the user's final workflow.

## Memory and privacy

Use relevant memory/history the host legitimately exposes before asking the user to reconstruct accessible information. Never invent inaccessible history. Access to a private connector is capability, not consent to mine unrelated data.

## Mutation boundary

Discovery and design are read-only by default. Repository writes, skill installation, publishing, sending, permission changes, or other side effects require the authority expected by the external host and destination.

A recommendation is not authorization.

## Passive-repository invariant

No instruction in this repository should imply that `skillz` itself executes, schedules, observes, validates, installs, synchronizes, fetches, or monitors anything.

If such language appears in a current first-party file, treat it as documentation drift and correct it.
