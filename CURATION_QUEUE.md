# Skill Curation Queue

This is the living evidence ledger for ongoing `skillz` corpus curation. The repository is entirely passive; the external host agent performs curation under explicit repository-maintenance authority.

## Current governed depth

- **43** first-party user-facing skills, **43/43** provenance-complete.
- **12** pinned upstream reference corpora under `skills/sources/`.
- **19** unique registered source identities.
- **261** persisted exact-version third-party verification companions.
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
- Current-standard companions: **89/189**.
- Remaining gaps: **100**.
- Direct `.NET`: **29/29** complete.
- Direct Java: **26/26** complete.
- Direct Python: **30/40** complete.

Python is complete source-order through `azure-monitor-query-py`. The pinned Python directory contains exactly **40** direct skill packages.

Latest tranche, behavioral evidence `not-run`:

- `azure-monitor-ingestion-py` — **rejected unchanged, 13/20**. Tree `6f77179d773886b1c5b47f79e40b6701680cf27c`; `SKILL.md` `b6146061c7cb223503d1de4b4c12864c643e4c1b`. Useful ingestion patterns remain prior art; arbitrary logs/JSON can be transmitted externally without sufficient data, destination, privacy, retention, cost, and fail-visible error boundaries.
- `azure-monitor-opentelemetry-exporter-py` — **rejected unchanged, 13/20**. Tree `6f3f29fc5ab34768abdb08ba9c85a038f7deccbe`; `SKILL.md` `bd9553c42ef1863efcf87aebd92225f305786934`. Useful exporter/sampling/lifecycle patterns remain prior art; external telemetry export and local retry storage lack sufficient data-admission, redaction, destination, and retention controls.
- `azure-monitor-opentelemetry-py` — **rejected unchanged, 12/20**. Tree `14a5c5e6184d8b29cca1dfe53d448b484a79f0a1`; `SKILL.md` `00f1d7534e6d2b49e3bf0e5b4ec4977fac99df69`. Useful distro/auto-instrumentation patterns remain prior art; broad automatic capture can export request, database, exception, and application data without sufficient privacy/telemetry authority.
- `azure-monitor-query-py` — **rejected unchanged, 14/20**. Tree `ac052e9e1c0ebee1c7f57d074c3b288a78429813`; `SKILL.md` `95defd74b998e686aa9d28ec8d5ecfc0cb2141bf`. Useful read-only query patterns remain prior art; examples print potentially sensitive logs/metrics without sufficient workspace/resource scope, data-sensitivity, disclosure, and least-data controls.

Freshness: ingestion/query bind to `df52e9a69b78c2759553efafe2f937fc53c1cbd1` (2026-05-18); both OpenTelemetry packages bind to `d94f007962067bb6bfecb9c9ac523d71880f946c` (2026-05-04).

**Next source-ordered package:** `azure-search-documents-py`.

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
**Microsoft Skills:** **89/189**, **100 gaps**. Python is **30/40**.  
**Next:** `azure-search-documents-py`.