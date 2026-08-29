# Agent Entry Contract

This repository is both a user-facing skill library and a passive skill-building engine.

**Start with [`AGENT_START_HERE.md`](AGENT_START_HERE.md).**

For normal first-visit or returning-user work, there is one canonical orchestrator:

[`engine/skills/skill-bootstrap/SKILL.md`](engine/skills/skill-bootstrap/SKILL.md)

Do not make the agent choose among the other engine helpers during normal bootstrap.

## Inventory boundary

- `skills/`: local/imported user-facing skills. Count them.
- approved indexed user-facing material under `vendor/`: count it.
- `engine/skills/`: engine and repository-maintenance procedures. Do **not** count them as user-facing inventory.
- `registry/skills/`: exact provenance for individually characterized third-party skills.
- `registry/verification/`: fingerprint-bound quality state and controlled tags.
- `registry/sources.yaml`: source-level identity, role, and pinning.

Availability and quality are separate concepts.

## Route before acting

Choose one route:

### DIRECT_LIBRARY

Use when the user asks to browse, search, compare, inspect, install, adapt, or use a known skill. Do not force full bootstrap.

### FIRST_VISIT

Use when the user wants a fitted skill system and no existing fitted system is being reviewed.

Follow `engine/skills/skill-bootstrap/SKILL.md` from S0 through S11.

### RETURNING_USER

Use when the user already has a fitted skill system and asks to review, improve, update, audit, revisit, or refine it.

Start from the current system. Preserve still-valid custom behavior. Make the smallest justified change. `NO CHANGE NEEDED` is a valid result.

### REPOSITORY_MAINTENANCE

Use only when the user explicitly wants to change `skillz` itself. Repo-bound helpers such as `skill-forge`, `skill-audit`, `skill-sync`, `skills-pulse`, and source-vetting belong here.

Do not transfer maintenance prerequisites into normal user bootstrap.

## Capability routing

Never assume local shell, Git, Node/Bun, initialized submodules, writable filesystem access, or GitHub Actions.

Use the strongest capability path the host actually exposes:

1. repository-native;
2. connector/API/web;
3. minimal read-only.

Normal direct-library use, first-visit bootstrap, returning-user refinement, custom synthesis, and portable handoff must remain possible without maintainer runtime.

## Third-party unchanged-reuse rule

Source reputation does not equal individual verification.

An unchanged third-party candidate may be considered only when:

- its individual record is `verified` or `validated`;
- the exact fingerprint/version matches when the host can establish it;
- provenance, dependency/package, authority, and license conditions are acceptable;
- it actually fits the user's capability requirement.

Other states:

- `unverified`: design evidence only;
- `trusted-baseline`: legacy characterization/design evidence only until replaced by current individual structured review;
- `stale`: exclude from unchanged selection until refreshed;
- `rejected` / `retired`: exclude from normal unchanged selection.

If exact fingerprint verification is unavailable on the current host, state that explicitly and choose a conservative path rather than fabricating certainty.

## Core doctrine

**Compare before creation. User-fit before reuse. Search capabilities before filenames. Smallest coherent system over maximum skill count.**

A reference skill can contribute useful components without becoming the final workflow. Useful components include triggers, safeguards, procedure fragments, decision gates, evidence rules, tests, failure handling, and abstractions.

When a component is reused, carry forward the useful mechanism without automatically importing the source author's terminology, ceremony, commands, file layout, UX, or authority assumptions.

## Memory and privacy

Use relevant accessible memory/history before asking the user to repeat information the host already exposes. Never reconstruct unavailable history from assumptions.

Access to a private connector is capability, not consent to mine it for a user profile.

## Mutation boundary

Discovery and design are read-only by default.

During normal FIRST_VISIT or RETURNING_USER work, do not modify the `skillz` repository merely because it is writable. Create/package artifacts for the user's target environment instead.

Installing skills, writing outside the active workspace, changing permissions, publishing, sending, or causing external side effects requires the authority expected by the target environment. A recommendation is not authorization.
