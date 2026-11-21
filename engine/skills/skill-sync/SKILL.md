---
name: skill-sync
description: >-
  Reconcile portable skills already represented in skillz with an explicitly
  authorized external destination using the host agent's own file/API tools.
  Use only when the user asks to move or update those artifacts.
metadata:
  author: frostwulf.zo.computer
  category: Meta
  display-name: Skill Sync
  emoji: "🚀"
  version: 2.1.0
  repo-bound: true
---

# Skill Sync

**Repository-maintenance / explicit export procedure only.**

There is no repository-owned installer or sync runtime. The active host agent performs any requested comparison or copy using capabilities it already has.

## Procedure

1. Confirm the user explicitly wants skills already represented in `skillz` copied, updated, or handed off to another destination.
2. Establish the exact destination account, path/API surface, supported format, intended recipients, and applicable authority/privacy/licensing constraints. Do not infer authorization from connector availability or a writable target.
3. Resolve the **exact source package**, not only its `SKILL.md`: all mandatory references, scripts, templates, fixtures, asset files, licenses and notices. Bind exact source revision/complete package identity when supported and confirm rights for the proposed destination and redistribution. Unknown or inaccessible required files are a HOLD, not a silently partial export.
4. Compare the complete source package with the intended destination when the host can inspect both. Separate text-only handoff, partial feature adaptation, exact copy and update in the classification. Existing destination changes must not be overwritten merely to force a hash match.
5. Classify each complete package and any necessary components as `CREATE`, `UPDATE`, `UNCHANGED`, `SKIP`, or `BLOCKED`. A destination that lacks any mandatory support is **PARTIAL/BLOCKED**, not `UNCHANGED` or `INSTALLED`. Treat generated files and symlinks with source authority and path containment; do not traverse unknown links or execute source scripts during comparison.
6. **Before any external mutation**, establish explicit action-appropriate authorization covering the destination account/path, exact artifact set, create versus overwrite/delete, disclosure/recipient scope, material costs, and any persistent access or retention. A generic export request, tool availability, destination selection, or a preview is not by itself approval for unbounded writes. When authority is absent or ambiguous, stop at a read-only plan or portable handoff.
7. Use only secure host-managed credential channels. Never ask for real secret values in chat, include credentials in handoff artifacts, or echo secret fragments, signed URLs, or private source contents into reports. Minimize any cross-account or external data transmission to the authorized scope.
8. Apply only the specifically authorized changes using legitimate host file/API tools. Recheck the target and write scope immediately before overwriting, deleting, sending, or changing persistent state; stop if the target or approval has changed. Transfer every required support file in a bounded package, preserve controlling licenses/NOTICE, and avoid running installed code merely to prove a copy.
9. **Verify the actual destination** after transfer when the host permits: compare each required file's content identity, package inventory/relative links, source rights/notice closure and host installation location. A passed API copy response or created folder is not proof the full skill can run offline. Report `COPIED_EXACT`, `COPIED_PARTIAL`, `UNCHANGED_VERIFIED`, `BLOCKED` or `HANDOFF_ONLY` with observed evidence, changed versus skipped items, partial failures, and recovery/rollback limits. Never claim success from a proposed plan or an unverified write.

## Export integrity probes

- A downloaded skill contains `references/`, `scripts/` and `assets/`,
  but only `SKILL.md` arrives: **partial**, even if the main file opens.
- A destination has the right folder/name but a different required
  script digest or missing NOTICE: **not unchanged**.
- A portable package references a parent Skillz repository policy at
  runtime: report package-closure defect, not a successful offline install.
- An authorized copy is attempted with unavailable readback: report the
  attempted write and verification gap, **not** confirmed installation.
- A user merely requested comparison or preview: no write authority.

These are static probes unless a real authorized export and destination
readback occurred. The passive repository owns no autonomous sync daemon.

## Negative rules

- Do not invent a universal installation path.
- Do not make this procedure a prerequisite for normal bootstrap.
- Do not treat a writable destination, existing connector, or prior unrelated approval as authorization to modify it.
- Do not perform an overwrite, deletion, disclosure, or recurring synchronization without action-specific authorization.
- Do not claim a copy/update occurred when the host could only produce a portable handoff.
