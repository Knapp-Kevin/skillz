---
name: skill-forge
description: >-
  Create or revise a first-party user-facing skill inside the skillz repository
  using the repository's current template, metadata, and semantic review rules.
  Use only for explicit repository maintenance.
metadata:
  author: frostwulf.zo.computer
  category: Meta
  display-name: Skill Forge
  emoji: "⚒️"
  version: 2.0.0
  repo-bound: true
---

# Skill Forge

**Repository-maintenance procedure only.**

Use this only when the active route is `REPOSITORY_MAINTENANCE` and the user explicitly intends a skill to become part of this repository's `skills/` tree.

For normal FIRST_VISIT or RETURNING_USER synthesis, use `engine/skills/skill-bootstrap/SKILL.md` and create or hand off artifacts for the user's actual environment instead.

## Procedure

1. Confirm the intended destination is this repository's first-party `skills/` library.
2. Define the skill's durable capability, trigger/non-trigger conditions, inputs/outputs, authority, dependencies, portability, and completion criteria.
3. Compare the proposed capability with existing local skills and governed external records. Do not create a duplicate merely because a new name is available.
4. Use `docs/skill-template.md` as the structural starting point when applicable.
5. Create or revise the full skill package under `skills/<name>/`. A skill package may legitimately include its own scripts, references, templates, fixtures, JSON, examples, or other components when those components are part of the skill itself.
6. Preserve those skill-owned components unless there is a specific quality, safety, licensing, or redundancy reason to change them.
7. Review the finished package semantically against `docs/skill-verification.md`, including provenance, licensing, dependencies, authority, portability, ambiguity, failure handling, and likely misuse.
8. Add or update the corresponding first-party review metadata so it describes the exact current artifact honestly.
9. Update human navigation only where the new or revised skill materially affects it.
10. Report the actual files changed and the semantic review result.

## Negative rules

- Never use this procedure to write a bootstrap user's personal/custom skills into `skillz` by default.
- Never require repository scripts, CI, tests, generated indexes, or runtime proof.
- Never delete a skill-owned script/reference/template/component merely because the repository engine is passive.
- Never overwrite an existing skill without first understanding the existing package and why the change is justified.
- Never claim semantic review or metadata were updated if they were not.
