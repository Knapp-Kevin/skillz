# Microsoft Azure infrastructure and migration: three exact-version static reviews

**2026-10-28.** Candidate `microsoft/skills@61fe0305ea70389ed8705eec6026a786f57865cf`; July pin `32cad4ee689c95c309e61aeefcbc6af356f1e6a7` unchanged. Entire package trees and **113/113 exact source blobs** were fetched and SHA-matched, totaling **461,601 bytes**, with **113 distinct blobs**. No Azure, source-cloud, CLI, IaC, scanner or behavioral execution; no source admission or pin movement.

## Macro-first map

The structural candidate denominator remains **208 = 106 exact-tree carry-forwards + 76 changed-existing + 26 new/ungoverned**. All 26 new have complete static companions. Changed-existing **66/76 → 69/76**, leaving **7**: five Azure operations (`azure-deploy`, `azure-diagnostics`, `azure-kubernetes` parent, `azure-prepare`, `azure-upgrade`) and `microsoft-foundry` root plus `microsoft-foundry-finetuning`. These three source packages each have one front-mattered SKILL.md and no nested first-class skill; ordinary Markdown, IaC and examples are supporting references, not extra denominator units. The 113 package exposures are 113 distinct Git blobs. No previous candidate-version companions existed for these three, while July-pin companions remain valid at their own exact version.

| Candidate package | Git package tree | Complete files | Score | Disposition |
|---|---|---:|---:|---|
| `azure-compute` | `eac48d13e7b19366050bd7a176c7b5189ad34cdb` | 41 | 11/20 | REJECT unchanged |
| `azure-cloud-migrate` | `064dc66880cee5694234690f2b9be17e135dd1dd` | 31 | 11/20 | REJECT unchanged |
| `azure-enterprise-infra-planner` | `6a82cbd081dc48dd74d5f726e2c032f8092fa3e4` | 41 | 15/20 | REJECT unchanged |

## Exact-package findings

**Azure Compute (41 files, 11/20, REJECT unchanged):** VM Creator includes a final live-apply confirmation, but Capacity Reservation proceeds from parameter collection directly to billable CRG/reservation creation and EMM provisions subscription-level identities, resource providers, monitoring workspaces and security controls without distinct action-specific approval. Terraform example uses destroy -auto-approve. Beginner path falls back to NSG source '*' when public-IP detection fails, exposing SSH/RDP; EMM monitoring and resource inventory need scoped authorization and data-retention review. Positive differentiated value: VM size/quota/cost selection, Plan Card, generate-only IaC adapters, quota checks, explicit VM-creation gate; extract and require CRG/EMM and network-security approvals.

**Azure Cloud Migrate (31 files, 11/20, REJECT unchanged):** Root and Functions/App Service global rules require ask_user for deployment and destructive actions, but Container Apps scenario deployment guides contain direct resource creation, image migration and role grants without consistent scenario-local approval; global rules are not uniformly routed to these guides. Kubernetes export includes unredacted Secret YAML; examples retrieve Log Analytics shared keys and pass decoded Kubernetes secrets into Azure CLI arguments, risking file, process-list, terminal/history and cross-cloud disclosure. Positive differentiated value: Assessment-first routing, source-preserving output workspace, runtime-specific bindings, managed-identity patterns, service discovery checks; extract with explicit source/target, secret, billing and deployment gates.

**Azure Enterprise Infra Planner (41 files, 15/20, REJECT unchanged):** Strong Phase 5 plan approval and Phase 7 risk-acknowledged post-prompt deploy gate; however Phase 1 defaults to subscription-wide insights retrieval when the user does not answer scope selection, and deployment.md describes a weaker 'yes, deploy' checkpoint than Phase 7. These are unsafe unchanged-use ambiguity for sensitive tenant reads and privileged deployment. Default subscription insights are sent to a subagent and persisted under .azure/insights.json without affirmative scope/privacy authorization; require explicit subscription/tenant read, minimization, retention and file destination approval. Positive differentiated value: Seven-phase gate discipline, existing-resource preservation, secure-by-default IaC, checkov evidence and risk-acknowledged deployment; adapt with explicit scoped reads and consistent deployment gate.

## Systemic synthesis

- **Authorization must cover each distinct branch.** A safe VM creation route does not authorize capacity reservations or subscription EMM; App Service/Functions confirmation does not automatically protect Container Apps recipes. A strong risk-acknowledged deploy gate does not authorize subscription-wide insight collection.
- **Sensitive data exposure is independent of write permissions.** Raw Kubernetes Secret export, process-visible secret arguments, Log Analytics shared keys, and default-scope Azure insights need explicit read/disclosure, minimization, retention and transfer controls.
- **High-value mechanisms survive unchanged-use rejection.** VM Plan Cards and quota checks, migration assessment and isolated outputs, and gated infrastructure design/IaC verification are valuable adaptation/checklist evidence. No blanket rejection of the source family follows from these three decisions.
- **Freshness is package-specific.** Exact candidate package trees and manifests, upstream path commits, all blob identities, dependencies, individual rubrics and controlled tags are in paired YAML companions. Candidate source identity remains separate from registered July material.
- **No behavioral or package-security promotion.** Source-owned scripts, Bicep/Terraform examples and CLI snippets were inspected only, never executed. The repo owns no runner, scanner, CI, generator or service.

## Flow and remaining frontier

Three genuine changed-existing gaps closed: **66/76 → 69/76**, Azure operations **20/30 → 23/30**, overall full candidate review gaps **10 → 7**. Three provenance and three verification companions; third-party YAML companions **816 → 819**, total verification YAML **860 → 863** (44 first-party + 819 third-party). Registered July **186/186**, structural candidate denominator **208**, 26 new-candidate reviews and source pin unchanged. Draft PRs #412/#413 remain external package-security and independent acceptance holds; #416 additionally needs current-main reconciliation. Issues #400/#402/#415 remain open.
