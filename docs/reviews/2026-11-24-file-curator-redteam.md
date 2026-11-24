# File Lifecycle Curator: adversarial hardening assessment

Assessment date: 2026-11-24
Subject: `skills/authored/file-lifecycle-curator/`
Starting accepted revision: `3cfbed8fcd1b21d3c71fe969164ea14d3dd1055f`
Disposition: **Qortara-harden / repair** (bounded component) with a separate
read-only, Qortara-schema-checked repository hardening assessment.
Reviewer: author-led adversarial review, **not independent host attestation**.

## Scope and method

Inspected the full skill entrypoint, its linked source authority, metadata,
archival, visual, incremental maintenance, durable checkpoint, host handoff,
federated intake, and scheduled-agent contracts; optional helper code and
synthetic/controlled-fixture tests. Followed the current
`docs/skill-verification.md` 10-dimension, 20-point semantic rubric and
the Qortara `qortara-harden` sequence: IQ-COMPLETE, IQ-CORRECT, IQ-TRUST,
IQ-CONTEXT, IQ-COMPLEX, IQ-RESOURCE, IQ-CONTRACT, IQ-MAINTAIN and IQ-OBSERVE.

The Qortara Logic hosted `qortara_gate_validate` call accepted the structured
`repo_hardening` **artifact shape**, routing the following three findings
to `qortara-harden` as LOCAL. It did not review the code, authenticate
the repository or independently execute a hardening skill.

## Confirmed attack paths and findings

| ID | Severity | Mechanism | Risk | Repair |
| --- | --- | --- | --- | --- |
| RT-01 | MAJOR, IQ-TRUST/CONTRACT | `host_handoff.py` enforced immutable plan membership while direct `state.py:guarded_plan` did not | A caller using the approved checkpoint API could add/remove a planned record without a new authorized plan revision | One shared `state.guard_plan_observation` used by both paths, checking exact membership for unchanged plan identity |
| RT-02 | MAJOR, IQ-CORRECT/OBSERVE | Direct durable writes did not compare VERIFIED/ROLLED_BACK receipt time to current source observation and approved plan baseline | An old operation receipt could be wrapped in a newer plan, then persisted as if fresh | Require per-record readback at least as recent as current source and strictly newer than prior accepted plan |
| RT-03 | MAJOR, IQ-COMPLETE | Caller-supplied plan `coverage=complete` was not bound to current source `coverage=partial` | A presentation path could show a misleading progress percentage, with the denominator claimed complete | Require source/plan coverage equality in the shared guard; partial coverage suppresses percentage |

The fixes do **not** prove provider identities, real source ACLs, independent
file-operation success, actual scheduler delivery or disaster recovery.
Claims and readback timestamps remain host assertions; the model must
label them as such. New actions still require current host/user permission.

## Adversarial design decisions

1. Put protections in the lowest reused **checkpoint and presentation
   contract**, not only in the display path, to eliminate alternate-call
   bypasses. No new scheduler, daemon, provider API, database schema or
   dependencies.
2. Accept valid explicit replans with distinct plan revision and proper
   approval. Do not silently change membership under a fixed revision.
3. Check current source coverage before producing any planned percent.
   A partial authorized scan never proves collection-wide completion.
4. Reject stale readbacks rather than silently downgrading them to current
   successes, even when the plan timestamp itself is fresh.
5. Preserve standard portability: Python 3.9+ stdlib optional, ordinary
   text-only skill valid without private state or a connected provider.

### Red-team qualification cases

- Attempt direct state commit with injected/removable planned member under
  identical revision: HOLD, unchanged generation.
- Attempt direct state commit with prior timestamped VERIFIED receipt:
  HOLD, no advancement.
- Attempt forged COMPLETE plan over PARTIAL current observation:
  HOLD with no progress or private counts.
- Test proper PARTIAL plan with a fresh readback: scoped counts allowed,
  **no percentage**.
- Existing denied access, cross-principal reuse, time and revision drift,
  replay, database-corruption and 90-day synthetic endurance regressions
  must still pass at the exact PR head.

## Ten-dimension semantic scorecard

Scores below use repository rubric, **not** a Qortara-produced score.
The post-remediation judgment is an **author-led, exact-package static semantic
assessment**. Current-head qualification is tracked separately from the score;
real agent-host validation remains NOT_RUN.

| Dimension | Before | After repair | Evidence / reason |
| --- | ---: | ---: | --- |
| Trigger precision | 2 | 2 | Explicit collection scope, non-trigger and default read-only |
| Procedural clarity | 1 | 1 | Good phased references but a large multi-component entrypoint; smaller activation paths may help |
| Authority and safety | 1 | 2 | Confirmed direct-write bypass removed by shared guard, subject to tests |
| Failure handling | 1 | 2 | Hold and unchanged generation for new attack cases |
| Evidence discipline | 1 | 2 | Freshness and honest source/plan coverage, all still host-asserted |
| Dependency coherence | 2 | 2 | Self-contained package references, optional stdlib helper; no external app required |
| Portability honesty | 2 | 2 | Host-owned connectors, permission, storage and scheduler |
| Usefulness / differentiation | 2 | 2 | Persistent, incremental, visual and bounded next-action workflow |
| Adversarial resilience | 1 | 2 | Actual injected/replay/coverage attack regressions, not only policy prose |
| Effectiveness design | 2 | 2 | Concrete checkpoints, reconciliation, safe reports, deliberate limits |
| **Total** | **15/20** | **19/20 static** | No claim of real-world consumer acceptance |

No 20/20 award is sought here merely to meet a target. Procedural complexity
is a real remaining opportunity. Even a later exact-version semantic
`verified` verdict cannot be presented as independent host behavioral
`validated` status or security-scanner certification.

## Qualification and ship gate

The first post-repair test run for PR #908 completed with **151/151 offline
contract tests passing in 3.419 seconds** (workflow #45336592672).
The authored fingerprint gate initially refused an obsolete registered package
tree, which must be reconciled and **requalified at the exact final head**.
GitHub merge must be confirmed separately before calling the work delivered. Record failed runs as failures and keep historical
source identities rather than overwriting earlier review evidence.

No user data, source credentials, external scheduler, or live file
organization operation was used in this review.
