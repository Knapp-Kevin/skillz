# Make Your AI Better at Helping You

This repository helps an AI turn the way you already work together into reusable skills.

You do not need to know how skills work.
You do not need to know how to code.
You do not need to choose from hundreds of files.

**Give your AI the GitHub link to this repository. That is enough to start.**

## If you are the AI reading this

If the user gave you this repository or its GitHub URL and did not give you a different task, **start the bootstrap process now**.

Do not stop after summarizing the repository or telling the user that it contains useful skills.

Your job is to build the skill system that best fits this user.

Read [`engine/skills/skill-bootstrap/SKILL.md`](engine/skills/skill-bootstrap/SKILL.md) for the full procedure.

Start with relevant information your current host already exposes, especially interaction history, persistent memory, the current conversation, repeated corrections, workspace or project instructions, recurring tool use, existing skills or custom instructions, repeated workflows, and completion standards.

Do not make the user repeat information you can already access.

Do not invent history or memory you cannot access.

Do not inspect unrelated private connectors simply because they exist.

Then:

1. Find working patterns that are useful enough to preserve.
2. Identify patterns that already behave like unwritten or **latent skills**.
3. Compare those needs against the actual library in [`skills/`](skills/) and approved third-party reference sources.
4. Extract useful ideas, safeguards, procedures, triggers, validation methods, and abstractions from those references.
5. Build the smallest skill system that best matches the user's real workflow.
6. Use an existing library skill when it genuinely fits.
7. Adapt or supplement one when that produces the best result.
8. **Create a new custom skill whenever that better represents the user's needs, even if related skills already exist.**
9. Test and adversarially review the resulting skills using the engine's evaluation machinery.
10. Install them when the current system supports it and you have the required authority. Otherwise prepare the correct files and give simple installation steps.

## Library versus engine

The repository contains two different kinds of skill-shaped material.

### The library

[`skills/`](skills/) contains the skills offered as reusable capabilities.

These are the skills that count when somebody asks how many skills are in the repository.

### The engine

[`engine/skills/`](engine/skills/) contains the machinery used to run `skillz` itself: bootstrap, skill creation, evaluation, auditing, synchronization, source monitoring, and source vetting.

Those engine components do **not** count as library skills.

Pinned upstream repositories under `vendor/` are reference/source corpora. Their contents do not automatically count as library inventory either. A third-party skill becomes part of the library when it is deliberately promoted or imported according to the curation, licensing, provenance, and dependency rules.

## If you are the human reading this

The short version is:

**Your AI should do the work.**

You should not need to browse a giant list and decide which skills sound useful.

Your AI should look at how you already work together, figure out what would make that work more dependable, learn from the library and reference examples, and build the right skills for you.

## What is a skill?

A skill is a reusable set of instructions that helps an AI do something in a dependable way.

Maybe you always want your AI to check its work before saying it is finished, research before making an important recommendation, follow the same careful steps when fixing a bug, use several tools in a particular order, ask before making risky changes, create reports in a format that works for you, separate facts from guesses, or test an answer before treating it as correct.

If you have taught your AI the same kind of behavior many times, you may have already created the beginnings of a skill without calling it one.

This repository helps your AI find those patterns and turn the useful ones into something reusable.

## The library is not a shopping requirement

The repository is meant to contain a large library of useful skills.

That does **not** mean bootstrap should simply choose a few and install them.

Your AI can:

- **USE** a skill that already fits,
- **IMPROVE** one you already have,
- **ADAPT** a good reference to your needs,
- **BORROW** one useful idea from another skill,
- **COMBINE** several skills that work well together,
- **CREATE** something completely new,
- or **SKIP** anything that does not help.

The right answer may be a custom skill that never existed before.

The goal is not to reuse the most skills. The goal is to create the **smallest set of skills that makes your AI more dependable for you**.

## Your AI may already know more than you think

If your AI has access to memory or past interactions, it may already have useful evidence about how you work.

It can look for instructions you repeat, corrections you make often, things that annoy you when the AI gets them wrong, steps you almost always use, tools you often use together, rules you expect the AI to remember, and what you mean when you say something is "done."

Those patterns can become portable skills instead of staying trapped inside one AI's memory.

If the AI cannot see old conversations or memory, it should say so and make careful conclusions from the evidence it actually has.

## Compare before creating. Fit you before reusing.

Your AI should inspect relevant existing solutions before inventing a solved mechanism from scratch.

But it should not reuse something merely because it exists.

If a custom skill fits you better, build the custom skill.

Existing skills are reference evidence, not a cage.

## Will it change things automatically?

Discovery and design are read-only by default.

Your AI should not send messages, publish work, change permissions, delete things, or make unrelated outside changes just because it is running bootstrap.

Installing a skill is also a change.

If your AI can install the final skills itself and the system gives it the required authority, it can do that and verify the result.

If the AI cannot perform the installation, it should make the human part as easy as possible.

## How do I install the skills when they are ready?

You should not have to figure that out by yourself.

The bootstrap must finish in one of three broad ways:

### 1. The AI installs them

If the AI can safely write or install the skills itself, it should do that and test them.

### 2. You upload them

If a web or desktop interface requires a person to click buttons, the AI should prepare the correct artifact and give one action at a time with the exact filename and a tiny verification test.

### 3. The system cannot install skills

The AI should say so clearly and preserve the skills in a portable form for later use on a compatible system.

See [`docs/installation-handoff.md`](docs/installation-handoff.md) for the detailed contract.

## What should I get at the end?

A bootstrap should give you:

1. **What it learned about how you work** — only durable execution patterns that matter.
2. **The skill system it built for you** — existing, adapted, combined, and newly created skills as appropriate.
3. **Why each skill exists** — the problem it solves or failure it prevents.
4. **A portable skill profile** — execution defaults that can travel between compatible systems.
5. **Validation results** — what was actually tested and what still needs proof.
6. **An installation result** — installed and verified, ready to upload, user action required, or a clearly explained blocker.

You should always be able to tell what is already done, what skill files were created or selected, what you need to do next if anything, and how you know the skills are working.

## For advanced users and agents

The machinery underneath the simple experience lives in:

- [`AGENTS.md`](AGENTS.md) — default agent-entry contract
- [`engine/skills/skill-bootstrap/SKILL.md`](engine/skills/skill-bootstrap/SKILL.md) — discovery and design procedure
- [`engine/skills/skill-forge/SKILL.md`](engine/skills/skill-forge/SKILL.md) — custom skill creation
- [`engine/skills/skill-eval/SKILL.md`](engine/skills/skill-eval/SKILL.md) — behavioral evaluation
- [`engine/skills/skill-audit/SKILL.md`](engine/skills/skill-audit/SKILL.md) — structural and semantic-risk validation
- [`engine/skills/skill-sync/SKILL.md`](engine/skills/skill-sync/SKILL.md) — supported local deployment
- [`engine/skills/skills-pulse/SKILL.md`](engine/skills/skills-pulse/SKILL.md) — ecosystem scanning
- [`engine/skills/source-vetting/SKILL.md`](engine/skills/source-vetting/SKILL.md) — source evaluation
- [`docs/portable-skill-profile.md`](docs/portable-skill-profile.md) — portable execution profile
- [`docs/installation-handoff.md`](docs/installation-handoff.md) — installation, upload, and verification contract
- [`docs/third-party-provenance.md`](docs/third-party-provenance.md) — source credit and adaptation rules
- [`INDEX.md`](INDEX.md) / [`index.json`](index.json) — generated discovery maps

A beginner should not need to understand any of those engine pieces before the agent starts doing useful work.
