# Microsoft Azure mirrored authority contradiction: five-package reconciliation

**Date:** 2026-10-30  
**Registered source pins:** `microsoft-azure-skills` `8f8c72bb9e22aee4366e07aadfd5766ef9add8f4`; `microsoft-skills` `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`.  
**Method:** Static inspection of exact pinned upstream SKILL.md and selected bundled references, reconciliation against the already complete Microsoft Skills exact-package reviews, and source-family macro synthesis. No external behavior or package-security scan was executed.

## Macro map and denominator

Azure Skills remains **34/34 current-standard reviewed, zero genuine static gaps**. Microsoft Skills remains **186/186**. These are two registered exposure families, not evidence of 220 different physical package identities: the two corrected packages have the **same exact Git package-tree and SKILL.md blobs** across both pins. Both already had individual provenance and verification companions in both families. No new review identity, source pin, denominator, or first-party inventory is introduced.

This tranche rechecks the **five Azure procedures still marked VERIFIED** after the prior ten-package authority review, using the exact-source package identity and the prior Microsoft Skills companion as a conflict detector. Two are contradictory false approvals; three retain their static disposition. All five still have behavioral validation **not-run**.

| Package | Azure before | Azure after | Decision |
| --- | --- | --- | --- |
| `airunway-aks-setup` | VERIFIED 17/20 | **REJECT unchanged 15/20** | Install/deploy confirmation does not authorize destructive rollback/secret deletion |
| `azure-cloud-migrate` | VERIFIED 17/20 | **REJECT unchanged 9/20** | Bundled Container Apps deployment/secret migration crosses resource, identity, credential, network and cost boundaries without granular authority |
| `azure-rbac` | VERIFIED 17/20 | VERIFIED 17/20 | Generate-only least-privilege role recommendations, CLI and Bicep artifacts; no role assignment executed |
| `microsoft-foundry-deploy-model-capacity` | VERIFIED 17/20 | VERIFIED 17/20 | Read-only capacity/quota comparison with explicit no-deploy boundary; downstream child remains separately governed |
| `microsoft-foundry-deploy-model-customize` | VERIFIED 17/20 | VERIFIED 17/20 | Phase 12 exact configuration confirmation precedes Phase 13 deployment; still requires authorized private account reads and disclosure minimization |

## Decisive package-level findings

**AI Runway AKS setup.** Azure and Microsoft exposures share package tree `72ec58c0a7c574dc71e14c63feb3d2aa529849ac`, SKILL.md blob `26bbd92815116826696fb6380d37446a285496b9`. The root explicitly asks for confirmation before *install or deployment*, and step-2, step-4 and step-5 preserve that positive-action gate. But bundled `references/troubleshooting.md` (blob `643f00b50c1f317cd6a81f1f35d0bce9859914dd`) supplies `kubectl delete modeldeployment`, `kubectl delete secret hf-token`, `make undeploy` and controller uninstall commands as rollback without a fresh resource/cluster/destructive-action approval. Those operations can destroy a persistent deployment, secret or shared controller. The root's install/deploy confirmation does not cover deletion. The already-rejected Microsoft Skills companion accurately captured this hard fail; Azure's VERIFIED record was an inconsistent mirror. Preserve staged GPU checks, cost warning, provider sizing, non-echoed terminal token handling and readiness diagnostics for ADAPT/EXTRACT/CHECKLIST. Behavioral validation not-run.

**Azure Cloud Migrate.** Both exposures share package tree `dd0d5a31e87576d5b46899b19aa3eedb24d412f4`, SKILL.md blob `b1634cf629d9358eb70a95c089b309c304f9c42c`. Root assessment-before-migration, separate output directory and explicit test-vs-deploy handoff are valuable but do not eliminate the actionable bundled deployment instructions. `references/services/container-apps/cloudrun-to-container-apps.md` and `fargate-to-container-apps.md` direct image pushes and cloud deployment, linking the actual deployment guides. The Cloud Run deployment guide (blob `29c8094da61eacf61a9416884ea76db3cebe186b`) creates resource groups, Log Analytics, networks, Key Vault, managed identity, RBAC grants, external ingress and Container Apps, reads a Log Analytics primary shared key, and passes a GCP secret as a CLI argument. The Fargate guide (blob `83453d6eb4fc413a68cea8332b51e0ebe90557a6`) improves some credential handling but still provisions and grants access without mandatory exact-action approval. The Kubernetes scenario additionally instructs exporting `secret` objects to YAML without a separate disclosure/redaction gate. Functions and App Service global rules require confirmation for some destructive or deployment operations, but they do not provide a universal authorization and secret-custody boundary for all Container Apps paths. The Microsoft Skills companion was already REJECT unchanged 9/20; the Azure VERIFIED record incorrectly ignored the complete bundled tree. Preserve service mapping, assessment, source preservation, conversion and staged handoff as prior art, not unchanged execution authority. Behavioral validation not-run.

## Systemic synthesis

- **Mirrored-source contradiction:** identical package-tree identities had opposite unchanged-use decisions. Shared evidence can be reused only when complete-package scope and the resulting disposition agree. The previous Azure high-authority macro incorrectly preserved both despite already-rejected Microsoft companions.
- **Authority cluster:** an approval to install or deploy is not permission to delete; a high-level migration/deploy choice is not an approval for every resource, IAM role, network exposure, secret transfer and billable side effect.
- **Sensitive-data cluster:** cross-cloud secret transfer, log workspace keys and Kubernetes Secret YAML are not ordinary reportable diagnostics. Use approved secure external custody and minimum disclosure.
- **Capability differentiation:** generate-only RBAC, read-only capacity discovery and the explicitly gated Foundry customize path remain useful, subject to normal user-fit, package-security and privacy gates.
- **Freshness/overlap:** both source pins and their tree/blob fingerprints are unchanged. This is correction of semantic approval, not new upstream content or a behavioral qualification. No taxonomy vocabulary change is required.

## Accounting and lifecycle

- Azure Skills: **34/34 → 34/34**, static gaps **0 → 0**, VERIFIED **5 → 3**, REJECT unchanged **29 → 31**.
- Microsoft Skills: **186/186 → 186/186**, existing mirrored REJECT dispositions unchanged.
- **2** exact package decisions corrected in Azure exposure, **4** Azure provenance/verification companions refreshed; new exact-version review records **0**.
- Public inventory unchanged: **44 first-party, 848 third-party exact-version reviews, 892 total verification records**, admitted denominator delta **0**.
- Security and behavioral states remain unqualified/not-run; no source-owned package, pinned gitlink, executable repository machinery, license or source admission changed.
- All five public accounting surfaces are reconciled in this tranche. Existing draft PRs #489, #492, #496, #412, #413 remain separate exact-package security/adversarial acceptance holds.

**Next priority:** Obtain complete pinned external SkillSpector v2.12.0 reports and independently executed adversarial acceptance for the 36 changed first-party package trees, reconcile the shared registry, then merge only qualified drafts.
