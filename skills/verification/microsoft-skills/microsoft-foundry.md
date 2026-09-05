# Verification: Microsoft Skills `microsoft-foundry`

- Source family: `microsoft-skills`
- Canonical path: `.github/plugins/azure-skills/skills/microsoft-foundry`
- Registered source revision: `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`
- Package tree: `75f1fef94394b6ffde32259d0268f2d3381938dc`
- `SKILL.md` blob: `49fe35776ef5ae8d8c028b8f28d5d11b00a47df2`
- Static disposition: **rejected unchanged**
- Score: **13/20**
- Behavioral validation: **not-run**
- Controlled tags: `agent-development`, `cloud`, `deployment`, `orchestration`, `operations`, `production-oriented`, `risk-aware`, `tool-routing`, `mutating`, `external-side-effect`, `low`

## Structured semantic review

### Useful material to preserve

The root orchestrator has strong routing and context-resolution prior art. It requires workflow-specific sub-skill loading, distinguishes hosted/prompt agents and public/private infrastructure paths, resolves agent roots before scanning, avoids sibling-folder scope creep, layers explicit user input over `azd` context and metadata overlays, treats `eval.yaml` as intent rather than proof of remote state, stops on conflicting configuration sources, avoids duplicating `azd`-owned deployment values, and asks before refreshing or overwriting local cache material.

The package also reflects a deliberate freshness strategy. Microsoft restructured the Foundry plugin toward language-agnostic concepts plus live discovery, and the registered pin carries the later `1.1.33` hosted-agent/`azd` contract update. Preserve the router, scope partitioning, configuration precedence, remote-state verification, review-before-overwrite, and concepts-to-live-discovery mechanisms as adaptation/reference evidence.

### Authority hard fail

Unchanged adoption fails the current authority standard. The root routes directly into workflows that provision Foundry projects/resources, deploy models and agents, alter RBAC and identities, request/manage quota, modify local `.foundry` metadata/cache state, optimize/apply candidates, and perform other persistent Azure and workspace mutations. Some branches contain useful review or user-choice gates, but the package does not impose a mandatory action-specific authorization checkpoint immediately before every consequential mutation. A broad request to work on Foundry is not sufficient authorization for each deployment, role assignment, infrastructure creation, overwrite, or destructive lifecycle action.

This is therefore valuable operational prior art, not safe unchanged procedure under the current hard-fail rule.

### Secret and sensitive-data discipline

The root resolves deployment context that can include `APPLICATIONINSIGHTS_CONNECTION_STRING`, and routes to trace, evaluation, dataset, monitoring, and optimization workflows involving production telemetry and model/agent content. The root does not establish a universal disclosure/minimization boundary before potentially sensitive trace, dataset, prompt, or telemetry material is transmitted to external Foundry services or persisted into local/remote evaluation assets. Any adaptation must keep credential-bearing values out of conversational output/logs and require explicit authority plus data minimization for production-derived content.

### Trigger and non-trigger boundary

Use as reference when orchestrating Microsoft Foundry project/resource, model, agent, evaluation, quota, RBAC, networking, or fine-tuning work and when designing multi-workflow routing with strong context resolution. Do not use unchanged for general Azure deployment, non-Foundry workloads, or as authorization to create/update Azure resources, permissions, deployments, local metadata, evaluation datasets, or other persistent state.

## Portability

Low unchanged portability. The orchestration structure and context-resolution patterns generalize, but the operational package is tightly coupled to Foundry/Azure MCP, `azd`, Azure CLI, Microsoft identity/resource concepts, and fast-moving preview contracts.

## Validation note

This review inspected the exact registered-pin root package and relevant bundled workflow behavior statically. No Azure/Foundry command, MCP operation, script, deployment, resource mutation, identity/RBAC change, trace query, evaluation, fine-tuning job, or local workspace mutation was executed. No representative external behavioral/adversarial evidence was produced, so behavioral validation remains `not-run`.