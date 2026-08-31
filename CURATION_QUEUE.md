# Skill Curation Queue

This is the living evidence ledger for ongoing `skillz` corpus curation. The repository is entirely passive; the external host agent performs curation under explicit repository-maintenance authority.

## Current governed depth

- **43** first-party user-facing skills.
- **43/43** first-party provenance-complete.
- **12** pinned upstream reference corpora under `skills/sources/`.
- **19** unique registered source identities.
- **173** persisted exact-version third-party verification companions.
- Broad **500+** first-party + pinned external reference surface.
- Historical source-level review evidence remains broader than the one-file companion shelf for some completed corpora and must be reconciled rather than discarded or blindly repeated.

## Curation and admission model

**discovery surface → candidate issue/source → source-vetting → exact-version static evaluation → decisive admission result → repository persistence when justified → user-fit decision**

New third-party discoveries use the issue-first workflow in `docs/candidate-intake.md`. Intentional discovery inputs are documented in `docs/discovery-surfaces.md`, including the connected Creator Technical Resource Catalog. Discovery intelligence never substitutes for canonical upstream identity, license/terms, exact version, or individual quality evidence.

Every governed user-facing skill must retain truthful provenance and exact-version evidence appropriate to its relationship. Missing provenance is a corpus-completeness defect.

## Mandatory provenance status

Issue #66 is the corpus-wide provenance-completeness audit.

- First-party denominator: **43**.
- First-party structured semantic reviews: **43/43**.
- First-party standalone provenance companions: **43/43** under `registry/skills/local-skills/`.
- Enforcement is documentary/evidentiary through external-agent curation, not repository-owned scripts, CI, scanners, or runtime.

## Completed historical source-level review evidence

| Source | Historical reviewed denominator | Recorded result/state |
|---|---:|---|
| Anthropic Skills | 17 / 17 | 10 verified, 7 rejected |
| Anthropic Knowledge Work Plugins | 74 / 74 | 36 verified, 38 rejected unchanged |
| Matt Pocock Skills | 29 / 29 | Complete |
| OpenHands Extensions | 1 / 1 | `theme-factory` rejected unchanged |
| Vercel Agent Skills | 9 / 9 | 6 verified, 3 rejected |
| Cloudflare Skills | 13 / 13 | 11 verified, 2 rejected |
| Google Agents CLI | 7 / 7 | All verified |
| Cline Skills | 36 / 36 | 19 verified, 17 rejected unchanged, plus one separately characterized internal/unlisted skill |
| Addy Osmani Agent Skills | 24 / 24 | Complete with decisive exact-version static states |

Search and reconcile this prior evidence before fresh re-review.

## Admitted-source curation

### AWS Agent Toolkit — CURRENT-STANDARD COMPLETE

- Registered pin: `ff1481a7bc1a04ee00ebf63d3a8a149aa6a2c546`.
- Exact eligible denominator: **72**.
- Historical inspection: **72/72**.
- Current-standard provenance + verification companion completeness: **72/72**.
- Remaining current-standard gaps: **0**.

The sequential campaign reconciled every core and specialized package, including analytics, database, EC2, migration/modernization, networking/content delivery, operations, security/identity, serverless, storage, system-table, and web/mobile. Completion preserves decisive negative states rather than converting everything to approval. Rejected packages remain reference/adaptation evidence when useful.

Representative authority findings from the final tranche:

- Storage packages retained valuable diagnostics and safety mechanisms but were rejected unchanged where create/remediate paths lacked a mandatory affirmative mutation gate.
- The three system-table packages contain useful read/query cores but also configuration/access-grant paths that mutate integrations or permissions without plan authorization, so the unchanged packages are rejected.
- `aws-amplify` contains strong Gen2/framework/deployment guidance but is rejected unchanged because deployment paths create apps, IAM roles/policies, resources, domains and release jobs without a distinct infrastructure/cost approval boundary; one example also passes a GitHub auth token in a command argument.

Behavioral evidence remains `not-run` unless representative external evaluation actually occurred. Upstream scripts, assets, references, templates and examples remain intact package dependencies rather than `skillz` execution machinery.

### Microsoft Skills — ACTIVE FRONTIER

- Registered pin: `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`.
- Current-standard provenance + verification companions persisted: **1**.
- Exact eligible denominator: **reconciliation in progress; no percentage claimed yet**.
- First completed unit: `applicationinsights-web-ts`, package tree `cb03b364b8f9dcb5fc2ee9662758a1f949c23102`, last package-path update `2026-04-23T17:15:18Z`.
- `applicationinsights-web-ts` is `rejected` unchanged under the current authority/privacy rule. Its main setup initializes browser telemetry before first user interaction and enables automatic collection without making consent or approved data handling a mandatory precondition. Later consent/PII guidance is useful but optional, so retain the package as adaptation/reference evidence with a mandatory consent/data-governance gate. Behavioral validation is `not-run`.
- Continue denominator reconciliation from the exact pinned tree and check both companion paths before every unit.
- Favor differentiated Microsoft/M365/Foundry/developer-platform mechanisms rather than assuming official branding proves value.

### Microsoft Azure Skills — QUEUED AFTER MICROSOFT SKILLS

- Registered pin: `8f8c72bb9e22aee4366e07aadfd5766ef9add8f4`.
- Establish the exact eligible denominator before completion claims.
- Distinguish planning/read-only guidance from deployment, RBAC, cost, identity and other higher-authority operations.

### Other admitted/tracked sources

- **Cole Medin Skills**: pin `fb2e876f057c5356d6603ba0c52d6b4418d893ba`; denominator 33; selective reviews exist.
- **David Ondrej Skills**: public pin `7d0ef87dad1f638cab58995eead9e0e6e3fae237`; current evidence describes 44 canonical `SKILL.md` files while a historical tracker recorded 55. Reconcile denominator before completion claims.
- **OpenClaw Agent Skills**: pin `6cd3366b10e2a8c5608265f692acf9f5da2b2448`; denominator 8; selective `handoff` review exists.
- **Archie Indian OpenClaw Superpowers**: pin `a95a59d221d44b89d4fc27a52934e24fb2060ddb`; denominator 56; selective `secrets-hygiene` review exists.
- **Sabrina Ramonov Learn Claude Code Skills**: historical denominator 2; canonical source identity/pin/license must be recovered before further work.

## Evidence-reconciliation lane

Historically completed corpora with broader prior review evidence than their current one-file companion shelf should be reconciled without automatic re-review. High-value targets include Anthropic Knowledge Work Plugins, Cline, Addy Osmani, and any completed Vercel/Cloudflare/Google/Matt records not represented one-for-one today.

## Discovery/source-vetting frontier

Discovery proceeds in parallel but does not interrupt admitted-source completion merely to increase issue counts.

Current intentional surfaces/candidates include Hugging Face Skills, Selamy Labs Agent Skills, Hypergiant Agent Skills, BCGov Agent Skills, GitHub Awesome Copilot, Agent Skills Specification, the connected Creator Technical Resource Catalog, and open candidate-evaluation issues.

New discoveries are queued as issues before admission. Restricted or unclear-license material remains reference-only unless terms later support a different relationship. Popularity and creator reputation are omission/context signals only.

## Working rules

1. **Finish the admitted corpus.** Sequential curation remains the default.
2. **Do not lower the bar for throughput.** Every unit gets duplication checking, exact identity, provenance, license/terms, dependency context, authority, portability, freshness, controlled tags, decisive static state and explicit behavioral-evidence status.
3. **Search before re-reviewing.** Recover compatible prior evidence first.
4. **Do not erase negative evidence.** Rejection/retirement reasons prevent repeated mistakes.
5. **Preserve complete upstream packages.** Their tooling is source context, not repository runtime.
6. **Keep discovery separate from admission.** Discovery intelligence is not proof.
7. **Keep `skillz` passive.** No repository-owned runtime, scripts, tests, CI, scheduler, monitor, crawler, installer, synchronizer, preflight, generator, background service, vector database, or autonomous observer.
8. **Keep public accounting synchronized.** README, System State, this ledger, `INDEX.md`, and `index.json` must agree after each material batch.
9. **Keep issues/PRs honest.** Every open item should have an active, blocked/waiting, superseded, or completed disposition rather than indefinite stale status.

## Current posture

**Core:** complete and passive.

**First-party:** 43/43 provenance-complete.

**AWS:** 72/72 historically inspected and **72/72 current-standard companion-complete**.

**Active frontier:** Microsoft Skills, now with **1** current-standard companion pair persisted while exact denominator reconciliation continues. Microsoft Azure Skills follows. Discovery and issue/PR hygiene continue in parallel.
