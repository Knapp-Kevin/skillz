# Skill Curation Queue

This is the living evidence ledger for ongoing `skillz` corpus curation. The repository is entirely passive; the external host agent performs curation under explicit repository-maintenance authority.

## Current governed depth

- **43** first-party user-facing skills, **43/43** provenance-complete.
- **12** pinned upstream reference corpora under `skills/sources/`.
- **19** unique registered source identities.
- **271** persisted exact-version third-party verification companions.
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
- Current-standard companions: **99/189**.
- Remaining gaps: **90**.
- Direct `.NET`: **29/29** complete.
- Direct Java: **26/26** complete.
- Direct Python: **40/40 complete**.

The pinned Python directory contains exactly **40** direct skill packages. Final source-ordered tranche, behavioral evidence `not-run`:

- `fastapi-router-py` — **rejected unchanged, 8/20**. Tree `8162d81b2c2856172b495333f5bc3addfcc89ffd`; `SKILL.md` `0d6f32e61e78dc533e0673791c1112e9ecce927e`. Useful FastAPI CRUD and dependency-injection structure remains prior art, but the bundled update path leaves ownership/resource authorization as a commented optional check and delete performs no equivalent resource authorization before destructive deletion.
- `m365-agents-py` — **rejected unchanged, 7/20**. Tree `160c753348c6709974d2d3ae1b6d6b8bf7df146c`; `SKILL.md` `743e9ac137dc5a5427436a270982824fcb3b2ace`. Useful Microsoft 365 Agents SDK architecture remains prior art, but unchanged workflows send user communications, use identity tokens/profile data, transmit content to external AI/service endpoints, and offer a client-secret configuration path without adequate tenant, audience, disclosure, communication, privacy, or credential-custody authorization.
- `pydantic-models-py` — **verified, 17/20**. Tree `591af99b6b71425df244508fc0b4d236b27fa683`; `SKILL.md` `56de5e4008552b3db86354a352a2105e26f59394`. The complete package is a low-authority multi-model schema-design pattern with one template and no unresolved hard fail.

Freshness: `fastapi-router-py` binds to `8ae5031f98413bcb3a8e17d0a87c655e51c23b96` (2026-04-24); `m365-agents-py` to `d94f007962067bb6bfecb9c9ac523d71880f946c` (2026-05-04); `pydantic-models-py` to `e1f9cce11758d305e6c77683fe34ccc394586291` (2026-04-20).

**Next:** select the next Microsoft Skills tranche from the live registered-pin tree and existing companion gaps. Do not infer it from superseded structure artifacts.

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
**Microsoft Skills:** **99/189**, **90 gaps**. Direct Python is **40/40 complete**.  
**Next:** recompute the next Microsoft Skills companion-gap tranche from the registered pin.