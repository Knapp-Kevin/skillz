# Skill Curation Queue

This is the living evidence ledger for the ongoing curation side of `skillz`.

The repository's passive bootstrap architecture is shareable and core-complete. **Curation is intentionally never "finished."** New skills, sources, techniques, and useful components will continue to appear. This document records what has already been examined, what evidence exists, what still needs reconciliation or individual review, and which discovery surfaces are worth revisiting.

It is not an implementation backlog and it does not reopen core completion.

## What this ledger proves

`skillz` is not a 42-skill repository with a few bookmarks attached.

Current depth includes:

- **42 first-party user-facing skills**, each with structured local semantic review metadata;
- **12 pinned upstream reference corpora** exposed under `skills/sources/`;
- a broad **500+ skill/reference surface** across the first-party and pinned external corpus;
- **120 currently persisted exact-version third-party verification companion files**;
- historical source-level curation records documenting **at least 210 reviewed external skill entry points** across nine corpora;
- additional partially reviewed admitted corpora and active discovery candidates.

The difference between the 120 persisted companion files and the broader historical review count is itself tracked here. Prior work is evidence to reconcile, not permission to invent missing records or pretend it never happened.

## Curation model

The lifecycle is:

**discovery surface → candidate issue/source → source-vetting for identity/terms/relevance/role → admitted corpus/reference/tracked source when justified → individual exact-version review → user-fit decision**

New third-party discoveries use the issue-first intake workflow. The candidate issue is the pre-admission evidence workspace; candidate material is not persisted as governed corpus inventory until the issue establishes a justified admission result. Finalized provenance and verification companions must bind to the exact evaluated identity.

Intentional discovery inputs are documented in [`docs/discovery-surfaces.md`](docs/discovery-surfaces.md). The connected Creator Technical Resource Catalog is useful lead-generation and gap-analysis intelligence, but its scores, verification labels, creator attributions, and summaries are not `skillz` provenance or individual quality evidence. Resolve every promoted lead to its canonical upstream source before issue-scoped evaluation.

Discovery does not grant quality, trust, redistribution authority, installation authority, or automatic corpus admission. Source reputation never grants blanket skill quality. A source may be excellent while individual skills are unsuitable unchanged. Conversely, a rejected whole skill may still contain a useful mechanism worth extracting with attribution and licensing respected.

For each deliberately governed skill, retain truthful provenance and exact-version evidence. Prefer to retain:

- source and author/publisher identity;
- canonical path;
- exact revision or other content identity;
- license and attribution context;
- dependencies and required components;
- authority and side-effect profile;
- portability/host assumptions;
- controlled tags;
- semantic score and findings;
- decisive disposition;
- notes on useful components even when unchanged reuse is rejected.

Missing provenance is a corpus-completeness defect, not an optional metadata improvement.

## Mandatory provenance reconciliation

Issue #66 is the active corpus-wide provenance-completeness audit.

A current first-party audit finding establishes:

- governed first-party denominator: **42** active user-facing skills;
- structured semantic review records: **42/42** in `registry/local-verification.json`;
- standalone first-party provenance companions under `registry/skills/`: **0/42**;
- therefore the first-party family must not be described as provenance-complete yet.

The semantic review records remain valid evidence for what they actually establish. They do not substitute for provenance under the current mandatory companion contract. Reconcile the gap from repository history and current evidence without inventing authorship dates, source history, or other unavailable facts. No script, CI gate, scanner, or repository runtime is required or desired.

## Completed source-level review evidence

The previous curation tracker recorded the following source denominators as reviewed to decisive static states. These are preserved as historical curation evidence even where current one-file companion coverage still needs reconciliation.

| Source | Historical reviewed denominator | Recorded result/state |
|---|---:|---|
| Anthropic Skills | 17 / 17 | Complete; 10 verified, 7 rejected |
| Anthropic Knowledge Work Plugins | 74 / 74 | Complete; 36 verified, 38 rejected unchanged |
| Matt Pocock Skills | 29 / 29 | Complete |
| OpenHands Extensions | 1 / 1 | Complete; `theme-factory` rejected unchanged |
| Vercel Agent Skills | 9 / 9 | Complete; 6 verified, 3 rejected |
| Cloudflare Skills | 13 / 13 | Complete; 11 verified, 2 rejected |
| Google Agents CLI | 7 / 7 | Complete; all verified |
| Cline Skills | 36 / 36 | Complete; 19 verified, 17 rejected unchanged, plus one separately characterized internal/unlisted skill |
| Addy Osmani Agent Skills | 24 / 24 | Complete with decisive exact-version static states |

That is **210 reviewed published/eligible entry points** across those nine corpora before counting the separately characterized Cline internal skill or later selective reviews.

### Evidence reconciliation lane

Current `registry/verification/` contains 120 persisted exact-version third-party companion files. Some historically completed source reviews therefore have broader source-level evidence than the present per-skill companion layout exposes.

Do **not** automatically redo those reviews from scratch. First locate and reconcile the prior evidence into the current provenance/verification model where it is still trustworthy and identity-compatible. Re-review only where exact content identity, licensing, dependencies, or the prior decision cannot be established honestly.

High-value reconciliation targets include:

- Anthropic Knowledge Work Plugins 74/74 historical review evidence;
- Cline 36/36 historical review evidence versus the smaller current companion shelf;
- Addy Osmani 24/24 historical review evidence versus the smaller current companion shelf;
- any completed Vercel/Cloudflare/Google/Matt records not represented one-for-one today.

## Admitted sources still under evaluation

These were already identified as unfinished enrichment work. They are not core blockers.

### AWS Agent Toolkit

- Pinned reference: `ff1481a7bc1a04ee00ebf63d3a8a149aa6a2c546`
- Historical denominator: **72** skill entry points, 14 core + 58 specialized.
- Prior work: all 72 entry points were inspected against the registered pin, with a prior full-pass disposition of 70 verified / 2 rejected.
- Current exact companion closure: **20/72** persisted provenance + verification pairs on `main`.
- Latest reconciled specialized skill: `finding-data-lake-assets`, package tree `e32f6445e9f80e2dca0bfe14ecf5e7ad53ac2721`, decisive state `verified` at 17/20, behavioral evidence `not-run`.
- Remaining work: **52** current-standard companion gaps. Search for compatible prior evidence and existing companions before any re-review. Re-review only when exact content identity, licensing, dependencies, authority, freshness, or prior decisive evidence cannot be recovered truthfully.

### Microsoft Skills

- Pinned reference: `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`
- Status: full source review remains pending.
- Priority: favor differentiated Microsoft/M365/Foundry/developer-platform capabilities; avoid duplicating stronger existing material merely because it is official.

### Microsoft Azure Skills

- Pinned reference: `8f8c72bb9e22aee4366e07aadfd5766ef9add8f4`
- Status: full source review remains pending.
- Priority: distinguish planning/read-only guidance from deployment, RBAC, cost, identity, and other higher-authority operations.

### Cole Medin Skills

- Pinned reference: `fb2e876f057c5356d6603ba0c52d6b4418d893ba`
- Denominator: **33** skills.
- Persisted selective reviews already include `second-brain-audit`, `rules-check-drift`, and `ablate-ai-layer`.
- Continue only where remaining skills add differentiated mechanisms or useful negative evidence.

### David Ondrej Skills

- Public pinned mirror: `7d0ef87dad1f638cab58995eead9e0e6e3fae237`
- Publisher private-source revision: `eed325a23bc29efca50084f85025d327460b2059`
- Mirror fingerprint: `cb682185dc410fb8615b36cd55ce10ecd9d9dbdf0bb7fd1209c0b065e36e0f3b`
- Current curation evidence describes **44 canonical `SKILL.md` files** at the public snapshot.
- Historical tracker recorded a denominator of **55**.
- Action: reconcile that denominator discrepancy before making any completion claim.
- Persisted selective reviews already include `effective-agent-skills`, `goal-loop`, and `fable-safe-prompt`.

### Sabrina Ramonov Learn Claude Code Skills

- Historical tracker says this creator-owned corpus was admitted with a denominator of **2** and remained under individual review.
- Current source registry does not expose an equivalent source entry.
- Action: recover canonical source identity, exact pin, license, and prior admission evidence before continuing. Do not infer or fabricate it.

## Active discovery and source-vetting frontier

These are promising discovery surfaces, not trusted inventory.

### Hugging Face Skills

- Official source: `huggingface/skills`.
- Previously source-vetted for selective deeper intake.
- Reviewed snapshot recorded as `cead19e10754e773bad24fecef83cb64be24094e`.
- Root license: Apache-2.0.
- README at review time advertised roughly **25 standardized Agent Skills**.
- `hf-cli` was specifically left preliminary because it combines read/discovery operations with credentials, uploads, jobs, scheduling, webhooks, endpoint mutation, extension installation, and token-display capability.

### Selamy Labs Agent Skills

- Candidate: `selamy-labs/agent-skills`.
- Last reviewed pin: `3dac515634d086e9b3f20541f568c84effdf0298`.
- Distinctive candidates identified: `connector-readiness`, `verify-real-artifact`, `grounded-generation`, `adaptive-loop-budgeting`, `process-aware-done`, `ephemeral-workspace-lifecycle`, `stakeholder-knowledge-projection`, `lean-on-oss-standards`, `iac-not-ad-hoc`, `data-connector-building`, `instrumented-service-scaffold`, `agentic-coding-loop`, `loop-governance-and-learning`, `product-feedback-loop`, `reddit-research`, `yield-on-wait`.
- Main risk: redundancy with existing local/governance material. Distinct value must beat duplication.

### Hypergiant Agent Skills

- Candidate: `gohypergiant/agent-skills`.
- Last reviewed pin: `459a846a65544cf311164059f2ea4623ec443b02`.
- Root license: Apache-2.0.
- Historical README denominator: **23** skill directories.
- Strongest areas to inspect: architecture documentation/synthesis, constraints, onboarding, persona/review, QRSPI workflow patterns.
- React/Next/TypeScript/security material is likely high-duplication unless it clearly improves on existing sources.

### Additional discovery surfaces

Keep as discovery candidates until source-vetted and issue-scoped:

- `bcgov/agent-skills` — public-sector source with explicit skill validation discipline;
- `devantler-tech/agent-skills` — interesting pointer/index approach that preserves upstream identity;
- `JayRHa/AgentSkills` — broad advertised corpus, source audit required;
- `Emmraan/agent-skills` — very large aggregate with provenance and duplication complexity;
- `luckys/agent-skills` — likely high generic overlap; do not bulk-admit;
- GitHub Awesome Copilot — registered dynamic discovery surface, never blanket trusted;
- Agent Skills Specification — normative format/portability reference, not normal installable inventory;
- connected Creator Technical Resource Catalog — internal governed discovery intelligence for identifying leads and corpus gaps, never a canonical source or verification authority.

New candidates should be queued as evaluation issues before corpus admission. Discovery/source-vetting issues #62 through #65 are examples of that pre-admission workflow; they do not themselves grant admission.

## Legacy candidate intelligence

[`registry/candidates.yaml`](registry/candidates.yaml) and [`docs/agent-skills-longlist.md`](docs/agent-skills-longlist.md) preserve additional historical candidate decisions and discovery intelligence, including tracked or rejected material such as agent configuration linting, verification loops, AI regression testing, HashiCorp skills, learning-resource indices, context-compression tooling, codebase-understanding projects, local-training ecosystems, and minimalism/process-rule candidates.

Those records are useful prior art. They should be re-checked for current provenance and fit before promotion because some were created under older repository assumptions.

## Working rules for future curation

1. **Do not chase counts.** Add coverage or differentiated mechanisms, not inventory theater.
2. **Do not erase negative evidence.** A well-explained rejection prevents future agents from rediscovering the same problem.
3. **Preserve complete skill packages.** Scripts, references, templates, fixtures, examples, and other required components are part of a skill when the upstream skill owns them.
4. **Evaluate independently.** Official branding, stars, popularity, reviewer comments, and prior recommendations are inputs, not conclusions.
5. **Require truthful provenance.** Every governed user-facing skill must satisfy the current provenance contract; pins and fingerprints make decisions inspectable, while unknown facts stay unknown.
6. **Separate availability from trust.** The 500+ reference corpus is broad prior art; unchanged reuse deserves stronger individual evidence.
7. **Extract mechanisms when whole-skill reuse is wrong.** Useful ideas can survive a rejection without importing unsafe authority or source-specific ceremony.
8. **Keep the engine passive.** Curation is performed by whichever agent/human is doing the work; this repository does not crawl, poll, schedule, or execute itself.
9. **No model-performance obligation.** Review the instructions and skill material as well as practical; do not turn curation into arbitrary multi-model benchmarking.
10. **Use issue-first intake for new discoveries.** Accumulate pre-admission evidence on the evaluation issue; persist governed skill/source material and finalized companions only after a justified admission decision.
11. **Search before re-reviewing.** For historically reviewed admitted corpora, check current companions and recoverable prior evidence first. Re-review only genuine evidence gaps.
12. **Update this ledger when meaningful work lands.** The ledger should make the depth and frontier of the repository legible to the next reader.

## Current posture

**Core:** shareable and complete.

**Corpus:** broad, pinned, and intentionally larger than the fully governed shelf.

**Curation:** active indefinitely, with prior evidence to reconcile, a mandatory provenance-completeness audit in progress, and promising sources still to evaluate.

That is the intended steady state.
