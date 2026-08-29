# Skill Evaluation Framework

`skillz` evaluates skills as **instruction artifacts and skill packages**, not as software deployed by this repository.

The repository is passive. It does not own a runtime, CI system, benchmark harness, model fleet, or behavioral-success metric. The evaluation goal is to give the acting agent the best available information about what a skill does, where it came from, what it requires, what authority it assumes, how portable it is, and whether its instructions are clear enough to be useful.

The normative scoring standard is [`skill-verification.md`](skill-verification.md).

## Responsibility boundary

`skillz` owns best-effort quality of:

- source and artifact provenance;
- exact-version identity when recorded;
- licensing and attribution context;
- dependency and component awareness;
- authority and side-effect characterization;
- portability/host assumptions;
- trigger/non-trigger clarity;
- structured semantic review;
- useful adversarial reading of likely failure modes;
- decisive curation state.

`skillz` does **not** own or guarantee the capability of the model that later reads the material. Multi-model benchmarks, weaker-model targets, success-rate thresholds, token-cost comparisons, CI, sandbox execution, or baseline-versus-treatment experiments are not repository completion requirements.

## Source review and individual skill review are separate

A tracked source answers: **is this upstream worth keeping as a discovery or prior-art reference?**

An individual review answers: **is this exact skill version sufficiently understood and well-formed for a governed disposition?**

An official, popular, or well-maintained source does not automatically promote every skill it contains.

Likewise, a rejected whole skill can still contain a useful component or design pattern if that component can be reused within its license, provenance, dependency, authority, and safety constraints.

## Intake flow

```text
discovered
  -> source vetting when the source is new
  -> selective individual skill review
  -> provenance + exact identity
  -> structured semantic score
  -> decisive state/disposition
  -> optional stronger scenario/adversarial semantic validation
```

Do not bulk-promote an upstream repository merely because it was admitted as a tracked source.

## What to inspect

For each deliberately governed skill, inspect the **complete skill package**, not just `SKILL.md` in isolation when supporting material affects behavior.

That may include:

- scripts or executable helpers;
- references and examples;
- templates;
- fixtures;
- `sources.json` or similar metadata;
- dependency declarations;
- bundled prompts/configuration;
- other files required for the skill to function as authored.

A skill-owned TypeScript/Python/shell helper is not repository engine code merely because it is executable. Preserve and evaluate legitimate skill components unless there is a specific reason to change them.

## Review sequence

1. **Identity**
   - canonical source/path;
   - exact revision/fingerprint when applicable;
   - authorship/provenance;
   - license/terms.
2. **Capability**
   - what durable job the skill performs;
   - triggers and important non-triggers;
   - expected outputs/completion criteria.
3. **Dependencies/components**
   - required files, scripts, templates, services, tools, or host capabilities;
   - whether those dependencies are complete and accurately described.
4. **Authority and safety**
   - read-only versus mutation;
   - cost, credentials, external side effects, destructive actions, approvals;
   - privacy/security boundaries.
5. **Portability**
   - universal mechanism versus host-specific assumptions;
   - fallback or handoff behavior where relevant.
6. **Usefulness/differentiation**
   - whether it adds meaningful reusable capability rather than generic duplication.
7. **Semantic quality**
   - ordered procedure;
   - failure handling;
   - evidence discipline;
   - ambiguity, scope creep, false certainty, or source-specific baggage.
8. **Disposition**
   - unchanged reuse candidate;
   - adapt;
   - supplement;
   - compose;
   - reference-only;
   - reject/retire.

## Semantic scenario review

Stronger review may examine representative situations such as:

- a clear positive trigger;
- an obvious non-trigger;
- a pressure/failure situation targeting the most important ambiguity;
- interaction with another skill or authority boundary;
- a host where one optional capability is unavailable.

This is still semantic review. It asks whether the instructions provide a sensible path through those situations. It is not a claim that a particular model will perform perfectly.

## Current quality vocabulary

- `verified`: exact version passed structured semantic review.
- `validated`: verified plus representative scenario/adversarial semantic review.
- `unverified`: useful reference/design evidence without the current structured gate.
- `trusted-baseline`: legacy compatibility state only, not current unchanged-reuse eligibility.
- `stale`: prior judgment should not be inherited silently after material change.
- `rejected` / `retired`: excluded from normal unchanged selection.

See [`skill-verification.md`](skill-verification.md) for the rubric and thresholds.

## Curation principle

The objective is not to maximize repository size or activity. It is to maintain enough high-quality, well-characterized material that an agent can compare alternatives intelligently and build a fitted system for the user.

If a new source or skill adds no meaningful differentiated value, **doing nothing is a successful curation decision**.
