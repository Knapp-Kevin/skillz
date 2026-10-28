# Microsoft candidate readiness, identity and authoring: four exact-version reviews

**2026-10-28.** Candidate `microsoft/skills@61fe0305ea70389ed8705eec6026a786f57865cf`; registered July `32cad4ee689c95c309e61aeefcbc6af356f1e6a7` unchanged. Complete source-tree and file-content static review only. No execution, package-security scan, behavioral validation, admission, or pin movement.

## Macro map and denominator

208 structurally eligible = 106 exact-tree carry-forwards + 76 changed-existing + 26 new/previously ungoverned. Before this tranche, 58/76 changed-existing had full reviews; the remaining 18 consisted of 17 Azure operations and one skill creator. These four genuine gaps comprise three Azure operations/identity/readiness packages plus the final non-Azure-operations authoring package. The four complete package trees contain **47 source-file exposures**, totaling **340317 bytes** (not asserted to be unique across packages). Nested first-class AKS readiness is separately counted; parent AKS remains unqualified. Historical registered-pin reviews do not substitute for candidate-version review.

| Package | Tree | Files | Score | Static disposition |
|---|---|---:|---:|---|
| `entra-agent-id` | `2757439372801955542e909dc218f74914811203` | 7 | 9/20 | REJECT unchanged |
| `azure-kubernetes-automatic-readiness` | `c8ffe7bbfd195951701a5514cbdad6263c817e7a` | 6 | 17/20 | VERIFIED semantic only |
| `azure-validate` | `23c61eed8d0009d712d71904e21e3c4e0df4d6d0` | 27 | 11/20 | REJECT unchanged |
| `skill-creator` | `f9dc3aaf9210af8eb06ba11bf4883e6ace705673` | 7 | 12/20 | REJECT unchanged |

## Individual findings

### entra-agent-id

**Authority:** POST creates persistent identity objects and grants User.Read.All or AllPrincipals User.Read Tasks.ReadWrite Mail.Send with ten-year expiry; no distinct tenant, permission, consent, expiry or sponsor approval before action.

**Privacy:** Bearer credentials and cross-tenant token exchange need strict custody, recipient and tenant isolation; env-backed secrets are safer than chat solicitation but not an authorization boundary.

**Retained adaptation value:** Per-instance identity separation, BlueprintPrincipal ordering, fmi_path/OBO exchange, managed identity and WIF guidance.

**Dependencies:** Microsoft Graph v1.0; Graph application/delegated permissions; Entra Blueprint and Principal; ClientSecretCredential or federated identity; PowerShell, Python requests, SDK AgentID sidecar; seven bundled source files

### azure-kubernetes-automatic-readiness

**Authority:** Explicitly forbids cluster mutation, restricts Kubernetes data projection and requires user approval for every local file fix; optional cluster read still must be host-authorized and scoped.

**Privacy:** Bundled jq allowlist removes Secret and ConfigMap values and token-bearing fields; namespace, workload and topology metadata still require authorized read scope and minimization.

**Retained adaptation value:** Deterministic constraint classification, conditional safeguard handling, safe offline fallback, consent-gated YAML diffs and allowlist sanitizer.

**Dependencies:** Host-approved Azure MCP AKS metadata reads or Azure CLI; permitted kubectl and jq allowlist filter; bundled AKS Automatic constraint spec, fix guidance and migration references

### azure-validate

**Authority:** Mandatory host script immediately writes .azure/validate-status.json; Terraform init and azd env set alter workspace/session, validation queries Azure, and failing checks prompt fixes. Destructive ask_user exists but no distinct authorization for non-destructive local/cloud changes or prerequisite chain; approved plan status is not general action authorization.

**Privacy:** Subscription, role and environment context may be sensitive; Aspire environment helper prints resolved values and can expose resource metadata. Avoid raw credential-bearing diagnostics.

**Retained adaptation value:** What-if previews, RBAC least-privilege inspection, fail-closed validation and separate deploy intent routing.

**Dependencies:** azure-prepare and azure-deploy skill chain; Azure CLI/AZD, Bicep, Terraform; source-owned Bash/PowerShell workflow and validation scripts; Azure RBAC and policy reads; 27 bundled files

### skill-creator

**Authority:** Prescribes writes under .github/skills, category symlinks, README changes, harness and optional eval execution without checking the host destination, repo maintenance authority, cost or side effects; cleanup/delete examples and test execution need separate authorization.

**Privacy:** Credential-safe managed identity guidance is useful; package and evaluation tools must not ingest secrets or upload private source/test data without explicit scope.

**Retained adaptation value:** SDK freshness checks, context/token budgets, hero versus non-hero scenario design, credential lifecycle patterns and acceptance criteria.

**Dependencies:** Microsoft Learn/microsoft-docs MCP; host Python for source-owned init_skill.py/package_skill.py/quick_validate.py; optional pnpm harness and Vally; 7-file package with 68,147-byte SKILL.md

## Systemic synthesis

- A documented user task, valid Azure credentials, role membership, or approved plan does not authorize arbitrary identity grants, infrastructure changes, external transmission, or local side effects. Entra Agent ID's ten-year AllPrincipals delegated Mail.Send/Tasks.ReadWrite grant is a particularly consequential unchanged-use failure.
- AKS Automatic Readiness is the positive exception: it prohibits cluster mutation, projects allowlisted workload fields before model exposure, distinguishes conditional safeguards, and requires explicit user approval before file edits. Security and behavioral evidence remain not-run.
- Azure Validate's workflow and Terraform/AZD helpers write workspace/session state and can initiate external validation. Destructive confirmation alone does not authorize all side effects. Preserve its fail-closed checks and what-if patterns as adapted checklists.
- The Skill Creator's 68,147-byte manifest and bundled source-owned tooling are reference evidence, not `skillz` runtime. Its repository-specific output paths, symlink/catalog changes, harness and optional evaluation require host/destination authority. Its concise-authoring advice also conflicts with the oversized upstream manifest.
- **Remaining 14 changed-existing packages** are all Azure operations: cloud-migrate, compute, deploy, diagnostics, enterprise-infra-planner, kubernetes, prepare, upgrade, and six nested/root Microsoft Foundry packages. The larger dependency-heavy packages need separate deep review. No source admission or taxonomy expansion.

## Flow and evidence

Four exact-version semantic reviews, four provenance and four verification companions, 47 source-file exposures. Changed-existing **58/76 → 62/76**, remaining **18 → 14** (Azure operations **13/30 → 16/30**, skill-creator **0/1 → 1/1**). Third-party verification **808 → 812**; total YAML **852 → 856** (44 first-party + 812 third-party). Candidate new **26/26**, structural denominator **208**, registered July **186/186** unchanged. Security **0**, behavioral **0**, cloud operations **0**, source admissions **0**.
