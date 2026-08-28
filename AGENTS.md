# Agent Entry Contract

This repository has **two valid operating modes** and **two different skill layers**.

## Repository structure rule

- `skills/` is the **user-facing skill library**. A skill in this directory counts as library inventory and should make sense to install or use independently of operating this repository.
- `engine/skills/` is **skillz machinery**. These skill-shaped procedures operate the bootstrap, curation, evaluation, auditing, authoring, synchronization, and source-maintenance system. They do **not** count as library inventory.
- `vendor/` contains pinned upstream reference sources. A skill hidden inside a vendored source does not count as a `skillz` library skill merely because the submodule exists.
- `registry/skills/` contains provenance and curation records for third-party skills.

The test is simple: **Would this capability make sense for a user to install independently of maintaining `skillz`?** If yes, it may belong in `skills/`. If its purpose is operating this repository's skill-building system, it belongs in `engine/skills/`.

## Direct skill-library mode

If the user asks to browse, search, compare, inspect, install, adapt, or use a specific skill, treat `skillz` as a normal skill library.

Use `INDEX.md`, `index.json`, `skills/`, `registry/`, and allowed reference sources to satisfy that request directly.

Do not force a full bootstrap when the user already knows what they want.

## Bootstrap mode

If a user gives you this repository or its GitHub URL and does not provide a more specific task, treat that as a request to **begin the skill bootstrap process now**.

Do not stop after describing, reviewing, or summarizing this repository unless the user explicitly asked for a repository overview.

### Default action

1. Read [`BOOTSTRAP.md`](BOOTSTRAP.md).
2. Read [`engine/skills/skill-bootstrap/SKILL.md`](engine/skills/skill-bootstrap/SKILL.md).
3. Inspect the relevant in-scope interaction history, memory, workspace context, existing instructions, existing skills, and recurring corrections that your current host actually exposes.
4. Infer the working methods that would benefit from durable reusable skills.
5. Search and compare this repository's accumulated skill library and allowed reference corpus.
6. Reuse, adapt, supplement, or compose existing skills when that is genuinely the best fit.
7. Create new custom skills when the user's workflow is not adequately represented, even when related reference skills exist.
8. Adversarially review and validate the resulting skill system.
9. Install the resulting skills when the current host supports installation and the required authority exists. Otherwise create the correct package and give the user the shortest beginner-readable installation handoff.

## Core rule

**The repository is both a skill library and a skill-building system.**

The library and the machinery are distinct.

For direct-use requests, help the user use the library.

For bootstrap requests, optimize for the user's actual workflow rather than maximizing reuse of existing skills.

An existing skill is valuable both as something that may be used directly and as evidence that a problem may already have useful design patterns. It is not a requirement to use that implementation during bootstrap.

A bootstrap result may contain existing skills used unchanged, adapted skills, supplemented skills, composed skills, entirely new custom skills informed by references, a mixture of those, or no new skill at all when formalization would not help.

Do not force the user's workflow to fit the library. Do not diminish the library merely because bootstrap exists.

## Memory and history

When the current host exposes prior interaction history or persistent memory, use that evidence before asking the user to explain themselves again.

Look especially for repeated instructions, recurring corrections, preferred completion standards, recurring task sequences, recurring tool combinations, approval or safety boundaries, repeated failure modes, and implicit workflows that already behave like skills but exist only in memory or conversation history.

Do not invent inaccessible history. Do not sweep unrelated private connectors merely because they exist. Follow the evidence-scope rules in `engine/skills/skill-bootstrap`.

## Library behavior

`skills/` is the primary browsable/installable library surface.

`INDEX.md` and `index.json` should report library inventory separately from engine tooling and reference-source inventory.

Experienced users and agents may browse, search, compare, reuse, and install library skills directly. During bootstrap, the library plus approved reference sources become comparison and design evidence. A beginner should not be required to browse hundreds of skills manually because the agent can perform that comparison on their behalf.

## Mutation boundary

Discovery and design are read-only by default. Installing skills, writing outside the active workspace, changing permissions, publishing, sending, or making other external mutations requires the authority expected by the target environment.

A recommendation is not authorization.
