# System State

## Snapshot

| Attribute | Value |
|---|---|
| **Last updated** | 2026-09-02 |
| **Milestone** | Core passive architecture complete |
| **State** | Governed curation mode |
| **Repository type** | Passive skill knowledge resource |
| **Reference surface** | 500+ first-party + pinned external skill/reference artifacts |
| **First-party skills** | 43 |
| **First-party provenance complete** | 43 / 43 |
| **Persisted third-party review companions** | 271 |
| **Pinned external corpora** | 12 |
| **Registered source identities** | 19 |
| **AWS current-standard companion complete** | 72 / 72 |
| **Microsoft Skills current-standard companions** | 99 / 189 |
| **Microsoft Skills current-standard gaps** | 90 |
| **Microsoft .NET direct-package companions** | 29 / 29 |
| **Microsoft Java direct-package companions** | 26 / 26 |
| **Microsoft Python direct-package companions** | 40 / 40 |
| **Evaluation model** | Static semantic review first; optional later external behavioral evidence |
| **Repository runtime/CI requirement** | None |

## Current architecture

The canonical boundary is stable: user-facing material lives under `skills/`; intact pinned upstream corpora live under `skills/sources/<source-id>/`; passive repository-use/curation procedures live under `engine/skills/` and are excluded from user-facing counts; provenance and exact-version evidence live under `registry/`.

`skillz` owns no runtime, scripts layer, tests gate, CI workflow, scheduler, monitor, crawler, installer, synchronizer, preflight process, generator, background service, vector database, autonomous observer, or personalization service. Tooling inside pinned third-party repositories remains upstream package material.

## Inventory boundaries

- First-party: **43/43 provenance-complete** with structured semantic review evidence.
- AWS Agent Toolkit: exact denominator **72**, **72/72 current-standard companion-complete** at pin `ff1481a7bc1a04ee00ebf63d3a8a149aa6a2c546`.
- Microsoft Skills: exact denominator **189**, **99/189 companion-complete**, **90 gaps** at pin `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`.
- Microsoft direct `.NET`: **29/29** complete.
- Microsoft direct Java: **26/26** complete.
- Microsoft direct Python: **40/40 complete**.

Completion means decisive current evidence for every eligible package, not universal approval. Rejected/retired material remains useful bounded prior art.

## Active Microsoft frontier

The direct Python slice is now complete at **40/40**. Its final source-ordered tranche has `validation_status: not-run` for all three packages:

- `fastapi-router-py` — **rejected unchanged, 8/20**. Useful FastAPI CRUD, response-model, dependency-injection, and authentication structure remains prior art. Its bundled update template leaves ownership/resource authorization as a commented optional check, while delete authenticates the caller but performs no equivalent resource-authorization check before destructive deletion. Authentication is not authorization, so unchanged adoption fails the authority hard gate.
- `m365-agents-py` — **rejected unchanged, 7/20**. Useful Microsoft 365 Agents SDK hosting, routing, JWT middleware, OAuth, streaming, Graph, Azure OpenAI, and Copilot Studio patterns remain prior art. Unchanged workflows send user-facing messages, obtain/use identity tokens, read profile data, transmit content to external services, and expose a client-secret configuration path without adequate tenant, audience, communication, disclosure, privacy, or credential-custody authority.
- `pydantic-models-py` — **verified, 17/20**. The package is a compact low-authority Pydantic schema-design procedure with one template and no credential, network, production-service, monetary, identity, communication, or destructive behavior. Host-specific fields, persistence conventions, and authorization remain application concerns rather than unresolved package hard fails.

Exact package identities at the registered pin are preserved in the companion records. Skill-specific freshness resolves to 2026-04-24 for `fastapi-router-py`, 2026-05-04 for `m365-agents-py`, and 2026-04-20 for `pydantic-models-py`.

Microsoft Skills remains active with **90** gaps after the completed direct `.NET`, Java, and Python slices. The next tranche must be selected from live pinned-tree evidence rather than inferred from historical structure.

## Source lifecycle

**discovery surface → candidate issue/source → source-vetting → exact-version static evaluation → decisive admission result → repository persistence when justified → user-fit decision**

Discovery is intelligence only. Popularity, branding, creator reputation, and source-level signals never prove individual skill quality.

## Quality model

Every governed user-facing skill must retain truthful provenance and applicable exact-version evidence before being called companion-complete. `verified` means exact material passed structured static semantic review. `validated` additionally requires representative external behavioral/adversarial evidence. `stale`, `rejected`, and `retired` are excluded from normal unchanged reuse while remaining useful evidence where appropriate.

Interpret candidate material in this order:

**user fit → exact-version quality → operational fit → skill freshness → provenance/source context**

## Current curation priority

1. Continue Microsoft Skills in coherent source-ordered batches; direct Python is now **40/40 complete**.
2. Complete Microsoft Azure Skills.
3. Reconcile historically completed external corpora from compatible prior evidence before fresh re-review.
4. Continue governed discovery/source-vetting and omission recovery.
5. Keep README, this file, `CURATION_QUEUE.md`, `INDEX.md`, and `index.json` aligned with live evidence.

The living work surface is `CURATION_QUEUE.md` plus applicable open evaluation/provenance issues. Historical closed Wayfinder/issues/PRs remain evidence, not active execution plans.