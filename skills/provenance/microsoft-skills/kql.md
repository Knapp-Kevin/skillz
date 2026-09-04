# Provenance: Microsoft Skills `kql`

- Source family: `microsoft-skills`
- Canonical source: `microsoft/skills`
- Canonical path: `.github/skills/kql`
- Registered source revision: `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`
- Package tree: `2dcd3bc9c947fd36356d5b91cc7d88841c9ce0c6`
- `SKILL.md` blob: `8be2bdeebd4cdfa0937d3457e70128042cd34904`
- Package contents: `SKILL.md` plus four bundled references: `advanced-patterns.md`, `discovery-queries.md`, `error-recovery.md`, and `query-templates.md`.
- Skill-path freshness evidence: `e7457389248c42433c940c3e497e2ee6c37604d4` (2026-04-15), converting remaining examples to public help-cluster data and recording live upstream query testing.
- License/terms: MIT, inherited from the registered Microsoft Skills source repository.

## Purpose and source context

`kql` is a static Kusto Query Language expertise package for writing, reviewing, debugging, and optimizing KQL across Azure Data Explorer, Fabric Real-Time Intelligence/EventHouse, Log Analytics, Sentinel, and related Kusto-backed systems. It emphasizes type discipline, joins, regex, serialization, memory/result-size safeguards, datetime handling, discovery, troubleshooting, and advanced geo/vector/graph/time-series patterns.

The package is preserved at the registered pin as third-party reference evidence. Upstream execution or testing claims are source provenance only and are not behavioral-validation evidence produced by `skillz`.

## Dependencies and authority profile

The skill itself requires no repository-owned runtime. Applying it against a live Kusto-backed environment requires an external authorized query surface and appropriate access to the target cluster/database. Most examples are read-only queries or `.show` discovery/diagnostic management commands, but even read-only execution can consume compute and disclose schema, principals, connection strings, operational diagnostics, logs, or other sensitive tenant data. The host agent must therefore scope target, authority, result size, and disclosure before live execution.
