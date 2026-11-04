# Maintainer Workboard

**What needs attention next in Skillz.** This is a **dated, hand-maintained issue/PR snapshot**, not a live monitor, and not a skill installer. It helps a maintainer find the active implementation, see what is blocked, and keep valuable earlier research. [Machine-readable snapshot](registry/maintenance/open-work-snapshot-20261103.json).

**Checked November 3, 2026:** **10 open draft PRs** and **12 open issues**. Merged `main` at `e083c47f13a8` still features **20 study references in 10 domains**; [Q8 draft #693](https://github.com/Knapp-Kevin/skillz/pull/693) proposes **50 across 33 domains**. Its source security breakdown is **10 pass, 7 fail, 33 incomplete; 0 unchanged-use approvals; 0 observed behavioral validations**. Those drafts have **not** been published to main.

## Next three maintenance actions

1. **Fix shipped first-party instructions safely.** [#673](https://github.com/Knapp-Kevin/skillz/pull/673) repairs 16 removed pulse-runner paths, but 3 scanner failures and 3 incomplete scans remain. [#686](https://github.com/Knapp-Kevin/skillz/pull/686) fixes five secret/privacy instructions and has 5/5 scanner passes, but still lacks executed adversarial permission and leakage tests. Reconcile exact current package identities and linked review registries before any merge. Track through [#415](https://github.com/Knapp-Kevin/skillz/issues/415), [#491](https://github.com/Knapp-Kevin/skillz/issues/491), [#402](https://github.com/Knapp-Kevin/skillz/issues/402).
2. **Assign the uncovered authority fixes.** [#478](https://github.com/Knapp-Kevin/skillz/issues/478) (five recurring skills), [#481](https://github.com/Knapp-Kevin/skillz/issues/481) (four more), [#483](https://github.com/Knapp-Kevin/skillz/issues/483) (two obsolete permission policies), and [#495](https://github.com/Knapp-Kevin/skillz/issues/495) (private receipts and cross-repo writes) have no confirmed open replacement implementation PR. `permissions-review` appears in both #481 and #483: **one writer should combine those edits** rather than produce conflicting patches. A one-time request never authorizes a recurring schedule, private source read or cross-repository write.
3. **Reconcile curation and publishing only once its source settles.** [Q8 #693](https://github.com/Knapp-Kevin/skillz/pull/693) is the source of 50 proposed study references; [Q12 #700](https://github.com/Knapp-Kevin/skillz/pull/700) gives 50 source-pinned per-method security receipts; [Q11 #699](https://github.com/Knapp-Kevin/skillz/pull/699) still renders an older 45-method draft checkpoint. Once Q8 is stable, regenerate Q11, run both Node generators with `--self-test` and `--check` in a real checkout, inspect the chart/README visually, then seek maintainer acceptance. **Never merge a stale generated chart because it happens to render.**

## Open PRs, grouped by purpose

| Lane | PRs | Why they remain open |
|---|---|---|
| First-party authority fixes | [#673](https://github.com/Knapp-Kevin/skillz/pull/673), [#686](https://github.com/Knapp-Kevin/skillz/pull/686) | Exact package and behavioral gates still pending; no new runner, private data or credentials may leak |
| Curated references | [#693](https://github.com/Knapp-Kevin/skillz/pull/693) | 50 study-only references across 33 areas, not install recommendations |
| Discovery and static reviews | [#697](https://github.com/Knapp-Kevin/skillz/pull/697), [#698](https://github.com/Knapp-Kevin/skillz/pull/698) | 8 distinct Q9 leads, all 8 statically reviewed by Q10; counts overlap, no hardware/runtime proof |
| Publication and scanner evidence | [#699](https://github.com/Knapp-Kevin/skillz/pull/699), [#700](https://github.com/Knapp-Kevin/skillz/pull/700) | Q11 is behind Q8; Q12 correctly distinguishes passed/failed/incomplete scanner results |
| Prior source research worth keeping | [#677](https://github.com/Knapp-Kevin/skillz/pull/677), [#682](https://github.com/Knapp-Kevin/skillz/pull/682), [#692](https://github.com/Knapp-Kevin/skillz/pull/692) | Independent discovery, MIDI review, historical Q7 identity-gap receipt; preserve even when newer ledgers supersede individual status claims |

## Open issues, by responsibility

| Lane | Issues | Main remaining outcome |
|---|---|---|
| First-party security/authority | [#402](https://github.com/Knapp-Kevin/skillz/issues/402), [#415](https://github.com/Knapp-Kevin/skillz/issues/415), [#491](https://github.com/Knapp-Kevin/skillz/issues/491) | Secure changed package trees, executed adversarial tests and exact evidence integration |
| Unassigned authority repairs | [#478](https://github.com/Knapp-Kevin/skillz/issues/478), [#481](https://github.com/Knapp-Kevin/skillz/issues/481), [#483](https://github.com/Knapp-Kevin/skillz/issues/483), [#495](https://github.com/Knapp-Kevin/skillz/issues/495) | Narrow consent boundaries and non-overlapping ownership |
| Rights | [#544](https://github.com/Knapp-Kevin/skillz/issues/544) | Resolve truncated pinned upstream MIT license; do not silently relicense |
| Coverage and corpus | [#588](https://github.com/Knapp-Kevin/skillz/issues/588), [#599](https://github.com/Knapp-Kevin/skillz/issues/599), [#624](https://github.com/Knapp-Kevin/skillz/issues/624) | Distinct lanes: capability-depth map, open-ended source universe, risk-tiered review throughput |
| External evidence | [#589](https://github.com/Knapp-Kevin/skillz/issues/589) | Pinned external scanners and representative host acceptance without adding repository runtime |

## Historic links that are **not** active work

[#412](https://github.com/Knapp-Kevin/skillz/pull/412), [#413](https://github.com/Knapp-Kevin/skillz/pull/413), [#489](https://github.com/Knapp-Kevin/skillz/pull/489), [#492](https://github.com/Knapp-Kevin/skillz/pull/492), [#496](https://github.com/Knapp-Kevin/skillz/pull/496), and [#590](https://github.com/Knapp-Kevin/skillz/pull/590) are **closed without merging**. Issue #402 previously described some of them as current; its current-status heading has been corrected. **Do not delete their useful source/evidence artifacts**. Reuse or archive a superseded draft only after checking its distinctive receipts and dependencies, recording the successor and obtaining the appropriate maintainer decision.

## What counts as complete

**Hygiene is not about shrinking counts.** A closed issue without a qualified fix is not progress. A scanner pass does not prove task behavior; a study-worthy idea is not an install-approved package. Report `discovered`, `reviewed`, `security complete`, `behavior tested`, `approved unchanged`, and `merged` separately. Global distinct eligible-package totals remain **UNKNOWN** until reconciled from source snapshots. No task here authorizes GitHub Actions, repository-run scanners, scheduled runtime, source installs or destructive cleaning.

*Snapshot only, November 3, 2026 (America/New_York). Before taking an action, re-read the named issue/PR head and the exact upstream source; GitHub state changes in parallel. This workboard should be updated in bounded batches rather than repeated as a growing chronological log.*
