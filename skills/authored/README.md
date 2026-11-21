# Authored Skills

This is the **canonical home for newly authored first-party skills** produced for this repository: `skills/authored/<skill-name>/`. It distinguishes maintainer-owned original work from the external discovery/reference corpus under `skills/sources/` and historical first-party skills at `skills/<name>/`. "Authored" denotes accountability for source and rights, **not** a claim that a human personally typed every instruction or that AI assistance was absent.

## Capability-adaptive execution applies to all skills

[The canonical standard](../../docs/capability-adaptive-skill-execution.md)
governs every reviewed skill, existing and future, not just CI Guard.
The [authoring template](../../docs/skill-template.md) and
[verification standard](../../docs/skill-verification.md) make
low-context guidance and stronger-method freedom explicit. No blanket
model-tier caps or mandatory modules; same safety and evidence floor.
Prior exact-version review scores remain historical until re-reviewed.

**Standalone install invariant:** a downloaded `skills/authored/<skill-name>/`
folder must carry all required execution rules and support files, including
the capability-adaptive behavior relevant to that skill. Repository-wide
policy is for maintainers; offline users must not need this README, the
repository's `docs/`, a live URL or sibling skills. See
[offline package closure](../../docs/capability-adaptive-skill-execution.md#offline-standalone-package-closure).

[CI Guard v1.2](ci-guard/SKILL.md) includes an optional
[diagnostic decision scaffold](ci-guard/components/diagnostic-paths.md).
This is a static design change, not measured cross-model validation.

## 2026-11-19: Technology Change Intelligence v1.2.4 qualification and routing

[Technology Change Intelligence v1.2.4 historical qualification](technology-change-intelligence/SKILL.md) is the preferred [Monitoring & Intelligence](../categories/monitoring-intelligence/README.md) consumer route for all 17 former specialist Pulse topics. It includes interest-first, offline-standalone subscriber drafts, differentiated provider evidence lanes, and a requirement for user-approved MCP connector baselines before declaring a capability overlap. [Complete historical-mode coverage](../../docs/evals/receipts/2026-11-19-pulse-85-controlled-comparison-coverage.json) consists of 85 *single-context, self-reviewed text emulations*, not independently observed host pairs. A [current-version, public-primary-source xAI smoke test](../../docs/evals/receipts/2026-11-19-pulse-xai-live-primary-sources-smoke.json) uses the November 2026 xAI API and SDK releases and checks semantic distinctions, while [five current-version synthetic xAI cases](../../docs/evals/receipts/2026-11-19-pulse-xai-v124-five-controlled-cases.json) remain controlled emulation. Historical rights and all Pulse retirement holds remain unresolved; no 1.5x effectiveness result is claimed.

## 2026-11-19: Technology Change Intelligence v1.2 subscriber-interest intake

[Technology Change Intelligence v1.2](technology-change-intelligence/SKILL.md) now opens broad discovery requests with one useful interest-and-purpose question, immediately serves specific one-off requests, allows portable **unsaved** preference drafts, and covers unfamiliar technologies through a bundled `AD_HOC_TOPIC` route. Existing 17 specialist profile contracts remain intact. [Exact nine-file offline-closure review](../../docs/reviews/2026-11-19-tci-interest-first-v1-2-static-review.md) recorded 17/17 source/link checks and 12/12 analyst synthetic decision assertions. **No** real account, recurring subscription, memory write, scheduled delivery, host-model parity or proven improvement is claimed. Source-rights and user authorization limits are unchanged.

## 2026-11-19: CI assurance and focused delivery components

- [CI Guard](ci-guard/SKILL.md) (v1.2, original MIT): three specialist components for threat/detection analysis and CI placement/experiments, plus ten adversarial scenarios. Indexed under `cloud-devops/ci-cd` and `software-engineering/maintenance`.
- [Repository Delivery Assessor](repository-delivery-assessor/SKILL.md) (v1.3): retains repository diagnosis and multi-repo pulse behavior; adds three optional modules: [issue resolution](repository-delivery-assessor/components/issue-resolution.md), [momentum](repository-delivery-assessor/components/delivery-momentum.md), and [delivery evidence](repository-delivery-assessor/components/delivery-evidence.md).
- [Static review and controlled evaluation](../../docs/reviews/2026-11-19-ci-guard-delivery-components.md). External host validation and measured CI savings not established.

## 2026-11-18: Independently redesigned legacy capabilities

The maintainer controlled the historical Zo Computer account but has **not**
established authorship or copyright for all 44 legacy `frostwulf.zo.computer`
entrypoints. Forty-four bounded historical entrypoints, `todo-harvester`, `agent-postmortem`, `automation-receipts`, `decision-log`, `permissions-review`, `mcp-vetting`, `agent-home-doctor`, `fact-check`, `paper-digest`, `career-radar`, `handoff-writer`, `standup-writer`, `week-in-review`, `deck-outline`, `devlog-draft`, `deep-dive`, `learning-plan`, `smallbiz-ops`, `daily-briefing`, `finance-review`, `inbox-triage` and `task-surface`, `xai-pulse`, `hf-pulse`, `qwen-pulse`, `deepseek-pulse`, `glm-pulse`, `mistral-pulse`, `claude-pulse`, `gemini-pulse`, `kimi-pulse`, `llama-pulse`, `openai-pulse`, `perplexity-pulse`, `github-pulse`, `governance-pulse`, `inference-pulse`, `mcp-pulse`, `memory-pulse`, `brief-writer`, `compare`, `repo-doctor`, `repo-pulse`, and `session-continuity`, are retired from the active tree through owner-authorized controlled acceptance. No historical entrypoints remain active; none may be silently moved or relicensed.

**21 original packages now cover the intended function categories of all 44
legacy entries at the design level.** Some are explicitly multi-mode,
and 17 old monitoring categories became one common intelligence procedure
with 17 specialized profiles. New original text and synthetic fixtures
are under MIT; exact source and tree fingerprints are in the
[authored index](../../registry/authored-skills-index.json).

- [Claim Evidence Adjudicator](claim-evidence-adjudicator/SKILL.md) · research/fact-checking · 18/20 static, host behavior NOT RUN
- [Research Methods Appraiser](research-methods-appraiser/SKILL.md) · research/literature-review, research/reproducibility · 18/20 static, host behavior NOT RUN
- [Source Debt Triage](source-debt-triage/SKILL.md) · software-engineering/maintenance · 18/20 static, host behavior NOT RUN
- [Decision Record Steward](decision-record-steward/SKILL.md) · planning/decision-frameworks, business/governance · 18/20 static, host behavior NOT RUN
- [Agent Workspace Footprint Assessor](agent-workspace-footprint-assessor/SKILL.md) · software-engineering/maintenance, agent-mcp-development/agent-observability · 17/20 static, host behavior NOT RUN
- [Connector Capability Risk Review](connector-capability-risk-review/SKILL.md) · agent-mcp-development/mcp-clients-servers, security/supply-chain · 18/20 static, host behavior NOT RUN
- [Privilege Exposure Mapper](privilege-exposure-mapper/SKILL.md) · security/identity-access, agent-mcp-development/permissions · 18/20 static, host behavior NOT RUN
- [Scheduled Work Proof Auditor](scheduled-work-proof-auditor/SKILL.md) · agent-mcp-development/agent-observability, time-productivity/scheduling · 17/20 static, host behavior NOT RUN
- [Technology Change Intelligence v1.2](technology-change-intelligence/SKILL.md) · research/source-discovery, research/synthesis · 19/20 exact-package static, host behavior NOT RUN
- [Agent Failure Boundary Analysis](agent-failure-boundary-analysis/SKILL.md) · agent-mcp-development/evaluation, security/incident-response · 18/20 static, host behavior NOT RUN
- [Decision Tradeoff Workbench](decision-tradeoff-workbench/SKILL.md) · planning/decision-frameworks, business/strategy · 18/20 static, host behavior NOT RUN
- [Research Question Dossier](research-question-dossier/SKILL.md) · research/synthesis, research/source-discovery · 18/20 static, host behavior NOT RUN
- [Professional Market Evidence Scout](professional-market-evidence-scout/SKILL.md) · career/job-search, career/compensation · 17/20 static, host behavior NOT RUN
- [Statement Variance Reviewer](statement-variance-reviewer/SKILL.md) · finance/reporting, finance/budgeting · 17/20 static, host behavior NOT RUN
- [Context Continuation Contract](context-continuation-contract/SKILL.md) · memory-context/context-compression, agent-mcp-development/multi-agent-collaboration · 18/20 static, host behavior NOT RUN
- [Evidence Narrative Composer](evidence-narrative-composer/SKILL.md) · communication/presentations, marketing/content · 17/20 static, host behavior NOT RUN
- [Personal Operations Control Board](personal-operations-control-board/SKILL.md) · time-productivity/task-systems, time-productivity/personal-planning, communication/organizational-communication · 17/20 static, host behavior NOT RUN
- [Learning Evidence Progression](learning-evidence-progression/SKILL.md) · education/curriculum, education/assessment · 18/20 static, host behavior NOT RUN
- [Repository Delivery Assessor](repository-delivery-assessor/SKILL.md) · software-engineering/maintenance, cloud-devops/ci-cd · 18/20 static, host behavior NOT RUN
- [Business Presence Observatory](business-presence-observatory/SKILL.md) · business/operations, marketing/seo · 17/20 static, host behavior NOT RUN
- [Work Period Evidence Reporter v1.2](work-period-evidence-reporter/SKILL.md) · communication/organizational-communication, time-productivity/collaboration · 18/20 static, 10 controlled synthetic report cases, host A/B NOT RUN

All 21 packages passed bounded direct **static text/package review**
(17–19/20); host-agent behavior, independent functional equivalence,
and downstream reference-migration acceptance remain NOT RUN.
[The migration ledger](../../registry/migration/frostwulf-independent-replacement-ledger-20261118.json)
and [functional/retirement gap audit](../../docs/reviews/2026-11-18-frostwulf-replacement-equivalence-and-retirement-gates.md)
define the unresolved gate. The exact old `todo-harvester/SKILL.md` is retired under the [controlled procedure evidence](../../docs/reviews/2026-11-18-todo-controlled-procedure-retirement.md), and `agent-postmortem/SKILL.md` under the [single-analyst controlled incident reports](../../docs/reviews/2026-11-19-agent-postmortem-controlled-retirement.md). Historical Git remains; external model-host parity and exhaustive consumer scan are unproven. See [automation receipt review](../../docs/reviews/2026-11-19-automation-receipts-controlled-retirement.md) and [decision review](../../docs/reviews/2026-11-19-decision-log-controlled-retirement.md) for the third and fourth sources. The fifth, [Permissions Review](../../docs/reviews/2026-11-19-permissions-review-controlled-retirement.md), adds a separately bounded synthetic privilege-graph assessment. The sixth, [MCP Vetting](../../docs/reviews/2026-11-19-mcp-vetting-controlled-retirement.md), covers version-bound connector security decisions. The seventh, [Agent Home Doctor](../../docs/reviews/2026-11-19-agent-home-controlled-retirement.md), restores context-cost reporting and pre-mutation identity checks. The latest [Fact Check](../../docs/reviews/2026-11-19-fact-check-controlled-retirement.md) and [Paper Digest](../../docs/reviews/2026-11-19-paper-digest-controlled-retirement.md) reviews document the eighth and ninth source-bound decisions. PR #736 had no deletions.
[PR #736](https://github.com/Knapp-Kevin/skillz/pull/736).

## New skill package requirements

**Required capability indexing:** A new first-party authored package is not complete merely because its files live under `skills/authored/<slug>/`. It must be indexed in `registry/authored-skills-index.json`, `registry/governed-review-name-index.json`, and the canonical `registry/capability-directory.json` under its evidence-backed domain/subdomain routes. The latter must include one canonical `skill_records` identity and `matched_skill_ids` links for every applicable domain; update browse previews and derived counts without counting cross-links as extra skills. Run `node scripts/qa/check-authored-capability-links.mjs` during authorized local repository maintenance. [November 8 example and exact evidence](../../registry/discovery/authored-capability-routing-20261108.json). This is discovery, not host permission or proof of behavioral validation.

1. Put the complete usable package under `skills/authored/<slug>/`: `SKILL.md` plus only the references, examples, fixtures and optional scripts it actually requires. No copied third-party contents without explicit rights.
2. Register **every package** in [`registry/authored-skills-index.json`](../../registry/authored-skills-index.json) with current source path, SPDX license expression, copyright holder, license evidence path, exact `SKILL.md` Git blob SHA, complete package tree SHA, provenance/verification links, and review/test status.
3. For the original first-party content, the repository root [MIT license](../../LICENSE) is the **current default**. This permits proprietary uses and commercial redistribution subject to required notice retention. It does **not** guarantee free-of-charge availability or that derivatives remain open source.
4. If a new skill should use **GPL-3.0** or **AGPL-3.0**, choose it explicitly *before publication*, include the complete applicable legal text and clear per-package `SPDX-License-Identifier` scope. Do not infer copyleft from author intentions or silently relicense third-party materials. AGPL's network-source clause primarily targets qualifying modified network software, not automatically every remotely used Markdown prompt.
5. Record third-party references separately with exact source pin, original publisher, actual rights and attribution. A root LICENSE file is evidence, but nested and bundled material may carry other restrictions. **Unknown rights => do not import.**
6. Keep static semantic review, external scanner evidence, host behavioral tests, permission/authority, and publication clearance as separate fields. A draft package may be statically reviewed with `behavioral_validation: not-run`.

The existing first-party `skills/<slug>/` entries are not automatically moved or relicensed. Move them only as separate, reviewed maintenance work with compatible index/registry updates.

## Repository README Architect (current v0.3.0)

[Repository README Architect](repository-readme-architect/SKILL.md) is a self-contained first-party MIT skill for **CREATE from zero**, **UPLIFT**, **AUDIT**, and **VERIFY**, with mandatory formatter preflight, section-preservation dispositions, generated-source ownership and exact-head CI qualification. It includes [an evidence and quality contract](repository-readme-architect/references/readme-quality-contract.md), complete [CREATE](repository-readme-architect/examples/create-python-library-output.md) and [AUDIT](repository-readme-architect/examples/audit-output.md) examples, and an **optional offline local-link verifier** with 101/101 actually executed Python tests. [Current v0.3 exact-package review](../../docs/reviews/2026-11-20-readme-architect-v030-preservation-review.md): maintainer static 19/20; independent agent-host/user acceptance **not run**. No sibling or repository-wide runtime dependency.

## Current authored packages

[Healthcare Contract Forensics](healthcare-contract-forensics/SKILL.md) | [Package record](../../registry/authored-skills-index.json) | [Review and licensing evidence](../../docs/reviews/2026-11-06-issue714-healthcare-contract-forensics-static-review.md).

[Narrative Scene Gap Audit](narrative-scene-gap-audit/SKILL.md) | [Synthetic acceptance cases](narrative-scene-gap-audit/examples/acceptance-cases.md) | [Exact-source review](../../docs/reviews/2026-11-08-writer-story-tools-original-skills-static-review.md).

[Character Motivation Interview](character-motivation-interview/SKILL.md) | [Synthetic acceptance cases](character-motivation-interview/examples/acceptance-cases.md) | [Exact-source review](../../docs/reviews/2026-11-08-writer-story-tools-original-skills-static-review.md).

**November 8, 2026:** Three original MIT-authored packages are indexed in this collection. All three have bounded static reviews and no executed agent-host behavioral validation. The writing workflows are not copies of [Writer Story Tools](https://writer-story-tools.mdlafilms.workers.dev/), whose external applications remain all-rights-reserved; see [source and rights findings](../../docs/discovery/2026-11-08-writer-story-tools-reference.md). Repository presence is not an installation or external-account authorization.

[Career Radar qualification](../../docs/reviews/2026-11-19-career-radar-controlled-retirement.md) and [complete-package Handoff Writer qualification](../../docs/reviews/2026-11-19-handoff-writer-controlled-retirement.md) document the tenth and eleventh replacements.
