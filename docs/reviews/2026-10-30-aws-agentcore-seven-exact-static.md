# AWS AgentCore seven-package exact-version static review (2026-10-30)

## Live source macro map

Registered AWS source: `aws/agent-toolkit-for-aws@ff1481a7bc1a04ee00ebf63d3a8a149aa6a2c546`, Apache-2.0 root license. Exact pinned recursive tree: **115** front-mattered SKILL.md exposure paths, **93** distinct skill names, **94** distinct package-tree identities. Duplicate mirrors collapse by exact tree; the plugin `aws-cdk` variant is materially distinct from the core package. Before this tranche **85/94** had companion pairs and **9** were genuine gaps: seven `plugins/aws-agents/skills/` AgentCore packages, `signing-in-to-aws`, and divergent plugin `aws-cdk`. This tranche resolves all seven AgentCore identities: **85/94 → 92/94**, **9 → 2** gaps; denominator unchanged.

All seven AgentCore manifests declare `aws-agentcore` and AgentCore CLI >=0.9.0. Each package has its own exact tree, manifest SHA and bundled dependency characterization. Root Apache-2.0 terms apply. Package-specific last-modified date was not established; pin is fixed, but AWS APIs, CLI behavior, regional availability and prices are volatile. These are static semantic decisions only, not package-security scans or behavioral passes.

## Individual exact-version dispositions

| Skill | Package tree | Manifest blob | Score | Decision |
|---|---|---|---:|---|
| `agents-build` | `a7c7cfc787cecf4dc7a20fd2e61540e6263ddc3e` | `3ec11ae8faaee5f33b2afbb80324c3b3e8c70c40` | 12/20 | REJECT unchanged |
| `agents-connect` | `d92b447658b287aaab5c91e04e910d8947c4ddef` | `0790cd87460eba885c66686d965c9f4d4991addb` | 13/20 | REJECT unchanged |
| `agents-debug` | `15df718425a2d246c9b517022f8cad98133aa647` | `6607ec6c6c689f457e9a31463faf563538d7e72b` | 14/20 | REJECT unchanged |
| `agents-deploy` | `821a52c3717b9cf6bab0a9741d7bd732992a558d` | `5cee1ceb11f57e7a97a48216a377336cb3fc2886` | 13/20 | REJECT unchanged |
| `agents-get-started` | `9a732edf9c0b65e14871bc3d293b4985cfaa6635` | `446f4171600406254530fd50ad65c56240d10303` | 15/20 | REJECT unchanged |
| `agents-harden` | `4da687d992a44da500a6b0b74b6a1ece4c5d260f` | `8c7ec90edc8de1ece219a9257144914ef26dbd1c` | 13/20 | REJECT unchanged |
| `agents-optimize` | `383f5d9466653d935ff645fbe9ecab2491775f3d` | `f18f0c53ea71ea71e58ee43e1468d40504889da3` | 14/20 | REJECT unchanged |

### agents-build

**Use/non-use:** Add capabilities to an existing AgentCore project; not new project scaffolding, external Gateway connection, or basic deployment diagnosis.

**Bundled dependencies:** AgentCore CLI >=0.9.0, AWS account/Bedrock permissions, memory/Gateway/VPC/identity resources, 11 bundled references and two upstream payment helper scripts, payment provider and x402 services.

**Authority and decision:** Top-level routing delegates to payment and teardown references. Payment reference says run provisioning, deploy, instrument/session setup and testing automatically with only connector-secret and wallet-funding pauses; teardown directs resource removals, deploy -y and optional CloudWatch log-group deletion. No independent exact account/resource/cost/destructive authority for these actions. Preserve reference routing, memory patterns, session controls and budget concepts for adaptation.

**Evidence:** Exact pinned package tree `a7c7cfc787cecf4dc7a20fd2e61540e6263ddc3e`, manifest `3ec11ae8faaee5f33b2afbb80324c3b3e8c70c40`; individual provenance and verification companions persisted. Semantic REJECT unchanged 12/20, behavioral `not-run`, no full pinned package-security scan. Source-owned reference files and helper scripts remain intact.

### agents-connect

**Use/non-use:** Connect an existing AgentCore agent to external services via Gateway or credential providers; not project scaffolding or general production hardening.

**Bundled dependencies:** AgentCore CLI >=0.9.0, AWS Gateway/Identity/IAM and Lambda, OAuth/API-key providers, MCP/OpenAPI/Smithy targets, project config, bundled policy reference.

**Authority and decision:** Offers gateway-target and credential creation followed by agentcore deploy -y without independent account/resource/endpoint authorization. Examples include --api-key and --client-secret literal command-line patterns despite later shell-history warnings and a safer interactive path. Target registration can expose external APIs and persistent cloud resources; require secure credential entry and explicit target/deploy authority. Retain Gateway-first and auth-type distinction as extraction.

**Evidence:** Exact pinned package tree `d92b447658b287aaab5c91e04e910d8947c4ddef`, manifest `0790cd87460eba885c66686d965c9f4d4991addb`; individual provenance and verification companions persisted. Semantic REJECT unchanged 13/20, behavioral `not-run`, no full pinned package-security scan. Source-owned reference files and helper scripts remain intact.

### agents-debug

**Use/non-use:** Diagnose broken AgentCore agents, tool failures, logs/traces and local CLI issues; not new deployment, proactive optimization or VPC design.

**Bundled dependencies:** AgentCore CLI >=0.9.0, AWS CloudWatch/X-Ray/Bedrock and IAM, agent logs and traces, local project files, bundled doctor reference.

**Authority and decision:** Step 3 says to read CloudWatch traces and logs automatically rather than request pasted logs, with no explicit AWS account, runtime, time window, sensitive field or disclosure authorization. Traces can expose model reasoning, tool arguments and private user data. Remediation suggestions include config edits and redeployment without a distinct write/deploy gate. Retain diagnostic decision trees and trace timing caveats as checklist input.

**Evidence:** Exact pinned package tree `15df718425a2d246c9b517022f8cad98133aa647`, manifest `6607ec6c6c689f457e9a31463faf563538d7e72b`; individual provenance and verification companions persisted. Semantic REJECT unchanged 14/20, behavioral `not-run`, no full pinned package-security scan. Source-owned reference files and helper scripts remain intact.

### agents-deploy

**Use/non-use:** Preflight, deploy, diagnose deployment failures, or version/rollback an existing AgentCore project; not new project scaffolding or security hardening.

**Bundled dependencies:** AgentCore CLI >=0.9.0, AWS CLI, CDK/CloudFormation, ECR, IAM, deployment target accounts, bundled versioning reference.

**Authority and decision:** Preflight and CDK diff are useful, but the run-deploy path gives agentcore deploy -y including staging/production without a separate action-specific account, environment, resource, cost and traffic authorization boundary. IAM permission repair and rollback references also affect persistent cloud state. Auto-confirm bypasses the CLI confirmation; preview is not consent. Retain dry-run/diff and region checks as checklist.

**Evidence:** Exact pinned package tree `821a52c3717b9cf6bab0a9741d7bd732992a558d`, manifest `5cee1ceb11f57e7a97a48216a377336cb3fc2886`; individual provenance and verification companions persisted. Semantic REJECT unchanged 13/20, behavioral `not-run`, no full pinned package-security scan. Source-owned reference files and helper scripts remain intact.

### agents-get-started

**Use/non-use:** Scaffold a new AgentCore project and guide first local run/deploy; not adding capabilities to an existing project or debugging prerequisites.

**Bundled dependencies:** AgentCore CLI >=0.9.0, AWS account/Bedrock model access, Strands/LangGraph/GoogleADK/OpenAI Agents, local development server, optional ECR/CDK and bundled support-agent example.

**Authority and decision:** Scaffold command is explicitly presented for developer confirmation, a meaningful local-write safeguard. But the later first-deploy flow advances from general project creation to paid AWS ECR/CDK/runtime provisioning and first invocation without a separately scoped account/region/resource/cost authorization gate; generic CLI preview/confirmation is not a complete host action boundary. The local dev server can call configured remote model providers. Retain framework selection, name validation and scaffold preview for adaptation.

**Evidence:** Exact pinned package tree `9a732edf9c0b65e14871bc3d293b4985cfaa6635`, manifest `446f4171600406254530fd50ad65c56240d10303`; individual provenance and verification companions persisted. Semantic REJECT unchanged 15/20, behavioral `not-run`, no full pinned package-security scan. Source-owned reference files and helper scripts remain intact.

### agents-harden

**Use/non-use:** Audit and harden production AgentCore security, auth, quotas, sessions and observability; not outbound credential wiring or general quality tuning.

**Bundled dependencies:** AgentCore CLI >=0.9.0, AWS IAM/EventBridge/CloudWatch/AgentCore APIs, JWT/OIDC identity provider, Secrets Manager, bundled limits reference.

**Authority and decision:** A production checklist proceeds to IAM/auth changes, EventBridge alert rule creation, CloudWatch log retention mutation, online evaluator creation and agentcore deploy -y without independent resource, recipient, telemetry, cost and change-window approval. It suggests decoding a sample JWT at jwt.io without explicitly prohibiting live token disclosure to a third-party site. Strong least-privilege and credential guidance is extractable, not unchanged safe.

**Evidence:** Exact pinned package tree `4da687d992a44da500a6b0b74b6a1ece4c5d260f`, manifest `8c7ec90edc8de1ece219a9257144914ef26dbd1c`; individual provenance and verification companions persisted. Semantic REJECT unchanged 13/20, behavioral `not-run`, no full pinned package-security scan. Source-owned reference files and helper scripts remain intact.

### agents-optimize

**Use/non-use:** Measure agent quality, configure evaluation/online monitoring, observability and cost analysis; not broken-agent debugging or production IAM hardening.

**Bundled dependencies:** AgentCore CLI >=0.9.0, AWS CloudWatch/X-Ray/Bedrock evaluation, OTEL traces, online evaluators and bundled evals/observability/cost references.

**Authority and decision:** Top-level skill delegates to eval and observability references; eval path can enable account-wide CloudWatch Transaction Search, add persistent online evaluators and deploy -y, transmitting potentially sensitive production traces with added evaluation cost. No independent account/data/retention/sampling/cost and deployment authorization before these side effects. Retain 1–5% sampling guidance and evaluation fixture discipline for adaptation.

**Evidence:** Exact pinned package tree `383f5d9466653d935ff645fbe9ecab2491775f3d`, manifest `f18f0c53ea71ea71e58ee43e1468d40504889da3`; individual provenance and verification companions persisted. Semantic REJECT unchanged 14/20, behavioral `not-run`, no full pinned package-security scan. Source-owned reference files and helper scripts remain intact.

## Cross-package synthesis

- **Delegated authority:** `agents-build` routes to payment and teardown references; `agents-optimize` routes to eval/observability references. The parent intent cannot authorize child provisioning, paid transactions, destructive cleanup, telemetry export, or persistent monitoring by implication.
- **High-consequence operations:** `agents-deploy` and several reference flows use `agentcore deploy -y`; `agents-harden` recommends IAM, EventBridge and retention mutations. A preview, available AWS credentials, or the fact a change is protective is not a scoped action authorization.
- **Sensitive data:** `agents-debug` reads production logs/traces automatically; `agents-optimize` exports traces/evaluation data. These may contain prompts, tool arguments, identifiers and private business data. `agents-connect` includes command-line credential examples that can leak into shell history despite subsequent warnings; `agents-harden` mentions third-party JWT decoding without a live-token disclosure prohibition.
- **Useful differentiated methods:** routing among build/connect/debug/deploy/get-started/harden/optimize, CLI version/name checks, CDK dry-run/diff, Gateway-first credential isolation, least-privilege IAM, session lifecycle management, evaluation fixtures and sampling, and payment budget concepts are worth ADAPT/EXTRACT/CHECKLIST use. Rejection is not a claim of zero value.
- **Source-family value:** the seven packages form a coherent AgentCore lifecycle reference, but unchanged host execution is unsafe without additional authorization, private-data and cost boundaries. Low portability reflects AWS/AgentCore CLI and service dependencies, not source-owned runtime in `skillz`.
- **Remaining omissions:** `plugins/aws-core/skills/signing-in-to-aws` (also mirrored at core path, identical package tree) and materially divergent `plugins/aws-core/skills/aws-cdk` remain two genuine unreviewed identities. No new discovery/source admission this tranche.

## Lifecycle and accounting

All seven exact-version records are new, each with its own score, authority profile, controlled tags, dependency description and explicit `validation_status: not-run`. AWS **92/94**, 2 gaps. Published first-party **44** unchanged; third-party exact-version companions **839 → 846**, total verification records **883 → 890**. Reconciled README, SYSTEM_STATE, CURATION_QUEUE, INDEX, index.json and registry/sources.yaml together. No source pin/package/license mutation, no scanner or behavioral execution, no repository-owned automation.

Existing draft PRs #489/#492/#496 remain qualification-blocked for 36 changed first-party package trees; #412/#413 remain separate admission holds. No draft is ready for merge solely from mergeability or empty checks. Existing seven open issues remain linked to unresolved first-party security/authority acceptance; none is closed by this AWS static tranche.

**Next:** review the two remaining AWS identities, deeply inspecting credential/SSO boundaries and the divergent CDK reference tree, then reconcile five public surfaces on closure.
