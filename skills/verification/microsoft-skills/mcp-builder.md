# Verification: Microsoft Skills `mcp-builder`

- Source family: `microsoft-skills`
- Canonical path: `.github/skills/mcp-builder`
- Registered source revision: `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`
- Package tree: `c87383e3a3a307ff9867adf610672e9f0b24687b`
- `SKILL.md` blob: `792635390fff9f4c0032b1f0e06db1d81affe678`
- Static disposition: **rejected unchanged**
- Score: **14/20**
- Behavioral validation: **not-run**
- Controlled tags: `agent-development`, `api-design`, `architecture`, `implementation`, `security`, `contract-first`, `safety-bounded`, `tool-assisted`

## Structured semantic review

### Useful material to preserve

The package contains strong MCP design prior art: build-vs-reuse guidance, tool naming/discoverability rules, input and output schemas, pagination and bounded-result discipline, transport selection, actionable errors, authentication patterns, DNS-rebinding protection, tool annotations, approval-mode examples, and explicit reminders that annotations are hints rather than security guarantees. Its evaluation guidance correctly constrains benchmark questions to read-only/non-destructive operations and encourages small paginated exploration rather than indiscriminate bulk retrieval.

The Microsoft-specific reference also usefully distinguishes local and remote servers, documents managed identity/OBO patterns, and shows client-side approval controls for destructive tools. Preserve those mechanisms for adaptation and secure MCP design.

### Authority and sensitive-data hard fail

Unchanged adoption fails the current authority and sensitive-data standard because consequential operations are presented as executable workflow steps without mandatory action-specific authorization boundaries. The package instructs dependency installation (`pip install`, `npx`/tool installation), project mutation, local server execution, `azd init`, and `azd up` deployment. Its Azure examples include create, upload, delete, secret, and other mutating tool shapes. General annotations, warnings, or optional client approval configuration do not themselves establish authorization for each consequential action.

The bundled evaluation harness is a separate hard fail. `scripts/evaluation.py` sends MCP tool outputs back to the Anthropic API as `tool_result` content. Evaluation tasks are intentionally based on real service content and may traverse users, messages, files, repositories, operational data, or other tenant information. The package does not require an explicit disclosure authorization, data-minimization/redaction step, or sensitive-data classification before forwarding those raw tool results to a third-party model provider. It also accepts bearer-token headers and environment variables at invocation time, which should be handled through secure credential paths and never surfaced into conversational context or logs.

No unchanged-adoption approval is therefore justified. A safe adaptation should separate design/code generation from execution, require explicit authorization immediately before installs, deployments, live mutations, or sensitive reads, keep credentials out of prompts/logs, and require disclosure authority plus minimization/redaction before any evaluation forwards live tool-returned data to an external model.

## Portability

High for MCP architecture, tool-design, schema, pagination, and transport guidance. Medium for implementation because examples depend on TypeScript/Python/.NET SDKs and host tooling. Low-to-medium for the bundled evaluation/deployment procedures because they depend on external credentials, Anthropic API access, live MCP targets, and Azure-specific tooling.

## Validation note

The package contains upstream scripts, acceptance criteria, and testing/evaluation instructions, but this review did not execute them. Upstream testing evidence is provenance/context only. `skillz` records behavioral validation as `not-run`.
