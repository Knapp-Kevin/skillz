# Microsoft Azure Upgrade: complete 50-file exact-version static review

**2026-10-28.** Candidate `microsoft/skills@61fe0305ea70389ed8705eec6026a786f57865cf`; registered July pin `32cad4ee689c95c309e61aeefcbc6af356f1e6a7` unchanged. Package tree `a6d9570e0e6d239a624592fd6eb667e20bb7e02d`, manifest blob `4d60fedcaa037dafd098d9ca3c4f8302c7520f1c`, upstream manifest v1.2.3, latest package-path commit `83a4616dcbaa52bea173fc133f7f974dc60de608` (2026-10-20). **50/50 source-owned blobs read**, 338,693 bytes, with full per-file blob identity recorded in `registry/skills/microsoft-skills-candidate/azure-upgrade.yaml`. No cloud command, scanner, source-owned script, or behavioral validation was run.

## Macro frontier and overlap

The candidate structural denominator remains **208 = 106 exact-tree carry-forwards + 76 changed-existing + 26 new/ungoverned**. New candidates remain **26/26**. Changed-existing advances **73/76 → 74/76**, leaving **2**: `azure-prepare` (166 source files) and `microsoft-foundry` root (220 parent/nested/shared file exposures). Azure operations advances **26/30 → 27/30**. The registered July corpus remains **186/186** with no pin movement. This 50-file package is one first-class skill, not 50 separate skills.

The source's five principal branches are Linux Functions migration, Windows Functions migration, Java SDK modernization, Redis ACR-to-AMR routing, and Redis Enterprise-to-AMR routing. Linux and Windows share a high-level assessment/approval vocabulary but have materially different secret and cutover mechanics. The Java references contain both modern identity-first advice and older conflicting credential-file examples. The Redis branch delegates operational execution to two external, independently versioned skill repositories; it does not establish their license, exact version, security, or action authority.

## Exact-version decision

| Package | Source blobs | Score | Decision |
|---|---:|---:|---|
| `azure-upgrade` | 50 | **13/20** | **REJECT unchanged; ADAPT / EXTRACT / CHECKLIST / REFERENCE** |

**Strengths:** precise source/target routing; mandatory assessment; target/SKU confirmation; many Windows source-change and per-function cutover approvals; non-HTTP trigger safeguards; rollback-first source retention; validation that refuses to relax security controls; scoped migration artifact paths; identity-first design; Java build/test and migration planning; Redis SKU disambiguation.

**Decisive failures:**

1. **Credential exposure despite a strong policy.** `references/services/functions/consumption-to-flex/linux/automation.md` lines 234–255 retrieves the live `AzureWebJobsStorage` connection string into `AZURE_STORAGE_CONNECTION_STRING` and uses it for blob listing/downloading. Windows `automation/configuration-inventory.md` lines 37–40 and 64–67 and `automation/deployment-package.md` lines 80–105 similarly retrieve credential-bearing source settings. Output suppression, subshells, variable cleanup and environment scoping mitigate but do not replace a secure external identity/credential path, scoped data-owner authority and explicit access justification.
2. **Contradictory Java credential advice.** `references/languages/java/package-specific/com.microsoft.azure.management.md` rejects reading legacy credential files and recommends `DefaultAzureCredential`, while `templates/PLAN_TEMPLATE.md` and `templates/SUMMARY_TEMPLATE.md` explicitly recommend parsing a credential file with Jackson and constructing `ClientSecretCredential`. These are source-authored example templates, not authoritative security approval; unchanged reuse risks reproducing an insecure pattern.
3. **Non-destructive side effects lack consistent authorization.** Linux `automation.md` and Windows `automation/discovery-and-assessment.md` install Azure CLI extensions without a distinct host-environment change approval. Java `workflow/phase-3-execute.md` edits code, runs builds/tests and commits to a branch without a separate destination/workspace write authorization gate. The global requirement to confirm destructive and Azure resource creation is not a universal authorization grant for every local or remote effect.
4. **Authority and privacy scope remain incomplete.** Subscription discovery, application settings and access-key inventory, private code-package downloads, and cross-environment migration require resource/data-owner scope, least disclosure and retention controls. Windows source-cutover gates are materially better than the Linux path; neither branch's approval can be inherited by another branch or external Redis skill.

**Source-owned tooling:** the Java BOM Python helper and migration command snippets remain intact upstream reference evidence. Their existence does not create any `skillz` runtime, test runner, installer or automation.

## Systemic synthesis and next frontier

The family is strong on *planning, migration sequencing, validation and rollback* but inconsistent on *secret provenance, identity-based access, destination authorization and branch-local approval*. This is a repeat of the authorization fragmentation found in Azure Deploy, Diagnostics, Kubernetes and Foundry. The preferred adaptation extracts a plan-first migration checklist with explicit tenant/subscription/resource/data-owner scope, approved credential broker or managed identity, scoped artifact retention, per-operation approval and independent validation. It does not execute upstream snippets unchanged.

One exact candidate provenance/verification pair advances third-party records **823 → 824**, total YAML **867 → 868** (44 first-party + 824 third-party). No source admission, security promotion, behavioral evidence, or pin movement. The remaining two large packages warrant independent deep review, not a forced quota.
