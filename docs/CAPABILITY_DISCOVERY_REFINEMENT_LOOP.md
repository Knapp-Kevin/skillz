# Continuous breadth → evidence → refinement → gap-fill program

**2026-11-01. Owner direction:** favor inclusive, comprehensive discovery before destructive narrowing; preserve competing schools of practice and methods. Use evaluation evidence to improve each domain, repeat discovery for revealed weaknesses, and only author a first-party skill when reusable prior art cannot satisfy a demonstrated capability need.

**This is repository-maintenance guidance, not a runtime, CI/scheduled job, autonomous installer, permission grant, or admission policy override.** An external authorized maintainer drives each iteration. [AGENT_START_HERE.md](../AGENT_START_HERE.md), [AGENTS.md](../AGENTS.md), [governed source registry](../registry/sources.yaml), [skill verification](skill-verification.md), and [security scanning](security-scanning.md) remain controlling contracts.

## 1. Maintain the universe of demand, not merely the number of skill files

The [provisional capability universe](discovery/2026-11-01/CAPABILITY_UNIVERSE.csv) currently contains **48 discovery families and 441 explicit subdomain checklist rows**: 25 previously defined families (including an unclassified catchall) and 23 new proposed specialist families. This is a **proposal**, not a unilateral change to controlled registry/taxonomy values; overlaps and family splits require review. A skills library is not complete because a file contains a promising category word.

For each subdomain, preserve three independent *denominators*:
- `candidate_entrypoints`: original-source exact-version SKILL.md records discoverable by path;
- `distinct_method_options`: actual methodologically differentiated implementations after semantic/source-relationship review;
- `qualified_options`: independently evaluated, license-compatible, security/authority-qualified options fit for the target host.

The initial `NOT_MAPPED / UNKNOWN / NOT_GRADED` statuses in the universe CSV are **intentional**. Do not convert unknown to zero, extrapolate one source into every related subdomain, or assign a quality score based on repository popularity or quantity.

## 2. Owner sequencing: comprehensive intake before comparative grading

**Current mode: COLLECTION / RIGHTS DISCLOSURE.** Broadly ingest original source references across all 48 provisional families and 441 subdomains. First pass should make every major category meaningfully represented by real, source-backed package paths and, where available, several independent source perspectives. Do **not** begin bulk behavioral ranking merely because a large number of files has been found.

For a subdomain to count as *provisionally represented*, it must have a mapped task outcome and at least one original pinned skill or documented evidence-backed source-search gap. Three independent methodological approaches per important subdomain remain a discovery target, not an admission quota. Record missing sources honestly and keep seeking additional specialist archives. A provisional representation score is not a qualification score.

At **every ingestion event**, preserve copyright/rights provenance immediately: pinned source license URL, restriction summary, per-skill license override where inspected, bundled-rights unknowns, and direct versus inspiration usage status. See [rights index](discovery/2026-11-01/RIGHTS_INDEX.md) and [licensing contract](SKILL_LICENSE_DISCLOSURE.md). Pending rights are not a reason to discard useful reference leads, but they **do block claims of unchanged reuse eligibility**. Only after substantial category representation should bulk comparative functional/security evaluations and quality grading become the dominant workstream. High-risk candidates may still require urgent safety triage to prevent accidental use.

## 3. Repeatable discovery-to-quality cycle

| Phase | Input | Active external host operation | Persistent passive evidence | Exit condition |
|---|---|---|---|---|
| A. Discover expansively | Explicit domain/subdomain needs | Search original repositories, registries, first-party and specialist sources, alternate languages and engines | Source lead, original owner, source URL, time, declared scope | Continue until a bounded search tranche has been recorded; don't declare a permanent exhaustiveness ceiling |
| B. Enumerate and preserve | Each discovered original source | Pin exact revision; enumerate complete Git tree or equivalent; record every SKILL.md, sibling assets and dependencies | Immutable commit, path, file blob, package tree, license pointers; candidate status | Every enumerated entrypoint is source-backed; duplicates retained as cross-references |
| C. Compare methods | Skill contents and target tasks | Classify same-byte, distribution copy, localization, fork, overlap, independent approach, specialist, or superseded | Source-relationship graph, task-differentiator notes, license conditions | A usable alternative view exists without treating synonyms as independent choices |
| D. Qualify and evaluate | Candidate packages, tasks and evaluation plan | Static provenance/license/authority triage, approved scanner, controlled with-vs-without-skill task tests, adversarial/negative tests and human domain review | Separate P, S, T, C and Q receipts; dated artifacts, reviewer, environment, scope, failure modes | A package's precise unchanged-reuse eligibility and limitations are evidence-backed |
| E. Diagnose and refine | Coverage ledger and failure evidence | Distinguish source scarcity, task weakness, portability, licensing, safety, out-of-date data and bad evaluation design; search again or adapt | Evidence-linked gap record and next decision | Weakness has a falsifiable cause and an authorized next action |
| F. Create only where warranted | Remaining substantiated task gap | Author original bounded skill or license-compatible adaptation, independently review, evaluate and seek maintainer admission | Draft skill package, provenance, evaluation baselines, safety/authority contracts | New skill meets the same evidence gates as reused packages before public eligibility |
| G. Re-evaluate and revisit | Updated sources / model / host / task mix | Repeat representative tests and source freshness checks; preserve prior versions and failure receipts | Dated comparison and drift evidence | Domain maturity is current, not inherited from stale assessment |

There is **no automatic loop executed by this repository**. The cycle is a repeatable instruction for external hosts during an explicitly authorized `REPOSITORY_MAINTENANCE` engagement.

## 4. Options and grades visible in index results

A comparison view for a specific subdomain must show **all viable independent choices** and still preserve unqualified prior-art references below them. Suggested display columns:

`domain/subdomain | exact skill identity | distinct method description | primary use-case | source/immutable revision | relation to alternatives | provenance P | security S | quality Q | portability T | currency C | licensing/authority | observed tasks and failures | current disposition | evidence links`.

- **Three independent approaches per important subdomain** is a discovery target where available, **not** a quota to admit three or fabricate diversity.
- A package's total grade stays `NOT_GRADED` if essential evidence is unknown. Show component statuses and failures instead of flattening them to five stars.
- Different host wrappers, fork names, translations, distribution copies or unchanged rebrands are not independent methodology evidence.
- More than three good methods may be useful; preserve narrow specialists, creative alternatives, distinct quality/latency/cost tradeoffs and accessibility-oriented options.
- Never erase rejected, superseded, unsafe or license-restricted **evidence records**. Keep their rationale, fingerprints and salvageable reference ideas; exclude them from unchanged recommendation if the current governed policy requires exclusion.

## 5. Evidence-based gap taxonomy

| Gap code | Meaning | Next action |
|---|---|---|
| `GAP_UNMAPPED` | No identity-level subdomain mapping yet; source records may exist | Map existing governed and discovery identities before claiming absence |
| `GAP_SOURCE_SCARCE` | Bounded source search found fewer genuinely distinct approaches than needed | Search other publishers, languages, ecosystems, standards and primary literature |
| `GAP_METHOD_DUPLICATE` | Apparent plurality is mostly mirrors, wrappers, translations or same-method forks | Keep paths linked but seek truly independent methods |
| `GAP_FUNCTIONAL` | Skill does not measurably improve or safely solve representative tasks | Fix prompts/steps, compare other candidates, or redesign |
| `GAP_SECURITY_AUTHORITY` | Unacceptable permissions, exfiltration, harmful side effects or unsafe defaults | Hold unchanged; isolate, narrow scope or seek safer reference |
| `GAP_RIGHTS` | No redistribution grant, contradictory per-package terms or rights-sensitive resources | Reference only, resolve rights or author an independent clean-room approach |
| `GAP_PORTABILITY` | Too host-specific, dependent on inaccessible tools/services, or not reproducible | Adapt with permission or find portable alternative |
| `GAP_FRESHNESS` | Pin obsolete, upstream changed, scientific or professional content outdated | Refresh and requalify exact revision; never silently carry old grade forward |
| `GAP_SPECIALIST_REVIEW` | High-stakes field lacks competent acceptance evidence | Require specialist reviewer; do not infer correctness from tests alone |
| `GAP_EVAL_MISSING` | Test suite cannot distinguish successful outcomes or negative cases | Improve evaluation first; do not manufacture performance metrics |

Each gap record should contain: `domain_id, subdomain_id, target_task, expected_output, candidate_ids, search_receipts, test_receipts, gap_code, severity, alternatives, disposition, reviewer, review_date, next_discovery_query, success_check`.

## 6. Guardrail for creating missing skills

Start authoring a new first-party `skillz` corpus candidate **only when** an identified task matters, previous references have been searched and compared, and there is evidence that existing eligible methods are absent, unsuitable, unsafe, too restrictive or meaningfully underperforming. A sparse count alone is not a reason.

A draft must include:
1. Bounded intent, triggers, non-triggers, expected artifacts and realistic user outcome.
2. Original text or lawfully adapted components with clear sources; no laundering noncommercial/proprietary instructions into the corpus.
3. Allowed tools, side-effect/egress authority, data minimization, consent gates and host dependencies.
4. Worked positive and negative cases, with-vs-without-skill baseline tasks and reproducibility/portability evidence.
5. Independent review, security receipts when applicable, release/change history and rollback route. High-stakes medical, veterinary, financial, legal, public-safety and physical-motion use cases require specialist acceptance.
6. An explicit `DRAFT_NOT_ADMITTED` state until repository-maintainer authority, controlled registry updates and eligibility gates are satisfied.

Normal user-specific skill creation belongs **in the user's active host or portable handoff**, not in this corpus. The owner has explicitly authorized ongoing `skillz` **repository maintenance** here; that permission does not bypass third-party rights or give new drafts automatic admission.

## 7. Priority of work right now

**Expansion first**, without pretending collection is qualification:
1. Maintain the full [65-source / 4,835-entrypoint reference collection](discovery/2026-11-01/INDEX.md), [per-skill original licensing evidence](discovery/2026-11-01/RIGHTS_INDEX.md), and expand into unrepresented disciplines.
2. Cross-map those records and the **995 governed third-party review identities** into the 441 provisional checklist rows. Preserve the 44 first-party and existing review denominators independently.
3. Identify real alternatives at the method and task level. Keep creative divergence visible.
4. **After broad subdomain representation**, qualify/evaluate promising alternatives and safety-critical cases with an authorized external evaluator. Keep licensing/authority triage at intake time.
5. Use evaluated weaknesses to drive targeted new searches, adaptations or original gap-fill drafts. Repeat.

**Acceptance for a claim of “strong” domain coverage:** every critical subdomain has a defined target task, at least one evidence-qualified safe option, explicit alternative search results, maintained source identity and comparable quality evidence. Where multiple high-quality independent options exist, present the choice. **“Mature”** additionally requires refreshed, independently reproduced task and adversarial evidence. No current domain has been proven to meet this standard in the discovery receipts.

This document deliberately leaves `registry/taxonomy.yaml`, original admitted counts and CI untouched.
