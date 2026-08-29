---
name: skill-audit
description: >-
  Validate the skillz repository's own conventions, script health, registry
  structure, and index freshness. Use only for repository-maintenance work such
  as validating skillz before commit, merge, reindex, or repository deployment.
metadata:
  author: frostwulf.zo.computer
  category: Meta
  display-name: Skill Audit
  emoji: "🔍"
  version: 1.2.0
  repo-bound: true
---

# Skill Audit

**Repository-maintenance helper only.**

This validates the `skillz` repository itself. It is not a prerequisite for normal FIRST_VISIT or RETURNING_USER bootstrap and should not be imposed on connector/API/read-only users.

## What This Does

Runs the repository audit at:

```text
engine/skills/skill-audit/scripts/audit.ts
```

It checks local user-facing skill conventions, script health, pulse/source fallback structure, registry lint, and index freshness. The semantic risk layer is at:

```text
engine/skills/skill-audit/scripts/risk-audit.ts
```

These are deterministic repository-maintenance checks. They do not establish that a skill improves user behavior; behavioral evidence is a separate concern.

## Execution Flow

Run from the repository root:

```text
node engine/skills/skill-audit/scripts/audit.ts
```

or, where Bun is the active runtime:

```text
bun run engine/skills/skill-audit/scripts/audit.ts
```

For the semantic risk layer:

```text
node engine/skills/skill-audit/scripts/risk-audit.ts
```

Then:

1. fix every FAIL finding;
2. if index freshness is the only warning, regenerate with `node scripts/build-index.ts`;
3. re-run until the intended checks pass;
4. report actual results only.

## Output Format

```text
FAIL: <skill>: <violation>
WARN: <message>

skill-audit: N library skill(s), X failure(s), Y warning(s)
```

## Negative rules

- Do not use this as evidence that a skill is behaviorally effective.
- Do not require this helper for normal user bootstrap.
- Do not use legacy `skills/skill-audit/...` paths; the canonical path is under `engine/skills/skill-audit/`.
- Do not suppress findings merely to obtain exit 0.
