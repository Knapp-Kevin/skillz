# File Lifecycle Curator: incremental maintenance and scheduled-agent portability review

Date: 2026-11-23. Scope: only first-party File Lifecycle Curator
v1.1.1 in Skillz, with no rights/behavior changes to third-party packages.

## Prior capability and missing workflow

The prior exact package had seven files and handled one-time authorized
inventory, classification, summaries, index cards, duplicate review,
physical organization proposals, archival decisions and source-bound
retrieval. It acknowledged that freshness and scheduling were separately
authorized but lacked a complete, executable maintenance-state comparison
and repeatable scheduled-agent run contract.

Four failure families were addressed:
1. A recurring run can redundantly reprocess unchanged records without
   previous accepted state or coverage evidence.
2. A partial source listing may masquerade as deletion evidence, which
   is particularly dangerous for archival or cleanup tasks.
3. A recalled private index can accidentally cross principal/root/audience
   boundaries, reuse revoked permission or present old extraction as fresh.
4. A scheduled trigger can be mistaken for authorized recurrence, a
   completed operation or successful delivery.

## Current original first-party component

- A standalone maintenance reference with BOOTSTRAP / REFRESH / RETRIEVE /
  AUDIT phases and strict private-checkpoint authority.
- A reusable **scheduled-agent invocation template**, not a live schedule:
  owner-bound cadence/timezone, scope, cost/batch, private delivery,
  checkpoint persistence and revocation requirements.
- An optional stdlib-only read-only JSON-delta helper that accepts exactly
  one current and an optional previous explicitly supplied snapshot;
  500 record and 1 MiB per-snapshot bounds, duplicate key/unknown field
  rejection and deterministic capped output.
- Thirty-three wholly fictional tests probing changed revisions, source-ID
  relocation, complete vs partial absence, revoked access, cross-scope
  checkpoint reuse, spoofed digest, conflicting revisions, duplicate input,
  source scope change, idempotent rerun, size/output bounds and no writes.
- Updated portable SKILL entrypoint, complete source fingerprints, rights
  and verification companions. The current package version remains 1.1.1.

## Protected safety and evidence boundaries

Reading is not permission to cache. A prior checkpoint is not current
source authority. No archive, retention disposal, deletion, external
export, file move or permission change follows from maintenance advice.
No SDK, scheduler, persistent database, backup or connected account is
introduced. Unknown index coverage remains UNKNOWN. Source-provided
digest metadata is not proof that this helper read and hashed bytes.

The CLI's **current-authorized** and completeness fields are caller
assertions, not real access validation or a provider listing guarantee.
The helper does not scan a source directory or synchronize content.
Its lexical symlink guard is not a hostile concurrent-filesystem sandbox.
Local Python tests cannot establish a consuming agent's actual file
behavior or real scheduled task delivery.

## Qualification needed for observed effectiveness

A separate authorized consumer trial can run the skill on a controlled
file collection, with a versioned known-good baseline and two snapshots.
Measure index staleness, correctly reprocessed changes, false missing
flags, duplicate work, cost/time and search-result correctness.
When scheduling is expressly approved, independently verify scheduler
creation, actual trigger, permission renewal, no-change reporting,
checkpoint readback, eventual delivery and revocation. None of these
host-facing tasks or human outcomes are claimed by the current source
method suite.

## Executed source qualification on PR #902

GitHub Actions job [offline maintenance](https://github.com/Knapp-Kevin/skillz/actions/runs/45279737987) at source head `b8bad75bf253359bb903c3bbfb58e6bb58529e66` executed **33/33 fictional Python unit tests PASS**. The example delta correctly emitted 1 changed source, 1 newly seen record, 1 not-observed record from a partial scan and 1 unchanged record. It reported checkpoint_written=false. The independently scoped [authored-source contract job](https://github.com/Knapp-Kevin/skillz/actions/runs/45279737985) executed **11/11 PASS**, and both Socket Security checks returned SUCCESS. The first test attempt failed one fixture that had unintentionally marked both prior and current access unknown. The fixture was corrected to isolate historical access; no source security boundary was relaxed. These results establish only offline method behavior, not actual scheduled-agent integration, source account authorization or measured human/file outcomes.
