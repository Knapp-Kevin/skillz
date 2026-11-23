# Authored skills

**Find a complete, reusable skill for the task you need to accomplish.** These are independently maintained first-party packages, not a running release log or a promise that every skill has been tested on every agent.

Choose a capability below, open its **SKILL.md**, and copy the **entire skill directory** into your supported host when installation is authorized. Required examples, scripts, reference files, and rules are bundled with each package. No Skillz checkout, sibling skill or internet access is required to use an offline-capable package.

[Explore all capability domains](../../registry/capability-directory.json) · [Skill quality and provenance](../../registry/authored-skills-index.json) · [How to evaluate a skill](../../docs/skill-verification.md)

## Optional feedback from a using agent

Every first-party authored `SKILL.md` includes a self-contained link to the
[optional skill feedback issue form](https://github.com/Knapp-Kevin/skillz/issues/new?template=agent-skill-feedback.yml).
An agent may prepare a minimal **fictionalized, sanitized** defect or
improvement report when a user/host has explicitly authorized public issue
submission. If posting is not authorized or unavailable, the agent can offer
a copyable issue draft or simply skip it. The skill still works completely
offline. **Nothing is automatically reported, and feedback is never required.**

These skills also carry **multi-turn continuity guidance**: a follow-up
continues the current task unless the user changes objectives, with completed
work, outstanding evidence, safety requirements and the next acceptance step
kept explicit. No automatic storage, sessions or background work is implied.

The GitHub account that posts an issue is publicly attributable. This is
**anonymous feedback content, not anonymous account submission**. Do not
include real conversations, customer/project names, identifiable repository
references, private logs, paths, credentials, or other sensitive data.
When a safe generalized report is impossible, do not submit one. This
policy applies to original authored skills, not to third-party reference
packages or historical repo-bound procedures that we do not own.

## Build, maintain, and deliver software

| Skill | What it helps you accomplish |
| --- | --- |
| [CI Guard](ci-guard/SKILL.md) | Classify CI changes and protect required delivery checks |
| [Repository Delivery Assessor](repository-delivery-assessor/SKILL.md) | Diagnose repository delivery readiness from actual evidence |
| [PR Integration Surgeon](pr-integration-surgeon/SKILL.md) | Resolve stacked PR dependency, conflict, stale-head CI and review blockers without treating a plan as a merge |
| [Repository README Architect](repository-readme-architect/SKILL.md) | Create, improve, audit, and verify repository READMEs |
| [Source Debt Triage](source-debt-triage/SKILL.md) | Identify and prioritize actionable source-code debt |
| [Reference Integrity Auditor](reference-integrity-auditor/SKILL.md) | Audit document references and scoped dependency impact |
| [Agent Workspace Footprint Assessor](agent-workspace-footprint-assessor/SKILL.md) | Inspect agent workspace storage and protected artifacts |

## Agent systems, security, and trustworthy execution

| Skill | What it helps you accomplish |
| --- | --- |
| [Skill Trial Evidence Auditor](skill-trial-evidence-auditor/SKILL.md) | Check paired skill-trial evidence and withheld effect claims |
| [Agent Failure Boundary Analysis](agent-failure-boundary-analysis/SKILL.md) | Reconstruct agent failure causes and falsifiable boundaries |
| [Connector Capability Risk Review](connector-capability-risk-review/SKILL.md) | Assess tool effects and connector security/authority |
| [MCP Tool Surface Auditor](mcp-tool-surface-auditor/SKILL.md) | Compare claimed backend, MCP, and host-visible tool lists without inventing a root cause |
| [Privilege Exposure Mapper](privilege-exposure-mapper/SKILL.md) | Map effective permissions and least-privilege change risk |
| [Scheduled Work Proof Auditor](scheduled-work-proof-auditor/SKILL.md) | Distinguish scheduled jobs from observed delivery |
| [Context Continuation Contract](context-continuation-contract/SKILL.md) | Carry verified context across agents and sessions |
| [Evidence-Driven Refinement Loop](evidence-driven-refinement-loop/SKILL.md) | Challenge real task outcomes, route supported improvements and keep personal preferences separate |
| [Recursive Refinement Trace](recursive-refinement-trace/SKILL.md) | Opt-in host-local trace capture and observed-only replay of recorded refinement attempts |

## Research, evidence, and information management

| Skill | What it helps you accomplish |
| --- | --- |
| [Claim Evidence Adjudicator](claim-evidence-adjudicator/SKILL.md) | Adjudicate contested claims with source independence |
| [Research Methods Appraiser](research-methods-appraiser/SKILL.md) | Evaluate methods, validity and reproducibility |
| [Research Question Dossier](research-question-dossier/SKILL.md) | Research bounded questions with rival explanations |
| [Technology Change Intelligence](technology-change-intelligence/SKILL.md) | Track technology changes by user interests and primary evidence |
| [Federated Source Catalog](federated-source-catalog/SKILL.md) | Discover authorized information across connected sources |
| [File Lifecycle Curator](file-lifecycle-curator/SKILL.md) | Organize and summarize scoped file collections safely |
| [Metadata Taxonomy Steward](metadata-taxonomy-steward/SKILL.md) | Govern categories, tags, aliases and vocabulary changes |
| [Decision Tradeoff Workbench](decision-tradeoff-workbench/SKILL.md) | Compare options with gates, weights and uncertainty |
| [Decision Record Steward](decision-record-steward/SKILL.md) | Capture and reconcile decisions and supersession |

## Business, operations, and professional work

| Skill | What it helps you accomplish |
| --- | --- |
| [Healthcare Contract Forensics](healthcare-contract-forensics/SKILL.md) | Review healthcare contracts against supplied evidence |
| [Professional Market Evidence Scout](professional-market-evidence-scout/SKILL.md) | Research professional roles and compensation evidence |
| [Statement Variance Reviewer](statement-variance-reviewer/SKILL.md) | Reconcile financial statements and explain variances |
| [Business Presence Observatory](business-presence-observatory/SKILL.md) | Assess public business presence and discoverability |
| [Personal Operations Control Board](personal-operations-control-board/SKILL.md) | Plan personal work with honest status and priorities |
| [Work Period Evidence Reporter](work-period-evidence-reporter/SKILL.md) | Report completed work using observable evidence |

## Creative production and learning

| Skill | What it helps you accomplish |
| --- | --- |
| [Narrative Scene Gap Audit](narrative-scene-gap-audit/SKILL.md) | Diagnose scene and story-structure gaps |
| [Character Motivation Interview](character-motivation-interview/SKILL.md) | Elicit consistent character motivations |
| [Develop a Melodic Motif](develop-melodic-motif/SKILL.md) | Develop reusable musical motifs within real constraints |
| [Evidence Narrative Composer](evidence-narrative-composer/SKILL.md) | Turn verified findings into presentations and narratives |
| [Learning Evidence Progression](learning-evidence-progression/SKILL.md) | Plan and assess learning through demonstrable outcomes |

## Use responsibly

- **Read first.** Inspect the complete package, scope, dependencies, source/license and your host's actual tool permissions. Reading a package never authorizes private-data access, installation, sending messages, spending money, repository writes or scheduling.
- **Match the output to the task.** Choose an existing skill for a real recurring need. When none fits, compare first-party, governed external and source-pinned discovery leads before independently authoring a specialized alternative. A missing catalog match is not proof the capability does not exist.
- **Separate evidence levels.** A static semantic score is not a host-run result. Local Python tests establish only the checked helper's bounded behavior. Real agent-host validation, rights and package-security evidence must each be inspected separately; the registry preserves `not-run` and `incomplete` states.
- **Keep offline packages complete.** The governing instructions must ship inside the skill folder. Scripts are optional unless the particular package needs them, and stronger models may use equivalent authorized methods without weakening safety, privacy, provenance or evidence thresholds.

**Contributing:** Build original skills under `skills/authored/<slug>/`, including in-package supporting files and applicable license. Register exact Git blob/tree fingerprints, provenance, static verification and capability paths. Do not import third-party material with unestablished rights or force a new domain for a single specialized skill. See the [authoring contract](../../docs/skill-template.md).

**Historical development notes:** The previous authored-directory activity log remains available in [Git history at the prior recorded source revision](https://github.com/Knapp-Kevin/skillz/blob/22558c8bcef39a9b69db207c8affeb890718197b/skills/authored/README.md). Current changes belong in [CHANGES.md](../../CHANGES.md), reviews and tracked issues, not this capability navigator.
