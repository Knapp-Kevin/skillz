# First-party pulse passive collection remediation, 2026-10-12

Issue: [#415](https://github.com/Knapp-Kevin/skillz/issues/415). Scope: the exact **17** first-party Monitoring & Intelligence skills in `index.json`.

## Whole-family macro inventory

- **17/17** first-party monitoring manifests inspected at repository main, exactly **16/17** contained a live command calling removed `node scripts/pulse-run.ts`. `claude-pulse` was already passive and did not need changes.
- **16** manifests revised to use the external host's authorized retrieval capabilities and the skill's bundled `sources.json`. No runner, fetcher, scheduler, CI, or background process added. The vendor-specific research targets, synthesis outputs, and source assets remain intact.
- Scheduling instructions now state that host-supported scheduling requires specific user authorization. A passive skill is not authorization to create a schedule.
- For each of the 16 changed manifests, the individual exact-version verification companion was refreshed to the **new Git blob SHA**, `reviewed_at` set to 2026-10-12, behavioral validation remains `not-run`, and historical scanner results are not inherited as current package-security evidence. The consolidated `registry/local-verification.json` was reconciled for the same 16 entries.
- Each changed first-party provenance companion received a 2026-10-12 freshness check. No third-party source identity, pin, or review count changed.

## Static verification

Read-back comparison of **17/17** current branch manifests and companions shows:
- zero live references to `node scripts/pulse-run.ts`, the shared repository engine, or repository-root invocation assumptions;
- exact manifest SHA equality with individual verification companions for **17/17**;
- no claimed representative external behavioral execution.

## Architectural and security notes

The problem was **live first-party documentation drift**, not evidence that an upstream pinned package cannot contain its own tools. Source-owned package scripts remain allowed as upstream reference material. In `skillz`, collection is initiated, authorized and executed by an external host.

This semantic/manual remediation does not establish a new exact-package security pass for changed content. The existing corpus security-backfill issue #402 still governs evidence collection. Avoid silently treating historical SkillSpector CI as current.

## Public accounting

This is a **16-of-17 first-party revision**, not new admissions: first-party inventory **44 -> 44**, first-party provenance **44/44 -> 44/44**, third-party semantic companions **721 -> 721**, registered sources **22 -> 22**, admitted source denominators unchanged. Five public surfaces must remain in agreement; PR #408 is concurrently modifying them for the passive-architecture correction, so avoid overwriting that branch's work before reconciliation.

## Review acceptance

- Inspect exact changes on the sixteen skills for retained specialized search targets, output contracts, privacy and host approval.
- Confirm first-party provenance and verification companions and consolidated local index cover all 16 exact current blobs.
- Confirm no deleted runner is referenced anywhere in the 17 skills.
- Check package-security/behavioral state truthfully, and coordinate the five public surfaces with PR #408 before merge.
- No repository-owned automation, or forced host execution.
