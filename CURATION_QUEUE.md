# Skill Curation Queue

This is the living evidence ledger for ongoing `skillz` corpus curation. The repository is entirely passive; the external host agent performs curation under explicit repository-maintenance authority.

## Current governed depth

- **43** first-party user-facing skills, **43/43** provenance-complete.
- **12** pinned upstream reference corpora under `skills/sources/`.
- **19** unique registered source identities.
- **268** persisted exact-version third-party verification companions.
- Broad **500+** first-party + pinned external reference surface.

Historical source-level review evidence remains broader than the one-file companion shelf for some completed corpora. Recover compatible prior evidence before fresh re-review.

## Curation and admission model

**discovery surface → candidate issue/source → source-vetting → exact-version static evaluation → decisive admission result → repository persistence when justified → user-fit decision**

New third-party discoveries use `docs/candidate-intake.md`. Discovery intelligence never substitutes for canonical upstream identity, license/terms, exact version, or individual quality evidence.

## Mandatory provenance status

Issue #66 is the corpus-wide provenance-completeness audit. First-party is **43/43** complete. Enforcement is documentary/evidentiary through external-agent curation, never repository-owned scripts, CI, scanners, or runtime.

## Admitted-source curation

### AWS Agent Toolkit — CURRENT-STANDARD COMPLETE

- Pin: `ff1481a7bc1a04ee00ebf63d3a8a149aa6a2c546`
- Denominator: **72**
- Current-standard companion completeness: **72/72**
- Gaps: **0**

### Microsoft Skills — ACTIVE FRONTIER

- Pin: `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`
- Exact eligible denominator: **189** independently front-mattered skill entry points.
- Current-standard companions: **96/189**.
- Remaining gaps: **93**.
- Direct `.NET`: **29/29** complete.
- Direct Java: **26/26** complete.
- Direct Python: **37/40** complete.

Python is complete source-order through `azure-storage-queue-py`. The pinned Python directory contains exactly **40** direct skill packages.

Latest tranche, behavioral evidence `not-run`:

- `azure-storage-blob-py` — **rejected unchanged, 10/20**. Tree `e12b45463c731c9e4a39721d7f52dbc16abdb8a9`; `SKILL.md` `45cb839141133f317683e77f2f3ecae2c8206a41`. Useful Entra-first authentication, upload/download, listing, performance, metadata, and user-delegation SAS patterns remain prior art. Unchanged use creates durable storage state, overwrites/deletes blob data, downloads content, mutates metadata/headers, and creates delegated SAS access without adequate scope, destructive-action, retention/recovery, disclosure, delegated-access custody, or budget authority.
- `azure-storage-file-datalake-py` — **rejected unchanged, 7/20**. Tree `32ae7f0ea087950c1699629ae7ff16f64e8af597`; `SKILL.md` `cbf9de12757e9718d6ff120bc4275b27c4118873`. Useful hierarchical storage and append/flush patterns remain prior art. Unchanged use creates/deletes file systems/directories, mutates files and metadata, and recursively changes ACLs without adequate scope, destructive-action, access-control, recovery, disclosure, service-impact, or budget authority.
- `azure-storage-file-share-py` — **rejected unchanged, 10/20**. Tree `9f58beb6bc9d022669483f4f7c911305a95789e4`; `SKILL.md` `5200889a0df5498bfe704c12358e2f2c1465c84f`. Useful Entra-first, streaming/range, snapshot, and quota patterns remain prior art. Unchanged use creates/deletes shares/directories/files, transfers persistent data, and creates snapshots without adequate scope, destructive-action, copy-source trust, recovery, disclosure, service-impact, or budget authority.
- `azure-storage-queue-py` — **rejected unchanged, 9/20**. Tree `c64f41958010e30f3a43fb8d80d91d174ee13d24`; `SKILL.md` `2e953c26116a950325eb44150571ceb784631420`. Useful visibility-timeout, poison-message, TTL, peek, update, and async patterns remain prior art. Unchanged use creates/deletes queues, publishes messages, exposes message content, destructively settles/clears messages, and mutates metadata without adequate scope, publication/downstream-effect, destructive-settlement, disclosure, recovery, or budget authority. The async example also omits credential cleanup required by its own package guidance.

Freshness: all four packages bind to `df52e9a69b78c2759553efafe2f937fc53c1cbd1` (2026-05-18).

**Next source-ordered package:** `fastapi-router-py`.

### Microsoft Azure Skills — QUEUED AFTER MICROSOFT SKILLS

Pin `8f8c72bb9e22aee4366e07aadfd5766ef9add8f4`. Establish its exact eligible denominator before completion claims and distinguish planning/read-only guidance from deployment, RBAC, cost, identity, and other higher-authority operations.

### Other admitted/tracked sources

- Cole Medin Skills: denominator 33, selective review ongoing.
- David Ondrej Skills: denominator discrepancy still requires reconciliation.
- OpenClaw Agent Skills: denominator 8, selective review exists.
- Archie Indian OpenClaw Superpowers: denominator 56, selective review exists.
- Sabrina Ramonov historical material: canonical source identity/pin/license must be recovered before further work.

## Discovery/source-vetting frontier

Open candidate issues remain temporary evaluation workspaces. Current open bounded candidate work includes DBOS durable-workflow skills (#63) and first-party `session-continuity` derivation (#73). Do not close them merely to improve issue statistics; close them when evidence supports a decisive admission/rejection result.

Discovery surfaces include Hugging Face Skills, GitHub Awesome Copilot, Agent Skills Specification, creator/source leads, and the connected Creator Technical Resource Catalog. Popularity and reputation are omission/context signals only.

## Working rules

1. Finish admitted sources in coherent source-ordered batches.
2. Do not lower individual evidence quality for throughput.
3. Check both companion paths before every unit.
4. Search compatible prior evidence before re-reviewing.
5. Preserve rejected/retired material and reasons.
6. Keep discovery separate from admission.
7. Keep `skillz` passive. No repository-owned runtime, scripts, tests, CI, scheduler, monitor, crawler, installer, synchronizer, preflight, generator, background service, vector database, or autonomous observer.
8. Reconcile README, System State, this ledger, `INDEX.md`, and `index.json` atomically after material batches.
9. Keep issues and PRs in an explicit active, blocked, superseded, or completed state.

## Current posture

**Core:** complete and passive.  
**First-party:** 43/43 provenance-complete.  
**AWS:** 72/72 current-standard companion-complete.  
**Microsoft Skills:** **96/189**, **93 gaps**. Python is **37/40**.  
**Next:** `fastapi-router-py`.