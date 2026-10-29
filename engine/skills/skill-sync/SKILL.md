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
  version: 2.0.0
  repo-bound: true
---

# Skill Sync

**Repository-maintenance / explicit export procedure only.**

There is no repository-owned installer or sync runtime. The active host agent performs any requested comparison or copy using capabilities it already has.

## Procedure

1. Confirm the user explicitly wants skills already represented in `skillz` copied, updated, or handed off to another destination.
2. Establish the exact destination account, path/API surface, supported format, intended recipients, and applicable authority/privacy/licensing constraints. Do not infer authorization from connector availability or a writable target.
3. Read the source skill and any material provenance/licensing obligations.
4. Compare the source artifact with the destination when the host can inspect both.
5. Classify each item as `CREATE`, `UPDATE`, `UNCHANGED`, `SKIP`, or `BLOCKED`.
6. **Before any external mutation**, establish explicit action-appropriate authorization covering the destination account/path, exact artifact set, create versus overwrite/delete, disclosure/recipient scope, material costs, and any persistent access or retention. A generic export request, tool availability, destination selection, or a preview is not by itself approval for unbounded writes. When authority is absent or ambiguous, stop at a read-only plan or portable handoff.
7. Use only secure host-managed credential channels. Never ask for real secret values in chat, include credentials in handoff artifacts, or echo secret fragments, signed URLs, or private source contents into reports. Minimize any cross-account or external data transmission to the authorized scope.
8. Apply only the specifically authorized changes using legitimate host file/API tools. Recheck the target and write scope immediately before overwriting, deleting, sending, or changing persistent state; stop if the target or approval has changed.
9. Report observed destination state, changed versus skipped items, partial failures, and any unresolved compatibility or rollback limitations. Never claim a write succeeded from a proposed plan.

## Negative rules

- Do not invent a universal installation path.
- Do not make this procedure a prerequisite for normal bootstrap.
- Do not treat a writable destination, existing connector, or prior unrelated approval as authorization to modify it.
- Do not perform an overwrite, deletion, disclosure, or recurring synchronization without action-specific authorization.
- Do not claim a copy/update occurred when the host could only produce a portable handoff.
