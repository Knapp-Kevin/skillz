# Architecture challenge: visual organization for a long-lived agent

Date: 2026-11-23. Current source: Skillz authored File Lifecycle
Curator v1.1.1. This review accompanies a bounded **read-only visual
projection** of the curator's existing organization plan and ledger.

## Decision: accept as a projection, reject as persistent truth

The visual layer makes the output of file curation more understandable:
what exists, what the future target could look like, what has truly
passed read-back, and what remains blocked. However, making the diagram
a separate persistent data store or agent-maintained source of truth
would introduce drift, access leakage and false "done" claims.
Decision: render anew from independently scoped source/plan/operation
evidence on each authorized run.

## Adversarial challenge matrix

| Priority | Attack/failure | Safe design response |
|---|---|---|
| P0 | Proposed folder tree looks like actual completed moves | Three explicitly labeled observed/proposed/read-back-attested views |
| P0 | Agent increments progress on approval, script exit or success toast | Count only strict current plan/revision/source-bound read-back receipts and observed target |
| P0 | Scheduled agent reuses cached private names after viewer access is revoked | Current collection and per-record viewer gates; suppress all IDs/counts on hold |
| P0 | Record absent due to per-file ACL filter appears from historical cache | Withhold old IDs and summary counts; return ABSENT_IDENTITY_ACCESS_HOLD |
| P0 | Duplicate destination or source path, traversal, Mermaid/HTML injection | Restrict to validated non-executable aliases, reject collisions and path escaping |
| P1 | Older receipt replays under a new plan revision | Exact plan ID/revision binding and REPLAN_REVIEW |
| P1 | Target path changes under the same plan revision | PLAN_DRIFT_HOLD instead of silently rewriting targets |
| P1 | Partial snapshot says 100% folder organization finished | Suppress percentage; show scoped counts, partial/omitted indicators |
| P1 | An EXECUTED move lacks destination integrity/ACL readback | Keep distinct EXECUTED-but-unverified count and no verified increment |
| P1 | Rollback counted as a completed target relocation | Separate ROLLED_BACK with original-path readback; no verified increment |
| P1 | Same scheduled snapshot gets processed again | SAME_SNAPSHOT_NO_WORK, not another transition; renderer never writes |
| P1 | Long folder tree overwhelms human user | 24-record deterministic visualization cap, explicit omission count |
| P1 | A current path changes without same identity evidence | Stable IDs and source revisions; current view does not invent causation |
| P2 | Host cannot display Mermaid or is inaccessible | Equivalent indented text-tree fallback and textual status, no color-only signal |
| P2 | User prefers a different visualization | Preference affects presentation only, never authority, evidence or canonical progress |

## Ownership and authority boundaries

- **User/owner:** approves source collection, target structure,
  action batches, result audience, persistence and cadence independently.
- **Source host:** verifies current viewer, root, native path identity,
  source revisions, completeness and ACL context.
- **Operation host:** performs specifically authorized mutations,
  records actual receipts, checks destination readback/collision
  safety and any rollback. The visualizer cannot take this role.
- **File Lifecycle Curator:** proposes categories and target mappings,
  reports holds and review candidates; no default write authority.
- **Visual projection:** validates input structure, binds asserted
  receipts, counts scoped milestones and renders Mermaid + plain text.
  It neither mutates a file nor certifies caller assertions.
- **Scheduler (optional):** triggers an already authorized invocation.
  It never upgrades viewer scope, user approval or success status.

## Long-term versioning and aging

Keep plan_id + plan_revision stable within an approved plan; only a
new explicit reviewed plan may replace target mappings. Keep snapshot
IDs/time monotonic and access scope constant when computing progress.
The helper can compare two supplied snapshots; persistent history
belongs only in the separately authorized private checkpoint store.
No "self-healing" mutation of source tasks, no unsupervised retention
change, no automatic recurrence, and no cross-user preference leakage.
Scope expansion is a new authorization request, not an incremental
refresh. Stored diagrams should have retention and expiry constraints,
since even abstract folder names and counts can be sensitive.

## Important limitation and recommended host trial

The Python helper is a strict **illustration** of the contract,
not a source-of-truth search engine. Native filenames may contain
spaces, non-ASCII symbols or provider-specific semantics not
accepted as safe CLI display aliases. The host can map permitted
names to aliases and render its own properly escaped private UI.
The parser cannot prove that "current-authorized", "complete" or
a "matched" read-back was actually observed, nor that a destination
outside the supplied records is safe. It cannot prevent time-of-check
vs time-of-use swaps. Source testing only proves deterministic
refusal/rendering, not real file navigation, restore, actual
authorization or human usability.

A future independent consumer trial should use a controlled file
library, a real approved host and at least two distinct snapshots:
observe native entries/permissions and original IDs; propose a
target; authorize one actual relocation; capture real read-back;
restart/resume; verify the observed/proposed/verified views match
current source; induce ACL revocation and interrupted operations;
then measure time to locate files, false completions, omitted
files and actual progress accuracy. **Until that happens, live
agent-host and user outcomes are NOT_RUN.**

## Release boundary

This is a bounded correctness/UX refinement of v1.1.1.
No cosmetic version increment, new scheduler, external backend,
background agent, database or task session is authorized.

## Post-green manual adversarial challenge

The first 76/76 source test pass missed two meaningful long-lived-agent concerns. (1) A proposed destination could overlap a *currently occupied* file path of an unplanned record or an item assumed to move earlier, even if planned destinations were unique. This requires a staging/collision review, not an optimistic diagram; the renderer now rejects within-snapshot target/current conflicts and file/directory prefix overlaps. It does not prove external destination vacancy. (2) The future tree silently omitted unplanned records. The proposed projection now retains them at their observed location with UNPLACED_KEEP_CURRENT, not an invented physical destination. Four additional synthetic test cases exercise occupancy conflicts and the original unplanned test also checks visibility. The revised expected total is **80 source tests** (38 prior maintenance plus 42 visualizer), subject to exact-head CI.

## Reviewer-identified false completion boundary

Automated adversarial PR review found that rounding the scoped progress indicator to a whole number could report **100% with 199 of 200 planned relocations verified**. The renderer now displays one decimal and reserves 100.0% for full planned-set verification. A new 200-record regression case qualifies 199/200 => 99.5%. The same review also flagged proposed-target versus currently occupied unplanned-file collision, already addressed in the preceding manual-review correction and tested for both unplanned and moving occupants. Final source coverage is now **81 tests** (38 existing + 43 visualizer), pending exact-head rerun.
