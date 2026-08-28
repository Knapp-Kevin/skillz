# Bootstrap Your Agent Skills

This is the easiest way into this repository.

You do **not** need to know what an agent skill is, which skills you need, or how this repository is organized. Point your agent at this file and ask it to bootstrap your skill system.

## Start here

Give your agent this repository and tell it:

> Read `BOOTSTRAP.md` and `skills/skill-bootstrap/SKILL.md`. Use whatever history, memory, workspace files, tools, repositories, and prior interactions you can actually access to identify the smallest useful set of reusable skills for how I work. Compare my needs against this repository before creating anything new. Do not claim to have inspected information you cannot access. Preserve my existing workflow unless a change is separately justified.

That is enough to begin.

## What the bootstrap does

The bootstrap process treats your existing behavior as evidence.

It looks for:

- workflows you repeat frequently
- reasoning patterns you repeatedly reconstruct
- sequences that coordinate several tools or systems
- places where mistakes are expensive or common
- corrections you repeatedly make to agents
- evidence, validation, security, or approval rules that matter to your work
- existing skills that already serve you well
- skills that exist implicitly in your behavior but have never been formalized
- areas where a checklist, helper, or dynamic reasoning is better than a skill

It then compares those needs against the repository's local skills and curated reference corpus.

The result is **not** "install everything." The result should be the smallest coherent skill layer that materially improves reliability, consistency, efficiency, governance, or portability.

## What the agent should produce

A successful bootstrap returns four things:

1. **Usage findings** — what recurring working patterns were actually supported by evidence.
2. **Skill decisions** — what to keep, refine, adopt, adapt, supplement, compose, create, or deliberately leave dynamic.
3. **Portable User Skill Profile** — durable execution preferences and skill selections that can move between compatible agent hosts without relying on one provider's memory system.
4. **Validation plan** — how proposed changes will be tested before they are trusted.

The profile format is defined in [`docs/portable-skill-profile.md`](docs/portable-skill-profile.md).

## How reference skills are used

This repository intentionally centralizes strong skill implementations so an agent can compare before inventing.

Reference skills are evidence, not automatic authority.

The bootstrap classifies useful references as:

- **ADOPT** — use the existing skill as-is when it already fits.
- **ADAPT** — customize a strong existing implementation for the target environment.
- **SUPPLEMENT** — keep the target skill but borrow a specific pattern that measurably strengthens it.
- **COMPOSE** — keep responsibilities separate and use both skills together.
- **BENCHMARK** — use the reference to test quality without incorporating it.
- **REJECT** — do not use it because it is redundant, unsafe, conflicting, stale, or simply worse for the job.

The user experience should remain recognizably yours. A clever external skill is not permission to replace your workflow with its author's workflow.

## Third-party skills and credit

Official and community skill sources remain attributable to their original authors and licenses.

If a local skill directly copies, materially adapts, or borrows distinctive procedures from another skill, provenance must be recorded according to [`docs/third-party-provenance.md`](docs/third-party-provenance.md).

Attribution is part of correctness, not decorative paperwork.

## Available evidence varies by host

Different agents expose different information.

A host may provide some combination of:

- current conversation history
- persistent memory
- project or workspace instructions
- repository history
- connected files and documents
- email/calendar/chat connectors
- task history
- tool invocation history

The bootstrap must use only evidence it can actually access.

If history or memory is unavailable, it should say so and continue with the evidence that exists. Missing evidence is not an invitation to manufacture a personality profile from three prompts and a hunch.

## Read-only first

Discovery and recommendation are read-only by default.

The bootstrap may propose skills, profiles, files, installation steps, or repository changes. It must not send messages, change permissions, install dependencies, mutate external systems, or deploy anything without the authority required by the target environment.

## For experienced users

If you already know the capability you need, skip bootstrap and use:

- [`INDEX.md`](INDEX.md) — human/agent-readable skill catalog
- [`index.json`](index.json) — machine-readable catalog
- [`skills/skill-eval/SKILL.md`](skills/skill-eval/SKILL.md) — baseline-versus-treatment skill evaluation
- [`skills/skill-forge/SKILL.md`](skills/skill-forge/SKILL.md) — local skill scaffolding
- [`skills/skill-audit/SKILL.md`](skills/skill-audit/SKILL.md) — structural and semantic-risk validation
- [`skills/skill-sync/SKILL.md`](skills/skill-sync/SKILL.md) — deployment to supported hosts

Bootstrap exists so beginners do not have to understand any of those pieces before getting value from them.
