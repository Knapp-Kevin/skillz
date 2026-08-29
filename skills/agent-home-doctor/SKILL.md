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
  version: 1.2.0
---

# Agent Home Doctor

An adaptive audit and cleanup framework for agent CLI home directories. Vendor layouts change; the durable mechanism is a pathology library plus evidence-backed, tiered remediation. The specific directory layout, retention policy, and migration rules bind at runtime.

## Execution Flow

1. **Bind.** Enumerate dot-directories in the relevant profile root instead of relying on a hardcoded vendor list. Classify each discovered directory as agent CLI home, toolchain/package cache, app data, or unknown. Read operator retention/migration/never-touch conventions when available. If no retention policy exists, propose 30 days as a starting point but do not turn that proposal into deletion authority.
2. **Inventory.** Build a top-level size/count map, then drill into offenders. Establish the never-touch set first: credentials/keys, memory/notes, user-authored skills/commands/hooks, active session state, downloaded model caches, and anything the operator marks.
3. **Diagnose against the pathology library:**
   - unbounded transcript/session/edit history beyond the bound/proposed retention period;
   - regenerable temp/cache material;
   - extension-surface duplication, hash-verified before any duplicate claim;
   - dead config references, path-verified;
   - deprecated-prefix remnants under an established migration map;
   - stale backups, diffed before classification.
4. **Prepare a remediation plan before mutation.** List the exact paths/actions, evidence, estimated reclaim, and tier. Show this plan to the operator. **No deletion, config edit, or move happens until the operator explicitly approves that plan or named items from it.** A request to "audit" is not approval to clean.
5. **Remediate only the approved items:**
   - **Tier 0 (delete only after explicit plan approval):** aged temp/history beyond the approved retention rule, confirmed regenerable caches, diffed-stale backups.
   - **Tier 1 (config edit only after explicit plan approval):** pin retention settings; remove verified-dead config references.
   - **Tier 2 (reversible move only after explicit plan approval):** move hash-verified duplicates/deprecated remnants into a dated backup directory; never delete them in the same operation.
   - **Tier 3 (report only):** third-party applications, plugin/marketplace changes, unknown ownership, credentials, model caches, or anything whose safe disposition is uncertain.
6. **Verify every mutation.** Re-list affected source/destination paths, re-count backup destinations after moves, and confirm reclaimed space rather than assuming commands succeeded.
7. **Report** before/after evidence, approved actions actually executed, backup locations, config diffs, failed/blocked actions, and any convention worth recording for future runs.

## Output Format

```text
# Agent home audit: <dir> — <date>
## Inventory
## Findings (by pathology, with evidence)
## Proposed remediation (approval required)
| Tier | Exact path/action | Evidence | Reclaim | Risk/reversibility |
## Approved + executed
- <action> — verified by <post-action check>
## Blocked / report-only
## Context-cost impact
```

## Negative rules

- Never delete, edit configuration, or move files on the basis of an audit request alone. Show the exact remediation plan first and require explicit approval.
- The never-touch set is absolute unless the user separately changes that policy: credentials, memory/notes, user-authored content, active sessions, and downloaded model caches.
- Duplicate claims require content/hash evidence. Similar names are not evidence.
- Never kill processes, take ownership, or weaken permissions merely to force cleanup.
- A failed move/delete remains failed until source and destination state proves otherwise.
- If ownership or regenerability is uncertain, demote the item to Tier 3 report-only.

## Notes

- Locked directories: when an approved move cannot proceed, report the lock. Copy-to-backup-then-clear is itself a distinct mutating plan and requires approval; do not silently substitute it.
- Recursive listings can obscure nesting. Confirm top-level versus nested paths before proposing a move.
- Third-party applications living inside an agent home are report-only. Recommend the application's normal uninstall path rather than deleting its data.
- Run per home directory. The pathology library is vendor-agnostic; the filesystem assumptions are not.