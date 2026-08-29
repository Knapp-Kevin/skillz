---
name: skill-bootstrap
description: >-
  Discover and build the smallest useful portable skill system for a user by
  reviewing legitimately available context, identifying durable working methods,
  comparing them against the governed skill corpus, and reusing, adapting,
  extracting, composing, or creating skills as justified. Use when the user gives
  an agent this repository, asks to bootstrap or refine their skills, or wants
  repeatable working methods to transfer across agent hosts.
metadata:
  author: frostwulf.zo.computer
  category: Meta
  display-name: Skill Bootstrap
  emoji: "🧰"
  version: 1.0.0
---

# Skill Bootstrap

This is a passive instruction set for the external agent reading `skillz`. The repository does not run discovery, select candidates, install skills, call tools, or execute validation.

## Goal

Turn durable working behavior already established between a user and an agent into the smallest useful portable skill set.

The corpus is reference and design material, not a shopping catalog. A good result may:

- reuse an existing skill unchanged;
- adapt an existing skill;
- extract one useful pattern without adopting the rest;
- supplement a user's existing skill;
- compose several independent skills;
- create a new custom skill;
- use a lightweight checklist when a formal skill would be excessive;
- make no durable change when evidence is weak or the behavior is too volatile.

## Evidence boundary

Inspect only information the host agent legitimately exposes and that is relevant to the task, such as:

- current conversation;
- accessible interaction history or persistent memory;
- recurring user corrections;
- project/workspace instructions;
- existing skills;
- repeated tool or workflow patterns;
- definitions of done;
- relevant repositories or artifacts already in scope.

Do not infer hidden model state. Do not sweep unrelated private connectors merely because access exists. Capability is not consent.

Distinguish:

- **preference/profile fact**: useful context but usually not a skill;
- **project-local rule**: belongs with that project rather than the user's portable skill set;
- **repeatable method**: a genuine skill candidate.

## Procedure

### 1. Establish the environment

Identify explicit user goals and restrictions, authoritative project instructions, relevant evidence the host can inspect, existing fitted skills, and capabilities the external host can use if later action is requested. Record unavailable evidence rather than guessing.

### 2. Find latent skills

Look for repeated corrections, reasoning sequences, tool combinations, failure-prevention rules, governance boundaries, human-verification points, definitions of done, workflows repeatedly reconstructed from scratch, and existing skills that are too generic or incomplete.

A repeated procedure living only in interaction history or memory may be a latent skill even if the user never named it.

### 3. Classify each candidate

Use one of:

- **SUFFICIENT**: current behavior/skill already works;
- **ADOPT**: an existing skill fits without material change;
- **ADAPT**: an existing skill is the best base but needs changes;
- **EXTRACT**: one or more patterns are useful without adopting the source workflow;
- **SUPPLEMENT**: strengthen an existing skill without replacing it;
- **COMPOSE**: keep independent skills separate but use them together;
- **CREATE**: a custom skill best fits the stable workflow;
- **CHECKLIST**: useful but not substantial enough for a full skill;
- **DYNAMIC**: formalization would reduce needed flexibility;
- **DO NOT CREATE**: trivial, volatile, redundant, or weakly supported.

### 4. Compare against the corpus

Inspect relevant material under `skills/` and companion evidence under `registry/`.

For a third-party candidate, reason in this order:

1. user fit;
2. exact-version quality state;
3. authority and dependency fit;
4. portability;
5. skill-specific freshness;
6. provenance and source context.

Popularity, stars, official branding, or repository age are context only.

Ask what failure the reference prevents, which procedure makes it useful, which assumptions are source-specific, what authority it expects, what should remain dynamic, and whether a smaller extracted pattern would provide the same benefit.

### 5. Design the fitted set

For each retained skill define its purpose, triggers/non-triggers, inputs/outputs, ordered method, decision points, evidence requirements, authority/privacy boundaries, human verification points, failure handling, completion criteria, relationship to references, and provenance when applicable.

Prefer a small coherent set over skill proliferation.

### 6. Adversarially review

Challenge the proposed set for overfitting, needless skill creation, catalog bias, duplicated authority, poor triggering, hidden capability assumptions, privacy overreach, unsupported validation claims, imported ceremony, and maintenance burden.

Revise, merge, split, or delete candidates as needed.

### 7. Materialize static artifacts

When the host can edit files and the user has authorized repository changes, create or refine the actual Markdown skill artifacts and passive companion metadata.

When the host cannot write files, provide complete portable skill content for the user or another agent to save.

Never claim a file was created unless the external host actually created it.

### 8. Evaluate when useful

Behavioral evaluation is performed by the external host agent, not by `skillz`.

For consequential new/adapted skills, the host agent may compare representative behavior with and without the skill when practical. Record actual evidence only. Static review and behavioral validation are distinct.

### 9. Installation or transfer

Installation, upload, synchronization, scheduling, or other external actions occur only through the host agent's own capabilities and normal authority rules.

`skillz` provides the portable instruction artifact. It does not install or execute it.

## Returning-user refinement

Do not restart from zero.

1. Inventory the current fitted set.
2. Re-check current user fit and accessible evidence.
3. Identify meaningful drift, overlap, gaps, or stale reference assumptions.
4. Preserve still-valid custom behavior.
5. Make the smallest justified change.
6. Permit **NO CHANGE NEEDED** as a successful result.

## Core rules

**Compare before creation.** Existing skills are evidence and prior art.

**User fit before reuse.** Do not distort the user's method to increase reuse.

**Source reputation is not skill quality.** Judge the individual skill and exact version.

**Formalize stable value only.** Repetition alone does not justify a skill.

**Keep `skillz` passive.** Any active behavior belongs to the external agent interacting with the repository.
