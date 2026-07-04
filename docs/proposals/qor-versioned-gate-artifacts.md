# Proposal for Qor-logic: iteration-versioned gate artifacts

**From**: skillz repo governance experience (sessions 2026-07-03T2023-ca9b2c, 2026-07-04T0405-927a53)
**To**: Qor-logic maintainers (MythologIQ/Qor-logic)
**Status**: draft for operator to carry upstream (BACKLOG B10)

## Problem

`gate_chain.write_gate_artifact` stores each phase's artifact at a mutable singleton path (`.qor/gates/<sid>/<phase>.json`). Multi-iteration phases are the *normal* path — audit VETO→PASS, substantiate FAIL→SEAL — and each re-run **overwrites the previous artifact in place**. When a ledger entry has already sealed the earlier iteration's content hash, the overwrite destroys the sealed evidence: the file a chain entry binds no longer exists on disk.

This is not hypothetical. In the skillz repo's first governed cycle, ledger Entry #2 sealed the iteration-1 VETO artifact at `3da98e31…`; the iteration-2 PASS overwrote the same `audit.json`, and the Judge's chain recalculation at audit iteration 3 found the binding broken (recorded as skillz Shadow Genome Failure #2, `CHAIN_BREAK`).

A sibling defect: the singleton `plan.json` retains the pre-amendment payload after a plan is amended and re-audited, silently misrepresenting the gated state.

## Proposal

**One seal, one immutable file.**

1. `write_gate_artifact` writes `<phase>-iter<N>.json` (N = per-phase, per-session iteration counter), never overwriting an existing artifact. The unversioned `<phase>.json` may remain as a convenience symlink/copy of the latest iteration, but sealed hashes always bind versioned files.
2. `check_prior_artifact` resolves the highest iteration by default.
3. `audit_history.jsonl` (already appended) gains the versioned filename per row, closing the loop between history and evidence.
4. Ledger tooling (`verify-ledger`) verifies entries against versioned artifacts using LF-normalized bytes (equivalently, the git blob) — a second lesson from the same repo: `core.autocrlf` checkouts rewrote working-tree bytes and broke naive hash verification of intact content (skillz Chain Integrity Note, 2026-07-04). Recommend shipping a `.gitattributes` stanza in `qor-logic seed` pinning `docs/*.md` and `.qor/**` to `eol=lf`.

## Compatibility

Additive: existing singleton readers keep working via the latest-copy convention; new seals reference versioned files. No retroactive migration — pre-existing chains note the discipline change in their Chain Integrity Notes, as skillz did.

## Evidence

- skillz `docs/SHADOW_GENOME.md` Failure #2 (CHAIN_BREAK) — the overwrite event, detection, and countermeasure.
- skillz `docs/META_LEDGER.md` Chain Integrity Notes — both the overwrite event and the line-ending ruling.
- Working versioned-artifact practice since: `audit-iter2.json`, `plan-iter4.json`, `implement-iter2.json` (session ca9b2c) and `ideation-iter1.json` onward (session 927a53).
