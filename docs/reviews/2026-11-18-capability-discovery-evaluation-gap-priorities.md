# Skillz capability gaps and evidence priorities: November 18, 2026

**Current follow-through (later November 18):** Two identified candidate gaps are now independently authored as exact MIT source packages: [Metadata Taxonomy Steward](../../skills/authored/metadata-taxonomy-steward/SKILL.md) and [Reference Integrity Auditor](../../skills/authored/reference-integrity-auditor/SKILL.md). [Bounded five-source comparison and exact static review](2026-11-18-taxonomy-reference-integrity-static-review.md) records each at 18/20 static, behavior NOT RUN. Five exact-pinned third-party reviews were also linked to existing recognized routes (3 verified, 2 rejected unchanged); these are evidence mapping, not eligibility. **Current canonical accounting is 1,047 reviewed, 131 mapped (104 static verified + 27 rejected), 916 unmapped, 78/247 recognized subdomains linked, and six partially decomposed subdomains / 241 remaining.** The earlier table below is the **before-change baseline**, not the latest state. File & Information Management now has 16 *proposed* subdomains, none promoted to canonical status. Further source comparison and host-agent testing remain open, owned by Skillz; outside testers are not required.


**Method:** Independent read-only analysis of live `main` source records and both original v1.1 file-management skill packages, followed by three bounded outcome-definition additions to `registry/capability-outcome-register.json` on this branch. This audit is not a behavioral-agent test, external-source full-corpus re-crawl or live multi-provider permission audit.

## Current recognized coverage (updated in this change)

| Measurement | Count | Interpretation |
|---|---:|---|
| Governed exact-version review identities | **1,045** | 50 first-party + 995 third-party; **not** 1,045 installable skills |
| Identity records linked to recognized capabilities | **124** | 99 static verified + 25 rejected; inclusion means evidence discoverability, not recommendation |
| Reviewed identities not linked | **921** | Primary provenance/capability crosswalk backlog, not 921 gaps in usable methods |
| Recognized capability domains / subdomains | **33 / 247** | Canonical taxonomy only |
| Subdomains with at least one linked governed identity | **78 / 247** | Navigation, not outcome completion; **169** without such a link |
| No governed links, but source-vetted candidates | **12 subdomains** | Discovery/search leads only |
| Subdomains marked unassessed | **157** | Requires fresh outcome/discovery work |
| Essential outcome definitions now partially specified | **4 / 247** | Previously 1: bounded melody; **3 added here** for document IA, source retrieval and provenance |
| Subdomains still needing essential-workflow decomposition | **243 / 247** | No mature outcome coverage asserted |
| Behavioral status among 124 mapped review identities | **123 not-run, 1 incomplete** | No mapped identity has a complete, observed behavioral acceptance |

**Grounding:** `registry/capability-directory.json`, `registry/capability-outcome-register.json`, `registry/authored-skills-index.json`, and `registry/local-verification.json`. These are the **current catalog figures as observed 2026-11-18**, not a claim that all 1,045 complete source packages were re-reviewed today.

## Discovery and evaluation: dated frontiers, not a single funnel

The latest *published pinned, broad G1-G3 discovery receipt* was captured in the November 3 corpus pipeline and carried into the November 6 README scope correction:

- **61,326 pinned package-identity records across 942 repositories**, representing **57,715 distinct package-tree SHA observations**; not necessarily distinct, eligible or secure skills.
- **5,351 distinct exact (source, pin, path) static candidate decisions** in the November 3 pipeline ledger: 3,773 rejected unchanged, 1,574 reference-only and 4 deferred.
- **1,522 reference-only candidates** awaiting a consumer qualification decision in that same dated ledger.
- **50 methods selected for study**, not install approval, in the historical November 3 featured shelf; **0 approved for unchanged use** in that historical pipeline.
- Unknown: globally distinct eligible corpus denominator, reconciled license/rights clearance, current per-source freshness, a true all-source review completion fraction, and comparable discovery/evaluation effort spent.

**Do not merge these denominators:** 61,326 source path identities, 5,351 candidate decisions, 1,045 governed exact-version review identities, 124 capability-linked reviewed identities and 247 recognized subdomains are **different populations and timestamps**. The 2026-11-03 counts are **last published checkpoint, not freshly rerun as of 2026-11-18**. See `registry/qualification-pipeline-20261103.json` and `docs/discovery/full-corpus-search-contract.md`.

## Ranked program gaps

| Priority | Finding and independent evidence | Required direct action | Done when |
|---|---|---|---|
| P0 | **Workflow outcomes underdefined:** 243/247 recognized subdomains still lack even a partially specified outcome | Define essential user jobs, outputs, inputs, source dependencies, failure criteria and authority per subdomain; separate optional tasks and accepted counterexamples | Each outcome has measurable acceptance, mapped source candidates and explicit **NOT RUN** behavior until tested |
| P0 | **Reviewed-but-unmapped evidence:** 921 exact-version review identities have no canonical capability route; 169 subdomains lack governed links | Batch inspect exact identity + source review/rights, then link with evidence only; maintain distinct `verified`, `rejected`, reference-only and unknown | Incremental link receipts reconcile to current canonical directory without hiding rejected candidates or inflating mature coverage |
| P0 | **Discovery identities are not an eligible source denominator:** 61,326 path identities overlap and license/semantic distinctness remain unreconciled | Produce pinned source-by-source identity/rights/dedup ledger; treat missing/unreachable source and duplicate revisions as distinct evidence states | Each declared snapshot has a defensible eligible denominator and unresolved rights list; **not** arbitrary all-time skill count |
| P0 | **Operational effectiveness unmeasured:** 123/124 mapped identities have behavior NOT RUN, one incomplete | Conduct independent, bounded, representative and adversarial synthetic host-agent tests for selected essential outcomes; tie receipts to exact hashes and tool/model setup | Observed action traces support PASS/FAIL; static grades alone cannot qualify execution or user benefit |
| P1 | **Discovery/evaluation effort balance is not quantified per tranche** | Track search scope and newly found candidates separately from complete-package reading, source/license/asset review, exact-version disposition and validation effort | Each bounded tranche reports discovery + evaluation work, reviewed/untouched leads and next candidate, rather than equating candidate count to equal effort |
| P1 | **Source freshness and cross-provider access limitations** | Independent provider adapter test matrices: page/truncation, 403/revocation, mutable revisions, viewer-specific results, result-not-searched accounting | Scope-bounded provider coverage receipts and no private metadata leakage are observed, not merely prescribed |
| P1 | **Retrieval, tagging and metadata-deck quality not quantified** | Construct own synthetic corpus/query ground truth, provenance/citation grading, tag precision/consistency, source visibility and false-zero cases | Repeatable comparisons to a basic baseline; report accuracy and failures without claiming full-corpus or semantic coverage |
| P2 | **Multimodal, long-lived archives, transformation lineage and lifecycle work** | Evaluate rights/retention and format-specific dependencies before separate skill authorship | Distinct tool-independent workflow or explicitly qualified host runtime supported by tests, with no implicit disposal/migration authority |

The canonical [capability quality plan](../capability-quality-plan.md) governs these outcomes; [issue #588](https://github.com/Knapp-Kevin/skillz/issues/588) tracks capability coverage, [issue #599](https://github.com/Knapp-Kevin/skillz/issues/599) continuous discovery and review, and [issue #402](https://github.com/Knapp-Kevin/skillz/issues/402) security/freshness. Do not close work because a record was linked, or infer that a name on the study shelf can be used unchanged.

## File and Information Management: distinct potential missing skills

The existing v1.1 [File Lifecycle Curator](../../skills/authored/file-lifecycle-curator/SKILL.md) handles a collection; [Federated Source Catalog](../../skills/authored/federated-source-catalog/SKILL.md) handles source discovery/identity/permission-aware retrieval. Their exact in-package handoff is statically aligned. The following are **candidate scope gaps** based on examined first-party packs, **not claims of absence across 61,326 source leads**.

### Priority 1: Metadata Taxonomy Steward (candidate new skill)

**Not another organizer.** Govern the **vocabulary itself** across teams and repositories: namespace definitions, source-native labels vs normalized tags, synonym/alias management, category versioning, sensitive-field handling, conflicting classifications, owners/reviewers and migration/diff proposals. Output a stable taxonomy manifest, backwards-compatible crosswalk and exception ledger without rewriting any provider tags.

**Acceptance:** Two independent source vocabularies with collisions and ambiguous synonyms map without dropping original terms or broadening ACL; a taxonomy rename has a reversible, explicitly approved proposal, not a silent bulk retag. **Distinct from curator:** curator *uses* a taxonomy for one collection; the steward governs changes to the taxonomy across collections. First inspect third-party exact-source methods and licensing before creating this skill.

### Priority 1: Reference & Relationship Integrity Auditor (candidate new skill)

Systematically examine permitted **links and dependencies** among files, GitHub paths, Drive shortcuts, citations, source IDs and metadata cards. Distinguish stale, inaccessible, orphaned, moved, broken, duplicate-alias and unknown links. Return source-revision-bound repair proposals and affected dependents without revealing private target existence.

**Acceptance:** Synthetic renamed file, moving GitHub branch, private shortcut, changed Drive object, copied document and deleted/revoked target generate correct bounded outcomes and no unauthorized dereference. **Distinct from federation:** the catalog can store relationships, but it does not define a full ongoing *referential integrity audit* or impact-assessment workflow. Evaluate existing exact-source methods before new authorship.

### Priority 2: Information Ownership & Lifecycle Stewardship (research/proposed scope)

Identify ambiguous stewardship, organizational records categories, source-of-truth proposals, decision ownership, authorized retention schedule links, access reviews and supersession disputes across systems. Do **not** choose binding legal retention or delete originals automatically. This is a separate governance/authority workflow, not a generic archive helper.

**Acceptance:** A cross-source sample with competing copies, different owners, undocumented retention and private references yields explicit unknowns, policy references and human decisions, never inferred deletion permission. Higher governance risk; hold authorship until rights, legal/records boundary and organizational need are qualified.

### Not yet a new passive skill: migration/sync executor

Bulk copy, two-way sync, ACL changes, storage cleanup, index persistence and retention-driven deletion are actual operational effects. A passive skills specification may guide a dry run, but effective execution requires supported host tools, idempotency, permission/tenancy isolation, conflict handling, read-back, restore and owner approval. Do not disguise missing runtime as a complete authored skill.

## Newly completed bounded outcome definitions

Three **partial essential outcomes** are added to `registry/capability-outcome-register.json`: `technical-writing/documentation-ia`, `memory-context/retrieval` and `memory-context/provenance`. They declare exact inputs/outputs, negative constraints, named method IDs and static versus behavioral qualification, with zero claim of agent-host completion. The previously defined music melody outcome remains intact.

**Recommended next execution:** Expand essential-outcome definitions for the 78 linked subdomains before selecting fresh authored skill packages indiscriminately; in parallel, perform a bounded evidence-backed mapping/evaluation tranche from the 921 identities. Choose one distinct first-party *taxonomy stewardship* or *reference integrity* method for authoring only after package-level search confirms an unmet outcome.
