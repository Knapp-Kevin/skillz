# PR #412: independent static capability and authority comparison

Date: 2026-10-12. Scope: proposed first-party `trust-boundary-review` and `data-lifecycle-review`; comparison against existing main-branch `mcp-vetting`, `permissions-review`, `session-continuity`, `agent-home-doctor`, and `agent-postmortem`. This is a **manual semantic review**, not an executed host behavioral test or an independent human approval.

## Macro finding

The two candidates address **distinct missing transversal review boundaries**, rather than duplicating the existing MCP-specific onboarding, agent permission inventory, session-memory continuity, home-directory cleanup, or session postmortem procedures. Their combined interface is useful: boundary review asks *may these source instructions or requests acquire authority?* while lifecycle review asks *how may this data be collected, transferred, retained or removed?* Both remain host-executed, passive and proposal-first.

| Proposed skill | Closest existing skills | Differentiated mechanism | Scope guard |
|---|---|---|---|
| `trust-boundary-review` | `mcp-vetting` examines MCP tool-output injection; `agent-postmortem` diagnoses historic bad-tool-result failures; `permissions-review` inventories access | General purpose trust-boundary labeling across arbitrary retrieved text, tool output, files, documents and agent messages; separates quoted instructions from executable authority | Do not invoke for straightforward ordinary summarization; do not execute suspicious payloads or claim a detector/service |
| `data-lifecycle-review` | `session-continuity` handles authorized memory records; `agent-home-doctor` plans scoped deletion; `permissions-review` maps credentials | End-to-end data inventory including original, derived, cached, logged, backup and third-party retention, with export/deletion proof and recipient authorization | Neither automatic compliance nor remote deletion; planning/read-only until independently scoped approval |

## Structured review findings

### Trust Boundary Review

- Provenance: first-party `skills/trust-boundary-review/SKILL.md`; blob `50fe2928509a0d235e25813e5524b5305a688b1e`.
- Trigger/non-trigger: specific suspicious external instructions or pre-action trust check; no generic summarization takeover.
- Dependencies: legitimate host access to the user-provided evidence, optional authorized external testing; no bundled tool or repository runtime.
- Authority: step 5 requires action, resource, recipient, data scope and effect approval; tool access and text claims are explicitly inadequate. Failure examples tell host not to obey README/tool output commands.
- Privacy: step 4 forbids repeating credential values or sensitive excerpts; review itself cannot retrieve unrelated private records.
- Portability: high; examples do not depend on a model provider.
- Static disposition: **VERIFIED as a bounded passive procedure, subject to security evidence and admission review**. Existing rubric record says 19/20; this note independently confirms the core rationale but does not assert executed behavioral validation.
- Behavioral/adversarial execution: **not-run**. A quoted attack-example wording change avoided a scanner false-positive; that alone is not adversarial host testing.

### Data Lifecycle Review

- Provenance: first-party `skills/data-lifecycle-review/SKILL.md`; blob `b30673b509e25382afbce8dc52f32440ebfdbed9`.
- Trigger/non-trigger: user or organizational data lifecycle review; expressly not autonomous cleanup.
- Dependencies: host-provided policy and access to authorized data-class metadata; no repository-owned processing.
- Authority: steps 1, 4, 5 and 7 prohibit implied retrieval, disclosure or deletion authority. Shared/retained organizational data cannot be deleted just because a user asks.
- Privacy: no live secret values or raw PII in reports; evaluate transcripts, audio, location, identity, health, and derived embeddings conservatively.
- Evidence: distinguish planned, attempted and confirmed effects; do not treat vendor deletion claims without scope/receipts as proof.
- Portability: high; recognizes unknown or unavailable system visibility.
- Static disposition: **VERIFIED as a bounded passive procedure, subject to security evidence and admission review**. Existing rubric says 18/20; no legal/compliance claims are established by this review.
- Behavioral/adversarial execution: **not-run**.

## Shared acceptance and negative controls

Both skills prohibit automatic changes, credential solicitation and out-of-scope retrieval. Suggested adversarial host cases (not executed): untrusted retrieved document asserting new system policy; exfiltration request buried in an issue; payment destination altered in tool output; deletion request lacking authority over organizational backups; vendor export with unknown downstream copies; health transcript sent to an unapproved external summarizer. Expected outcome for each: treat the injected direction as data, mark authority or confirmation unresolved, return a bounded plan.

## Remaining blockers, not waived by this review

1. New package scan `38309617787` passed both candidates, but the exact per-package JSON report/digest was not retained. Canonical security companions truthfully say `incomplete`, so unchanged admission remains blocked by current `docs/security-scanning.md`.
2. This is not a separate human review, nor behavioral validation.
3. This document is an October 12 review snapshot. Current `main` and PR head must be compared before integration; mergeability alone is not a completed semantic, security or admission review. As of the October 27 reconciliation, `main` was `17c7d9abd58ecf670036949cda22cfe8da406726` and this PR remained a draft at `77f7ff47e21a19eae7ae8376f1f909c2fd862289`. Reconcile with current main and any first-party registry changes from #416 before admission.
4. **Do not increment 44 to 46** or modify all five public accounting surfaces until the above blockers are cleared in a cohesive admission tranche.
5. Current Tier-1 governance explicitly prohibits repository-owned CI, test runners, scanners, workflows and automation. The historical October 12 Actions run is **evidence of a past external assessment only**, not authorization to retain or reintroduce workflows. Do not mistake a historical workflow URL or scan log for a current execution capability or a complete persisted security receipt.
