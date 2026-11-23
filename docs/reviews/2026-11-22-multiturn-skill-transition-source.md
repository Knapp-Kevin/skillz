# Adversarial multi-turn skill continuation: deterministic source milestone

**Date:** 2026-11-22. **Umbrella:** #828. **Status:** source candidate, hosted tests pending.
**Scope:** five original authored skills, one source-based cross-skill contract.

## Executable result
- Context Continuation Contract gains optional offline, Python 3.9+
  `scripts/check_transition.py` with 44 planted tests over caller-supplied
  prior/updated checkpoints. It checks scope/workstream and sequential
  revisions, decisions, protected guardrails, completion criteria, declared
  evidence category and exact source, unblocking/reopening receipts, next
  executable action and false completion. It never contacts GitHub,
  executes repo code, posts feedback, alters memory or mutates state.
- A bundled, fictional three-JSON fixture and adversarial scenario matrix
  exercise CI Guard, Repository Delivery Assessor, Repository README
  Architect and Evidence-Driven Refinement Loop. Each skill now has its
  own domain-specific continuation checkpoint guidance without a
  mandatory sibling-tool dependency.
- Root `scripts/qa/test_multiturn_skill_checkpoints.py` tests static
  presence and full source contracts for those four domains. A single,
  path-filtered, draft-skipping workflow executes the context package
  suite and root checks on PR HEAD.

## Safety and qualification
The tool checks only a **caller-supplied text/JSON structure**.
`STATIC_TRANSITION_RECONCILED` says nothing about the authenticity of
the stated user/owner permission, full source SHA, provider merge/CI,
real checklist acceptance, or how a language model acted across prompts.
A declared scope change always HOLDs for independent host authorization.
A reported proof reference is not a signed receipt. Actual observed
multi-turn agent behavior remains **NOT_RUN**, and improvements against
an unskilled baseline are **NOT_MEASURED**.

All five exact source/package fingerprints and ten provenance/verification
companions require reconciliation before merge; previous exact-version
quality scores and CI receipts remain historic. The published version
identifiers are unchanged, per conservative release policy. This is a
source improvement rather than an independent production release.
