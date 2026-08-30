# Candidate Intake Policy

`skillz` uses an **issue-first admission workflow** for newly discovered third-party skills and source families.

This policy refines the discovery and curation lifecycle in `docs/curation-policy.md`. It does not change the passive repository boundary: the external host agent performs discovery, inspection, evaluation, scoring, fingerprinting, behavioral validation, and any external action. The repository stores instructions and resulting evidence only.

## Standard lifecycle

**discovery surface → candidate issue → source/terms vetting → exact-version static evaluation → decisive admission result → repository persistence when justified → optional later external behavioral evidence → user-fit decision**

A candidate issue is required before a newly discovered third-party skill or source family is admitted to the governed corpus.

## What belongs in the issue

The issue is the pre-admission evidence workspace. Establish, when applicable:

- canonical source and publisher/author identity;
- exact source revision or equivalent exact content identity;
- complete package tree/fingerprint when establishable;
- license, redistribution, attribution, and applicable terms;
- skill-specific freshness or last-update evidence when establishable;
- purpose, trigger boundary, exclusions, and intended use;
- complete dependencies, shared references, scripts, assets, templates, and package context;
- authority, side effects, credentials, privacy, cost, and mutation assumptions;
- portability and host/tool assumptions;
- controlled taxonomy tags;
- overlap and differentiation against the existing governed corpus;
- structured exact-version semantic review and score;
- behavioral-evidence state, which remains `not-run` unless representative external evaluation actually occurred;
- useful mechanisms for adaptation/extraction even when unchanged reuse is rejected;
- a decisive result.

## Decisive results

A candidate issue should end in a clear state such as:

- admit unchanged candidate;
- admit source for selective individual curation;
- adapt/extract/supplement/compose only;
- reference-only;
- reject unchanged;
- reject source.

Popularity, stars, official branding, repository age, or creator reputation may inform discovery and source context but cannot replace individual evidence.

## Persistence gate

Before the issue reaches a justified admission result:

- do not copy the candidate skill into the governed repository;
- do not add a new pinned corpus merely because it was discovered;
- do not create final provenance or verification companions that imply admission or review completion;
- do not count the candidate in governed corpus totals.

After admission is justified, persist only the material appropriate to the decision and bind provenance/verification metadata to the **exact evaluated identity**. If source material remains external or reference-only, metadata must say so truthfully.

Rejection is a valid result. Preserve the reason so later agents do not repeatedly rediscover the same defect or duplication problem.

## Source-family issues versus individual-skill issues

A compact source family may be evaluated in one issue when the denominator is small and the skills share one source/terms context. Large or heterogeneous corpora should use a source-vetting issue first, followed by individual or coherent-slice skill issues as needed.

No issue implies automatic execution. The issue is simply the durable coordination and evidence surface for the external agent performing the work.

## Template

Use `.github/ISSUE_TEMPLATE/skill-candidate-evaluation.md` for new candidate evaluations.