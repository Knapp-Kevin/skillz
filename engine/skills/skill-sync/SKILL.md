---
name: skill-sync
description: >-
  Deploy portable user-facing skills from the skillz repository to supported
  local consumer targets with dry-run drift reporting. Use only for repository-
  maintenance deployment of skills already present in this repository.
metadata:
  author: frostwulf.zo.computer
  category: Meta
  display-name: Skill Sync
  emoji: "🚀"
  version: 1.1.0
  repo-bound: true
---

# Skill Sync

**Repository-maintenance deployment helper only.**

This deploys portable skills that already live in the `skillz` repository. It is not the universal installation adapter for a user's newly synthesized bootstrap package.

For normal FIRST_VISIT or RETURNING_USER work, follow `engine/skills/skill-bootstrap/SKILL.md` and adapt/install the fitted artifacts using the active host's real installation mechanism.

## What This Does

The repository sync script is:

```text
engine/skills/skill-sync/scripts/sync.ts
```

It discovers portable skills in this repository and can reconcile them against supported local targets such as Claude Code user skills, arbitrary local directories, COREFORGE-style bundles, or supported host directories.

Dry-run is the default. Nothing should be written without the script's explicit apply mode.

## Execution Flow

1. Confirm the route is `REPOSITORY_MAINTENANCE` and the source artifacts already belong to this repository.
2. Validate the repository with:

   ```text
   node engine/skills/skill-audit/scripts/audit.ts
   ```

3. Run a dry-run using the canonical script path, for example:

   ```text
   node engine/skills/skill-sync/scripts/sync.ts --claude-user --dest D:\\agents\\skills
   ```

4. Review the planned create/update/up-to-date/skip actions.
5. Apply only when the requested destination and authority are established.
6. Report actual per-target results.

## Output Format

```text
[dry-run|apply] <target> <skill>: create|update|up-to-date|skip:repo-bound
```

## Negative rules

- Do not use legacy `skills/skill-sync/...` paths; the canonical path is under `engine/skills/skill-sync/`.
- Do not make this helper a prerequisite for normal user bootstrap.
- Do not infer that a host supports this repository's sync mechanism merely because the host supports skills generally.
- Do not apply writes without the authority required by the target environment.
