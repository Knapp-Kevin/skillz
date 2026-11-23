# Visual folder organization: long-lived agent contract and challenge review

This optional component is designed for repeatable **File Lifecycle Curator**
runs. It produces a visual representation of **observed current structure**,
**hypothetical target structure**, and **read-back-attested completed changes**
without manipulating source data or treating a diagram as an action ledger.

## Architecture choice

The operation ledger, source identities and time-bound host observations
remain authoritative. **A visual tree is a pure, reproducible projection.**
Do not store a drawing as a second source of truth, infer completion from its
layout, let visualization code approve file operations, or use a prior
rendered diagram as a fresh inventory. The actual authorization and operation
states are defined by
[operation-and-archive-rules.md](operation-and-archive-rules.md).

Three distinct user-facing views:
1. **OBSERVED (caller asserted)**: the latest actually supplied source
   listing; say when it was captured and whether coverage is partial.
   An unvisited folder or filtered file is UNKNOWN, not absent.
2. **PROPOSED (NOT APPLIED)**: the structure produced by a reviewed
   non-mutating organization plan. Preserve original identity and show
   blocked/ambiguous candidates separately. It is not proof the target
   directory exists, is writable, conflict-free across the entire
   provider, or has safe ACL inheritance.
3. **READ-BACK-ATTESTED (not independently verified by helper)**: only
   changes whose current source observation and per-record scoped
   operation receipt agree on record ID, plan ID/revision, original
   source revision, destination and access/integrity preservation.
   APPROVED and EXECUTED must not be shown as completed changes.
   ROLLED_BACK does not count as a completed migration.

Never present a merged "after" diagram without visibly separating
PROPOSED from OBSERVED/VERIFIED. Do not imply that a completed-looking
diagram authorizes moving, sharing, rewriting, deleting, archiving,
purging, or changing access permissions.

## Progress measurement and truthfulness

The only migration-progress numerator is the number of records
qualifying for **read-back-attested VERIFIED** in the current accepted
scope. The denominator is the set of *planned relocations*, not all
files processed, tagged, summarized or displayed. Do not count
unchanged records, rejected proposals, approved actions or execution
attempts as completed organization.

- For a source-declared COMPLETE coverage snapshot, show the scoped
  planned count, verified count and provisional percentage. Label
  the denominator as **caller-asserted complete**, not an independently
  exhaustive crawl or a guarantee of user benefit.
- For PARTIAL coverage, show verified/planned **within observed scope**,
  but suppress the percentage; the full collection denominator is
  unknown. A truncated diagram is explicitly a sample, not a full tree.
- For no planned relocations, show "0 planned", not 100% complete.
- Show FAILED, BLOCKED, EXECUTED-but-unverified, ROLLED_BACK and
  UNKNOWN counts independently. A rollback may require re-planning.
- Preserve verified-to-unverified regressions across permitted
  checkpoints instead of silently retaining a green progress indicator.
- A successful scheduled trigger, index creation or diagram export
  is not evidence of a verified physical relocation.

## Stable planning and scheduled-agent replay

A plan has immutable source-scoped **plan ID and plan revision** and
each input record has stable source ID and source revision. A later
snapshot with a changed target or original path under the same plan
revision returns PLAN_DRIFT_HOLD. A new revision is a deliberate
REPLAN_REVIEW: do not combine its percent or receipts with the old
denominator. The host should present it as a new approved plan
baseline only after separate authorization.

An identical snapshot ID with identical content is idempotent and
may render again without performing new work. An identical snapshot ID
with different content is INVALID. A strictly newer snapshot must
have a later timezone-aware observation time. A previously visible
record missing in a new listing triggers ABSENT_IDENTITY_ACCESS_HOLD
with no old ID/count, because an ACL filter may have hidden it.

The scheduled-agent handoff may generate a new diagram and report
only from a *current authorized* private snapshot, within the
owner-selected budget and delivery audience. It cannot create
its own recurring task, change a plan, write a cached image,
renew a permission or invent a restore receipt. An approved persisted
checkpoint is a separately authorized write with readback, not
the diagram's stdout output. No persistent scheduler is needed
to run the helper.

## Security challenges and rejected shortcuts

- **Path/render injection:** arbitrary host filenames can contain
  Markdown, Mermaid syntax, HTML, Unicode bidi, secrets, traversal
  and operating-system reserved names. The optional CLI accepts
  only **strict lowercase ASCII display aliases**, with relative
  paths up to six segments, and constructs safe diagram labels.
  Host-native names remain in its authorized private index and
  must be separately escaped and access-filtered by any richer UI.
  Display aliases are NOT executable filesystem paths.
- **Cross-account mixing:** principal/root/audience changes break
  checkpoint reuse. Each record must be currently allowed for
  the actual viewer. A previously indexed ID absent from a current
  ACL-filtered view is not displayed just because old permission
  existed.
- **Plan and destination conflicts:** reject within-snapshot
  case-insensitive duplicate targets, file-versus-directory path
  conflicts and ambiguous source paths. This does **not** prove
  that a destination exists or lacks a conflicting file outside
  the supplied inventory. Host must re-evaluate native permissions,
  links, symlinks, hardlinks, provider-specific normalization,
  external target content and storage/cost before any approved act.
- **Forged progress:** an input flag marked VERIFIED alone is not
  sufficient. A read-back receipt must bind the exact plan revision,
  record ID, source revision, declared target, attested integrity,
  preserved access and time; the latest observed path must match
  that target. The helper does not independently authenticate those
  receipt claims. A host must establish the facts.
- **Interrupted operations:** EXECUTED is not VERIFIED, and
  ROLLED_BACK is not a successful target relocation. Reports keep
  each state distinct and do not silently retry.
- **Big libraries:** a diagram showing only the first 24 records
  is TRUNCATED, with the actual observed-scope denominator and
  count of omitted records. The host should offer scope/folder
  drill-down from a separately authorized data source rather
  than claiming the partial picture is complete.
- **Visual accessibility:** status must be in text, not only
  color; a deterministic plain-text tree fallback is mandatory.
  Mermaid and actual interactive host widgets are optional.
- **Privacy:** diagrams, folder labels, relation edges and
  numbers can expose file existence. The CLI returns no
  per-file data when current access fails. Sharing/exporting
  a chart requires a separate audience/privacy decision.

## Portable original offline visualizer

The [render_structure.py](../scripts/render_structure.py) helper
takes one explicit JSON plan snapshot and optionally its previous
accepted snapshot, with no network, filesystem crawl, mutation,
index storage, account reader, scheduler or dependencies beyond
Python 3.9+ stdlib. It emits JSON with three portable text trees,
one Mermaid flowchart, progress counts and caveats. Two wholly
fictional snapshots are bundled:

    python3 scripts/render_structure.py --previous examples/structure-plan.json --current examples/structure-progress.json
    python3 -m unittest discover -s tests -p 'test_*.py' -v

A plan snapshot includes exactly schema_version, plan_id,
plan_revision, snapshot_id, observed_at (timezone-aware),
scope (collection_id, root_id, principal_id, audience_id),
viewer_check, coverage and records. Each record has record_id,
original_path, observed_path, target_path or null, source_revision,
state, viewer_check and readback or null.

Readback has record_id, plan_id, plan_revision, source_revision,
destination_path, integrity (matched), access (preserved) and
observed_at. These are host-provided **assertions**, not signed
authority tokens or independent crypto evidence. Input bounds
are 1 MiB and 200 records; display is limited to 24 records
to avoid making a giant and mostly unusable diagram.

**Known limitations by design:** not a general-purpose filename
renderer, not a content hash verifier, not an authorization system,
not an agent user study, not actual whole-source directory coverage,
not a collision detector across an unseen provider namespace,
not a project-memory service, not a scheduler, and not a
file-operation executor. Reports must not claim those outcomes.

## Acceptance beyond source tests

Source-code unit tests establish deterministic refusal/format
behavior only. A real long-lived agent trial should verify:
- two or more authorized repeat invocations against a controlled
  collection with actual provider access and a persisted checkpoint;
- partial or ACL-filtered refreshes; revoked permissions suppress
  cached identity; no unauthorized diagram export;
- proposed/approved/executed/verified/rolled-back sequence with
  real operation receipts and destination readbacks;
- plan drift/new approved revision/retry, no duplicated operations,
  stale receipt rejection and correct rollback recovery;
- large folder coverage, unexpected target collision, broken links
  and human readability/accessibility of the displayed diagram;
- measured findability, accurate progress, reduced unnecessary
  work and truthful reporting, not just a visually pleasing chart.

These host/user outcomes remain NOT_RUN until actually observed.
