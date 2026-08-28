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

Start with the relevant information your current host already exposes, especially:

- interaction history,
- persistent memory,
- the current conversation,
- repeated corrections,
- workspace or project instructions,
- recurring tool use,
- existing skills or custom instructions,
- repeated workflows and completion standards.

Do not make the user repeat information you can already access.

Do not invent history or memory you cannot access.

Do not inspect unrelated private connectors simply because they exist.

Then:

1. Find working patterns that are useful enough to preserve.
2. Identify which of those patterns already behave like unwritten or **latent skills**.
3. Compare those needs against the local and third-party references in this repository.
4. Extract useful ideas, safeguards, procedures, triggers, validation methods, and abstractions from those references.
5. Build the smallest skill system that best matches the user's real workflow.
6. Use an existing skill when it genuinely fits.
7. Adapt or supplement one when that produces the best result.
8. **Create a new custom skill whenever that better represents the user's needs, even if related skills already exist here.**
9. Test and adversarially review the resulting skills.
10. Install them when the current system supports it and you have the required authority. Otherwise prepare the correct files and give simple installation steps.

Read [`skills/skill-bootstrap/SKILL.md`](skills/skill-bootstrap/SKILL.md) for the full procedure.

## If you are the human reading this

The short version is:

**Your AI should do the work.**

You should not need to browse a giant list and decide which skills sound useful.

Your AI should look at how you already work together, figure out what would make that work more dependable, learn from the examples in this repository, and build the right skills for you.

## What is a skill?

A skill is a reusable set of instructions that helps an AI do something in a dependable way.

Maybe you always want your AI to:

- check its work before saying it is finished,
- research before making an important recommendation,
- follow the same careful steps when fixing a bug,
- use several tools in a particular order,
- ask before making risky changes,
- create reports in a format that works for you,
- separate facts from guesses,
- test an answer before treating it as correct.

If you have told your AI the same kind of thing many times, you may have already created the beginnings of a skill without calling it one.

This repository helps your AI find those patterns and turn the useful ones into something reusable.

## The skills in this repository are not a shopping list

The repository contains many useful skills and references.

That does **not** mean your AI should simply choose a few and install them.

Think of the repository as a big box of examples, tools, parts, and tested ideas.

Your AI can use them in different ways:

- **USE** a skill that already fits you,
- **IMPROVE** one you already have,
- **ADAPT** a good reference to your needs,
- **BORROW** one useful idea from another skill,
- **COMBINE** several skills that work well together,
- **CREATE** something completely new,
- or **SKIP** anything that does not help.

The right answer may be a custom skill that never existed before.

For example, your day-to-day work may have a very particular sequence that no public skill describes. Your AI should study the closest references, learn what makes them strong, and then build a new skill around **your** real process.

The goal is not to reuse the most skills.

The goal is to create the **smallest set of skills that makes your AI more dependable for you**.

## Your AI may already know more than you think

If your AI has access to memory or past interactions, it may already have useful evidence about how you work.

It can look for things such as:

- instructions you repeat,
- corrections you make often,
- things that annoy you when the AI gets them wrong,
- steps you almost always use,
- tools you often use together,
- rules you expect the AI to remember,
- what you mean when you say something is "done."

Those patterns can become portable skills instead of staying trapped inside one AI's memory.

If the AI cannot see old conversations or memory, that is okay. It should tell you what it can actually see and make more careful conclusions from the smaller amount of evidence.

## Why use other people's skills at all?

Because someone else may already have solved part of the problem very well.

A reference skill might contain:

- a better way to know when it should activate,
- a safer permission rule,
- a strong debugging loop,
- a better test,
- a useful failure check,
- a cleaner way to split a large workflow,
- a good way to keep evidence from guesses,
- a more dependable completion rule.

Your AI can learn from those parts without copying somebody else's whole workflow or forcing you to work like they do.

## Compare before creating. Fit you before reusing.

Your AI should look at relevant existing solutions before inventing another one from scratch.

But it should not reuse something merely because it exists.

If a custom skill fits you better, build the custom skill.

Existing skills are reference evidence, not a cage.

## Will it change things automatically?

Discovery and design are read-only by default.

Your AI should not send messages, publish work, change permissions, delete things, or make unrelated outside changes just because it is running this bootstrap.

Installing a skill is also a change.

If your AI can install the final skills itself and the system gives it the required authority, it can do that and verify the result.

If the AI cannot perform the installation, it should make the human part as easy as possible.

## How do I install the skills when they are ready?

You should not have to figure that out by yourself.

The bootstrap must finish in one of three ways:

### 1. The AI installs them

If the AI can safely write or install the skills itself, it should do that and test them.

You should get a clear result such as:

**Installed and tested. You do not need to do anything else.**

### 2. You upload them

Some web apps require a person to click a few buttons.

In that case, the AI should prepare the correct file and give you one action at a time.

For example:

1. Open the AI app.
2. Open its Skills page.
3. Choose the option to add a skill.
4. Select the exact file the AI created.
5. Turn the skill on if needed.
6. Type the small test prompt the AI gives you.

The real instructions should use the current buttons and exact filename for the AI system you are actually using.

### 3. The system cannot install skills

The AI should tell you clearly.

It should preserve your skills in a portable form so they can be used later on a compatible system. A temporary workaround may be offered separately, but it must not be described as a real skill installation when it is not one.

## What should I get at the end?

The bootstrap should give you:

1. **What it learned about how you work**
   Only the durable patterns that matter for execution.

2. **The skill system it built for you**
   Existing, adapted, combined, and newly created skills as appropriate.

3. **Why each skill exists**
   The problem it solves or the failure it prevents.

4. **A portable skill profile**
   A small description of important execution defaults that can travel between compatible systems.

5. **Validation results**
   What was actually tested and what still needs proof.

6. **An installation result**
   Installed and verified, ready to upload, or a clearly explained blocker.

You should always be able to tell:

- what is already done,
- what skill files were created or selected,
- what you need to do next, if anything,
- and how you know the skills are working.

## For advanced users and agents

The machinery underneath the simple experience lives in:

- [`AGENTS.md`](AGENTS.md) — default agent-entry contract
- [`skills/skill-bootstrap/SKILL.md`](skills/skill-bootstrap/SKILL.md) — full discovery and design procedure
- [`docs/portable-skill-profile.md`](docs/portable-skill-profile.md) — portable execution profile
- [`docs/installation-handoff.md`](docs/installation-handoff.md) — installation, upload, and verification contract
- [`docs/third-party-provenance.md`](docs/third-party-provenance.md) — source credit and adaptation rules
- [`INDEX.md`](INDEX.md) / [`index.json`](index.json) — reference maps for agents
- [`skills/skill-eval/SKILL.md`](skills/skill-eval/SKILL.md) — behavioral evaluation
- [`skills/skill-forge/SKILL.md`](skills/skill-forge/SKILL.md) — custom skill creation
- [`skills/skill-audit/SKILL.md`](skills/skill-audit/SKILL.md) — structural and risk validation
- [`skills/skill-sync/SKILL.md`](skills/skill-sync/SKILL.md) — supported local deployment

A beginner should not need to understand any of those pieces before the agent starts doing useful work.
