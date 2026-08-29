---
name: skill-forge
description: >-
  Scaffold a new user-facing skill inside the skillz repository, then run
  repository audits and reindexing. Use only when maintaining skillz itself and
  the user explicitly wants to add a skill to this repository's skills/ tree.
metadata:
  author: frostwulf.zo.computer
  category: Meta
  display-name: Skill Forge
  emoji: "⚒️"
  version: 1.1.0
  repo-bound: true
---

# Skill Forge

**Repository-maintenance helper only.**

This skill scaffolds a new user-facing skill **inside the `skillz` repository**. It is not the normal artifact-creation mechanism for `skill-bootstrap`, and it must not be used merely because a bootstrap user needs a custom skill.

Use this only when the active route is `REPOSITORY_MAINTENANCE` and the user explicitly intends the new skill to become part of this repository's `skills/` tree.

For normal FIRST_VISIT or RETURNING_USER synthesis, follow `engine/skills/skill-bootstrap/SKILL.md` and create/package artifacts for the user's target environment instead.

## Execution Flow

1. Confirm this is repository-maintenance work and that the intended destination is this repository's `skills/` tree.
2. Confirm the spec:
   - **Name** — kebab-case; must not collide with an existing skill.
   - **Description** — one sentence describing the capability plus `Use when` trigger guidance.
   - **Category** — use the current repository category model.
   - **Cadence** — one-shot or recurring when scheduling semantics are actually needed.
   - **Deployment class** — portable, portable-with-fallback, or repo-bound.
3. Instantiate `docs/skill-template.md` into `skills/<name>/SKILL.md` and fill every required field.
4. If the skill needs standalone source fallback, add the appropriate `sources.json` and fallback contract.
5. Run the repository audit from the repository root:

   ```text
   node engine/skills/skill-audit/scripts/audit.ts
   ```

6. Fix every FAIL finding.
7. Regenerate the repository index:

   ```text
   node scripts/build-index.ts
   ```

## Output Format

```text
# Skill Forge — <name>
Route: REPOSITORY_MAINTENANCE
Files created: skills/<name>/SKILL.md [, skills/<name>/sources.json]
Audit: exit 0 | findings fixed: <list>
Index: regenerated
```

## Negative rules

- Never use this helper to write a bootstrap user's personal/custom skills into `skillz` by default.
- Never overwrite an existing skill; a name collision aborts the forge.
- Never claim audit/index success unless those commands actually ran.
- If the template and audit disagree, correct the repository convention rather than silently bypassing the check.
