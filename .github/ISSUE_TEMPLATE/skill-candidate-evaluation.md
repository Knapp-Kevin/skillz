---
name: Skill candidate evaluation
about: Queue a newly discovered skill or source for evidence-first evaluation before repository admission
title: "Candidate evaluation: "
labels: ""
assignees: ""
---

## Candidate

- Source repository / canonical location:
- Candidate skill or source family:
- Upstream path:
- Discovery surface:
- Discovery rationale / differentiated capability:

## Issue-first admission gate

This issue is the evaluation workspace. **Do not add candidate skill material or final provenance/verification companions to the governed repository before this issue reaches a decisive admission result.** Discovery is not admission, and source reputation is not individual skill proof.

## Evidence to establish before decision

- [ ] Canonical source and publisher/author identity
- [ ] Exact source revision or other exact content identity
- [ ] Complete package tree/fingerprint when establishable
- [ ] License, redistribution, attribution, and applicable terms
- [ ] Skill-specific freshness / last-update evidence when establishable
- [ ] Purpose, trigger boundary, exclusions, and intended use
- [ ] Complete dependency/shared-reference/package context
- [ ] Authority, side effects, credentials, privacy, cost, and mutation profile
- [ ] Portability and host/tool assumptions
- [ ] Controlled taxonomy tags
- [ ] Duplication / overlap comparison against the existing governed corpus
- [ ] Structured exact-version semantic review and score
- [ ] Behavioral-evidence state (`not-run` unless representative external evaluation was actually performed)
- [ ] Useful extraction/adaptation mechanisms identified even if unchanged reuse is rejected

## Decisive result

Choose and justify one or more as appropriate:

- [ ] Admit unchanged candidate
- [ ] Admit source for selective individual curation
- [ ] Adapt / extract / supplement / compose only
- [ ] Reference-only
- [ ] Reject unchanged
- [ ] Reject source

## Admission and persistence rule

Only after the issue records a justified admission decision may `skillz` persist the candidate skill/source material as appropriate and create or finalize its provenance and verification metadata. Persisted metadata must match the exact evaluated identity. Rejection and retirement reasons remain useful evidence and should be preserved.

## Passive boundary

All discovery, inspection, scoring, verification, behavioral evaluation, installation, and external action are performed by the external host agent/environment under user authority. `skillz` gains no crawler, runtime, evaluator, scheduler, test harness, installer, monitor, or autonomous intake process.