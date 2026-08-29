---
name: skill-sync
description: >-
  Prepare and transfer selected portable skills to another agent host using
  only the external host agent's available installation or file capabilities.
  Use when a user asks to install, copy, upload, package, or hand off a fitted
  skill set to another supported agent environment.
metadata:
  author: frostwulf.zo.computer
  category: Meta
  display-name: Skill Transfer
  emoji: "🚀"
  version: 2.0.0
  repo-bound: true
---

# Skill Transfer

This is a passive instruction set. `skillz` does not synchronize, install, copy, junction, package, or deploy anything itself.

The external agent may perform those actions only when its host provides the necessary capability and the user has authorized the mutation.

## Procedure

1. Identify the exact skill artifacts to transfer.
2. Confirm they are intended for user-facing use rather than repository-maintenance instructions.
3. Identify the destination host and the installation/packaging mechanism from authoritative host information when available.
4. Compare the source skill format with the destination format.
5. Preserve skill identity, instructions, provenance, and any material license obligations.
6. If adaptation is needed for the host, keep host packaging separate from the portable behavioral source of truth.
7. Before mutation, present or internally verify the intended destination and files.
8. Use the external host's own write/upload/API capabilities only when authorized.
9. Verify the resulting destination state when the host makes that possible.
10. Report one truthful completion state.

## Completion states

Use a state such as:

- `INSTALLED + VERIFIED`
- `INSTALLED, VERIFICATION PENDING`
- `READY TO UPLOAD`
- `USER ACTION REQUIRED`
- `BLOCKED: HOST DOES NOT SUPPORT SKILLS`
- `BLOCKED: INSTALLATION METHOD NOT ESTABLISHED`

Do not claim installation merely because the skill artifact exists in `skillz`.

## Boundaries

- No destination mutation without the authority normally required by the external host.
- Do not assume two surfaces of the same product share installed skills.
- Do not invent filesystem paths, upload formats, APIs, or product capabilities.
- Third-party source material under `skills/sources/` retains its upstream identity and license obligations.
- When direct unchanged reuse is unsuitable, create an adapted portable skill rather than mutating the pinned reference source.

The repository supplies instructions and artifacts. All active transfer behavior belongs to the external agent.
