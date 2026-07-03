---
name: skill-audit
description: >-
  Validate this repository's conventions mechanically: SKILL.md frontmatter
  (name/directory match, trigger-bearing description, version), script
  health (--help exit codes), intake-registry enums, and index freshness.
  Use when the user asks "audit the skills repo", "validate the skills",
  "lint the registry", before running skill-sync, or as a pre-commit check
  after adding or editing any skill.
metadata:
  author: frostwulf.zo.computer
  category: Meta
  display-name: Skill Audit
  emoji: "🔍"
  version: 1.0.0
  repo-bound: true
---

# Skill Audit

Mechanical validation of the skillz repo. Drift is a failing exit code, not a code-review catch. Repo-bound: this skill operates on this repository's tree and is never deployed by skill-sync.

## What This Does

Runs `scripts/audit.ts`, which checks in order:

1. **Skill conventions** — every `skills/<dir>/SKILL.md`: frontmatter parses, `name` matches the directory, `description` is non-empty and carries "Use when" trigger guidance, `metadata.version` present.
2. **Script health** — every `skills/<dir>/scripts/*.ts` answers `--help` with exit 0 (spawned, 30s timeout).
3. **Registry lint** — every `registry/candidates.yaml` entry has a valid `status` and `permission_tier` (enums from `docs/evaluation-framework.md`), a non-empty `rationale`, and — for adopted entries — an existing `resolved_path`.
4. **Index freshness** (WARN-only) — `INDEX.md` must be newer than every SKILL.md.

Exit 0 = clean (warnings allowed); exit 1 = failures found.

## Execution Flow

1. Run from the repo root (either runtime works):

   ```
   node skills/skill-audit/scripts/audit.ts
   bun run skills/skill-audit/scripts/audit.ts
   ```

2. For each FAIL finding, fix the named file and re-run until exit 0.
3. If the only findings are index-staleness WARNs, run `node scripts/build-index.ts` and re-run.
4. Report the final counts. Do not suppress findings; a convention worth breaking is a convention worth changing in `docs/skill-template.md` first.

## Scheduling

- **Claude Code:** run ad hoc before commits, or `/schedule` a weekly repo-health run paired with skills-pulse.
- **CI:** `node --test "tests/*.test.mjs"` plus `node skills/skill-audit/scripts/audit.ts` are the repo's declared CI commands.

## Output Format

```
FAIL: <skill>: <violation>
WARN: <message>

skill-audit: N failure(s), M warning(s)
```

## Notes

- Validates structure and script health, not skill *quality* — that stays model judgment.
- `vendor/` trees are never audited; official sources own their own conventions.
- `--skills-dir` and `--registry` flags exist for test fixtures.
