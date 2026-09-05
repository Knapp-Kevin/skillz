# 🛠️ skillz

![Reference Corpus](https://img.shields.io/badge/reference_corpus-500%2B-blue)
![First-Party Skills](https://img.shields.io/badge/first--party_skills-43-brightgreen)
![Persisted Third-Party Reviews](https://img.shields.io/badge/exact--version_reviews-345-8A2BE2)
![Registered Sources](https://img.shields.io/badge/registered_sources-19-6f42c1)
![Repository](https://img.shields.io/badge/repository-passive-blueviolet)
![License](https://img.shields.io/badge/license-MIT-green)

**A passive skill knowledge resource for AI agents.** `skillz` accumulates reusable skills, procedures, safeguards, anti-patterns, rejected examples, creator methods, standards, pinned source material, provenance, exact-version review evidence, tags, source context, catalog snapshots, and instructions so an external host agent can construct the smallest useful skill set for the user.

> **AI agent? Start with [`AGENT_START_HERE.md`](AGENT_START_HERE.md).** For first-visit or returning-user skill-system work, [`engine/skills/skill-bootstrap/SKILL.md`](engine/skills/skill-bootstrap/SKILL.md) is the canonical passive procedure.

> **Normal-use boundary:** skills created, adapted, composed, or refined for a user belong in that user's active AI/agent environment or in a portable handoff. They are not written back here unless repository maintenance/curation was explicitly requested.

## What `skillz` is

`skillz` is entirely passive. The external host agent is the active system. The repository owns no runtime, scripts, tests, CI workflows, schedulers, monitors, crawlers, installers, synchronizers, preflight processes, generators, background services, vector databases, autonomous observers, or personalization services.

The repository provides four surfaces:

1. **43 first-party user-facing skills** under [`skills/`](skills/).
2. **12 intact pinned third-party corpora** under [`skills/sources/`](skills/sources/) at exact upstream revisions.
3. **Governed provenance and exact-version evidence** under [`registry/skills/`](registry/skills/) and [`registry/verification/`](registry/verification/).
4. **Passive repository-use and curation procedures** under [`engine/skills/`](engine/skills/), excluded from user-facing inventory.

Third-party packages may contain their own scripts, tests, examples, fixtures, templates, or tools. Those remain upstream package material, not repository-owned execution machinery.

## Core use

The host agent should identify durable user needs, inspect the minimum relevant evidence, compare available first-party and governed third-party material, then evaluate in this order:

**user fit → exact-version quality → operational fit → skill freshness → provenance/source context**

Valid outcomes include ADOPT, ADAPT, EXTRACT, SUPPLEMENT, COMPOSE, CREATE, CHECKLIST, DYNAMIC behavior, or NO CHANGE. The goal is the smallest coherent fitted system, not maximum reuse.

## Corpus and evidence

[`skills/`](skills/) contains **43 active first-party user-facing skills**, all **43/43 provenance-complete** under [`registry/skills/local-skills/`](registry/skills/local-skills/) with structured semantic review evidence in [`registry/local-verification.json`](registry/local-verification.json).

The 12 pinned corpora are Anthropic Skills, Anthropic Knowledge Work Plugins, Vercel Agent Skills, Microsoft Skills, Microsoft Azure Skills, AWS Agent Toolkit, Matt Pocock Skills, Addy Osmani Agent Skills, OpenHands Extensions, Cline Skills, Cloudflare Skills, and Google Agents CLI. Exact source identity, role, terms, and pins live in [`registry/sources.yaml`](registry/sources.yaml). The registry contains **19 unique source identities** across pinned-reference, tracked-corpus, normative-spec, and dynamic-discovery roles.

There are currently **345 persisted exact-version third-party verification companions** under the canonical registry contract. `verified` means structured static semantic review of an exact version. `validated` additionally requires representative external behavioral/adversarial evidence. `rejected` and `retired` remain useful bounded prior art but are excluded from normal unchanged selection. Current semantics are defined in [`docs/skill-verification.md`](docs/skill-verification.md).

## Discovery and admission

Discovery is separate from admission and quality:

**discovery surface → candidate issue/source → source-vetting → exact-version static evaluation → decisive admission result → repository persistence when justified → user-fit decision**

New third-party discoveries use [`docs/candidate-intake.md`](docs/candidate-intake.md). Discovery scores, popularity, official branding, creator reputation, or catalog recommendations are signals only. Restricted or unclear-license material remains reference-only unless terms justify another role.

## Current curation state

Core passive architecture is complete. Ongoing work is corpus enrichment and evidence reconciliation.

- **AWS Agent Toolkit:** **72/72** current-standard provenance + verification companion complete at pin `ff1481a7bc1a04ee00ebf63d3a8a149aa6a2c546`.
- **Microsoft Skills:** exact denominator **189** at pin `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`; **173/189** current-standard companion complete, **16** gaps remain.
- Microsoft direct `.NET`: **29/29** complete.
- Microsoft direct Java: **26/26** complete.
- Microsoft direct Python: **40/40** complete.
- Microsoft direct Rust: **9/9** complete.
- Microsoft direct TypeScript: **25/25** complete.

A 2026-09-05 contract reconciliation restored ten Microsoft reviews from auxiliary Markdown evidence into the mandatory `registry/skills/` + `registry/verification/` YAML companion paths. `skill-creator` already had a YAML pair and was therefore not counted twice; its existing pair was refreshed to the current 15/20 rejected authority disposition.

Latest non-direct Microsoft closure: `wiki-onboarding` is **rejected unchanged, 13/20**. It is bound to package tree `3c95e30a619b223fb2ad107322fcbb9be46f13f5` and `SKILL.md` blob `c708309fd6314cb58788dcacc40216675024b989`, with freshness revision `67ae723a23ba880e3e5c8a3e5e2320092024476e` from 2026-04-02. Preserve its audience-specific onboarding decomposition, source-repository resolution, language-aware contributor guidance, evidence-linked diagrams/tables, and validation checklist. Unchanged adoption is rejected because it directs creation of an `onboarding/` directory and five persistent Markdown artifacts without a mandatory action-specific authorization checkpoint immediately before mutation. Its Executive and Product Manager requirements also demand ownership, bus factor, cost/scaling, SLA/current metrics, roadmap, compliance, and planned-status assertions without requiring unknowns when evidence is absent. Behavioral validation is `not-run`.

Microsoft Skills remains the active admitted-source family with **16** gaps. The next gap should be established from the exact registered-pin `deep-wiki` skill tree after `wiki-onboarding`, checking both canonical companion shelves and repository history before review. Microsoft Azure Skills follows Microsoft Skills. Historically completed external corpora should be reconciled from compatible prior evidence before fresh re-review.

## Repository map

| Area | Purpose |
|---|---|
| [`AGENT_START_HERE.md`](AGENT_START_HERE.md) | Agent routing and capability floor |
| [`AGENTS.md`](AGENTS.md) | Repository-wide agent contract |
| [`skills/`](skills/) | First-party user-facing corpus |
| [`skills/sources/`](skills/sources/) | Intact exact-revision external reference corpora |
| [`INDEX.md`](INDEX.md) / [`index.json`](index.json) | Hand-maintained passive catalog snapshots |
| [`CURATION_QUEUE.md`](CURATION_QUEUE.md) | Living curation and source-vetting ledger |
| [`registry/sources.yaml`](registry/sources.yaml) | Source identities, roles, pins, licenses, paths |
| [`registry/skills/`](registry/skills/) | Mandatory per-skill provenance companions |
| [`registry/verification/`](registry/verification/) | Exact-version semantic review evidence |
| [`engine/skills/`](engine/skills/) | Passive repository-use/curation procedures |
| [`docs/GOVERNANCE_INDEX.md`](docs/GOVERNANCE_INDEX.md) | Current governance precedence |
| [`docs/SYSTEM_STATE.md`](docs/SYSTEM_STATE.md) | Current live corpus and architecture snapshot |

## Licensing

First-party content is MIT-licensed. Third-party repositories and materially derived content retain their applicable upstream obligations; the root MIT license does not relicense pinned source corpora. See [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md) and [`docs/third-party-provenance.md`](docs/third-party-provenance.md).