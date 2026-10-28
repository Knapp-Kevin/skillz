# Microsoft Foundry model deployment: four exact-version static reviews

**2026-10-28.** Candidate `microsoft/skills@61fe0305ea70389ed8705eec6026a786f57865cf`, July pin `32cad4ee689c95c309e61aeefcbc6af356f1e6a7` unchanged. Exact package trees and 17 distinct source blobs inspected statically. No cloud operation, bundled script execution, scanner, behavioral validation, admission or source-pin movement.

## Macro map and accounting

Candidate structural denominator **208** = **106** exact-tree carry-forwards + **76** changed-existing + **26** new/ungoverned. New **26/26** already complete. This tranche closes four genuine changed-existing gaps: the parent `deploy-model` router and its three independently front-mattered nested skills. **30 package-file exposures = 17 distinct Git blobs (104,511 bytes)**. Parent-child overlaps are counted once in unique evidence and four times only as distinct eligible package identities. Ordinary references are not new skills.

| Package | Exact tree SHA | Files | Score | Decision |
|---|---|---:|---:|---|
| `microsoft-foundry-deploy-model` | `5e60a08596808fd2dc6209ab309d682664d2e03c` | 17 | 16/20 | VERIFIED semantic only |
| `microsoft-foundry-deploy-model-capacity` | `547adfbf066ba49a8e748a4cb0bbd827c2ab6cbd` | 5 | 11/20 | REJECT unchanged |
| `microsoft-foundry-deploy-model-customize` | `118035ed1dad47d2389464e2968c92923dc2c7b5` | 4 | 16/20 | VERIFIED semantic only |
| `microsoft-foundry-deploy-model-preset` | `643a38ce95fbe3e737002335bd52cb2b164b4380` | 4 | 10/20 | REJECT unchanged |

## Individual findings

**Parent deploy-model, VERIFIED semantic only (16/20):** Explicit target presentation (project, region, resource group) and affirmative "Yes, deploy here" precede deployment. This is action authorization, unlike mere input confirmation or credential availability. Its intent router, live SKU/quota checks and cross-region chaining are useful, but parent approval cannot be inherited by independently invoked nested skills.

**Capacity, REJECT unchanged (11/20):** `capacity/scripts/discover_and_rank.sh` lines 54–60 embeds Azure API `CAPACITY_JSON`, `PROJECTS_JSON` and quota JSON directly into `python3 -c` source using triple-quoted literals. Untrusted JSON containing string delimiters can become executable Python source. Subscription-wide project metadata is also printed without a minimal read/disclosure scope. Preserve read-only capacity/quota ranking for a data-only adaptation, not unchanged script execution.

**Customize, VERIFIED semantic only (16/20):** Phase 12 presents full SKU, model, version, capacity, RAI and project configuration for user approval before Phase 13 persistent deployment. This is a real action-specific gate. Unexpected PTU/priority billing, policy changes and Anthropic `modelProviderData` tenant country/organization disclosure still need separately appropriate consent. No cost quote or behavioral evidence was verified.

**Preset, REJECT unchanged (10/20):** Fast path moves directly from capacity check to persistent deployment; alternative-region path can create billable AI Services/AIProject resources before deployment. The directly invocable sub-skill lacks a distinct authorization checkpoint. Its workflow writes raw capacity API JSON to `/tmp/capacity_check.json` without cleanup/retention policy. Preserve region fallback, quota checks and status polling as adaptation/checklist evidence.

## Systemic synthesis

- **Nested authority is not inherited.** Parent and customized paths have approval gates; preset directly invoked does not. Credentials, project selection and valid quota do not grant deployment authority.
- **Read-only Azure operations can still create host execution risk.** The capacity script promotes API tool output into Python code, a concrete trust-boundary defect independent of cloud mutation.
- **Billing, disclosure and data retention require their own scopes.** Capacity is not cost consent; tenant metadata, subscription/project names and temporary API responses require minimization and authority.
- **Source-owned scripts remain upstream reference evidence.** Upstream TEST_PROMPTS claims of successful tests are not independent execution or behavioral validation by this review. No repository-owned machinery was introduced.
- **Ten changed-existing gaps remain:** eight large Azure operations packages (`azure-cloud-migrate`, `azure-compute`, `azure-deploy`, `azure-diagnostics`, `azure-enterprise-infra-planner`, `azure-kubernetes`, `azure-prepare`, `azure-upgrade`) and Foundry root plus finetuning. The 220-blob Foundry root requires isolated deep review.

## Flow

Changed-existing **62/76 → 66/76**; Azure operations **16/30 → 20/30**; remaining **14 → 10**. Four provenance/verification pairs; third-party **812 → 816** and total verification YAML **856 → 860** (44 first-party + 816 third-party). July registered **186/186**, candidate denominator **208**, and new **26/26** unchanged. Package security, behavioral validation and candidate pin acceptance remain open. Draft PRs #412/#413/#416 retain independent acceptance/security blockers; issues #400/#402/#415 remain active.
