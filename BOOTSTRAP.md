# Make Your AI Better at Helping You

You do not need to understand skills, write code, or browse hundreds of files.

**Give your AI the GitHub link to this repository. That is enough to start.**

`skillz` is passive. The repository provides instructions, examples, reference material, and governance metadata. The agent you already use performs the reasoning and creates or hands off the fitted skill system with whatever capabilities its host legitimately provides.

There is no CI, application runtime, or executable proof requirement for normal use or repository completion.

## First visit: build a fitted skill set

If the user supplied this repository or its URL without a different task and does not already have a fitted skill set to review, **start first-visit bootstrap now**. Do not stop after describing the repository.

Read [`AGENT_START_HERE.md`](AGENT_START_HERE.md), [`engine/skills/skill-bootstrap/SKILL.md`](engine/skills/skill-bootstrap/SKILL.md), and [`AGENTS.md`](AGENTS.md).

Start with relevant evidence the host already exposes: interaction history, persistent memory, the current conversation, recurring corrections, workspace/project instructions, repeated tool combinations, existing skills, and definitions of done. Do not make the user repeat accessible information. Do not invent inaccessible history or sweep unrelated private connectors.

Then:

1. identify durable working methods and latent skills;
2. translate them into capability requirements before searching by skill name;
3. search local and third-party reference material for whole skills and useful components;
4. distinguish governed exact-version reuse from reference/design evidence;
5. inspect provenance, controlled tags, authority, portability, dependencies, license, identity, and semantic quality state for third-party candidates;
6. prefer unchanged reuse only when an exact `verified` or `validated` candidate genuinely fits;
7. adapt, supplement, or compose when that produces a better fit;
8. create a custom skill when the user's real workflow is not adequately represented;
9. adversarially review important instructions for likely misinterpretation, overreach, hidden assumptions, or unnecessary ceremony;
10. install when the host supports installation and authority exists, otherwise provide a complete portable handoff.

## Returning visit: review, refine, and improve

If the user already has a fitted skill system, **do not restart from zero**.

1. inventory the current skills and the jobs they are meant to perform;
2. identify material drift, overlap, conflict, changed needs, or missing capabilities;
3. preserve custom behavior that still fits;
4. re-run capability definition and comparison only for affected areas;
5. check whether materially better references or components now exist;
6. refine, replace, supplement, compose, retire, or leave unchanged only where evidence supports it;
7. semantically review changed instructions again;
8. update the installation or portable-handoff state.

A returning review may correctly conclude **`NO CHANGE NEEDED`**. More skills are not inherently better.

## Governed selection

The broad local/vendor/tracked corpus is **reference and discovery material**. Source admission, popularity, or publisher reputation does not make every skill trusted unchanged inventory.

An unchanged third-party skill is eligible for consideration only when its individual exact-version record is `verified` or `validated` and its provenance, license, dependencies, authority, portability, identity, and user fit are acceptable.

Other states:

- `unverified`: design/reference evidence only;
- `trusted-baseline`: legacy characterization only;
- `stale`: previous review should not be silently inherited;
- `rejected` / `retired`: excluded from normal unchanged selection.

A rejected or unverified skill may still contain a useful idea. Component reuse does not bypass provenance, licensing, dependency, authority, or the reason the whole skill was rejected.

## Skill quality is semantic

The quality model is defined in [`docs/skill-verification.md`](docs/skill-verification.md).

- `verified` means the exact text passed the structured semantic quality rubric.
- `validated` means it also received representative scenario/adversarial semantic review.

These are probabilistic judgments about instruction quality and likely interpretation, not deterministic claims about model behavior.

## Compare before creating. Fit the user before reusing.

Existing skills are reference evidence, not a cage.

A good result may use an existing skill unchanged, adapt one, supplement one, compose several, create something entirely new, use a smaller checklist/helper, retire something that no longer helps, or decide no durable skill change is warranted.

The goal is the **smallest dependable skill system that matches the user's actual workflow now**.

## Installation is part of the user result

Finish with an explicit host-level state such as `INSTALLED + VERIFIED`, `READY TO UPLOAD`, `USER ACTION REQUIRED`, or a clearly explained compatibility blocker. See [`docs/installation-handoff.md`](docs/installation-handoff.md).

A host that cannot write files may still produce a complete portable artifact. Do not convert "cannot install here" into "cannot use skillz here."

## What the human should receive

For a first visit:

1. durable working patterns inferred from legitimate evidence;
2. the fitted skill set and why each piece exists;
3. which pieces were reused, adapted, composed, or newly created;
4. the semantic quality/evidence state of selected third-party skills;
5. important uncertainty or limitations;
6. the complete artifacts or portable package;
7. a concrete installation/handoff state.

For a returning visit, also explain what changed, what stayed unchanged, and why.

The human should always be able to tell what is done, what is governed, what is merely reference material, what changed, and what action remains.