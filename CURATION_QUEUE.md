# Skill Curation Queue

This is the living evidence ledger for ongoing `skillz` corpus curation. The repository is entirely passive; the external host agent performs curation under explicit repository-maintenance authority.

## Current governed depth

- **43** first-party user-facing skills.
- **43/43** first-party provenance-complete.
- **12** pinned upstream reference corpora under `skills/sources/`.
- **19** unique registered source identities.
- **216** persisted exact-version third-party verification companions.
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

Behavioral evidence remains `not-run` unless representative external evaluation actually occurred. Upstream scripts, assets, references, templates and examples remain intact package dependencies rather than `skillz` execution machinery.

### Microsoft Skills — ACTIVE FRONTIER

- Registered pin: `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`.
- Exact eligible denominator: **189** independently front-mattered skill entry points.
- Current-standard provenance + verification companions persisted: **44/189**.
- Remaining current-standard gaps: **145**.
- The direct `.github/plugins/azure-sdk-dotnet/skills/` slice is **29/29 current-standard companion-complete**.
- The direct `.github/plugins/azure-sdk-java/skills/` slice has an exact denominator of **26** and is **11/26 current-standard companion-complete**.

Previously reconciled Microsoft units include `applicationinsights-web-ts`, `skill-creator`, `cloud-solution-architect`, `copilot-sdk`, and the complete direct `.NET` SDK slice. Their exact individual evidence remains in `registry/skills/microsoft-skills/` and `registry/verification/microsoft-skills/` rather than being flattened into a family-level verdict.

The direct `.NET` slice closed at 29/29 with decisive exact-version evidence for every package. Negative dispositions remain differentiated across resource/cost mutation, secret and credential handling, identity/token operations, message and background-processing effects, data transmission, local-file access, destructive actions, and dependency defects. Completion means decisive current evidence, not universal approval.

#### Java plugin slice — ACTIVE

The Java slice is now **11/26** current-standard companion-complete. All reviewed packages were evaluated as complete packages, including bundled examples/references where present. Exact upstream path revisions differ where the pinned history differs; each record retains its own package-tree, skill-blob, source revision, and freshness identity.

| Skill | State | Score | Decisive unchanged-adoption blockers / disposition basis |
|---|---|---:|---|
| `azure-ai-agents-persistent-java` | rejected | 14/20 | Remote agent/thread/run/file/vector-store mutation, local-file upload, metered execution, downstream function/tool effects without distinct authority gates. |
| `azure-ai-anomalydetector-java` | rejected | 13/20 | Time-series transmission, SAS-backed model training/inference, model deletion and metered external-service use without data/cost/lifecycle gates. |
| `azure-ai-contentsafety-java` | rejected | 12/20 | Text/image transmission plus blocklist mutation without privacy/data/cost gates; top-level and bundled example SDK versions conflict. |
| `azure-ai-formrecognizer-java` | rejected | 12/20 | Sensitive document transmission and custom model/classifier lifecycle mutation without mandatory data/privacy/cost boundaries; version-sensitive guidance. |
| `azure-ai-projects-java` | rejected | 13/20 | Dataset/index mutation, local-file upload, connection credential access and external evaluation operations without distinct authorization. |
| `azure-ai-vision-imageanalysis-java` | rejected | 13/20 | Local/remote image transmission, OCR and people detection without mandatory privacy/data and metered-service boundaries. |
| `azure-ai-voicelive-java` | rejected | 12/20 | Live audio sessions, transcription, microphone capture and function execution without recording/privacy/cost/tool-action gates. |
| `azure-appconfiguration-java` | rejected | 13/20 | Production configuration, feature targeting, secret-reference metadata, read-only protection and snapshot transitions without distinct configuration, targeting, sensitive-metadata and destructive/state-transition gates. |
| `azure-communication-callautomation-java` | rejected | 11/20 | PSTN call initiation/answering, speech/DTMF processing, recording/download, transfer, participant changes and termination without mandatory telephony, consent/privacy, cost and destructive-action boundaries; top-level SDK 1.6.0 conflicts with bundled examples at 1.5.2. |
| `azure-communication-callingserver-java` | retired | 14/20 | Microsoft explicitly marks CallingServer deprecated and directs new development to Call Automation. Preserve only for migration/legacy maintenance; legacy recording control lacks a distinct participant-consent/privacy gate. |
| `azure-communication-chat-java` | rejected | 12/20 | Thread/message creation and deletion, participant changes, history sharing, read/typing privacy signals, and external message/user-metadata transmission lack distinct communication, participant, privacy/data, destructive-action and service-use gates; top-level SDK 1.6.0 conflicts with bundled examples at 1.6.4. |

Behavioral validation is `not-run` for all eleven because no separate representative external scenario/adversarial evidence has been recorded.

- Denominator accounting is closed at the exact registered pin. The unit is an independently front-mattered `SKILL.md` entry point. The count includes 129 language-SDK plugin entries; real canonical `.github/skills` packages; 28 Azure-plugin top-level packages; 10 Deep Wiki entries; 5 Microsoft 365 Agents Toolkit top-level entries; and 6 additional nested skill entry points (`microsoft-foundry/finetuning`, `models/deploy-model`, `models/deploy-model/capacity`, `models/deploy-model/customize`, `models/deploy-model/preset`, and `teams-app-developer/slack-to-teams`). Duplicate exposure paths are de-duplicated by skill identity, `.github/skills` symlink mirrors and plugin symlink aliases do not create additional units, and ordinary workflow/reference `.md` files remain part of their parent package. The upstream README's conflicting 174/175 headlines are not used as denominator evidence.
- Continue sequential review from the pinned tree and check both companion paths before every unit. The remaining **15 Java direct packages** are the next coherent Microsoft tranche before moving to the next plugin/language family.
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

**Active frontier:** Microsoft Skills, now **44/189** current-standard companion-complete with **145** gaps. The direct `.NET` plugin slice is **29/29 complete** and Java is **11/26** complete with **15** direct Java packages remaining. Microsoft Azure Skills follows after the Microsoft Skills frontier. Discovery and issue/PR hygiene continue in parallel.