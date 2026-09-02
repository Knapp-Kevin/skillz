# Skill Curation Queue

This is the living evidence ledger for ongoing `skillz` corpus curation. The repository is entirely passive; the external host agent performs curation under explicit repository-maintenance authority.

## Current governed depth

- **43** first-party user-facing skills, **43/43** provenance-complete.
- **12** pinned upstream reference corpora under `skills/sources/`.
- **19** unique registered source identities.
- **252** persisted exact-version third-party verification companions.
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
- Current-standard companions: **80/189**.
- Remaining gaps: **109**.
- Direct `.NET`: **29/29** complete.
- Direct Java: **26/26** complete.
- Direct Python: **21/40** complete.

Python is complete source-order through `azure-keyvault-py`.

Latest tranche, behavioral evidence `not-run` for all:

- `azure-eventhub-py` — **rejected unchanged, 10/20**. Package tree `0fbf762f81763b55040414428dcb0a3a0d29bd5f`; `SKILL.md` blob `289676f5c80a9f4064980ff98283575502fe1d99`. Complete-package review includes checkpointing/partition references and setup CLI. Useful streaming mechanics remain prior art, but unchanged use lacks distinct publication/data-disclosure, checkpoint-mutation, downstream-impact, retention and budget authority, and the CLI's async credential lifecycle conflicts with the package rule.
- `azure-identity-py` — **rejected unchanged, 12/20**. Package tree `e5a4071f391ba8b2236bc20a3a1e8dd8998d96b1`; `SKILL.md` blob `37e6a034b861e30c675b7b2029e391612f69a535`. Useful identity guidance, but sensitive credential/token handling, wildcard additional-tenant access, secret/assertion flows and verbose logging need explicit scope/tenant authority and redaction controls before adoption.
- `azure-keyvault-py` — **rejected unchanged, 8/20**. Package tree `cbcf7a71066e1d3b1a073b07d358efbbe6b8e77b`; `SKILL.md` blob `20c836c7b6e903dfce8d3fb90cc38c57892d0154`. Useful Key Vault patterns are outweighed unchanged by secret-value output, permanent purge, key/certificate mutation, private-key retrieval and cryptographic operations without explicit disclosure/destructive/crypto/lifecycle authorization.

All three bind skill-specific freshness to upstream revision `df52e9a69b78c2759553efafe2f937fc53c1cbd1` dated 2026-05-18.

**Next source-ordered package:** `azure-messaging-webpubsubservice-py`.

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
**Microsoft Skills:** **80/189**, **109 gaps**. Python is **21/40**.  
**Next:** continue source-order with `azure-messaging-webpubsubservice-py`.