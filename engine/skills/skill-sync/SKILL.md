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
2. Establish the destination's actual supported format, path/API surface, and authority requirements.
3. Read the source skill and any material provenance/licensing obligations.
4. Compare the source artifact with the destination when the host can inspect both.
5. Classify each item as `CREATE`, `UPDATE`, `UNCHANGED`, `SKIP`, or `BLOCKED`.
6. Present the intended changes before any external mutation when approval is required by the target environment or user instructions.
7. Apply only authorized changes using the host's legitimate file/API tools.
8. Report actual destination state and any unresolved compatibility issues.

## Negative rules

- Do not invent a universal installation path.
- Do not make this procedure a prerequisite for normal bootstrap.
- Do not treat a writable destination as authorization to modify it.
- Do not claim a copy/update occurred when the host could only produce a portable handoff.
