---
name: skill-forge
description: >-
  Scaffold a new skill in this repository: elicit name, triggers,
  category, cadence, and deployment class; instantiate
  docs/skill-template.md; then audit and reindex. Use when the user asks
  "create a new skill", "scaffold a skill", "forge a skill", "add a
  pulse skill", or wants a convention-clean skills/<name>/ starting point.
metadata:
  author: frostwulf.zo.computer
  category: Meta
  display-name: Skill Forge
  emoji: "⚒️"
  version: 1.0.0
  repo-bound: true
---

# Skill Forge

Scaffolds a new skill in this repository so it is born convention-clean:
the template is instantiated, the audit passes, and the index is fresh in
one pass. Repo-bound: this skill operates on this repository's tree and is
never deployed by skill-sync.

## Execution Flow

1. **Elicit the spec.** Confirm with the user:
   - **Name** — kebab-case; must not collide with an existing skill
     (check `skills/` directories and `INDEX.md` before proceeding).
   - **Description** — one sentence of what it does plus "Use when"
     trigger phrases (skill-audit fails descriptions without them).
   - **Category** — Productivity | Development | Research | Ops | Meta.
   - **Cadence** — one-shot or recurring; recurring skills get a
     `## Scheduling` section.
   - **Deployment class** — portable, portable-with-fallback (it will
     carry a `sources.json`), or repo-bound (`metadata.repo-bound: true`).
2. **Instantiate.** Copy `docs/skill-template.md` into
   `skills/<name>/SKILL.md` and fill every placeholder from the spec.
3. **Pulse scaffolding.** If the skill is pulse-like, also scaffold
   `skills/<name>/sources.json` (must parse as valid JSON — mirror
   `skills/mcp-pulse/sources.json`) and include the standalone-fallback
   marker sentence in the SKILL.md: "If the engine is unavailable (skill
   deployed standalone), read `sources.json` beside this file and
   fetch/search those sources directly with web tools."
4. **Audit.** Run `node skills/skill-audit/scripts/audit.ts` from the
   repo root and fix every FAIL finding until it exits 0.
5. **Reindex.** Run `node scripts/build-index.ts` to regenerate
   `INDEX.md` and `index.json`.

## Output Format

```
# Skill Forge — <name>
Files created: skills/<name>/SKILL.md [, skills/<name>/sources.json]
Audit: exit 0 (N skills validated) | findings fixed: <list>
Index delta: <new INDEX.md entry line>
```

## Notes

- Never overwrite an existing skill — a name collision aborts the forge;
  editing an existing skill is a different task.
- Conventions are enforced mechanically by skill-audit; if the template
  and the audit disagree, fix `docs/skill-template.md` first.
