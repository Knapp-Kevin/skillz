---
name: skill-bootstrap
description: >-
  Discover and build the smallest useful portable skill system for a user by
  inspecting legitimate user evidence, translating needs into capabilities,
  searching the governed and reference corpus, extracting safe reusable
  components, composing or creating the best-fit artifacts, validating them,
  and adapting the result to the active host. Use when the user gives you this
  repository or its URL without another task, asks to bootstrap or improve
  their skills, or wants working methods to transfer between agent hosts.
metadata:
  author: frostwulf.zo.computer
  category: Meta
  display-name: Skill Bootstrap
  emoji: "🧰"
  version: 0.6.0
---

# Skill Bootstrap

Build the **smallest dependable skill system that fits the user and the environment they are actually using**.

This is the single canonical orchestrator for normal first-visit and returning-user skill-system work.

`skillz` is passive. The active agent performs discovery, comparison, synthesis, validation, packaging, and handoff using capabilities it legitimately has.

## Hard boundary: user work is not repository maintenance

During normal bootstrap, **do not modify the `skillz` repository** unless the user explicitly asked to maintain or develop `skillz` itself.

In particular:

- do not use repo-bound `skill-forge` as the default way to create the user's skills;
- do not require repo-bound `skill-audit`, `skill-sync`, `skills-pulse`, or source-vetting procedures;
- do not assume a local clone, shell, Git executable, Node/Bun, initialized submodules, writable repository, or GitHub Actions;
- do not confuse the user's target skill location with this repository's `skills/` directory.

Repo-bound helpers under `engine/skills/` are maintainer tools. Normal bootstrap must remain possible through repository-native, connector/API/web, or read-only portable-handoff paths.

## Default entry behavior

If the user gives the agent this repository or its URL without a narrower task, begin bootstrap. Do not stop at a repository summary, catalog dump, or request that the user manually choose skills.

If the user already has a fitted skill system and asks to review or improve it, use the returning-user path instead of rebuilding from zero.

## Global stop rules

More evidence, more searching, and more skills are not inherently better.

Stop expanding a stage when its additional work is unlikely to materially change the next decision.

Specifically:

- stop evidence collection when the current evidence is sufficient to define stable capability requirements;
- stop corpus search when adequate fit is established and no material requirement remains uncovered;
- do not search live external sources for novelty after the governed/reference corpus already provides an adequate answer;
- do not create a formal skill for a volatile, trivial, rare, or better-left-dynamic behavior;
- do not continue refining merely to produce visible change for a returning user.

## Canonical state machine

Follow the stages in order. Each stage has an input, required action, output, and fallback. The output becomes the next stage's input.

### S0 — Route

**Input:** user request and current context.

**Action:** choose exactly one route:

- `DIRECT_LIBRARY` — user named a skill or wants browse/search/compare/install help only;
- `FIRST_VISIT` — user wants a fitted system and no existing fitted system is being reviewed;
- `RETURNING_USER` — user already has a fitted system to review/refine;
- `REPOSITORY_MAINTENANCE` — user explicitly wants to change `skillz` itself.

**Output:** one route.

**Fallback:** if FIRST_VISIT and RETURNING_USER both seem plausible, inspect accessible current skill/profile state. If a meaningful fitted set exists, use RETURNING_USER. Do not ask the user to resolve information the host can already inspect.

Stop this skill for `DIRECT_LIBRARY` or `REPOSITORY_MAINTENANCE` and use the appropriate path instead.

### S1 — Bind to environment and authority

**Input:** routed bootstrap request.

**Action:** establish, as far as the host permits:

- current explicit user instruction;
- applicable safety/security/project/workspace rules;
- available and unavailable evidence sources;
- read/write/tool capabilities;
- current host and surface;
- installation/packaging capability;
- privacy, cost, and authority limits.

Use the strongest capability path actually available:

1. repository-native;
2. connector/API/web;
3. minimal read-only.

**Output:** environment record with `host`, `surface`, `read_capabilities`, `write_capabilities`, `evidence_available`, `evidence_unavailable`, `authority_limits`, and `installation_capability`.

**Fallback:** an unknown installation method does not block discovery. If it remains unknown at handoff time, report `BLOCKED: INSTALLATION METHOD NOT ESTABLISHED` rather than guessing.

### S2 — Discover durable user needs

**Input:** environment record plus legitimate accessible evidence.

**Action:** inspect the **minimum relevant evidence** needed to identify stable reusable patterns. Prefer already-exposed conversation history, persistent memory, workspace rules, existing skills, recurring corrections, repeated tool sequences, definitions of done, recurring failure modes, and repeated human-verification points.

For each candidate need, record:

- observed evidence;
- inference, if any;
- recurrence/stability;
- failure/cost it prevents;
- current workaround, if visible.

Do not sweep unrelated private connectors merely because they exist. Capability to access a private source is not consent to profile the user from it.

**Stop condition:** stop collecting evidence when additional sources are unlikely to materially change the capability requirements. Do not build a comprehensive personal profile for the sake of feeling thorough.

**Output:** short list of durable need statements.

**Fallback:** if evidence is thin, mark uncertain items `PROVISIONAL`. Never reconstruct unavailable history from assumptions.

### S3 — Translate needs into capability requirements

**Input:** durable need statements.

**Action:** define what the fitted system must accomplish **before searching by skill name**.

For each need define:

- required outcome;
- trigger and non-trigger conditions;
- important invariants/safeguards;
- required inputs/outputs;
- tool/authority needs;
- human judgment points;
- completion evidence.

**Output:** capability requirements.

**Fallback:** classify requirements that are too volatile or trivial to formalize as `DYNAMIC`, `CHECKLIST/HELPER`, or `DO_NOT_CREATE` rather than forcing a skill.

### S4 — Discover candidate skills and components

**Input:** capability requirements.

**Action:** search by capability and controlled metadata, not filename resemblance alone.

Search in this order when available:

1. user's existing skills and instructions;
2. current project/repository skills;
3. local user-facing `skills/`;
4. built-in host capabilities;
5. approved indexed vendor/reference sources;
6. individually governed tracked external skills;
7. live external sources only for a still-unmet material capability and only when current task scope permits it.

The broad vendored/tracked corpus is **reference/discovery material**. It does not receive unchanged-reuse eligibility merely because it is present or comes from an official source.

Use controlled metadata such as use case, lifecycle, characteristics, authority, and portability to narrow candidates.

For each relevant candidate inspect both:

- **whole-skill fit** — could it be used substantially as written?
- **component value** — are only its triggers, safeguards, procedure fragments, evidence rules, tests, failure handling, or abstractions useful?

**Stop condition:** once every material requirement has an adequate candidate path or a justified CREATE/DYNAMIC/no-skill path, stop searching. Do not continue into external sources merely to maximize novelty.

When live external discovery is necessary, bound it to the unmet capability. Newly found material remains design evidence until its exact provenance/quality is governed well enough for stronger use.

**Output:** candidate map linking requirements to whole-skill candidates and reusable components.

**Fallback:** zero adequate candidates is valid. Continue toward custom creation instead of forcing reuse.

### S5 — Gate eligibility and transferable material

**Input:** candidate map.

**Action A: unchanged third-party reuse.** Establish as much as the host can truthfully verify:

- canonical source/provenance;
- exact version/fingerprint;
- current quality state;
- license/attribution obligations;
- package/dependency completeness;
- authority/side-effect level;
- portability/environment assumptions.

Current unchanged-reuse rule:

- `verified` or `validated` plus matching exact identity may be considered for unchanged reuse;
- `unverified` and legacy `trusted-baseline` are design evidence only;
- `stale`, `rejected`, and `retired` are excluded from normal unchanged selection;
- when exact identity cannot be established, do not invent a match.

**Action B: component borrowing/adaptation.** A blocked whole skill may still contain useful ideas, but component reuse does not bypass governance. Before materially carrying source content or a mechanism forward, check:

- source and applicable license/attribution obligations;
- dependency/package assumptions attached to the component;
- whether the whole-skill rejection/staleness reason affects the component;
- privacy, authority, cost, and side-effect assumptions;
- host-specific assumptions;
- whether an independently expressed clean implementation is safer than copying source-specific text/ceremony.

A general principle may inform clean custom design. Material copying or adaptation remains subject to provenance and license obligations.

**Output:** each whole-skill candidate marked `ELIGIBLE_UNCHANGED`, `ADAPTATION_EVIDENCE_ONLY`, or `EXCLUDED`, plus component-level constraints for anything that may be borrowed.

**Fallback:** when proof is insufficient, prefer clean adaptation/custom synthesis or a better-established candidate.

### S6 — Make the fit decision

**Input:** capability requirements plus gated candidates.

**Action:** choose one explicit disposition for every meaningful requirement:

- `SUFFICIENT` — existing user skill already does the job;
- `REFINE` — existing user skill has the right abstraction but needs improvement;
- `ADOPT` — eligible reference fits substantially unchanged;
- `ADAPT` — reference is the best base but needs workflow/environment changes;
- `SUPPLEMENT` — keep the user's workflow and borrow bounded mechanisms;
- `COMPOSE` — separate skills should cooperate without being merged;
- `CREATE` — clean custom skill is the best fit;
- `CHECKLIST/HELPER` — formal skill is excessive;
- `DYNAMIC` — preserve adaptive reasoning instead of encoding it;
- `DO_NOT_CREATE` — rare, redundant, unstable, or unjustified.

Do not prefer reuse merely because reuse is available.

**Output:** disposition map with a one-sentence reason per requirement.

### S7 — Extract transferable components

**Input:** disposition map and gated references.

**Action:** for every ADAPT, SUPPLEMENT, COMPOSE, or CREATE decision informed by a reference, identify exactly what is worth carrying forward.

Components may include:

- trigger/non-trigger logic;
- ordered procedure;
- decision gates;
- evidence requirements;
- authority boundaries;
- failure fallbacks;
- validation tests;
- output contract;
- useful abstractions.

For every material component record:

`source -> exact mechanism/idea -> governance/license constraints -> destination -> omitted baggage`

Explicitly omit unnecessary source-specific commands, terminology, ceremony, interview flows, file layouts, UX, or authority assumptions.

**Output:** component ledger.

**Fallback:** if a useful mechanism cannot be separated safely/legal-coherently from source assumptions, either use the whole eligible skill as governed or create an independently expressed clean implementation.

### S8 — Compose the smallest coherent system

**Input:** disposition map plus component ledger.

**Action:** design the fitted system and resolve:

- responsibility boundaries;
- trigger overlap;
- precedence;
- conflicting instructions;
- duplicate process authority;
- shared dependencies;
- universal/user-wide versus domain/project behavior;
- what should remain dynamic.

Favor a few coherent composable skills over one omnibus skill or dozens of microscopic ones.

**Output:** final skill-system architecture.

**Fallback:** if two proposed skills repeatedly override each other, merge or redraw responsibilities before artifact creation.

### S9 — Adapt/create artifacts for the active environment

**Input:** final architecture plus environment record.

**Action:** create actual user-facing artifacts in the representation supported by the target environment.

For each artifact define at minimum:

- name/purpose;
- triggers/non-triggers;
- inputs/outputs;
- required/optional tools;
- ordered procedure;
- decision points;
- authority/security/privacy boundaries;
- human-verification points;
- failure handling;
- completion criteria;
- validation checks;
- provenance/attribution when material was copied or adapted.

Use the current host's packaging conventions only when established. Otherwise produce a portable Markdown artifact preserving the semantic contract.

**Do not use repo-bound `skill-forge` for normal user artifact creation.** Write to the user's target workspace when authorized, use the active host's artifact surface, or provide complete portable artifacts.

**Output:** complete artifacts plus target format/location.

**Fallback:** inability to write files is not inability to complete bootstrap. Produce exact portable artifacts and continue.

### S10 — Adversarial review and validation

**Input:** complete artifacts.

**Action:** attack the fitted system for:

- overfitting/underfitting;
- incorrect or missed triggers;
- unnecessary ceremony;
- hidden tool/dependency assumptions;
- privacy overreach;
- unsafe authority/cost;
- duplicated process authority;
- reference contamination;
- missing evidence/failure handling;
- cross-skill conflicts;
- maintenance burden;
- false completion or validation claims.

For every important custom/adapted artifact, perform at least a **static three-case check** even when isolated behavioral execution is unavailable:

1. a positive trigger case;
2. a non-trigger case;
3. a pressure/failure case targeting its highest-risk behavior.

When the host can provide genuinely isolated treatment evidence, predefine success checks and run behavioral comparison. Never convert a static thought experiment into a claim that behavioral validation ran.

**Output:** `PASS`, `REVISE`, `MERGE`, `SPLIT`, or `DELETE` for each artifact, static case results, and truthful behavioral-validation status.

**Fallback:** revise failures and repeat this stage. A security-relevant failure is not averaged away by stronger scores elsewhere.

If a stage failed, classify the failure as one of:

- `REPOSITORY_AMBIGUITY`;
- `BROKEN_OR_STALE_REFERENCE`;
- `HOST_CAPABILITY_LIMITATION`;
- `MISSING_EVIDENCE`;
- `MODEL_NONCOMPLIANCE` after the instruction was otherwise clear.

Repeated failures at the same step should be treated as repository/design evidence, not dismissed reflexively as model stupidity.

### S11 — Install or hand off

**Input:** reviewed artifacts plus environment record.

**Action:** determine one installation mode per target:

- `DIRECT-WRITE`;
- `API-INSTALL`;
- `UI-UPLOAD`;
- `PORTABLE-HANDOFF`.

Verify the host's current installation method from authoritative local/current official documentation when needed.

Install only with both capability and authority. Otherwise create the exact package and give the shortest correct beginner-readable handoff.

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

A returning user starts from the current fitted system rather than pretending no prior work exists.

1. Inventory the fitted set, versions/fingerprints, intended jobs, and installation state.
2. Treat the existing system as primary evidence.
3. Re-run S1 for the current environment.
4. Identify only capabilities affected by changed needs, drift, overlap, failure, or a material gap.
5. For affected capabilities, re-run **S3 through S11**. Do not skip capability definition or capability-first search merely because an old skill already exists.
6. Preserve still-valid custom behavior.
7. Search only where a material improvement or missing capability is plausible.
8. Prefer the smallest justified change.
9. `NO CHANGE NEEDED` is correct when no material improvement is established.

## Completion record

At the end, report these fields without guessing:

```text
Route: FIRST_VISIT | RETURNING_USER
Evidence used: <source categories, not copied private content>
Evidence unavailable: <important unavailable categories>
Needs found: <count + concise list>
Decisions: <SUFFICIENT/REFINE/ADOPT/ADAPT/SUPPLEMENT/COMPOSE/CREATE/etc.>
References/components used: <whole skills and/or mechanisms + provenance constraints>
Artifacts produced: <names + target format/location>
Static adversarial checks: <positive/non-trigger/pressure results>
Behavioral validation: <performed evidence | not run + reason>
Installation/handoff: <explicit state per target>
Failure classification: <only if a material stage failed>
Remaining uncertainty: <only material unresolved items>
```

Do not end at recommendations if complete artifacts can be produced.

## Non-negotiable rules

- Compare before creation, but there is no reuse quota.
- Fit the user before fitting the corpus.
- Search capabilities before filenames.
- Treat the broad corpus as reference/discovery material, not blanket trusted inventory.
- Extract mechanisms without importing unnecessary ceremony.
- Component reuse does not bypass provenance, licensing, dependency, authority, or rejection reasons.
- `verified` and `validated` are the only current unchanged-reuse quality states.
- Never fabricate fingerprint, validation, installation, artifact, or evidence claims.
- Do not mine unrelated private connectors.
- Do not mutate `skillz` during normal user bootstrap.
- Do not make maintainer runtime a user prerequisite.
- Stop evidence/search expansion when it is no longer decision-relevant.
- Prefer the smallest coherent system over maximum skill count.