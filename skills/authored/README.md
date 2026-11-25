# Authored skills

**Find a complete, reusable skill for the task you need to accomplish.** These are independently maintained first-party packages, not a running release log or a promise that every skill has been tested on every agent.

Choose a capability below and identify your AI host. The individual **ZIP** links download canonical source archives; for installation use the manifest-selected asset and follow the [manual installation instructions for your AI](../../docs/getting-started-with-skills.md). Each archive contains the **entire skill directory**. Inspect the source and package before installing. Required examples, scripts, reference files, and rules are bundled with each package. No Skillz checkout, sibling skill or internet access is required to use an offline-capable package.

[Manual installation by host](../../docs/getting-started-with-skills.md) · [Download manifest and SHA-256 hashes](https://github.com/Knapp-Kevin/skillz/releases/latest/download/authored-download-manifest.json) · [Published snapshots](https://github.com/Knapp-Kevin/skillz/releases) · [Explore all capability domains](../../registry/capability-directory.json) · [Skill quality and provenance](../../registry/authored-skills-index.json) · [How to evaluate a skill](../../docs/skill-verification.md)

**Archive choice:** consult the [manifest](https://github.com/Knapp-Kevin/skillz/releases/latest/download/authored-download-manifest.json) for the exact host's `PACKAGE_READY` asset and checksum. Claude Apps may use `-claude.zip`; Gemini Apps uses `-gemini.zip`; Microsoft uses `-m365.zip`. Download the asset from the same source-pinned release as the manifest, not a second moving `latest` URL. See [download steps and host holds](../../docs/getting-started-with-skills.md#download-your-skill). A missing or held host variant is not permission to bypass host limits. Never install an unverified or incomplete archive.

## Optional feedback from a using agent

Every first-party authored `SKILL.md` includes a self-contained link to the
[optional skill feedback issue form](https://github.com/Knapp-Kevin/skillz/issues/new?template=agent-skill-feedback.yml).
An agent may prepare a **categorical, source-blind** canonical defect report only when safe and explicitly authorized. Keep fictional reproducers private; do not paste them in the public form. Personal preferences remain private. If posting is not authorized or unavailable, the agent can offer
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
**Do not rely on removing a name alone.** Exact workflow/job counts,
runner durations, timestamps, commit or run IDs, distinctive command or
platform combinations, charts, and verbatim error text can be matched
against public CI history to reidentify a consumer. Generalize the failure
mode; use entirely fictional names, workloads, numbers and timestamps
for private reproductions. Preserve authentic exact-run evidence only
inside the authorized consuming project, not as a public Skillz citation
or cross-repository link. Review the full public issue/PR body, comments,
fixtures, screenshots, commit messages and outbound links for inadvertent
attribution before publishing. When an exact real number matters to a
technical claim, disclose that the public sample is illustrative and
keep the evidence boundary explicit, rather than pretending the
fictional value was observed.
When a safe generalized report is impossible, do not submit one. This
policy applies to original authored skills, not to third-party reference
packages or historical repo-bound procedures that we do not own.

## Build, maintain, and deliver software

| Skill | What it helps you accomplish | Download |
| --- | --- | --- |
| [Offline Hyper-V Qualification VM](offline-hyperv-qual-vm/SKILL.md) | Safely provision and qualify isolated Windows evidence VMs with owner-held credentials and checkpoint discipline | [ZIP](https://github.com/Knapp-Kevin/skillz/releases/latest/download/offline-hyperv-qual-vm.zip) |
| [CI Guard](ci-guard/SKILL.md) | Classify CI changes and protect required delivery checks | [ZIP](https://github.com/Knapp-Kevin/skillz/releases/latest/download/ci-guard.zip) |
| [Repository Delivery Assessor](repository-delivery-assessor/SKILL.md) | Diagnose repository delivery readiness from actual evidence | [ZIP](https://github.com/Knapp-Kevin/skillz/releases/latest/download/repository-delivery-assessor.zip) |
| [PR Integration Surgeon](pr-integration-surgeon/SKILL.md) | Resolve stacked PR dependency, conflict, stale-head CI and review blockers without treating a plan as a merge | [ZIP](https://github.com/Knapp-Kevin/skillz/releases/latest/download/pr-integration-surgeon.zip) |
| [Release Evidence Reconciler](release-evidence-reconciler/SKILL.md) | Compare tested source, build and published bytes, provenance claims, and installation evidence | [ZIP](https://github.com/Knapp-Kevin/skillz/releases/latest/download/release-evidence-reconciler.zip) |
| [First-Run Experience Validator](first-run-experience-validator/SKILL.md) | Audit a newcomer's published install/setup journey through an actually observed first useful outcome | [ZIP](https://github.com/Knapp-Kevin/skillz/releases/latest/download/first-run-experience-validator.zip) |
| [Repository README Architect](repository-readme-architect/SKILL.md) | Create, improve, audit, and verify repository READMEs | [ZIP](https://github.com/Knapp-Kevin/skillz/releases/latest/download/repository-readme-architect.zip) |
| [Source Debt Triage](source-debt-triage/SKILL.md) | Identify and prioritize actionable source-code debt | [ZIP](https://github.com/Knapp-Kevin/skillz/releases/latest/download/source-debt-triage.zip) |
| [Reference Integrity Auditor](reference-integrity-auditor/SKILL.md) | Audit document references and scoped dependency impact | [ZIP](https://github.com/Knapp-Kevin/skillz/releases/latest/download/reference-integrity-auditor.zip) |
| [Agent Workspace Footprint Assessor](agent-workspace-footprint-assessor/SKILL.md) | Inspect agent workspace storage and protected artifacts | [ZIP](https://github.com/Knapp-Kevin/skillz/releases/latest/download/agent-workspace-footprint-assessor.zip) |

## Agent systems, security, and trustworthy execution

| Skill | What it helps you accomplish | Download |
| --- | --- | --- |
| [Skill Trial Evidence Auditor](skill-trial-evidence-auditor/SKILL.md) | Check paired skill-trial evidence and withheld effect claims | [ZIP](https://github.com/Knapp-Kevin/skillz/releases/latest/download/skill-trial-evidence-auditor.zip) |
| [Agent Failure Boundary Analysis](agent-failure-boundary-analysis/SKILL.md) | Reconstruct agent failure causes and falsifiable boundaries | [ZIP](https://github.com/Knapp-Kevin/skillz/releases/latest/download/agent-failure-boundary-analysis.zip) |
| [Connector Capability Risk Review](connector-capability-risk-review/SKILL.md) | Assess tool effects and connector security/authority | [ZIP](https://github.com/Knapp-Kevin/skillz/releases/latest/download/connector-capability-risk-review.zip) |
| [MCP Tool Surface Auditor](mcp-tool-surface-auditor/SKILL.md) | Compare claimed backend, MCP, and host-visible tool lists without inventing a root cause | [ZIP](https://github.com/Knapp-Kevin/skillz/releases/latest/download/mcp-tool-surface-auditor.zip) |
| [Privilege Exposure Mapper](privilege-exposure-mapper/SKILL.md) | Map effective permissions and least-privilege change risk | [ZIP](https://github.com/Knapp-Kevin/skillz/releases/latest/download/privilege-exposure-mapper.zip) |
| [Scheduled Work Proof Auditor](scheduled-work-proof-auditor/SKILL.md) | Distinguish scheduled jobs from observed delivery | [ZIP](https://github.com/Knapp-Kevin/skillz/releases/latest/download/scheduled-work-proof-auditor.zip) |
| [Context Continuation Contract](context-continuation-contract/SKILL.md) | Carry verified context across agents and sessions | [ZIP](https://github.com/Knapp-Kevin/skillz/releases/latest/download/context-continuation-contract.zip) |
| [Evidence-Driven Refinement Loop](evidence-driven-refinement-loop/SKILL.md) | Challenge real task outcomes, route supported improvements and keep personal preferences separate | [ZIP](https://github.com/Knapp-Kevin/skillz/releases/latest/download/evidence-driven-refinement-loop.zip) |
| [Recursive Refinement Trace](recursive-refinement-trace/SKILL.md) | Opt-in host-local trace capture and observed-only replay of recorded refinement attempts | [ZIP](https://github.com/Knapp-Kevin/skillz/releases/latest/download/recursive-refinement-trace.zip) |

## Research, evidence, and information management

| Skill | What it helps you accomplish | Download |
| --- | --- | --- |
| [Claim Evidence Adjudicator](claim-evidence-adjudicator/SKILL.md) | Adjudicate contested claims with source independence | [ZIP](https://github.com/Knapp-Kevin/skillz/releases/latest/download/claim-evidence-adjudicator.zip) |
| [Research Methods Appraiser](research-methods-appraiser/SKILL.md) | Evaluate methods, validity and reproducibility | [ZIP](https://github.com/Knapp-Kevin/skillz/releases/latest/download/research-methods-appraiser.zip) |
| [Research Question Dossier](research-question-dossier/SKILL.md) | Research bounded questions with rival explanations | [ZIP](https://github.com/Knapp-Kevin/skillz/releases/latest/download/research-question-dossier.zip) |
| [Technology Change Intelligence](technology-change-intelligence/SKILL.md) | Track technology changes by user interests and primary evidence | [ZIP](https://github.com/Knapp-Kevin/skillz/releases/latest/download/technology-change-intelligence.zip) |
| [Federated Source Catalog](federated-source-catalog/SKILL.md) | Discover authorized information across connected sources | [ZIP](https://github.com/Knapp-Kevin/skillz/releases/latest/download/federated-source-catalog.zip) |
| [File Lifecycle Curator](file-lifecycle-curator/SKILL.md) | Organize and summarize scoped file collections safely | [ZIP](https://github.com/Knapp-Kevin/skillz/releases/latest/download/file-lifecycle-curator.zip) |
| [Metadata Taxonomy Steward](metadata-taxonomy-steward/SKILL.md) | Govern categories, tags, aliases and vocabulary changes | [ZIP](https://github.com/Knapp-Kevin/skillz/releases/latest/download/metadata-taxonomy-steward.zip) |
| [Decision Tradeoff Workbench](decision-tradeoff-workbench/SKILL.md) | Compare options with gates, weights and uncertainty | [ZIP](https://github.com/Knapp-Kevin/skillz/releases/latest/download/decision-tradeoff-workbench.zip) |
| [Decision Record Steward](decision-record-steward/SKILL.md) | Capture and reconcile decisions and supersession | [ZIP](https://github.com/Knapp-Kevin/skillz/releases/latest/download/decision-record-steward.zip) |

## Business, operations, and professional work

| Skill | What it helps you accomplish | Download |
| --- | --- | --- |
| [Healthcare Contract Forensics](healthcare-contract-forensics/SKILL.md) | Review healthcare contracts against supplied evidence | [ZIP](https://github.com/Knapp-Kevin/skillz/releases/latest/download/healthcare-contract-forensics.zip) |
| [Professional Market Evidence Scout](professional-market-evidence-scout/SKILL.md) | Research professional roles and compensation evidence | [ZIP](https://github.com/Knapp-Kevin/skillz/releases/latest/download/professional-market-evidence-scout.zip) |
| [Statement Variance Reviewer](statement-variance-reviewer/SKILL.md) | Reconcile financial statements and explain variances | [ZIP](https://github.com/Knapp-Kevin/skillz/releases/latest/download/statement-variance-reviewer.zip) |
| [Business Presence Observatory](business-presence-observatory/SKILL.md) | Assess public business presence and discoverability | [ZIP](https://github.com/Knapp-Kevin/skillz/releases/latest/download/business-presence-observatory.zip) |
| [Effort Allocation Navigator](effort-allocation-navigator/SKILL.md) | Prioritize dependent tasks, blockers and payoff versus effort with a primary next action and bounded alternative | [ZIP](https://github.com/Knapp-Kevin/skillz/releases/latest/download/effort-allocation-navigator.zip) |
| [Personal Operations Control Board](personal-operations-control-board/SKILL.md) | Plan personal work with honest status and priorities | [ZIP](https://github.com/Knapp-Kevin/skillz/releases/latest/download/personal-operations-control-board.zip) |
| [Work Period Evidence Reporter](work-period-evidence-reporter/SKILL.md) | Report completed work using observable evidence | [ZIP](https://github.com/Knapp-Kevin/skillz/releases/latest/download/work-period-evidence-reporter.zip) |

## Creative production and learning

| Skill | What it helps you accomplish | Download |
| --- | --- | --- |
| [Narrative Scene Gap Audit](narrative-scene-gap-audit/SKILL.md) | Diagnose scene and story-structure gaps | [ZIP](https://github.com/Knapp-Kevin/skillz/releases/latest/download/narrative-scene-gap-audit.zip) |
| [Character Motivation Interview](character-motivation-interview/SKILL.md) | Elicit consistent character motivations | [ZIP](https://github.com/Knapp-Kevin/skillz/releases/latest/download/character-motivation-interview.zip) |
| [Develop a Melodic Motif](develop-melodic-motif/SKILL.md) | Develop reusable musical motifs within real constraints | [ZIP](https://github.com/Knapp-Kevin/skillz/releases/latest/download/develop-melodic-motif.zip) |
| [Evidence Narrative Composer](evidence-narrative-composer/SKILL.md) | Turn verified findings into presentations and narratives | [ZIP](https://github.com/Knapp-Kevin/skillz/releases/latest/download/evidence-narrative-composer.zip) |
| [Learning Evidence Progression](learning-evidence-progression/SKILL.md) | Plan and assess learning through demonstrable outcomes | [ZIP](https://github.com/Knapp-Kevin/skillz/releases/latest/download/learning-evidence-progression.zip) |

## Additional authored skills

| Skill | What it helps you accomplish | Download |
| --- | --- | --- |
| [Sandler-aligned Conversation Strategist](sandler-conversation-strategist/SKILL.md) | Prepare and improve evidence-grounded sales conversations | [ZIP](https://github.com/Knapp-Kevin/skillz/releases/latest/download/sandler-conversation-strategist.zip) |
| [MEDDPICC Opportunity Assurance](meddpicc-opportunity-assurance/SKILL.md) | Assess complex B2B opportunity evidence and qualification gaps | [ZIP](https://github.com/Knapp-Kevin/skillz/releases/latest/download/meddpicc-opportunity-assurance.zip) |

## Use responsibly

- **Read first.** Inspect the complete package, scope, dependencies, source/license and your host's actual tool permissions. Reading a package never authorizes private-data access, installation, sending messages, spending money, repository writes or scheduling.
- **Match the output to the task.** Choose an existing skill for a real recurring need. When none fits, compare first-party, governed external and source-pinned discovery leads before independently authoring a specialized alternative. A missing catalog match is not proof the capability does not exist.
- **Separate evidence levels.** A static semantic score is not a host-run result. Local Python tests establish only the checked helper's bounded behavior. Real agent-host validation, rights and package-security evidence must each be inspected separately; the registry preserves `not-run` and `incomplete` states.
- **Keep offline packages complete.** The governing instructions must ship inside the skill folder. Scripts are optional unless the particular package needs them, and stronger models may use equivalent authorized methods without weakening safety, privacy, provenance or evidence thresholds.

**Contributing:** Build original skills under `skills/authored/<slug>/`, including in-package supporting files and applicable license. Register exact Git blob/tree fingerprints, provenance, static verification and capability paths. Do not import third-party material with unestablished rights or force a new domain for a single specialized skill. See the [authoring contract](../../docs/skill-template.md).

**Historical development notes:** The previous authored-directory activity log remains available in [Git history at the prior recorded source revision](https://github.com/Knapp-Kevin/skillz/blob/22558c8bcef39a9b69db207c8affeb890718197b/skills/authored/README.md). Current changes belong in [CHANGES.md](../../CHANGES.md), reviews and tracked issues, not this capability navigator.
