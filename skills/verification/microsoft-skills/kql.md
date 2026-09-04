# Verification: Microsoft Skills `kql`

- Source family: `microsoft-skills`
- Canonical path: `.github/skills/kql`
- Registered source revision: `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`
- Package tree: `2dcd3bc9c947fd36356d5b91cc7d88841c9ce0c6`
- `SKILL.md` blob: `8be2bdeebd4cdfa0937d3457e70128042cd34904`
- Static disposition: **rejected unchanged**
- Score: **15/20**
- Behavioral validation: **not-run**
- Controlled tags: `data`, `analysis`, `debugging`, `performance`, `security`

## Structured semantic review

### Useful material to preserve

The package is unusually strong KQL reference material. It gives explicit trigger boundaries, query-vs-management-plane distinctions, dynamic-type casting rules, join-cardinality checks, serialization requirements, memory-safe filtering, result-size discipline, datetime corrections, self-correction mappings, and reusable advanced patterns. Its public help-cluster examples materially improve reproducibility and reduce dependence on private tenant data for learning and syntax checks.

The bundled discovery and troubleshooting material also provides useful static checklists for schema inspection, ingestion failures, capacity, workload groups, and operational diagnostics.

### Authority and sensitive-data hard fail

Unchanged adoption fails the current authority and sensitive-data standard because the skill repeatedly frames live execution as the default behavior without a mandatory authorization boundary before querying a target environment. The package explicitly says to execute queries, inspect schemas, and iterate automatically, and its discovery reference includes commands that can expose database/table principals, external-table `ConnectionStrings`, current identity, running queries, completed commands, administrative operations, ingestion-failure details, and workload-group configuration.

Those operations may be read-only, but read-only is not authority-free. They can consume production compute and disclose credentials or credential-bearing connection strings, identity/access data, operational metadata, logs, and other sensitive tenant information. The package does not require target authorization, data-minimization, redaction, or an explicit sensitive-disclosure boundary before returning such results. `ConnectionStrings` is particularly problematic because the reference projects it directly from `.show external tables` rather than instructing the agent to omit or redact credential-bearing fields.

No unchanged-adoption approval is therefore justified. Preserve the language mechanics, safety/performance patterns, public help-cluster examples, and read-only diagnostic checklists as adaptation/reference evidence. Any host-agent adaptation should default to public/synthetic data where possible, require explicit authority for live tenant execution, avoid credential-bearing fields, minimize sensitive result sets, and separate query generation/review from execution.

## Portability

High for query authoring/review and public help-cluster examples. Medium for live execution because available commands, permissions, engine variants, data schemas, and tenant sensitivity differ across ADX, Fabric, Log Analytics, Sentinel, and related Kusto surfaces.

## Validation note

The upstream package states that its marked examples were tested against Microsoft's public help cluster. That is useful source evidence, not behavioral validation performed or witnessed by this repository. `skillz` records behavioral validation as `not-run`.
