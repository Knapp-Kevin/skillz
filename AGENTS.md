# Agent Entry Contract

If a user gives you this repository or its GitHub URL and does not provide a more specific task, treat that as a request to **begin the skill bootstrap process now**.

Do not stop after describing, reviewing, or summarizing this repository unless the user explicitly asked for a repository overview.

## Default action

1. Read [`BOOTSTRAP.md`](BOOTSTRAP.md).
2. Read [`skills/skill-bootstrap/SKILL.md`](skills/skill-bootstrap/SKILL.md).
3. Inspect the relevant in-scope interaction history, memory, workspace context, existing instructions, existing skills, and recurring corrections that your current host actually exposes.
4. Infer the working methods that would benefit from durable reusable skills.
5. Use this repository's local and third-party skill corpus as **reference material**, not as a menu the user must choose from.
6. Compare useful patterns, safeguards, trigger designs, validation methods, and abstractions from the corpus against the user's observed needs.
7. Build the smallest skill system that best fits the user. Reuse, adapt, supplement, or compose existing skills when that is genuinely best. Create new custom skills when that is a better fit, even when related reference skills already exist.
8. Adversarially review and validate the resulting skill system.
9. Install the resulting skills when the current host supports installation and the required authority exists. Otherwise create the correct package and give the user the shortest beginner-readable installation handoff.

## Core rule

**Optimize for the user's actual workflow, not for reuse of the repository's existing skills.**

An existing skill is evidence that a problem may already have useful design patterns. It is not a requirement to use that implementation.

The correct result may be:

- existing skills used unchanged,
- existing skills adapted to the user's environment,
- existing skills supplemented with stronger patterns,
- several skills composed together,
- entirely new custom skills informed by reference implementations,
- a mix of all of the above,
- or no new skill at all when formalization would not help.

Do not force the user's workflow to fit the catalog.

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

## The corpus is not the product

`INDEX.md`, `index.json`, `skills/`, and `vendor/` exist to give the bootstrap process strong material to compare against.

They are not the beginner experience.

Do not ask a beginner to browse hundreds of skills and choose what sounds good. The agent should do the comparison work and present a fitted result.

## Mutation boundary

Discovery and design are read-only by default. Installing skills, writing outside the active workspace, changing permissions, publishing, sending, or making other external mutations requires the authority expected by the target environment.

A recommendation is not authorization.
