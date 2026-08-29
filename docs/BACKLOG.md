# Backlog

Status: **CURATION MODE**

Core implementation is complete. There is no outstanding CI, runtime, preflight, treatment-harness, or deterministic proof task required before normal curation continues.

## Active curation work

| ID | Item | Area | Notes |
|---|---|---|---|
| C01 | Continue selective source discovery | curation | New sources are seeds for review, not automatic admissions |
| C02 | Evaluate high-value skills from admitted/tracked sources | quality | Assign provenance, score, controlled tags, authority, portability, and decisive semantic disposition |
| C03 | Continue Hugging Face selective intake | curation | Review exact skills rather than treating the source as blanket trusted inventory |
| C04 | Source-vet Selamy Labs | curation | Prioritize differentiated governance/loop/artifact mechanisms; reject redundant ceremony |
| C05 | Source-vet Hypergiant | curation | Prioritize differentiated architecture/onboarding/persona/workflow mechanisms |
| C06 | Improve category/navigation only when corpus growth justifies it | human UX | Avoid structural churn for its own sake |
| C07 | Refresh semantic review when bootstrap/front-door behavior changes materially | evaluation | Literal/weaker-model adversarial reading, not executable proof |

## Completed core work

| ID | Item | Evidence |
|---|---|---|
| D01 | Separate user-facing library from repository engine machinery | `skills/`, `engine/skills/`, README/AGENTS boundary |
| D02 | Human-first README with explicit AI-agent jump | `README.md` |
| D03 | Single canonical first-visit/returning-user orchestrator | `engine/skills/skill-bootstrap/SKILL.md` |
| D04 | Capability-first discovery before filename search | bootstrap S2-S4 |
| D05 | Whole-skill plus component-level reasoning | bootstrap S4-S7 |
| D06 | Explicit ADOPT/ADAPT/SUPPLEMENT/COMPOSE/CREATE/no-skill decisions | bootstrap S6 |
| D07 | Host adaptation and portable handoff | bootstrap S9-S11 |
| D08 | Returning-user smallest-change and no-op behavior | bootstrap returning-user path |
| D09 | Third-party provenance/attribution companion model | `registry/skills/`, provenance docs |
| D10 | Exact-version semantic verification model | `registry/verification/`, `docs/skill-verification.md` |
| D11 | Controlled characterization taxonomy | `registry/taxonomy.yaml` |
| D12 | First-party quality review | `registry/local-verification.json` covers 42 active local skills |
| D13 | Repair local dependency/authority defects discovered during review | `agent-home-doctor`, `deck-outline`, `finance-review` |
| D14 | Reference corpus separated from governed unchanged-selection surface | README, bootstrap, CURATED, registry docs |
| D15 | Semantic adversarial closeout review | `docs/evals/share-ready-semantic-review.md` |
| D16 | Remove CI and executable completion-proof architecture | no `.github/workflows/ci.yml`; current docs explicitly reject CI/runtime gates |

## Curation rule

A new skill/source does not reopen core implementation merely because it exists.

Admission is deliberate:

1. determine whether it adds meaningful capability;
2. establish source/provenance/license/dependencies;
3. inspect the exact skill text;
4. score it with the current semantic rubric;
5. assign controlled metadata, authority, and portability;
6. choose a decisive state;
7. preserve useful negative/adaptation evidence when unchanged use is inappropriate.

## Historical records

Older alpha/Qor backlogs, executable proof tasks, and gate artifacts remain available in Git history or historical documents. They are not current work and must not be treated as completion requirements.