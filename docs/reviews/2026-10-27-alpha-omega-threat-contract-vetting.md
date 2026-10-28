# Alpha-Omega threat-model family: exact-revision candidate decision (2026-10-27)

**Issue:** [Candidate vetting: Alpha-Omega implicit security-contract threat-model skill family](https://github.com/Knapp-Kevin/skillz/issues/423). **Disposition: EXTRACT / REFERENCE-ONLY, no unchanged admission.** This is pre-admission source vetting, not a `verified` or `validated` governed corpus record. No tool was executed, no scanner ran, and no external behavioral evidence exists from this review.

## Wayfinder destination and evidence scope

[Wayfinder destination](https://github.com/Knapp-Kevin/skillz/issues/35): production-ready **passive** knowledge for an external host, with bounded authority and exact provenance. This decision resolves whether a differentiated eight-skill security-contract source should enter the governed corpus now. It does not create a `skillz` runtime, perform security triage, or authorize an agent to write to another repository.

- Canonical source: [alpha-omega-security/threat-model](https://github.com/alpha-omega-security/threat-model), publisher Alpha-Omega, observed HEAD **`192fd60cd0afe8851128ce4c68ed68c174c11948`**, rechecked 2026-10-27.
- Terms: root `LICENSE` blob `4eb87275c6cf70339d101368341a7ef04e489e19` is **MIT**, Copyright (c) 2026 Alpha-Omega. This establishes root terms; independently licensed nested components were not exhaustively audited. Nothing is copied or vendored.
- Exact denominator: **8 distinct first-class `skills/threat-model*/SKILL.md` manifests**, each with YAML frontmatter. The source `skills/README.md` names the orchestrator and seven specialists, and GitHub code search surfaced all eight matching manifests. The repeated orchestrator row in the phase table is **not a ninth skill**. Shared `references/*.md`, root `schema.json`, Python adapters, test harness, examples and generated documents are **dependencies/reference artifacts**, not independent first-class skills.
- Checked shared assets: `principles.md`, `output-structure.md`, `question-bank.md`, `sidecar-schema.md`, `json-report-schema.md`, `self-check.md`, `glossary.md`, `worked-example.md`, `schema.json`, `new_threat_model.py`, and `fetch_security_context.py` all exist at this revision. Their full dependency trees and exact package-tree hashes were **not** established.
- Freshness: source revision observed on 2026-10-27; this is not a commitment to follow future HEADs. Skill-specific last-change dates and complete package-tree identities remain unknown.
- **All eight:** `package_security_status: not-run`, `behavioral_validation_status: not-run`, `governed_semantic_status: not-admitted`. No package scanner reports, execution observations or individual governed companions were produced.

## Whole-family macro map

| Axis | Evidence and implication |
| --- | --- |
| Distinct mechanism | Models a project's *implicit security contract* rather than scanning for vulnerabilities: claimed/disclaimed properties, per-input-operand trust, side effects, source-backed assertions, maintainer question waves, historical report routing, and derived structured sidecars |
| Duplication | Partial overlap with `mcp-vetting`, `permissions-review`, `agent-postmortem`, and draft #412's `trust-boundary-review`. The contract-dimension matrix and false-closure-sensitive triage are meaningfully different, but do not warrant eight new first-party copies |
| Shared dependencies | All specialists refer to orchestrator-owned reference files. Standalone use still depends on these sibling references; extracting a single file without the contract would be misleading |
| Authority clusters | Recon/surface are read-only; interview can alter claims and draft state; authoring/backtest/sidecar/orchestrator write artifacts; triage makes consequential *advisory* security dispositions. Root batch runner clones targets, installs skills, invokes agents with broad permissions, and optionally gathers external security context |
| Privacy | Repository contents, private security findings, vulnerability corpora and draft security contracts may be sensitive. Public advisory retrieval is not permission to inspect private issues, copy secrets, publish an internal model, or send source content to a model/provider |
| Evidence | The source claims a test harness and historical backtests. These are upstream design/evaluation claims, **not** observed validation of these eight packages by this review |
| Operational fit | Strong reference methodology for security engineering, but high integration burden, large shared reference specification, source-specific schemas and a project-write/publish workflow |
| Freshness and license | MIT root inspected; exact observed revision pinned for this decision. No copy/redistribution and no automatic upgrade |
| Primary failure mode | Treating a request to *analyze* a repository, an available coding agent, or a configured output path as blanket authority to mutate project files, publish a model, run broad-permission automation, or close a vulnerability report |

## Individual exact-manifest static assessments

The ten-number rubric vector is in canonical `docs/skill-verification.md` order: **trigger / procedure / authority / failure / evidence / dependencies / portability / differentiation / adversarial resilience / effectiveness**, each 0–2. These are **pre-admission static characterizations**, not persisted `verified` companions. A score of 15+ cannot override an authority hard fail or a missing package-security gate.

| First-class skill | Exact `SKILL.md` Git blob | Rubric / 20 | Individual disposition and decisive rationale |
| --- | --- | --- | --- |
| [threat-model](https://github.com/alpha-omega-security/threat-model/blob/192fd60cd0afe8851128ce4c68ed68c174c11948/skills/threat-model/SKILL.md) | `e6462250f8dfabbafff908d825e8405878dbc9e0` | **15** (2/2/0/1/2/2/1/2/1/2) | **REJECT unchanged; EXTRACT** contract matrix and provenance method. Delegates all phases, writes three target-root artifacts and can publish an unratified draft after a waiting policy, without an action-specific host approval boundary for project writes/publication |
| [threat-model-recon](https://github.com/alpha-omega-security/threat-model/blob/192fd60cd0afe8851128ce4c68ed68c174c11948/skills/threat-model-recon/SKILL.md) | `40da707678b3092d3e2238eed435588ae006dbdc` | **18** (2/2/2/2/2/2/1/2/1/2) | **EXTRACT** exact released-ref orientation and maintainer-policy provenance. Explicit read-only scope and rejection of environment credential harvesting; still depends on orchestrator references and optional externally prefetched public history |
| [threat-model-surface](https://github.com/alpha-omega-security/threat-model/blob/192fd60cd0afe8851128ce4c68ed68c174c11948/skills/threat-model-surface/SKILL.md) | `0611fb21f2647a8b295944c414e053ecd57fd150` | **18** (2/2/2/1/2/2/1/2/2/2) | **EXTRACT** per-input trust, contract-dimension and no-surprise side-effect inventory. Explicitly read-only and bounded by in-scope components, but assumes deep authorized code access and shared specification |
| [threat-model-interview](https://github.com/alpha-omega-security/threat-model/blob/192fd60cd0afe8851128ce4c68ed68c174c11948/skills/threat-model-interview/SKILL.md) | `4a4013583ac21d5e6bdad6566af43b58be512c30` | **17** (2/2/1/2/2/2/1/2/1/2) | **ADAPT / EXTRACT** proposed-answer waves, maintainer ratification and unresolved-claim provenance. Must distinguish actual maintainer confirmation from inferred model answers and require approval before writing/publishing draft changes |
| [threat-model-authoring](https://github.com/alpha-omega-security/threat-model/blob/192fd60cd0afe8851128ce4c68ed68c174c11948/skills/threat-model-authoring/SKILL.md) | `3e7f520b9261a88a2b7b4ee02dfd30073e9dd06f` | **17** (2/2/0/2/2/2/1/2/2/2) | **REJECT unchanged; ADAPT** source-backed claim tags, unresolved security-critical guarantees and section discipline. Writes target documents without explicit action-specific target authorization |
| [threat-model-backtest](https://github.com/alpha-omega-security/threat-model/blob/192fd60cd0afe8851128ce4c68ed68c174c11948/skills/threat-model-backtest/SKILL.md) | `c304836c5038e89f88061443008d88eb6e47974f` | **17** (2/2/0/2/2/2/1/2/2/2) | **REJECT unchanged; EXTRACT** asymmetric false-closure gate, historical-versus-synthesized case labels and stratified coverage. Reads potentially sensitive findings and writes `.threat-model/backtest.md`; scoped access, artifact location and confidentiality must be approved before action |
| [threat-model-sidecar](https://github.com/alpha-omega-security/threat-model/blob/192fd60cd0afe8851128ce4c68ed68c174c11948/skills/threat-model-sidecar/SKILL.md) | `da41b887d4ff46de7537edaef4caf459d836a104` | **17** (2/2/0/2/2/2/1/2/2/2) | **REJECT unchanged; EXTRACT** canonical prose > YAML > lossy JSON authority ordering, provenance downgrade-only projection and source-hash binding. Output file writes need scoped target authorization |
| [threat-model-triage](https://github.com/alpha-omega-security/threat-model/blob/192fd60cd0afe8851128ce4c68ed68c174c11948/skills/threat-model-triage/SKILL.md) | `c9f0667eaf3e1a4314af6416a70730b3326392b2` | **18** (2/2/1/2/2/2/1/2/2/2) | **EXTRACT** conservative single-disposition routing, no closure from inferred claims, and `MODEL-GAP` escalation. This is advisory only: an agent must not close or disclose an actual security report merely because a model suggests a disposition |

### Controlled taxonomy and dependency characterization

All eight use existing controlled vocabulary, without extending `registry/taxonomy.yaml`:

| Skill | `use_case` | `lifecycle` | `characteristic` | `authority` | `portability` |
| --- | --- | --- | --- | --- | --- |
| threat-model | security, architecture, orchestration | planning, verification | evidence-first, orchestration, traceable | mutating | medium |
| threat-model-recon | security, research | discovery, planning | evidence-first, source-driven | read-only | medium |
| threat-model-surface | security, code-review | planning, verification | risk-aware, evidence-first | read-only | medium |
| threat-model-interview | security, communication | planning, verification | human-review, traceable | mutating | medium |
| threat-model-authoring | security, documentation | implementation | evidence-first, traceable | mutating | medium |
| threat-model-backtest | security, evaluation | verification | holdout-aware, risk-aware | mutating | medium |
| threat-model-sidecar | security, documentation | implementation, verification | contract-first, deterministic | mutating | medium |
| threat-model-triage | security, decision-support | operations, verification | safety-bounded, traceable | read-only | medium |

Dependencies: all require an external agent with access to explicitly authorized project material and sibling shared reference documents. `threat-model` orchestrates specialists; `threat-model-backtest` needs historical finding corpus or clearly labeled synthesized cases; `threat-model-sidecar` needs the canonical prose and shared schemas; `threat-model-triage` needs an existing model. The optional upstream Python adapters require Python/agent CLIs and may use GitHub/OSV/network access, but were not executed and are not adopted as `skillz` machinery.

## Terminal decision and accounting

**EXTRACT / REFERENCE-ONLY at this exact revision.** Retain this source-linked evidence as prior art for security-contract modeling; do not copy its eight skills, auto-install upstream tools, register a new admitted source, claim eight new governed `verified` records, or increment corpus counts. The extraction target is **methodological knowledge**, not a new standalone runtime or unapproved project mutation.

Why no unchanged admission: four direct artifact-writing procedures lack a clear action-specific project-write/publish gate, and all eight lack qualifying exact-package SkillSpector reports. The source's own tests/CI and root MIT license do not substitute for those requirements. Read-only specialists may be reconsidered individually under a *new* issue with a bounded use case, full package identity, explicit dependency and security evidence; this is not a hidden open-ended blocker on the present decision.

**Flow:** eight first-class candidate manifests assessed; eight pre-admission individual static decisions; **0** admitted; **0** governed exact-version verification/security companions; **0** source identities added; **0** first-party inventory changes; **0** public-accounting changes. Existing catalog remains 44 first-party / 22 registered sources / 721 third-party exact-version reviews. Five-surface accounting changes are neither justified nor made.

**Systemic finding:** new discovery is not the same as new eligible skills. The previous October 26 discovery waves identified **26 canonical source leads** (14 + 12) without admission; the limiting factor is bounded exact-package evaluation and external security evidence, not a shortage of source leads. This family now has a terminal decision rather than becoming a permanent intake queue.
