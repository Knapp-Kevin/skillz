# Pinned j4flmao architecture, backend and data qualification (2026-11-02)

**Source:** [j4flmao/agent-skills](https://github.com/j4flmao/agent-skills/tree/982203e52afe0b726a7847599a8bfb293890e0c5) at `982203e52afe0b726a7847599a8bfb293890e0c5`. Dynamic discovery only, not admitted. Root MIT notice blob `0e8b6e6d8678128ebfcc28d7cad91fa9ed7f2354` does not grant rights to external libraries, cloud services or private data. [Eight individual ten-dimension grades](../../registry/discovery/j4flmao-backend-data-eight-static-20261102.json).

## Macro frontier and decisions

Before: **61/645** exact-path decisions (23/424 direct, 38/221 other). Eight distinct complete direct-shape packages, **11 package-owned files** including all three bundled references, become **69/645** (31 direct, 38 other). Pending: **576 raw** (393 direct, 183 other). Four-source path-matched decisions **148 → 156/4,813**; deduplicated eligible denominator **unknown**. These are source-vetting candidate grades, not governed semantic review pairs.

| Pinned package | Grade | Decision | Decisive reason |
|---|---:|---|---|
| `skills/architecture/crdts/SKILL.md` | 15/20 | REJECT | The Yjs example persists documents in IndexedDB and sends document/presence data to a WebSocket endpoint without a scoped user/document egress or persistence authorization. Strong convergence and server-invariant warnings are useful extraction evidence. |
| `skills/architecture/micro-frontends/SKILL.md` | 16/20 | REFERENCE-ONLY | Strong organizational go/no-go and singleton/contract checklist, but executable remoteEntry from a CDN has no trust/integrity/version pin, deployment ownership approval, or production rollout authorization. Design prior art only. |
| `skills/backend/caching-strategies/SKILL.md` | 13/20 | REJECT | The Go example writes a user's email into Redis without data-scope, tenant-isolation, encryption or retention approval; database updates and cache invalidation have no action-specific authority. The write-behind example explicitly has a double-count failure window. Preserve TTL jitter and singleflight patterns. |
| `skills/backend/event-driven-architecture/SKILL.md` | 13/20 | REJECT | Producer publishes customer IDs and monetary totals to a broker without destination/recipient/data authority; examples include SQL writes and operational DLQ replay without an action-specific approval gate. The consumer sample returns on first handler failure despite claiming retry/DLQ handoff. Keep envelope and dedupe guidance. |
| `skills/backend/graphql-optimization/SKILL.md` | 13/20 | REJECT | Per-request loaders avoid cross-request cache leaks, but SQL batch queries select by arbitrary IDs without a demonstrated tenant/row authorization predicate. Advice to enable SQL logging can expose private queries; GET/CDN caching needs per-user isolation. Useful DataLoader ordering and cost-limit reference. |
| `skills/data/etl-pipelines/SKILL.md` | 12/20 | REJECT | Sample DAGs schedule recurring production warehouse transformations and trigger dbt Cloud jobs with no approval for schedule, cost, warehouse target, external provider or downstream data publishing. Airflow connections protect credentials but are not authorization. Preserve dependency-isolation and freshness checks. |
| `skills/data/database-internals/SKILL.md` | 14/20 | REFERENCE-ONLY | Useful engine-specific isolation and amplification comparisons, but the bundled WAL reference says a commit is acknowledged immediately after append without requiring durable log flush, conflicting with the main SKILL. pg_stat_activity query can reveal sensitive SQL; durability-setting changes need approval. Reference-only until corrected. |
| `skills/architecture/event-driven/SKILL.md` | 14/20 | REJECT | Transactional outbox and inbox are useful, but executable CREATE/INSERT, broker relay, event-carried state and DLQ replay lack target/recipient/PII and production-change authorization. Bundled event-sourcing note overclaims perfect audit logs and presents crypto-shredding as a universal deletion solution. |

## Systemic findings

- Eight direct-shape first-class pinned packages: six single-SKILL trees, one two-file tree and one three-file tree; 11 package-owned files read including all bundled references.
- Strong overlap between architecture/event-driven and backend/event-driven-architecture: distinct exact blobs and package trees, similar outbox/inbox patterns; do not treat as semantic duplicates without full comparative mapping.
- Hard fails concentrate on durable cloud/warehouse scheduling, broker publication, private GraphQL reads, Redis PII caching, and collaborative document egress. Credentials in a secret backend or good architecture patterns are not authorization.
- Database-internals bundled WAL note conflicts with the parent manifest on durability; source-package review must inspect bundled files, not only SKILL.md.
- No source admission, governed verification pair, external security scan or representative behavioral validation; cross-source eligible denominator remains unknown.

## Review boundary

Every exact SKILL.md and required bundled file was read against its pinned blob and package tree. Each record contains purpose/trigger, exclusions, dependencies, rights, authority/privacy, 10 rubric scores, controlled tags, static disposition and explicit `not-run` security/behavioral state. No external code was run, no source was copied or installed, and no unchanged use was approved. The remaining source paths and cross-source semantic mirrors require further classification.
