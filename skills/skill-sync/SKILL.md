---
name: skill-sync
description: >-
  Deploy this repository's portable skills to their consumers: junction into
  the Claude Code user skills directory, copy to any local path, or emit
  COREFORGE Synapse-style manifest.json bundles — dry-run by default with
  drift reporting. Use when the user asks "sync the skills", "deploy skills
  to Claude Code", "install the skills locally", "generate COREFORGE
  manifests", or after skill-audit passes on new or changed skills.
metadata:
  author: frostwulf.zo.computer
  category: Meta
  display-name: Skill Sync
  emoji: "🚀"
  version: 1.0.0
  repo-bound: true
---

# Skill Sync

One command deploys portable skills to any local consumer with visible drift. Repo-bound: this skill operates on this repository's tree and never deploys itself.

## What This Does

Runs `scripts/sync.ts`, which discovers portable skills (frontmatter without `repo-bound: true`) and reconciles them against targets:

| Target | Flag | Mechanism |
|--------|------|-----------|
| Claude Code user skills | `--claude-user` | Directory junction at `<root>/<name>` (root defaults to `~/.claude/skills`, overridable via `--claude-user-root`) |
| Any local directory | `--dest <path>` | Recursive copy; drift = any byte difference |
| COREFORGE Synapse | `--coreforge <path>` | Per-skill `manifest.json` derived from frontmatter (skillId, version, entryPoint, runtime) plus SKILL.md and scripts |

**Dry-run by default** — prints `create` / `update` / `up-to-date` / `skip:repo-bound` per skill per target. Nothing is written without `--apply`.

## Execution Flow

1. Run `skill-audit` first; do not deploy a failing tree.
2. Dry-run to see planned actions:

   ```
   node skills/skill-sync/scripts/sync.ts --claude-user --dest D:\agents\skills
   ```

3. Review the action list. If it matches intent, re-run with `--apply`.
4. Report per-target results. Junctions mean edits in this repo are live immediately; copies need re-sync (drift shows as `update` on the next dry-run).

## Scheduling

- **Claude Code:** run ad hoc after merging skill changes, or `/schedule` a weekly sync following the skills-pulse/skill-audit pair.
- **Other agents:** dry-run output is safe to include in any automation report; gate `--apply` behind approval.

## Output Format

```
[dry-run|apply] <target> <skill>: create|update|up-to-date|skip:repo-bound
```

## Notes

- Only local skills deploy; `vendor/` content is consumed via its own install channels (e.g., `/plugin marketplace add`).
- Repo-bound skills (this one and skill-audit) are excluded by construction (LD-2).
- Mutating targets outside the repo requires `--apply` — read-only by default per the repo's design rules.
