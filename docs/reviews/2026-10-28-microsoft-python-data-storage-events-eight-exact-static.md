# Microsoft Python data, storage and events: eight changed-existing exact-version static reviews

**2026-10-28.** Source: `microsoft/skills` candidate `61fe0305ea70389ed8705eec6026a786f57865cf`. Registered July pin `32cad4ee689c95c309e61aeefcbc6af356f1e6a7` is unchanged. All review work was static. No Azure service was contacted, no SDK examples executed, no SkillSpector scan or behavioral validation was performed, and no candidate package was vendored.

## Macro-first denominator and package identity

The candidate structural denominator remains **208**: 106 exact-tree carry-forwards + 76 changed-existing + 26 new/previously ungoverned. The 26 new candidates and 16 changed-existing packages had full static reviews before this tranche. These eight genuine changed-existing Python packages advance **16/76 → 24/76**, leaving **52** (21 Python, 30 Azure operations, one skill-creator). Four removed-path candidate decisions were already resolved; registered July **186/186** and its pin remain unchanged.

All eight canonical packages have **one front-mattered SKILL.md and two supporting reference Markdown files**, for **24 exact Git blobs** inspected. Source package tree SHAs, SKILL.md blobs and both reference blobs were checked at the candidate revision against exact Git objects. No alias, duplicate mirror, nested first-class package or ordinary reference Markdown was counted as an extra skill. The upstream root and each manifest declare MIT; external Azure SDK/service/transitive terms were not independently audited. Each package has individual provenance and 10-dimension verification records, controlled tags, dependencies, exact fingerprints, a decisive disposition and explicit security/behavioral `not-run`.

## Individual dispositions

| Canonical package | Score | Static state | Decisive authority/privacy defect |
|---|---:|---|---|
| `azure-appconfiguration-py` | 12/20 | REJECT unchanged | Setting create/delete, read-only toggles, snapshot creation and feature-flag mutation can change production traffic without resource/environment/owner approval. |
| `azure-cosmos-py` | 12/20 | REJECT unchanged | Creates databases/containers/items, deletes items, performs read_all_items and cross-partition queries, and changes throughput without scoped owner, tenant or cost approval. |
| `azure-data-tables-py` | 12/20 | REJECT unchanged | Create/delete table, upsert/replace/delete entities and submit batch transactions without action-specific authorization; listing all entities crosses logical data boundaries. |
| `azure-eventgrid-py` | 11/20 | REJECT unchanged | Publishes externally visible events that can trigger downstream automation and billing without approval for topic, recipient, event class or effects. |
| `azure-storage-blob-py` | 11/20 | REJECT unchanged | Creates containers, uploads with overwrite=True, deletes blobs including snapshots, changes metadata and issues SAS URLs without owner, target, expiry or disclosure approval. |
| `azure-storage-file-datalake-py` | 10/20 | REJECT unchanged | Deletes filesystems, directories and files, uploads with overwrite=True and recursively changes ACLs without explicit resource/owner/permission approval. |
| `azure-storage-file-share-py` | 11/20 | REJECT unchanged | Creates/deletes shares and directories, uploads/deletes/copies files and creates snapshots without resource/owner/destination authorization. |
| `azure-storage-queue-py` | 10/20 | REJECT unchanged | Creates/deletes queues, sends messages, changes visibility, deletes received messages and clears entire queues without action-specific owner/consumer authorization. |

## Systemic synthesis

- **Authority hard fail, 8/8.** Managed identity, SDK capability, configured endpoints and example parameters are not authorization for live feature-flag changes, database writes/deletes, event publication, storage overwrite, ACL mutation, share deletion or queue clearing.
- **Privacy/tenant boundaries.** App Configuration examples print complete setting values; Cosmos and Tables include broad or cross-partition reads and raw record printing. Partitioning optimizes access, but does not authorize a tenant to see another tenant's data. EventGrid payloads and queue message bodies can disclose sensitive material to downstream recipients or logs.
- **Destructive and security-sensitive patterns.** Blob uploads use `overwrite=True`, and examples delete snapshots; Data Lake offers filesystem deletion and recursive ACL changes; Files offers share deletion and copy; Queue includes `clear_messages()` and deletion on consumption. These require target-scoped approval, data retention and rollback policies, not merely credential availability.
- **Credential-bearing links.** Blob user-delegation SAS is a valuable improvement over account-key SAS, but the generated signed URL is still a credential and must not be printed, logged, or transmitted without explicit disclosure authority.
- **Evidence and operational fit.** All eight favor Entra credentials, production credential-chain constraints and client context managers, but installations are unpinned and some async examples do not close the credential context as strongly as their own prose recommends. The reference files frequently duplicate hero examples; they remain package dependencies, not independent first-class skills.
- **Differentiated extraction value.** Feature-flag snapshots; partition-aware queries and parameterization; same-partition Table transactions; CloudEvent/namespace schemas; user-delegation SAS; ADLS path and ACL inspection; Azure Files ranged transfer/snapshots; Queue visibility and poison-message patterns. Adapt with explicit resource, data class, tenant, recipient, cost and destructive-action boundaries.
- **Priority/omissions.** The source remains valuable for SDK design prior art, but unchanged-use authority defects recur across the Python family. `azure-cosmos-db-py` (nine-file service-layer package), identity and telemetry packages deserve separate deeper tranches rather than an artificial quota. This tranche does not change source admission, freshness pin, package-security or behavioral status.

The exact-version candidate companions are in `registry/skills/microsoft-skills-candidate/` and `registry/verification/microsoft-skills-candidate/`. Prior July-pin companions remain intact. Public counts after this tranche: **774 third-party** and **818 total** verification YAML records (44 first-party). No repository-owned runtime, scripts, CI, scanner, monitor, scheduler or generator was introduced.
