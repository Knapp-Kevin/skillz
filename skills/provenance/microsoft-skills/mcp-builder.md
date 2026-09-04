# Provenance: Microsoft Skills `mcp-builder`

- Source family: `microsoft-skills`
- Canonical source: `microsoft/skills`
- Canonical path: `.github/skills/mcp-builder`
- Registered source revision: `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`
- Package tree: `c87383e3a3a307ff9867adf610672e9f0b24687b`
- `SKILL.md` blob: `792635390fff9f4c0032b1f0e06db1d81affe678`
- Package contents: 10 files: `SKILL.md`; five bundled references (`evaluation.md`, `mcp_best_practices.md`, `microsoft_mcp_patterns.md`, `node_mcp_server.md`, `python_mcp_server.md`); and four bundled script/support files (`connections.py`, `evaluation.py`, `example_evaluation.xml`, `requirements.txt`).
- Skill-path freshness evidence: `e1f9cce11758d305e6c77683fe34ccc394586291` (2026-04-20), which moved acceptance criteria out of the skill package into the repository test surface and therefore defines the latest package-boundary change before the registered pin.
- License/terms: MIT, inherited from the registered Microsoft Skills source repository.

## Purpose and source context

`mcp-builder` is a cross-language MCP server design and implementation package covering TypeScript, Python, and C#/.NET. It combines protocol/framework research, API/tool design, schemas, pagination, transport selection, authentication, security guidance, Microsoft/Azure MCP patterns, implementation examples, testing, and evaluation construction.

The package is preserved intact at the registered pin as third-party reference evidence. Its bundled scripts and upstream evaluation/test claims remain upstream package material; they are not repository-owned runtime and do not constitute behavioral validation performed by `skillz`.

## Dependencies and authority profile

The static guidance is portable, but applying the package can mutate a target codebase, install local dependencies, launch local or remote MCP servers, authenticate to external services, deploy Azure resources, and invoke MCP tools against live data. The bundled evaluation harness uses the Anthropic API and forwards MCP tool results into model requests. Any unchanged use therefore requires explicit authority for target mutations, installs, deployments, credentials, live-service access, and third-party disclosure of tool-returned data. Secret-bearing headers/environment values must remain in secure external credential paths rather than conversational or logged context.
