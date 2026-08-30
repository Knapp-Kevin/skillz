# Candidate Intake Policy

`skillz` uses an **issue-first admission workflow** for newly discovered third-party skills and source families.

This policy refines the discovery and curation lifecycle in `docs/curation-policy.md`. It does not change the passive repository boundary: the external host agent performs discovery, inspection, evaluation, scoring, fingerprinting, behavioral validation, and any external action. The repository stores instructions and resulting evidence only.

## Standard lifecycle

**discovery surface → candidate issue → source/terms vetting → exact-version static evaluation → decisive admission result → repository persistence when justified → optional later external behavioral evidence → user-fit decision**

A candidate issue is required before a newly discovered third-party skill or source family is admitted to the governed corpus.

The issue-first rule governs **new admission**, not whether provenance is optional. Provenance is mandatory for every governed user-facing skill, including existing skills. Newly discovered candidates accumulate pre-admission provenance evidence in the issue first; after admission, finalized provenance and verification companions are persisted with the exact admitted identity.

## Governed discovery inputs

Use `docs/discovery-surfaces.md` to guide intentional discovery. High-signal discovery inputs should be inspected before broad undirected searching when they are relevant to the capability gap being investigated.

The connected Google Drive **Creator Technical Resource Catalog** is an intentional internal discovery surface. It may identify candidate repositories, creators, standards, methods, capability clusters, duplication risks, and trust/burden questions. It is **not** itself provenance or verification evidence for the candidate material it references.

Before opening or resolving a candidate issue from any discovery surface, independently resolve the candidate to its canonical upstream source. Catalog scores, source reputation, popularity, creator attribution, discovery metadata, or another system's verification label must not be copied into `skillz` as if they established exact-version quality.

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

After admission is justified, persist only the material appropriate to the decision and bind provenance/verification metadata to the **exact evaluated identity**. A newly admitted governed skill is not complete until those companions exist. If source material remains external or reference-only, metadata must say so truthfully.

Rejection is a valid result. Preserve the reason so later agents do not repeatedly rediscover the same defect or duplication problem.

## Existing-corpus rule

Existing governed user-facing skills are held to the same provenance and exact-version metadata contract. Historical presence, prior scoring, first-party authorship, or inclusion in a catalog does not waive provenance requirements.

When an existing governed skill lacks required provenance or exact-version metadata:

1. record the gap as corpus incompleteness;
2. establish or repair the missing evidence from authoritative repository/upstream history;
3. do not invent unavailable facts;
4. do not count the record as companion-complete or statically complete until repaired;
5. preserve the correction through normal repository history.

This is passive governance enforcement. It requires no repository-owned scanner, CI job, script, test runner, or background process. The external agent checks the contract during curation and records the resulting evidence.

## Source-family issues versus individual-skill issues

A compact source family may be evaluated in one issue when the denominator is small and the skills share one source/terms context. Large or heterogeneous corpora should use a source-vetting issue first, followed by individual or coherent-slice skill issues as needed.

No issue implies automatic execution. The issue is simply the durable coordination and evidence surface for the external agent performing the work.

## Template

Use `.github/ISSUE_TEMPLATE/skill-candidate-evaluation.md` for new candidate evaluations.
