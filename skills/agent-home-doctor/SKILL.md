---
name: agent-home-doctor
description: >-
  Audit and clean an AI agent CLI's home directory (~/.claude, ~/.codex,
  ~/.gemini, ~/.kilo, or any equivalent): find unbounded history growth,
  uncleaned temp dirs, extension-surface duplication, dead config
  references, deprecated-prefix remnants, and stale backups, then remediate
  in risk tiers. Use when the user asks "clean up my .claude folder",
  "audit my agent directories", "why is my agent home huge", "what's safe
  to delete here", or after major CLI updates that historically leave cruft.
metadata:
  author: frostwulf.zo.computer
  category: Meta
  display-name: Agent Home Doctor
  emoji: "🩺"
  version: 1.0.0
---

# Agent Home Doctor

An adaptive framework: agent CLI vendors change their extension surfaces and storage layouts across updates and never migrate or clean up — the home directory is where that churn fossilizes. This skill ships the *pathology library* and the *tiered remediation discipline*; the specific directory layout, retention policy, and migration rules bind at runtime.

## Execution Flow

1. **Bind.** Identify the target home dir (ask, or enumerate `~/.claude`, `~/.codex`, `~/.gemini`, `~/.kilo`, `~/.copilot`, editor dirs). Read the operator's conventions from profile/memory (retention days, deprecated-prefix migration maps like a legacy→successor rename, never-touch additions). Absent a policy, default retention 30 days and propose recording the choices.
2. **Inventory.** Top-level size/count map (`dirs` with recursive sums), then per-offender drilldowns. Establish the never-touch set FIRST: credentials/keys, memory/notes dirs, user-authored content (custom skills/commands/hooks), active session state, anything the operator marks.
3. **Diagnose against the pathology library** — check each:
   - **Unbounded history**: transcript/session/edit-history dirs with entries older than retention (`file-history/`, `projects/`, `sessions/`); check whether the CLI has a retention setting that's unset.
   - **Uncleaned temp**: `tmp/`, `.tmp/`, `paste-cache/`, sandbox scratch — anything regenerable.
   - **Surface-generation duplication**: the same content loaded via multiple extension mechanisms (flat vs categorized copies — hash-verify; agents mirrored as commands; collections installed locally that are also available via plugins/vendored sources). Note the per-session context cost, not just disk.
   - **Dead config references**: settings entries pointing at files that no longer exist (verify each path).
   - **Deprecated-prefix remnants**: apply the bound migration map (e.g., legacy-prefixed skills/subagents/permissions whose successors exist).
   - **Stale backups**: `.bak` files (diff before judging) and dated backup dirs from old updates.
4. **Remediate in tiers**, reporting reclaim per tier:
   - **Tier 0 (execute on general approval)**: delete aged temp/history beyond retention, cleared caches, diffed-stale `.bak`s.
   - **Tier 1 (config)**: pin retention settings explicitly; remove verified-dead config references.
   - **Tier 2 (reversible only)**: MOVE duplicates and deprecated remnants into a dated `backups/dedupe-<date>/` dir — never delete; hash-verify before moving anything claimed as a duplicate.
   - **Tier 3 (report only)**: third-party applications squatting in the dir, plugin/marketplace review, anything whose ownership is unclear.
5. **Report**: per-dir before/after, files moved (with backup path), config diffs, and what will now stop loading into sessions. Propose recording new conventions discovered (e.g., a migration map) to the operator's profile/memory.

## Output Format

```
# Agent home audit: <dir> — <date>
## Inventory (top offenders)
## Findings (by pathology, with evidence)
## Executed
- Tier 0: <deleted, MB reclaimed>
- Tier 1: <config changes>
- Tier 2: <moved to backups/..., reversible>
## Report-only (needs your call)
## Context-cost impact (what stops loading per session)
```

## Notes

- The never-touch set is absolute: credentials, memory/notes, user-authored content, active sessions. When ownership of an item is uncertain, it is report-only.
- Duplication claims require hash verification; "looks the same" is not evidence.
- Tier 2 is moves-to-backup by definition — deletion of moved content is a later, separate operator decision.
- Cross-CLI: run per home dir; the pathology library is vendor-agnostic even though every layout differs.
