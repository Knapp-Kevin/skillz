# Google Agents CLI pinned authority and taxonomy review

**Date:** 2026-10-29  
**Source:** `google/agents-cli`, Apache-2.0  
**Exact registered pin:** `ef7808f33fc3038112b69d4ad488ce33b72699b1`  
**Scope:** seven first-class `skills/google-agents-cli-*/SKILL.md` packages. No aliases, mirrors or ordinary reference Markdown were counted as additional skills.

## Exact pinned frontier

The upstream pinned Git tree contains seven first-class manifests; all seven existing verification fingerprints match those exact source blobs. The source remains intact under `skills/sources/google-agents-cli/`; bundled references, templates, Terraform and CLI tools are upstream source material, not repository-owned execution machinery.

| Skill | Exact pinned manifest Git blob | Final semantic state |
|---|---|---|
| `google-agents-cli-adk-code` | `73dc82088f15c56ba35ebb9d9a817dacf4d326cf` | VERIFIED semantic only, 17/20, unchanged |
| `google-agents-cli-deploy` | `e473814cd2e2cfe9e8cfeb24e972704756dc5184` | REJECT unchanged, 15/20 (was 19/20) |
| `google-agents-cli-eval` | `2ce4c881733de6cc75dce97bb7e3c4391df69c75` | VERIFIED semantic only, 18/20, unchanged |
| `google-agents-cli-observability` | `c8f468b58e0ac645647c72d818b156b42521a921` | REJECT unchanged, 14/20 (was 18/20) |
| `google-agents-cli-publish` | `5c9e6c59a1473f65d859d321cea06ab4f3728595` | REJECT unchanged, 14/20 (was 16/20) |
| `google-agents-cli-scaffold` | `d61c2e45697f1724cd229b55283e2548929a936c` | VERIFIED semantic only, 19/20, taxonomy-only repair |
| `google-agents-cli-workflow` | `b33bd1202885bbdaf17b5c50df0660ae01452b3a` | VERIFIED semantic only, 19/20, unchanged |

All seven remain current-standard decisive static records. All seven have `validation_status: not-run`. No external scanner execution, host behavioral acceptance, package mutation or source-pin change is claimed.

## Deep review: authority hard fails

**Deploy:** The standard dev deployment sequence explicitly asks for human approval before `agents-cli deploy`. That is a useful safeguard, but it does not authorize separate `agents-cli infra single-project` Terraform provisioning, cloud API enablement, IAM grants, Secret Manager create/update, Agent Gateway binding or production rollback by git push/traffic shift. The procedure supplies these as operational steps without a separate action-specific authorization boundary. A selected target, known project ID, CLI credential or general dev-deploy approval is not authorization for every additional persistent, billable or security-affecting operation. Preserve target comparison, dry-run, timeout recovery and rollback planning as ADAPT/EXTRACT/CHECKLIST evidence.

**Observability:** The exact manifest discloses that Terraform deployment defaults to **full prompts/responses uploaded to GCS/BigQuery** even when `OTEL_INSTRUMENTATION_GENAI_CAPTURE_MESSAGE_CONTENT=NO_CONTENT` disables trace/event content. Asking which observability tier the user prefers is not consent to transmit sensitive conversations, select retention or provision paid telemetry resources. The guide also offers deletion of an existing Reasoning Engine with session loss, redeployment and broad telemetry IAM roles without separate action-specific approval. Preserve its accurate two-tier telemetry explanation and no-content troubleshooting as adaptation material.

**Publish:** The guide offers non-interactive Gemini Enterprise registration and Agent Registry service create/update/delete, including destructive deletion, without an explicit approval gate bound to each exact app/service, visibility, identity, metadata and deletion target. CLI flags, available roles and an initial request to learn publishing do not grant all these mutations. Preserve A2A/ADK registration comparison, read-only inventory and permissions reference for ADAPT/EXTRACT/CHECKLIST.

## Macro synthesis

The seven-skill family has clear lifecycle decomposition and meaningful upstream reference depth. Its recurring weakness is conflating a user-approved objective with separate high-impact cloud actions. Observability adds a privacy-specific failure: describing full-content telemetry is not permission to disclose user data. `adk-code`, `eval`, `scaffold` and `workflow` were screened without a newly proven hard-fail disposition change; cloud-side evaluation trace submission deserves focused future privacy review. The source remains useful, but unchanged reuse of the three rejected procedures is not endorsed.

Five existing verification records also contained out-of-vocabulary tags relative to `registry/taxonomy.yaml`: deploy (`infrastructure`, `agent-operations`, lifecycle `deployment`, `rollback-aware`), observability (`agent-operations`, `privacy-aware`), publish (`publishing`, `agent-operations`, `registry-management`, lifecycle `deployment`, `idempotent`), scaffold (`scaffolding`, `template-driven`, `rollback-aware`), and workflow (lifecycle `deployment`). Those were mapped to existing controlled tags without expanding the taxonomy or changing scaffold's semantic disposition.

## Reconciliation and constraints

**Google Agents CLI: 7/7 -> 7/7; VERIFIED semantic only 7 -> 4; REJECT unchanged 0 -> 3; static gaps 0 -> 0.** Denominator delta zero. Published inventory stays 44 first-party / 826 third-party review companions / 870 total verification records. README, SYSTEM_STATE, CURATION_QUEUE, INDEX and index.json are reconciled as one tranche. Provenance companions for the three reclassified packages and verification companions for those three plus scaffold and workflow were refreshed.

The five existing draft PRs #412, #413, #489, #492 and #496 remain separate external security/adversarial acceptance holds. The 36-package first-party repair frontier is unchanged. No repository-owned runtime, scanner, script, CI, scheduler, generator or other execution mechanism was introduced.
