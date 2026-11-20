# Federated authority, revocation, and freshness gates

This is a passive skill, not an OAuth broker, connector runtime, secure
cache, scheduler, index database, synchronizer or deletion service.

| Plane | Default | Additional requirements |
|---|---|---|
| Discovery | Scoped read-only listing/search | Approved principal/tenant/root, observed host action, bounded query |
| Enrichment | In-session source-bound summaries/tags | Explicit authorized content read, citations, privacy limits |
| Persistence | NOT-RUN | Approved destination, audience, per-item access checks, retention, encryption/egress, cost, revocation plan and readback |
| Modification | NOT-RUN | Action-specific approval, source/destination ACL, conflicts, version drift, recoverability and post-action proof |

Read permission does not authorize exports, embeddings, persistent storage,
provider permission changes, sync, cross-source copies or deletion. A
source ACL does not automatically protect a derived card, cached result,
embedding, summary or relationship edge.

## Freshness and eventual consistency

- Record observation time, principal scope, query boundaries, item
  version, pagination state and access-check status independently.
- A mutable branch path, cloud document or local file is an observation.
  A commit-bound Git path is stable for that snapshot, not evidence
  that the current branch still points to it.
- Independent connector reads are not globally transactional. Report
  the **observation window**, not a magically consistent point-in-time
  snapshot.
- If an authorized implementation uses provider delta tokens/webhooks,
  account for missed events, invalid cursors, revocation, deletes,
  visibility changes, and partial rescans. A lost token requires
  re-establishing coverage, not silently advancing a full watermark.
- Distinguish last attempted refresh from last **successful complete**
  refresh. A failed refresh must not advance the latter.
- On permission revocation, stop new reads and suppress stale cached
  data to unauthorized viewers. Derived-cache deletion/retention
  follows an explicitly approved destination policy with receipts.
- Do not establish recurrence or background polling unless explicitly
  authorized with scope, interval, cost, access, delivery and revocation
  controls.

## Cross-source mutation is outside this skill

Before proposing copy/migration/synchronization, require a separate
implementation plan with exact source/destination, current permissions,
tenant boundaries, ownership, retention/legal holds, rights, conversion
losses, version/conflict policy, idempotency, dry-run, costs, reversible
restore and integrity verification. No default last-writer-wins,
permission broadening, automatic deletion propagation or mirror-as-backup
claim. Connector success does not prove destination readback.

When current permission, revision or restore verification is unavailable,
keep the risky operation BLOCKED and return a non-mutating plan.

A production shared federated index additionally requires observed
tenant isolation, source revocation, deletion propagation, rescan
completeness, safe caching and per-user retrieval tests. Static source
review is not evidence these systems work.
