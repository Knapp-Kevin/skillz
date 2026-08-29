---
name: skill-bootstrap
description: >-
  Build or refine the smallest dependable skill system for a user by discovering
  durable needs, translating them into capabilities, comparing governed skills
  and reference patterns, composing or creating the best fit, semantically
  reviewing the result, and adapting it to the active host. Use for first-visit
  or returning-user skill-system work.
metadata:
  author: frostwulf.zo.computer
  category: Meta
  display-name: Skill Bootstrap
  emoji: "🧰"
  version: 0.7.0
---

# Skill Bootstrap

Build the **smallest dependable skill system that fits the user and the environment they are actually using**.

This is the single canonical orchestrator for normal first-visit and returning-user work.

`skillz` is passive. The active agent reads these instructions and does the work with capabilities it legitimately has.

## Hard boundary

Normal user bootstrap is **not repository maintenance**.

Unless the user explicitly asked to maintain `skillz` itself:

- do not modify this repository;
- do not use repo-bound `skill-forge` as the user's artifact generator;
- do not require `skill-audit`, `skill-sync`, `skills-pulse`, source-vetting, repository scripts, or CI;
- do not assume a local clone, shell, Git, Node/Bun, initialized submodules, or writable filesystem;
- do not confuse the user's target skill location with this repository's `skills/` directory.

## Global stop rule

More evidence, more searching, and more skills are not inherently better.

Stop a stage when additional work is unlikely to materially change the next decision.

## S0 — Route

Choose exactly one route:

- `DIRECT_LIBRARY` — browse/search/compare/install a known skill; stop this bootstrap.
- `FIRST_VISIT` — build a fitted skill system.
- `RETURNING_USER` — review/refine an existing fitted system.
- `REPOSITORY_MAINTENANCE` — change `skillz` itself; stop this bootstrap and use maintainer procedures.

If FIRST_VISIT and RETURNING_USER are both plausible, inspect accessible current skill/profile state. If a meaningful fitted set exists, use RETURNING_USER.

**Output:** one route.

## S1 — Bind to environment and authority

Establish, as far as the host permits:

- explicit user instruction;
- applicable safety/security/project rules;
- available and unavailable evidence sources;
- read/write/tool capabilities;
- host/surface;
- installation/packaging capability;
- privacy, cost, and authority limits.

Use the strongest path actually available: repository-native, connector/API/web, or minimal read-only.

Unknown installation method does not block discovery. If still unknown at handoff, report that honestly.

**Output:** environment/authority record.

## S2 — Discover durable needs

Inspect the **minimum relevant evidence** needed to identify stable reusable patterns. Prefer already-exposed history, memory, workspace rules, existing skills, recurring corrections, repeated tool sequences, definitions of done, failure modes, and human-verification points.

For each candidate need record:

- observed evidence;
- inference, if any;
- recurrence/stability;
- failure or cost it prevents.

Do not mine unrelated private connectors merely because they are accessible.

Stop when more evidence is unlikely to change the capability requirements. Mark thinly supported items `PROVISIONAL`; never invent unavailable history.

**Output:** short durable-need list.

## S3 — Define capability requirements

Before searching by skill name, define for each need:

- required outcome;
- trigger and non-trigger conditions;
- safeguards/invariants;
- inputs and outputs;
- tool/authority needs;
- human judgment points;
- completion evidence.

If the behavior is too volatile, trivial, or rare for a skill, classify it `DYNAMIC`, `CHECKLIST/HELPER`, or `DO_NOT_CREATE`.

**Output:** capability requirements.

## S4 — Discover skills and components

Search by capability and controlled metadata, not filename resemblance alone.

Search in this order when available:

1. user's existing skills/instructions;
2. current project/repository skills;
3. local user-facing `skills/`;
4. built-in host capabilities;
5. approved vendor/reference sources;
6. individually governed tracked external skills;
7. live external sources only for a still-unmet material capability.

The broad vendored/tracked corpus is **reference/discovery material**, not blanket trusted inventory.

For each relevant candidate inspect:

- **whole-skill fit**;
- **component value** such as triggers, safeguards, decision gates, evidence rules, procedure fragments, failure handling, or abstractions.

Stop when every material requirement has an adequate candidate path or a justified custom/dynamic/no-skill path.

**Output:** capability-to-candidate/component map.

## S5 — Gate reuse and transferable material

### Unchanged third-party reuse

Check, as far as the host can truthfully establish:

- source/provenance;
- exact version/fingerprint;
- semantic quality state;
- license/attribution;
- dependencies;
- authority/side effects;
- portability/host assumptions.

Rules:

- `verified` or `validated` plus matching exact identity may be considered unchanged;
- `unverified` and legacy `trusted-baseline` are design evidence only;
- `stale`, `rejected`, and `retired` are excluded from normal unchanged selection;
- never invent an exact identity match.

### Component borrowing

A blocked whole skill may still contain a useful idea, but component reuse does not bypass governance. Check whether license/provenance, dependencies, rejection reason, authority, privacy, cost, or host assumptions affect the component.

Prefer an independently expressed clean implementation when copying source-specific text or ceremony would create avoidable risk or baggage.

**Output:** `ELIGIBLE_UNCHANGED`, `ADAPTATION_EVIDENCE_ONLY`, or `EXCLUDED` for whole-skill candidates, plus component constraints.

## S6 — Make the fit decision

Choose one disposition for each meaningful requirement:

- `SUFFICIENT`
- `REFINE`
- `ADOPT`
- `ADAPT`
- `SUPPLEMENT`
- `COMPOSE`
- `CREATE`
- `CHECKLIST/HELPER`
- `DYNAMIC`
- `DO_NOT_CREATE`

Do not prefer reuse merely because reuse is available.

**Output:** disposition map with a short reason per requirement.

## S7 — Extract transferable components

For every ADAPT, SUPPLEMENT, COMPOSE, or CREATE decision informed by a reference, record:

`source -> useful mechanism -> constraints -> destination -> omitted baggage`

Omit source-specific commands, terminology, ceremony, interview flows, file layouts, UX, and authority assumptions that do not belong in the user's system.

If a mechanism cannot be separated coherently from problematic assumptions, use an eligible whole skill or create an independently expressed implementation instead.

**Output:** component ledger.

## S8 — Compose the smallest coherent system

Resolve:

- responsibility boundaries;
- trigger overlap;
- precedence/conflicts;
- duplicate process authority;
- shared dependencies;
- user-wide versus project-specific behavior;
- what should remain dynamic.

Favor a few coherent composable skills over one omnibus skill or many microscopic skills.

If proposed skills repeatedly override each other, redraw responsibilities before artifact creation.

**Output:** final fitted-system architecture.

## S9 — Create/adapt artifacts for the active host

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
- provenance/attribution when material was copied or adapted.

Use host-specific packaging only when established. Otherwise produce portable Markdown preserving the semantic contract.

Do not use repo-bound `skill-forge` for normal user artifact creation.

Inability to write files is not inability to complete bootstrap. Produce complete portable artifacts instead.

**Output:** artifacts plus target format/location.

## S10 — Semantic adversarial review

Read each important custom/adapted artifact as a literal or weaker model might.

Challenge it for:

- incorrect or missed triggers;
- unnecessary ceremony;
- hidden tool/dependency assumptions;
- privacy overreach;
- unsafe authority/cost;
- duplicated process authority;
- reference contamination;
- missing failure handling;
- cross-skill conflicts;
- maintenance burden;
- false completion or certainty claims.

Use at least three representative readings:

1. **positive trigger** — should activate and guide correctly;
2. **non-trigger** — should stay out of the way;
3. **pressure/failure** — targets its highest-risk ambiguity or shortcut.

This is semantic, probabilistic review of instructions. Do not describe it as runtime proof.

**Output:** `PASS`, `REVISE`, `MERGE`, `SPLIT`, or `DELETE` for each artifact, with material findings and remaining uncertainty.

Revise material failures and review again. A serious safety/authority ambiguity is not averaged away by strong wording elsewhere.

## S11 — Install or hand off

Determine the target's real installation/handoff mode from the active host:

- `DIRECT-WRITE`
- `API-INSTALL`
- `UI-UPLOAD`
- `PORTABLE-HANDOFF`

Install only with both capability and authority. Otherwise provide the complete package and shortest correct handoff.

Finish each target with an explicit state such as:

- `INSTALLED + REVIEWED`
- `READY TO UPLOAD`
- `USER ACTION REQUIRED`
- `BLOCKED: HOST DOES NOT SUPPORT SKILLS`
- `BLOCKED: INSTALLATION METHOD NOT ESTABLISHED`

**Output:** installation/handoff state, one representative trigger example, and what success should look like.

## Returning-user path

A returning user starts from the fitted system already in use.

1. Inventory the current set, intended jobs, versions/fingerprints when available, and installation state.
2. Treat that system as primary evidence.
3. Re-bind the current environment/authority.
4. Identify only capabilities affected by changed needs, drift, overlap, failure, or a material gap.
5. Re-run S3 through S11 only for affected capabilities.
6. Preserve still-valid custom behavior.
7. Search only where material improvement is plausible.
8. Prefer the smallest justified change.
9. `NO CHANGE NEEDED` is correct when no material improvement is established.

## Completion record

Report without guessing:

```text
Route: FIRST_VISIT | RETURNING_USER
Evidence used: <source categories>
Evidence unavailable: <material gaps>
Needs found: <concise list>
Decisions: <SUFFICIENT/REFINE/ADOPT/ADAPT/SUPPLEMENT/COMPOSE/CREATE/etc.>
References/components used: <sources/mechanisms + constraints>
Artifacts produced: <names + format/location>
Semantic adversarial review: <positive/non-trigger/pressure findings>
Installation/handoff: <explicit state per target>
Remaining uncertainty: <only material unresolved items>
```

Do not end at recommendations if complete artifacts can be produced.

## Non-negotiable rules

- Compare before creation; there is no reuse quota.
- Fit the user before fitting the corpus.
- Search capabilities before filenames.
- Treat broad source material as reference/discovery, not blanket trusted inventory.
- Extract mechanisms without importing unnecessary ceremony.
- Component reuse does not bypass provenance, licensing, dependencies, authority, or rejection reasons.
- `verified` and `validated` are the only current unchanged-reuse quality states.
- Never fabricate identity, review state, installation, artifacts, or evidence.
- Do not mine unrelated private connectors.
- Do not mutate `skillz` during normal user bootstrap.
- Do not make repository-maintenance tooling a user prerequisite.
- Stop evidence/search expansion when it is no longer decision-relevant.
- Prefer the smallest coherent system over maximum skill count.