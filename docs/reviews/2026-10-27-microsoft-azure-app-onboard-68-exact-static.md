# Microsoft Azure App Onboard: full exact-version static review

**Date:** 2026-10-27. **Source:** `microsoft/skills` at `61fe0305ea70389ed8705eec6026a786f57865cf`. **Registered July pin:** `32cad4ee689c95c309e61aeefcbc6af356f1e6a7` unchanged. **Scope:** `.github/plugins/azure-skills/skills/azure-app-onboard/`, Git tree `ce62e3df0d860115631b3fb7658eb7a6c35cf141`, manifest blob `00635c01fc9518e171e5157185a60999e1455b84`. All **68 bundled blobs** (382,357 upstream tree bytes) were fetched at the exact revision and each returned blob SHA matched the non-truncated Git tree. No Azure command, script, scanner, cloud operation or behavioral trial was executed.

## Macro frontier

The candidate denominator remains **208** = 106 exact-tree carry-forwards + 76 changed-existing + 26 new/previously ungoverned. Before this tranche, 23/26 new packages had full static companions. The remaining three were `azure-app-onboard` (68 files), `foundry-iq` (85 files), and `slack-to-teams` (one local manifest plus 100+ parent shared references). The nested `prepare/SKILL.md`, `scaffold/SKILL.md` and `deploy/SKILL.md` have no independent frontmatter and are bundled phase references, not three additional eligible packages. The 76 changed-existing packages have been screened, **not** fully requalified.

## Decision: REJECT unchanged, 12/20

The MIT-licensed, Microsoft-authored v1.2.6 manifest covers new/existing app Azure onboarding through planning, scaffolding, deployment and handoff. It explicitly excludes existing azd deployment, standalone validation/cost optimization, AKS management and troubleshooting. **Two independent user approval gates** for scaffolding and deployment display subscription, resource group, region, services/SKUs, costs and database network exposure. These are real safeguards, not absent approvals.

Material defects found in the bundled package:

1. `references/session-protocol.md` orders automatic deletion of inactive session directories after seven days without action-specific deletion approval or retention review, including potentially sensitive session artifacts and displaced IaC.
2. `scaffold/references/bicep-patterns-security.md` allows generated administrative secrets to be displayed in conversation; `deploy/references/deploy-checklist-template.md` permits recovering secure parameters from `deploy-audit.log`; `deploy/references/database-post-deploy.md` uses `deploy-secrets.env` and password-bearing CLI arguments. Other references use Key Vault and managed identity, but those positive controls do not make the weaker alternatives safe. No real secret was viewed.
3. `scaffold/references/bicep-app-service.md` enables SCM basic publishing credentials in generated IaC. `deploy/references/code-deployment-appservice.md` requires re-disabling after deployment but says failure to re-disable should be logged without blocking, potentially leaving the publishing surface enabled.
4. `deploy/references/database-post-deploy.md` automatically executes discovered database migration commands before health checks, without separate authorization for schema/data mutation, destructive migration effects, backups or rollback.
5. `deploy/references/code-deployment-container-apps.md` can add an ACR resource and identity role assignment as a healing step. Updating the cost estimate is not independent approval for a newly billable resource or permission grant.
6. `scaffold/references/self-review-checklist.md` offers “Continue with risks” on critical security findings, while `references/approval-gates.md` blocks unresolved critical findings. The inconsistent stop policy requires fail-closed resolution.

Additional qualification risks: Terraform local state can hold sensitive material; quota checks may warn and proceed on failed API calls; AI inference cost is excluded but **explicitly disclosed**. The broad database access to Azure services is **explicitly disclosed with a private-access alternative and consent gate** in `references/approval-gates.md`, so it must not be falsely classified as ungated. Static observations do not establish exploit execution.

## Preserve and adapt

Useful prior art: separate approval gates, scoped Azure target and cost displays, deterministic phase orchestration, quota/service mapping, Bicep/Terraform templates, managed identity/Key Vault/RBAC patterns, evidence-first health checks, compaction-safe checklists and bounded healing. Adapt with action-specific local deletion consent, secret-safe credential paths and retention, fail-closed SCM re-hardening, separate migration and new-resource/RBAC approval, and consistent security-stop gates. The bundled `scaffold/scripts/scaffold-conformance.sh` and `.ps1` are **source-owned reference material**, not repository-owned runtime. External Azure CLI/MCP, Bicep/Terraform, cloud permissions and separately reviewed `azure-app-onboard-prereq` remain dependencies, not execution evidence.

## Accounting and lifecycle

New-candidate full static companions **23/26 → 24/26** (4 semantic VERIFIED only / 20 REJECT unchanged); current-version qualification frontier **79 → 78** (2 new + 76 changed). Third-party verification companions **747 → 748**; all verification YAML **791 → 792** (44 first-party + 748 third-party). Registered July **186/186** and candidate denominator **208** remain unchanged; four removed-path successor decisions remain. No admission, pin advancement, scanner approval or behavioral validation. Reconcile README, SYSTEM_STATE, CURATION_QUEUE, INDEX, index.json and the candidate ledger together; fix a stale CURATION_QUEUE 4+18 mismatch. Issues #400/#402/#415 and draft PRs #412/#413/#416 retain their separate security/acceptance blockers.
