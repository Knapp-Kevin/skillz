# Provenance: Microsoft Skills `microsoft-foundry`

- Source family: `microsoft-skills`
- Source repository: `https://github.com/microsoft/skills`
- Source class: official Microsoft
- License: MIT
- Registered source revision: `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`
- Canonical package path: `.github/plugins/azure-skills/skills/microsoft-foundry`
- Canonical `SKILL.md`: `.github/plugins/azure-skills/skills/microsoft-foundry/SKILL.md`
- Package tree: `75f1fef94394b6ffde32259d0268f2d3381938dc`
- `SKILL.md` blob: `49fe35776ef5ae8d8c028b8f28d5d11b00a47df2`
- Plugin mirror path: `.github/plugins/microsoft-foundry/skills/microsoft-foundry`
- Mirror relationship: symlink to `../../azure-skills/skills/microsoft-foundry`; not an independent eligible skill
- Freshness evidence: registered pin `32cad4ee689c95c309e61aeefcbc6af356f1e6a7` updates this skill to metadata version `1.1.33` and synchronizes the latest hosted-agent creation/`azd` contract; the earlier major language-agnostic restructure landed in `c5b4c00929f2d81e64366b9a4d19faa1323c54c5` on 2026-05-04
- Behavioral validation: `not-run`

## Package identity and boundary

`microsoft-foundry` is a first-class, front-mattered orchestrator skill. Its package is not just the root `SKILL.md`: the canonical tree includes nested first-class sub-skills such as `finetuning/SKILL.md`, Foundry agent workflows, model/project/quota/RBAC/resource material, references, and bundled scripts. Those nested independently front-mattered skills remain separate denominator entries where applicable; this companion binds only the root `microsoft-foundry` entry point while preserving the complete canonical package context.

The `microsoft-foundry` plugin exposes this same canonical skill through a symlink. That duplicate exposure path does not create a second eligible identity.

## Purpose and dependencies

The root skill is a Foundry orchestration/router procedure for project/resource creation, model deployment, hosted and prompt agents, evaluation/optimization, traces, troubleshooting, RBAC, quota, private networking, and fine-tuning. It depends on its bundled sub-skill/reference tree for workflow-specific instructions and, operationally, may route an external host to Azure/Foundry MCP tools, `azd`, `az`, SDKs, local workspace files, and Azure resources.

Its package intentionally contains upstream scripts and operational helpers. Those are Microsoft package evidence, not repository-owned `skillz` runtime.

## Authority and portability

Authority profile: **mutating + external-side-effect**. Workflows can create or alter local agent workspaces, metadata, Azure resources, role assignments, model/agent deployments, evaluation assets, and other persistent state. Some branches include explicit review/choice gates, but the root package does not establish a universal mandatory action-specific authorization boundary for every consequential mutation.

Portability: **low** for unchanged operational use because the package is deeply coupled to Microsoft Foundry/Azure tooling, identities, resources, and current preview contracts. Its routing, context-resolution, metadata-layering, freshness, and review patterns remain useful adaptation/reference evidence elsewhere.

## Secret and sensitive-data context

The root skill resolves Azure environment and deployment context, including an Application Insights connection string, and routes into trace/evaluation/dataset workflows. Any host adaptation must keep credentials out of conversational output/logging and require explicit authority plus minimization before transmitting or persisting production traces, datasets, prompts, telemetry, or other potentially sensitive content.