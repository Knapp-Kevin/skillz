# File and Information Management: scope/refinement gap audit

**Date:** 2026-11-18. **Baseline:** File Lifecycle Curator v1.0.0 at SKILL blob `63577971773ae0d923f6d38165c13c34f36b8f72` and complete tree `12e7f8d07bdd1553f7ed78e377ebc7b5e9742a84`. **Follow-on:** Federated Source Catalog v1.0.0 at `4d028afe00921af05f8258e0c7f50707d2ebb68c` and `130b199cc7c5549d8905196d62f54617198d1976`.

This is a **static repository/document review**, not a report of work by the external implementer/testing agent or a claim that any connector or filesystem was exercised. The local curator is deliberately **not modified** here while separate behavioral qualification is in progress. Any future changes to it require new version/hash and an updated review.

## Two-skill composition and non-overlap

| Request | Responsible skill | Output / excluded effects |
|---|---|---|
| Summarize, tag, create metadata deck, plan local organization, assess archive candidates | File Lifecycle Curator | A scoped, source-cited per-file catalog and safe dry-run plan, no unauthorized file operations |
| Discover which connected account/repository contains files, compare or link sources, search sources together | Federated Source Catalog | Per-source capability/coverage receipts, native identities, relationship links, access-scoped query response |
| Both kinds of request | Federated Source Catalog selects authorized source records; File Lifecycle Curator enriches only selected readable files | Caller preserves original record IDs/revision/audience and receives no mutation authority |
| Mirror, sync, migrate, apply ACL or delete across systems | Neither passive skill | Separate governed implementation and explicit owner approval, operational tests and rollback evidence |

**Why:** One document can have several locations, identities, representations and permissions. A logical relationship is not physical sameness. An index is not an authorization service. A copy is not an archive or verified backup.

## Remaining gaps by priority

| Priority | Gap | Evidence state | Measurable acceptance / owner |
|---|---|---|---|
| P0 | Original curator end-to-end host behavior and negative cases | Static 18/20 only; no observed tests in Skillz | External implementer runs representative tests against exact pinned tree; report trigger/nontrigger, unsafe actions, extraction and archive boundaries with observed receipts |
| P0 | Federation connector permission isolation (cross-account, cross-tenant, per-viewer) | New text boundary only; no deployed search service | Synthetic two-user/two-account fixture; unauthorized user receives no private title, existence count, tag, snippet, relationship or cached result |
| P0 | Source enumeration/partial-failure honesty | No end-to-end connector acceptance | Pagination, 403, rate limit, truncated GitHub search, stale cursor and missing source each yield per-source PARTIAL/NOT-RUN instead of false zero |
| P0 | Source-native identity, version and export semantics | Static contract authored, no live observations | Verify native Docs/exports/shortcuts vs GitHub path at commit; never falsely merge, dedup or infer ownership |
| P1 | Search quality and actual indexing | Index contract is a proposal; no measured recall, ranking or persistent search | Defined synthetic corpus, query ground truth, top-k recall/precision, source citation and NOT INDEXED counts; compare to simple baseline |
| P1 | Controlled taxonomy, metadata deck and synonym portability | Text rules only | Same corpus tagged consistently across provider boundaries; provenance, confidence and category conflicts logged and reviewed |
| P1 | Freshness and incremental updates | No delta process or scheduler | Simulate move/rename/revision/delete/revoke; last-success watermark and access-filtering behavior verified; no cached leakage |
| P1 | Archive integrity, restore, ACL inheritance and retention | Textual holds; no actual archive restore | Separate explicitly approved test fixture; copy/archive readback, restore, versions/ACL loss disclosures and no original deletion |
| P1 | Connector capabilities and native document extraction | Provider/tool support variable | Capability matrix based on real actions; native Doc/Sheet, PDF, Markdown, image, encrypted, large and unreadable cases show truthfully bounded extraction |
| P2 | Large libraries, costs and paging efficiency | No benchmark | Measure bounded representative source batch, query latency, budgets, failure/retry and resumability without assuming full inventory |
| P2 | User feedback, search ranking calibration, cross-language tags, multi-modal semantic matching | Exploratory only | Controlled synthetic evaluation and privacy/rights approval before scope upgrade |
| P2 | Full third-party source comparison and taxonomy promotion | 921 identities unmapped at baseline; new file domain proposed | Search/inspect exact complete source packages and rights; compare to two first-party methods, then promote only evidence-backed outcomes |

## Authority gates for the implementer

The external host may expose Google Drive, GitHub and local file tooling with different scopes. The implementer must report **what tool actually executed** rather than assuming a generic integration. Provider documentation references are not proof of the current host action.

Do not:
- grant app-wide read or admin access merely to improve catalog coverage;
- copy private documents into a common index without a separate destination/audience policy;
- promote static expected outcomes to validated status;
- treat a combined file metadata search as exhaustive account inventory;
- implicitly schedule recurring tasks, monitoring or synchronization;
- mark archived files safe for deletion without explicit disposal authority and tested recovery.

## Next work packages

1. **Behavioral qualification:** Ask the existing implementer to report exact skill SHA/tree and observed outputs against the 12 federation cases and local curator safety examples, including a clear FAIL report for violated invariants.
2. **Connector adapter acceptance:** For each available account, record actual operations, pagination, identity/revision, ACL/scope, export/read limits and error behaviors. Start read-only and scoped.
3. **Retrieval evidence:** Establish bounded synthetic relevant-query ground truth, pass/fail criteria, distinct duplicate/version relations and stale index rejection.
4. **Separate implementation decision:** Only after permission-scoped prototypes should a durable shared index, incremental ingestion, sync/migration or archival executor be approved as a different component. The two passive Skillz packs are not those runtime components.

The new cross-source skill should be mapped to the existing `memory-context/retrieval`, `memory-context/provenance` and `technical-writing/documentation-ia` routes. Expand the existing *proposed* `file-information-management` domain without counting those proposals as qualified canonical outcomes until reviewed.
