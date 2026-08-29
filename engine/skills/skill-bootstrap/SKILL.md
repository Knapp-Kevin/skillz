---
name: skill-bootstrap
description: >-
  Discover and build the smallest useful portable skill system for a user by
  inspecting legitimate user evidence, translating needs into capabilities,
  searching the governed corpus, extracting useful skill components, composing
  or creating the best-fit artifacts, validating them, and adapting the result
  to the active host. Use when the user gives you this repository or its URL
  without another task, asks to bootstrap or improve their skills, or wants
  working methods to transfer between agent hosts.
metadata:
  author: frostwulf.zo.computer
  category: Meta
  display-name: Skill Bootstrap
  emoji: "🧰"
  version: 0.5.0
---

# Skill Bootstrap

Build the **smallest dependable skill system that fits the user and the environment they are actually using**.

This is the single canonical orchestration skill for normal first-visit and returning-user bootstrap work.

`skillz` is passive. The active agent does the discovery, reasoning, synthesis, validation, packaging, and handoff using capabilities it legitimately has.

## Hard boundary: user work is not repository maintenance

During normal bootstrap, **do not modify the `skillz` repository** unless the user explicitly asked to maintain or develop `skillz` itself.

In particular:

- do not use repo-bound `skill-forge` as the default way to create the user's skills;
- do not require repo-bound `skill-audit`, `skill-sync`, `skills-pulse`, or source-vetting procedures;
- do not assume a local clone, shell, Git executable, Node/Bun, initialized submodules, or GitHub Actions;
- do not confuse a user's target skill directory with this repository's `skills/` directory.

Repo-bound helpers under `engine/skills/` are maintainer tools. Normal bootstrap must be completable through repository-native, connector/API/web, or read-only artifact handoff paths.

## Default entry behavior

If the user gives the agent this repository or its URL without a narrower task, begin bootstrap. Do not stop at a repository summary, catalog dump, or request that the user choose skills manually.

If the user already has a fitted skill system and asks to review or improve it, use the returning-user flow below instead of rebuilding from zero.

## Canonical state machine

Follow these stages in order. Do not skip a stage because the next action feels obvious.

Each stage has an input, required action, output, and fallback. The output becomes the next stage's input.

### S0 — Route

**Input:** the user's request and current context.

**Action:** classify the request as one of:

- `DIRECT_LIBRARY` — user named a skill or only wants browse/search/compare/install help;
- `FIRST_VISIT` — user wants a fitted skill system and no existing fitted system is being reviewed;
- `RETURNING_USER` — user already has a fitted system to review/refine;
- `REPOSITORY_MAINTENANCE` — user explicitly wants to change `skillz` itself.

**Output:** one route.

**Fallback:** if both FIRST_VISIT and RETURNING_USER appear plausible, inspect accessible current skill/profile state. If a meaningful fitted set exists, use RETURNING_USER. Do not interrogate the user merely to resolve something the host can inspect.

Stop this skill for `DIRECT_LIBRARY` or `REPOSITORY_MAINTENANCE`; use the appropriate path instead.

### S1 — Bind to environment and authority

**Input:** routed bootstrap request.

**Action:** establish:

- current explicit user instruction;
- applicable safety, security, repository, or workspace rules;
- available evidence sources;
- available read/write tools;
- current agent host and surface when knowable;
- installation or packaging capabilities;
- privacy and authority limits.

Use the strongest capability path available:

1. repository-native;
2. connector/API/web;
3. minimal read-only.

**Output:** an environment record containing `host`, `surface`, `read_capabilities`, `write_capabilities`, `evidence_available`, `evidence_unavailable`, `authority_limits`, and `installation_capability`.

**Fallback:** unknown host does not block discovery. Record installation as `BLOCKED: INSTALLATION METHOD NOT ESTABLISHED` only if the installation method still cannot be established at handoff time.

### S2 — Discover durable user needs

**Input:** environment record plus legitimate accessible evidence.

**Action:** inspect the minimum relevant evidence needed. Prefer already-exposed conversation history, memory, workspace rules, current skills, repeated corrections, recurring tool sequences, definitions of done, recurring failure modes, and repeated human verification points.

Look for stable reusable patterns, not biographical trivia.

For each candidate need, record:

- observed evidence;
- inference, if any;
- recurrence/stability;
- failure or cost it prevents;
- current workaround, if visible.

Do not sweep unrelated private connectors merely because access exists. Connector availability is not consent to profile the user.

**Output:** a short list of durable need statements.

**Fallback:** if evidence is too thin for durable inference, mark uncertain items `PROVISIONAL`. Do not fabricate history. Continue with what is supportable.

### S3 — Translate needs into capability requirements

**Input:** durable need statements.

**Action:** describe what the fitted system must accomplish **before searching by skill name**.

For each need define:

- required outcome;
- trigger conditions;
- non-trigger conditions;
- important invariants/safeguards;
- required inputs and outputs;
- tool/authority needs;
- human judgment points;
- completion evidence.

**Output:** capability requirements.

**Fallback:** if a requirement is too volatile or trivial to formalize, classify it `DYNAMIC` or `CHECKLIST/HELPER` and do not force a skill.

### S4 — Discover candidate skills and components

**Input:** capability requirements.

**Action:** search the governed reference surface by capability and metadata, not filename resemblance alone.

Search in this order when available:

1. user's existing skills and instructions;
2. current project/repository skills;
3. local user-facing `skills/`;
4. built-in host capabilities;
5. approved indexed vendor sources;
6. individually characterized tracked external skills;
7. live external sources only when the governed corpus is inadequate and current task scope permits discovery.

Use controlled metadata such as use case, lifecycle, characteristics, authority, and portability to narrow candidates.

For every relevant candidate inspect both:

- **whole-skill fit** — could this skill be used substantially as written?
- **component value** — are only its triggers, safeguards, procedure fragments, evidence rules, tests, failure handling, or abstractions useful?

Do not make the human browse the catalog unless they explicitly asked to browse it.

**Output:** candidate map linking each capability requirement to zero or more whole-skill candidates and reusable components.

**Fallback:** zero good candidates is a valid result. Continue toward custom creation instead of forcing reuse.

### S5 — Eligibility gate

**Input:** candidate map.

**Action:** before unchanged third-party reuse, establish as much of the following as the host can truthfully verify:

- canonical source and provenance;
- exact version/fingerprint identity;
- current quality state;
- license/attribution requirements;
- package/dependency completeness;
- authority/side-effect level;
- portability/environment assumptions.

Current unchanged-reuse rule:

- `verified` or `validated` + matching exact fingerprint may be considered for unchanged reuse;
- `unverified` and legacy `trusted-baseline` are design evidence only;
- `stale`, `rejected`, and `retired` are excluded from normal unchanged selection;
- if exact identity cannot be established, do not invent a match.

Quality state establishes eligibility, not user fit.

**Output:** each candidate marked `ELIGIBLE_UNCHANGED`, `ADAPTATION_EVIDENCE_ONLY`, or `EXCLUDED` with the reason.

**Fallback:** when exact proof is unavailable, prefer adaptation/custom synthesis or another candidate with stronger evidence.

### S6 — Make the fit decision

**Input:** capability requirements plus gated candidates.

**Action:** choose one explicit disposition for every meaningful requirement:

- `SUFFICIENT` — existing user skill already does the job;
- `REFINE` — existing user skill has the right abstraction but needs improvement;
- `ADOPT` — eligible reference fits substantially unchanged;
- `ADAPT` — reference is the best base but needs environmental/workflow changes;
- `SUPPLEMENT` — keep the user's workflow and borrow one or more useful mechanisms;
- `COMPOSE` — separate skills should cooperate without being merged;
- `CREATE` — a clean custom skill is the best fit;
- `CHECKLIST/HELPER` — formal skill is excessive;
- `DYNAMIC` — preserve adaptive reasoning instead of encoding it;
- `DO_NOT_CREATE` — rare, redundant, unstable, or unjustified.

Do not prefer reuse merely because reuse is available.

**Output:** disposition map with one-sentence rationale per requirement.

### S7 — Extract transferable components

**Input:** disposition map and source candidates.

**Action:** for every ADAPT, SUPPLEMENT, COMPOSE, or CREATE decision that uses reference evidence, identify exactly what is worth carrying forward.

Possible components include:

- trigger/non-trigger logic;
- ordered procedure;
- decision gates;
- evidence requirements;
- authority boundaries;
- failure fallbacks;
- validation tests;
- output contract;
- useful abstractions.

Explicitly reject unnecessary source-specific ceremony, terminology, commands, interview flows, file layouts, or authority assumptions.

**Output:** a component ledger: `source -> useful mechanism -> destination -> omitted baggage`.

**Fallback:** if the useful mechanism cannot be separated safely from the source's assumptions, use the whole eligible skill or create a clean implementation instead.

### S8 — Compose the smallest coherent system

**Input:** disposition map plus component ledger.

**Action:** design the final fitted set. Resolve:

- responsibility boundaries;
- trigger overlap;
- precedence;
- conflicting instructions;
- duplicate process authority;
- shared dependencies;
- universal/user-wide versus domain/project behavior;
- what should remain dynamic.

Favor a small number of coherent, composable skills over one giant omnibus skill or dozens of microscopic skills.

**Output:** final skill-system architecture.

**Fallback:** if two proposed skills repeatedly need to override each other, merge or redraw responsibilities before artifact creation.

### S9 — Adapt artifacts to the active environment

**Input:** final architecture plus environment record.

**Action:** create the actual user-facing skill artifacts in the representation supported by the target environment.

For each artifact define at minimum:

- name and purpose;
- triggers and non-triggers;
- inputs and outputs;
- required and optional tools;
- ordered procedure;
- decision points;
- authority/security boundaries;
- human verification points;
- failure handling;
- completion criteria;
- validation checks;
- provenance when material was copied or adapted.

Use the current host's packaging conventions when established. Otherwise produce a portable Markdown skill artifact that preserves the semantic contract and can be adapted later.

**Do not use repo-bound `skill-forge` for normal user artifact creation.** Create files directly in the user's target workspace when authorized, use the host's artifact surface, or provide the complete artifact in the response/handoff package.

**Output:** complete artifacts plus target locations/formats.

**Fallback:** inability to write files is not inability to complete bootstrap. Produce exact portable artifacts and continue.

### S10 — Adversarial review and validation

**Input:** complete artifacts.

**Action:** attack the fitted system for:

- overfitting/underfitting;
- incorrect or missed triggers;
- unnecessary ceremony;
- hidden tool assumptions;
- privacy overreach;
- unsafe authority;
- duplicated process authority;
- reference contamination;
- missing evidence/failure handling;
- cross-skill conflicts;
- maintenance burden.

For important custom or adapted behavior, define representative success checks before treatment and run behavioral comparison when the host can actually provide isolated evidence.

Never claim behavioral validation that did not run. Record `not run` or the actual limitation instead.

**Output:** `PASS`, `REVISE`, `MERGE`, `SPLIT`, or `DELETE` for each artifact, plus truthful validation status.

**Fallback:** revise failing artifacts and repeat this stage. A security-relevant failure is not averaged away by stronger scores elsewhere.

### S11 — Install or hand off

**Input:** reviewed artifacts plus environment record.

**Action:** determine one installation mode per target:

- `DIRECT-WRITE`;
- `API-INSTALL`;
- `UI-UPLOAD`;
- `PORTABLE-HANDOFF`.

Verify the current host's installation method from authoritative local or current official documentation when needed.

Install only when the agent has both capability and authority. Otherwise create the exact package and give the shortest correct beginner-readable handoff.

Finish each target with one state:

- `INSTALLED + VERIFIED`;
- `INSTALLED, VERIFICATION PENDING`;
- `READY TO UPLOAD`;
- `USER ACTION REQUIRED`;
- `BLOCKED: HOST DOES NOT SUPPORT SKILLS`;
- `BLOCKED: INSTALLATION METHOD NOT ESTABLISHED`.

**Output:** installed state or portable package, one trigger smoke test, and what success looks like.

Bootstrap is not complete until this state is explicit.

## Returning-user flow

A returning user does not need S2 performed as if nothing exists.

1. Inventory the current fitted set, versions/fingerprints, intended jobs, and installation state.
2. Treat the existing system as primary evidence.
3. Re-run S1 for the current environment.
4. Compare present needs with current responsibilities, drift, overlap, stale evidence, failures, and gaps.
5. Search only where a material improvement or missing capability is plausible.
6. Preserve still-valid custom behavior.
7. Run S5-S11 only for affected capabilities.
8. Prefer the smallest justified change.
9. `NO CHANGE NEEDED` is a correct outcome when no material improvement is established.

## Completion record

At the end, the agent must be able to report these fields without guessing:

```text
Route: FIRST_VISIT | RETURNING_USER
Evidence used: <source categories, not copied private content>
Evidence unavailable: <important unavailable categories>
Needs found: <count + concise list>
Decisions: <SUFFICIENT/REFINE/ADOPT/ADAPT/SUPPLEMENT/COMPOSE/CREATE/etc.>
References used: <whole skills and/or components>
Artifacts produced: <names + target format/location>
Structured review: <pass/revisions>
Behavioral validation: <performed evidence | not run + reason>
Installation/handoff: <explicit state per target>
Remaining uncertainty: <only material unresolved items>
```

Do not end at recommendations if complete artifacts can be produced.

## Non-negotiable rules

- Compare before creation, but there is no reuse quota.
- Fit the user before fitting the corpus.
- Search capabilities before filenames.
- Treat the corpus as reference material, not the deliverable.
- Extract mechanisms without importing unnecessary ceremony.
- `verified` and `validated` are the only current unchanged-reuse quality states.
- Never fabricate fingerprint, validation, installation, or evidence claims.
- Do not mine unrelated private connectors.
- Do not mutate `skillz` during normal user bootstrap.
- Do not make maintainer runtime a user prerequisite.
- Prefer the smallest coherent system over maximum skill count.
