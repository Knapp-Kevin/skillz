# Provenance: Microsoft Skills `microsoft-docs`

- Source family: `microsoft-skills`
- Canonical source: `microsoft/skills`
- Canonical path: `.github/skills/microsoft-docs`
- Registered source revision: `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`
- Package tree: `2e0eef527e4fafac394cca00144736954ecc9528`
- `SKILL.md` blob: `a5129731352a4dcad109b03e6f8e96bbdd00695b`
- Package contents: 1 file: `SKILL.md`.
- Skill-path freshness evidence: `c80e39837bb085dd852a900f2580b9351d111a92` (2026-03-31), which introduced the Microsoft Docs skill and is the latest path change before the registered pin.
- License/terms: MIT, inherited from the registered Microsoft Skills source repository.

## Purpose and source context

`microsoft-docs` is a retrieval-oriented Microsoft documentation skill. It routes conceptual, tutorial, configuration, quota, and best-practice questions to the Microsoft Learn MCP Server, with the `@microsoft/learn-cli` package as a fallback. It emphasizes specific version/task/platform-aware queries, search-before-fetch behavior, and bounded full-page retrieval when excerpts are insufficient.

The package is preserved intact at the registered pin as third-party reference evidence. Microsoft Learn MCP and CLI behavior are external capabilities of a host environment; they are not repository-owned runtime or behavioral validation performed by `skillz`.

## Dependencies and authority profile

The primary MCP search/fetch workflow is read-only and highly portable when the host already exposes the Microsoft Learn MCP tools. The fallback requires Node/npm access and may use `npx @microsoft/learn-cli`; the package also explicitly offers `npm install -g @microsoft/learn-cli`, which persistently mutates host tooling. Unchanged use therefore requires an action-specific authorization boundary before any global installation or other persistent host mutation. Documentation queries should also avoid placing secrets or private tenant data into external search requests when such disclosure is unnecessary.
