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

1. Confirm explicit `REPOSITORY_MAINTENANCE` authority for the proposed repository change, including the intended `skills/` destination and affected paths. A general request to create a skill for a user's own agent does not authorize a repository write.
2. Define the skill's durable capability, trigger/non-trigger conditions, inputs/outputs, authority, dependencies, portability, and completion criteria.
3. Compare the proposed capability with existing local skills and governed external records. Do not create a duplicate merely because a new name is available.
4. Use `docs/skill-template.md` as the structural starting point when applicable.
5. Create or revise the full skill package under `skills/<name>/`. A skill package may legitimately include its own scripts, references, templates, fixtures, JSON, examples, or other components when those components are part of the skill itself.
6. Preserve those skill-owned components unless there is a specific quality, safety, licensing, or redundancy reason to change them.
7. Review the finished package semantically against `docs/skill-verification.md`, including provenance, licensing, dependencies, authority, portability, ambiguity, failure handling, and likely misuse.
8. Bind first-party provenance and the individual verification record to the exact finished package identity/fingerprint; record the controlled taxonomy, rubric score, disposition, dependencies, authority, and behavioral-validation state honestly. Static scenarios do not establish behavioral `validated`.
9. For new or materially revised user-facing packages, assess the **separate** exact-package security gate in `docs/security-scanning.md`. Missing, incomplete, failed, or stale security evidence cannot be called a pass or silently used to admit an unchanged-use candidate. The external host, not this repository, performs any authorized scanner execution.
10. Do not publish/count a new governed user-facing skill as admitted until the required provenance, semantic, security, licensing, and authorization decisions are satisfied. If blocked, keep the candidate explicitly unadmitted; preserve useful draft/reference material without inflating inventory.
11. After a material admitted tranche, reconcile `README.md`, `docs/SYSTEM_STATE.md`, `CURATION_QUEUE.md`, `INDEX.md`, and `index.json` together from live evidence. For an unmerged draft, do not falsely increment published counts.
12. Update human navigation only where the new or revised skill materially affects it, and report actual files, evidence, limitations, and unresolved gates.

## Negative rules

- Never use this procedure to write a bootstrap user's personal/custom skills into `skillz` by default.
- Never require repository scripts, CI, tests, generated indexes, or runtime proof.
- Never delete a skill-owned script/reference/template/component merely because the repository engine is passive.
- Never overwrite an existing skill without first understanding the existing package and why the change is justified.
- Never claim semantic review, scanner execution, behavioral validation, provenance, or metadata were updated if they were not.
- Do not equate a ready PR or a high rubric score with authorized admission.
