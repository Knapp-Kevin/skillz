# File & Information Management

Two complementary first-party skills for approved files and knowledge sources.

- **[File Lifecycle Curator](../../authored/file-lifecycle-curator/SKILL.md)** (within a collection): inventory, extraction, grounded summaries, metadata decks, normalized keywords, duplicates/versioning, proposed folder organization and archive assessment. [Schema](../../authored/file-lifecycle-curator/references/metadata-contract.md) · [archive/mutation gates](../../authored/file-lifecycle-curator/references/operation-and-archive-rules.md) · [v1.1 static review](../../../docs/reviews/2026-11-18-file-pack-v1-1-static-review.md).
- **[Federated Source Catalog](../../authored/federated-source-catalog/SKILL.md)** (across collections and connectors): scope-aware discovery, per-source capability and completeness receipts, source-native IDs and revisions, permission-preserving query, cross-source relationships, and freshness/revocation discipline. [Adapter matrix](../../authored/federated-source-catalog/references/provider-adapter-matrix.md) · [record contract](../../authored/federated-source-catalog/references/federated-record-contract.md) · [v1.1 static review](../../../docs/reviews/2026-11-18-file-pack-v1-1-static-review.md).

**Current exact versions (2026-11-18):** File Lifecycle Curator **v1.1.0** (7 files) and Federated Source Catalog **v1.1.0** (8 files). Both now include [independently static-reviewed source/permission-preserving handoff contracts](../../../docs/reviews/2026-11-18-file-pack-v1-1-static-review.md) and H01–H12 synthetic cases. Each remains **18/20 static-reviewed; model/host behavioral validation NOT RUN**. The earlier v1.0 reviews remain historical evidence.

**Composition:** For “find it across my connectors”, start with Federation. For “summarize/tag/organize these approved files”, use the Curator. For both, Federation chooses authorized source records and hands only permitted data to the Curator; the Curator does not grant new source permissions.

Both exact v1.1 packages retain **18/20 static reviews**. **Behavioral validation remains NOT RUN in Skillz.** No connector, persistent index, executable storage system, ACL enforcement service, synchronization or file mutation is bundled or authorized by these reference skills.

[First-party adversarial assessment](../../../docs/reviews/2026-11-18-owner-led-file-pack-adversarial-review.md) identifies the unqualified cross-skill handoff and prioritizes our own checks. The [proposed composition contract](../../../docs/reviews/2026-11-18-file-pack-composition-contract.md) defines identity, revision, viewer scope and 12 synthetic acceptance cases. Neither depends on outside testers; current v1.0 skill package bytes remain unchanged.

The [File & Information Management taxonomy proposal](../../../registry/discovery/file-information-management-domain-proposal-20261118.json) now describes **14 proposed subdomains**; they are not yet canonical or operationally qualified. The [independent gap audit and owner-led qualification](../../../docs/reviews/2026-11-18-file-information-management-gap-audit.md) tracks evidence needed next.
