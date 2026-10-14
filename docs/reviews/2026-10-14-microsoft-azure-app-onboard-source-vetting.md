# Microsoft Azure App Onboard: exact-version source vetting (2026-10-14)

**Status:** candidate-only static review, not canonical admission. **Disposition:** REJECT unchanged plugin/skill; ADAPT planning and approval-gate patterns. **Behavioral validation:** not-run. **Package-security scan:** not-run.

- Source: `microsoft/skills`, exact revision `fc164ba1d7a0c10377dbcc1c9ac07253b9329fdb`.
- Canonical package: `.github/plugins/azure-skills/skills/azure-app-onboard/`.
- Package tree: `ce62e3df0d860115631b3fb7658eb7a6c35cf141`; root SKILL.md blob: `00635c01fc9518e171e5157185a60999e1455b84`.
- 68 package blobs examined; three nested phase SKILL.md documents lack first-class frontmatter and remain supporting references, not separate eligible skills.
- License: MIT at exact plugin LICENSE blob `356b112bcc4f07e03b6e57569eedf9d79978d2d5`. Source-owned shell/PowerShell scripts are upstream evidence, not skillz-owned runtime.
- Purpose: Azure app architecture, cost planning, IaC generation, and deployment. Trigger: user requests Azure app onboarding or migration; non-trigger: isolated cost optimization, azd deployment, existing AKS operations.
- Dependencies: Azure CLI, Azure MCP, optional subagents, Bicep/Terraform, Key Vault, session artifacts, shell/PowerShell conformance scripts, shared Azure plugin hooks. Portability: low.
- Controlled tags: use_case=[cloud,deployment,planning,security], lifecycle=[planning,design,implementation,release], characteristic=[evidence-first,risk-aware,orchestration], authority=[mutating,external-side-effect], portability=[low].
- Static rubric: trigger precision 2, procedural clarity 2, authority safety 0, failure handling 1, evidence discipline 1, dependency coherence 2, portability honesty 1, differentiation 2, adversarial resilience 0, effectiveness design 1 = **12/20**.

## Decisive findings

1. **Authorization hard fail: automatic deletion.** `references/session-protocol.md:23` and `references/pipeline-rules.md:59` require deletion of non-active session folders older than seven days without separate destructive-action authorization. These folders can contain user prompts, identity, and deployment credentials.
2. **Credential-handling contradictions.** `deploy/references/blocked-patterns.md:26-27` prohibits inline secrets and temporary secret files; `deploy/references/deploy-safety.md:38` requires a plaintext `deploy-secrets.env` cache; `references/pipeline-rules-runtime.md:17,29` prescribes temporary secret files or inline generation; `deploy/references/code-deployment-container-apps.md:49,86-89` passes secrets via CLI arguments. Gitignore does not make plaintext persistence secure. Do not endorse unchanged handling.
3. **Destructive local temp path.** `deploy/references/code-deployment-swa.md:25,27` unconditionally removes `C:\\temp\\swa-deploy` or `/tmp/swa-deploy` without proving the directory is owned by this invocation.
4. **Broad database network access.** `scaffold/references/bicep-patterns-data.md:33-37,75-79` emits 0.0.0.0 Azure-service firewall rules. `references/approval-gates.md:27` does explicitly disclose this and treats a user Yes as consent; therefore the concern is an unsafe default and incomplete least-privilege design, not an absence of any disclosure.
5. **SCM policy drift.** `scaffold/references/bicep-app-service.md:54` requires SCM basic publishing auth enabled in IaC, while `deploy/SKILL.md:51` disables it imperatively after deployment. Subsequent IaC reconciliation may re-enable it. Model secure post-deploy desired state.
6. **Unreliable audit evidence.** `deploy/references/deploy-checklist-template.md:90` says to reconstruct missing deploy-audit.log entries from memory. Never present reconstructed evidence as observed execution.
7. **Unapproved diagnostic writes.** `deploy/references/health-check-patterns.md:93` recommends a database read/write route without an independent safe-test-data boundary.
8. **Shared plugin execution.** The Azure plugin's SessionStart/PostToolUse telemetry hooks invoke unpinned `npx -y @azure/mcp@latest`; unchanged plugin installation is not authorized by static source vetting.

## Preserve through adaptation

Separate scaffold and deploy approval gates with visible subscription/RG/region/cost, explicit what-if previews, evidence-first service mapping, quota checks, health verification beyond HTTP 200, resource-group deletion prohibition, and phase-scoped state. Remove auto-pruning, unsafe secret handling, unowned temp deletion, misleading audit reconstruction, and default broad network access before any unchanged recommendation.

**Accounting:** no new admissions; Microsoft registered 186/186 at July pin; no pin advancement; no canonical verification promotion; five public accounting surfaces unchanged.
