# Make Your AI Better at Helping You

You do not need to understand skills, write code, or browse hundreds of files.

**Give your AI the GitHub link to this repository. That is enough to start.**

There are two normal ways to arrive here.

## First visit: build a fitted skill set

If the user supplied this repository or its URL without a different task and does not already have a fitted skill set to review, **start first-visit bootstrap now**. Do not stop after describing the repository.

Your job is to build the smallest skill system that best fits this user.

Read [`engine/skills/skill-bootstrap/SKILL.md`](engine/skills/skill-bootstrap/SKILL.md) for the detailed procedure and [`AGENTS.md`](AGENTS.md) for the repository contract.

Start with relevant evidence the host already exposes: interaction history, persistent memory, the current conversation, recurring corrections, workspace/project instructions, repeated tool combinations, existing skills, and definitions of "done." Do not make the user repeat accessible information. Do not invent inaccessible history or sweep unrelated private connectors.

Then:

1. Identify durable working methods and latent skills.
2. Compare those needs against the complete indexed library: local/imported skills plus approved indexed vendor skills.
3. For third-party candidates, inspect provenance, controlled tags, authority, portability, freshness, fingerprint, and verification status.
4. Prefer unchanged reuse only when the exact characterized version is eligible and genuinely fits.
5. Adapt, supplement, or compose when that produces a better fit.
6. Create a new custom skill whenever the user's real workflow is not adequately represented.
7. Evaluate and adversarially review the fitted system.
8. Install it when the host supports installation and authority exists. Otherwise package it and provide simple installation steps.

## Returning visit: review, refine, and improve

If the user already has skills from `skillz`, a prior bootstrap, or another compatible source and asks to review, update, refine, improve, audit, or revisit them, **do not restart from zero**.

Treat the current set as evidence about the user's working system.

1. Inventory the current skills, their intended jobs, installation state, and any available fingerprints or versions.
2. Compare the current set with relevant recurring behavior and the user's present definitions of done.
3. Detect stale, overlapping, conflicting, unused, underperforming, over-broad, or missing capabilities.
4. Check whether any referenced upstream skill changed since the recorded fingerprint or freshness check.
5. Search the current library for materially better fits or useful new patterns.
6. Preserve custom behavior that still fits instead of resetting it to a generic upstream version.
7. Refine, replace, supplement, compose, or retire only where the evidence supports change.
8. Re-run appropriate structured verification and behavioral evaluation for anything materially changed.
9. Update installation state and the portable skill profile when applicable.
10. Return the smallest improved set, plus a concise change log explaining what changed and why.

A returning review should be capable of concluding **no change needed**. More skills are not inherently better.

## Browse by purpose

Humans can browse the locally maintained portion of the library through [`skills/categories/`](skills/categories/), including planning, writing, research, software/repository work, agent operations/security, monitoring/intelligence, and business/career categories.

The complete indexed library also includes approved third-party sources under [`vendor/`](vendor/).

## What counts as the library?

The library includes:

- user-facing skills under [`skills/`](skills/), and
- approved indexed user-facing skills from pinned sources under [`vendor/`](vendor/).

Repository machinery under [`engine/skills/`](engine/skills/) is excluded from the library count.

A vendor skill can be available and searchable without being verified. Availability answers "can we find/use this as reference?" Verification answers "has this exact version earned trusted unchanged selection?"

## How skill quality works

Matt Pocock is the only current source allowed to default to `trusted-baseline` quality. Individual Matt skills still need fingerprinting and characterization before they are fully governed selection candidates.

Every other third-party skill starts `unverified`, even when it comes from an official vendor repository.

Individually characterized skills have a companion under [`registry/verification/`](registry/verification/) bound to the exact canonical `SKILL.md` Git blob SHA.

- `trusted-baseline`: quality accepted by the Matt source policy; no local behavioral-validation claim.
- `verified`: passed the structured skillz quality/effectiveness rubric.
- `validated`: also has representative behavioral evidence.
- `unverified`: useful as design evidence, but not silently trusted for unchanged installation.
- `stale`: the underlying skill/evidence changed and must be reviewed again.
- `rejected` / `retired`: excluded from normal selection.

Tags from [`registry/taxonomy.yaml`](registry/taxonomy.yaml) characterize use case, lifecycle phase, workflow characteristics, authority, and portability. Use those dimensions to refine matching rather than selecting by name alone.

## Compare before creating. Fit the user before reusing.

Existing skills are valuable reference evidence, not a cage.

A good result may use an existing skill unchanged, adapt one, supplement one, compose several, create something entirely new, use a smaller checklist/helper, retire something that no longer helps, or decide that no durable skill change is warranted.

The goal is not maximum reuse or maximum skill count. The goal is the **smallest dependable skill set that matches the user's actual workflow now**.

## Installation is part of the result

A bootstrap or returning refinement pass is not complete merely because Markdown exists.

Finish with an explicit host-level state such as `INSTALLED + VERIFIED`, `READY TO UPLOAD`, `USER ACTION REQUIRED`, or a clearly explained compatibility blocker. See [`docs/installation-handoff.md`](docs/installation-handoff.md).

## What the human should receive

For a first visit:

1. The durable working patterns inferred from legitimate evidence.
2. The fitted skill set and why each skill exists.
3. Which pieces were reused, adapted, composed, or newly created.
4. The quality/evidence state of selected third-party skills.
5. Evaluation results and remaining uncertainty.
6. A portable skill profile when useful.
7. A concrete installation or handoff result.

For a returning visit, also include:

1. what changed since the prior set;
2. which skills stayed unchanged and why;
3. which skills were refined, replaced, added, or retired and why;
4. any stale fingerprints, upstream drift, or evidence that requires follow-up;
5. the updated installation/evaluation state.

The human should always be able to tell what is done, what is trusted, what is merely promising, what changed, what still needs proof, and what action remains.
