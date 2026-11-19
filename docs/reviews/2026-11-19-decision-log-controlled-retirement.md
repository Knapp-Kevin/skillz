# decision-log controlled retirement qualification (source-bound)

Date: 2026-11-19. Tracking: [#738](https://github.com/Knapp-Kevin/skillz/issues/738). Two sources share a PR but retain **separate qualification and rollback**.

## Immutable original and independent replacement

- [Historical original](https://github.com/Knapp-Kevin/skillz/blob/52a6b0419630091e04a53b04161d200ab5ef3f38/skills/decision-log/SKILL.md) `skills/decision-log/SKILL.md`, Git blob `53b82e2a4838cdba57ee2e4c9158d6d2b4150c6b`, complete single-file Git tree `ca790304801fd1717841a8fab98bb4ebeed4c9bf` verified at pinned historical revision `319b6eae2dedf3e8ca1ceac77aaed5a710d91ff0` and unchanged in pre-retirement main. Inventory: exactly one 100644 `SKILL.md`.
- [Decision Record Steward](../../skills/authored/decision-record-steward/SKILL.md), independently authored v1.1.0, entrypoint blob `d9005c5c1b3fbed122a52d106104dbee02b5a165`, full package tree `56b32d80412fbae75f05914e992156f081d8ce05` with license and example fixtures. New MIT text does **not** establish authorship/copyright of historic texts. Historical origin rights remain unresolved; Git history is preserved.

## Function-level outcome and safety comparison

Original essential behaviors: an owner-specified decision, context, alternatives only when supplied, rationale provenance, revisit date or NOT_SET, authorized append-only storage and overdue/upcoming reports. New instructions explicitly retain and broaden these to effective dates, review triggers, supersession, approval and readback. Five cases checked an authorized draft not saved, overdue/upcoming with a superseded entry, unknown context/date without fabrication, malicious legacy-note instructions inert, and a write-acknowledgement with failed readback remaining ATTEMPTED. An additional temporary-file append/readback actually executed and verified preservation of the original prefix and the newly appended entry. No user files or decision stores were changed.

## Executed and emulated checks

- Published case contracts: [docs/evals/frostwulf-phase1-paired-scenarios.json](../evals/frostwulf-phase1-paired-scenarios.json).
- [Procedure receipt](../evals/receipts/2026-11-19-automation-decision-controlled-procedures.json) lists **five of five** bounded case assertions passing for this individual predecessor, observed emulated outputs and SHA-256 identities of the ephemeral driver/local result. No missing outputs were silently promoted to verified.
- A real disposable Python evaluation and synthetic-file experiment took place outside Skillz. The driver interprets author-written process rules; **it is not a matched original-versus-new isolated model-host execution**. No independent blind adjudication, actual customer/job execution, overall functional parity or measured >=1.5× gain established. The ephemeral driver and full output are not committed; the checked scenario/output summaries are retained in the repository receipt. This limits reproducibility.
- Negative authority gates: no new scheduler, secrets, third-party contact, unauthorized writes, silent permission widening or fabricated persisted success. Historic account ownership does not grant rights in original expression.

## Consumer disposition and explicit owner exception

Update known root/category navigation, active governed name and local verification indexes, capability directory and preview, README, summary chart, migration/evaluation records and two historical provenance companions. The full repository-wide consumer scan is still **NOT_PROVEN**, a specific recorded risk under the owner's per-source controlled-emulation authorization. Only this one original entrypoint is qualified within the shared change; other historical entries are unaffected.

## Rollback and exact-head gate

Restore Git blob `53b82e2a4838cdba57ee2e4c9158d6d2b4150c6b` at `skills/decision-log/SKILL.md` from immutable commit `52a6b0419630091e04a53b04161d200ab5ef3f38`, restore indexed visibility and reconcile counts if an unknown consumer breaks. Require exact-head source and routing checks before merge and live-main readback afterwards. Do not claim success on main because the proposed branch contains a deletion.
