# Skill Curation Queue

This is the living evidence ledger for ongoing `skillz` corpus curation. The repository is entirely passive; the external host agent performs curation under explicit repository-maintenance authority.

## Current governed depth

- **43** first-party user-facing skills, **43/43** provenance-complete.
- **12** pinned upstream reference corpora under `skills/sources/`.
- **19** unique registered source identities.
- **249** persisted exact-version third-party verification companions.
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
- Current-standard companions: **77/189**.
- Remaining gaps: **112**.
- Direct `.NET`: **29/29** complete.
- Direct Java: **26/26** complete.
- Direct Python: **18/40** complete.

Python is complete source-order through `azure-eventgrid-py`.

Latest tranche, behavioral evidence `not-run` for all:

- `azure-cosmos-py` — **rejected unchanged, 9/20**. Package tree `159aea3f186349abfb5004b51587e3dfe210ab56`; `SKILL.md` blob `9800d67e64c753e221128e38c43a81bfabdff944`. Complete-package review includes partitioning/query references and setup CLI. Useful prior art for Cosmos partitioning, parameterized queries, CRUD, throughput, transactions, change feed, and lifecycle. Unchanged use lacks explicit environment/data/destructive/financial/cost authority around resource provisioning, throughput/index changes, durable mutation/deletion, and a funds-transfer transaction example; the setup CLI also permits `COSMOS_KEY` account-key auth. Adapt/reference only.
- `azure-data-tables-py` — **rejected unchanged, 12/20**. Package tree `6f143c9a8c7ceafc01a5ec691b5e136b34b642ff`; `SKILL.md` blob `ef513ce507818533f5bee1477d07dab5c3bf3fdd`. Useful Entra-first table/entity CRUD, partition queries, transaction and async patterns, but create/delete tables and mutate/delete entities without distinct account/table/data-scope, destructive, retention, rollback, or cost authorization. Adapt/reference only.
- `azure-eventgrid-py` — **rejected unchanged, 13/20**. Package tree `604b049cc7e1550e604b6f9e60fc896e1121211a`; `SKILL.md` blob `907ee84b85bfaa87cc2dada271d27e03ae5dae28`. Useful CloudEvents/EventGridEvent, batching and namespace-topic material, but publishing can disclose payloads and trigger downstream systems without explicit publication/data/downstream-impact/budget authority; async credential cleanup is also inconsistent. Adapt/reference only.

All three bind skill-specific freshness to upstream revision `df52e9a69b78c2759553efafe2f937fc53c1cbd1` dated 2026-05-18.

**Next source-ordered package:** `azure-eventhub-py`. Its references/scripts make it a complete-package review unit rather than a one-file quick pass.

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
**Microsoft Skills:** **77/189**, **112 gaps**. Python is **18/40**.  
**Next:** complete-package review of `azure-eventhub-py`, then continue source-order.