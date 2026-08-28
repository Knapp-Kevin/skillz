# skillz Engine

This directory contains the machinery that operates the `skillz` repository.

**Nothing under `engine/` counts as user-facing skill-library inventory.**

The procedures may use the Agent Skills format because that makes them explicit and composable. They are still repository infrastructure.

## Engine skills

- `skill-bootstrap`: discover and assemble a fitted user skill system
- `skill-forge`: author new skills
- `skill-eval`: behaviorally evaluate skills
- `skill-audit`: validate library structure and semantic risk
- `skill-sync`: install/deploy library skills to supported local targets
- `skills-pulse`: monitor the skill ecosystem for candidates
- `source-vetting`: evaluate source suitability and verification integrity

## Verification integrity

Third-party characterization is bound to exact canonical skill content. The offline drift checker lives at:

```text
engine/skills/source-vetting/scripts/verify-characterization-integrity.ts
```

Run it deliberately with:

```bash
node engine/skills/source-vetting/scripts/verify-characterization-integrity.ts
```

It performs no network calls. A real hash mismatch reports `STALE / REVERIFY REQUIRED`; missing uninitialized submodules are reported as unavailable rather than misclassified as content drift.

## Boundary test

A capability belongs in `engine/skills/` when its primary purpose is maintaining, curating, generating, validating, or deploying the `skillz` system itself.

A capability belongs in [`../skills/`](../skills/) when it makes sense for a user to install independently of maintaining this repository.
