# skillz Engine

This directory contains the machinery that operates the `skillz` repository.

## Important counting rule

**Nothing under `engine/` counts as skill-library inventory.**

The procedures here may themselves use the Agent Skills format because that makes them executable and composable by agents. They are still repository infrastructure, not catalog items offered to users as part of the public skill count.

## Engine skills

`engine/skills/` currently contains:

- `skill-bootstrap` — discover and assemble a user's fitted skill system
- `skill-forge` — author new skills
- `skill-eval` — behaviorally evaluate skills
- `skill-audit` — validate library structure and semantic risk
- `skill-sync` — install/deploy library skills to supported local targets
- `skills-pulse` — monitor the skill ecosystem for curation candidates
- `source-vetting` — evaluate source trust and suitability

These skills exist to operate the library and bootstrap system.

## Boundary test

A capability belongs in `engine/skills/` when its primary purpose is maintaining, curating, generating, validating, or deploying the `skillz` system itself.

A capability belongs in [`../skills/`](../skills/) when it makes sense for a user to install and use independently of maintaining this repository.

Internal use does not automatically make a skill an engine skill. If a normal user would independently benefit from the capability, it can remain a library skill even when `skillz` also uses it internally.
