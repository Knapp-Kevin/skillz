# Agent Entry Contract

This repository has **two valid operating modes**.

## Direct skill-library mode

If the user asks to browse, search, compare, inspect, install, adapt, or use a specific skill, treat `skillz` as a normal skill library.

Use `INDEX.md`, `index.json`, `skills/`, `registry/`, and allowed sources under `vendor/` to satisfy that request directly.

Do not force a full bootstrap when the user already knows what they want.

## Bootstrap mode

If a user gives you this repository or its GitHub URL and does not provide a more specific task, treat that as a request to **begin the skill bootstrap process now**.

Do not stop after describing, reviewing, or summarizing this repository unless the user explicitly asked for a repository overview.

### Default action

1. Read [`BOOTSTRAP.md`](BOOTSTRAP.md).
2. Read [`skills/skill-bootstrap/SKILL.md`](skills/skill-bootstrap/SKILL.md).
3. Inspect the relevant in-scope interaction history, memory, workspace context, existing instructions, existing skills, and recurring corrections that your current host actually exposes.
4. Infer the working methods that would benefit from durable reusable skills.
5. Search and compare this repository's accumulated local and third-party skill library.
6. Reuse, adapt, supplement, or compose existing skills when that is genuinely the best fit.
7. Create new custom skills when the user's workflow is not adequately represented, even when related reference skills exist.
8. Adversarially review and validate the resulting skill system.
9. Install the resulting skills when the current host supports installation and the required authority exists. Otherwise create the correct package and give the user the shortest beginner-readable installation handoff.

## Core rule

**The repository is both a skill library and a skill-building system.**

For direct-use requests, help the user use the library.

For bootstrap requests, optimize for the user's actual workflow rather than maximizing reuse of existing skills.

An existing skill is valuable both as something that may be used directly and as evidence that a problem may already have useful design patterns. It is not a requirement to use that implementation during bootstrap.

A bootstrap result may contain:

- existing skills used unchanged,
- existing skills adapted to the user's environment,
- existing skills supplemented with stronger patterns,
- several skills composed together,
- entirely new custom skills informed by reference implementations,
- a mix of all of the above,
- or no new skill at all when formalization would not help.

Do not force the user's workflow to fit the library. Do not diminish the library merely because bootstrap exists.

## Memory and history

When the current host exposes prior interaction history or persistent memory, use that evidence before asking the user to explain themselves again.

Look especially for:

- instructions the user repeats,
- corrections the user makes repeatedly,
- preferred completion and evidence standards,
- recurring task sequences,
- recurring tool combinations,
- approval or safety boundaries,
- places where the agent repeatedly disappoints the user in the same way,
- implicit workflows that already behave like skills but exist only in memory or conversation history.

Do not invent inaccessible history. Do not sweep unrelated private connectors merely because they exist. Follow the evidence-scope rules in `skill-bootstrap`.

## Library behavior

`INDEX.md`, `index.json`, `skills/`, and `vendor/` are useful outputs in their own right.

Experienced users and agents may browse, search, compare, reuse, and install from them directly.

During bootstrap, those same resources become the comparison and design corpus. A beginner should not be required to browse hundreds of skills manually because the agent can perform that comparison on their behalf.

## Mutation boundary

Discovery and design are read-only by default. Installing skills, writing outside the active workspace, changing permissions, publishing, sending, or making other external mutations requires the authority expected by the target environment.

A recommendation is not authorization.
