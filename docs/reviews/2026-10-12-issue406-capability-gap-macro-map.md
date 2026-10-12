# Capability gap macro-map: issue #406, 2026-10-12

**Authority:** issue [#406](https://github.com/Knapp-Kevin/skillz/issues/406). This is a passive assessment of *named first-party coverage*, not an assertion of absence across all governed third-party sources or of demonstrated demand. Exact first-party baseline on main: 44 skills; 17 monitoring/intelligence and 3 software/repository. Pending #412 adds 2 candidates; pending #413 adds 2. **No candidate is admitted by this assessment.**

## Eight-hypothesis adjudication

| Priority | Capability | Current first-party overlap (actual mechanisms) | Disposition and missing evidence |
|---|---|---|---|
| P1 | Behavioral evaluation/regression | `fact-check` checks factual claims, `agent-postmortem` diagnoses previous incidents, `automation-receipts` verifies scheduled execution receipts; none supplies scenario matrix with trigger/non-trigger and baseline/candidate version comparison | **NEW FIRST-PARTY proposed** `skill-behavior-evaluation` on #413; static-review path, no behavioral-run claim; independent acceptance/security and catalog reconciliation outstanding |
| P1 | Trust-boundary injection handling | `mcp-vetting` checks tool-output injection at MCP onboarding and `permissions-review` inventories host access; general untrusted document/source boundary absent by name | **NEW FIRST-PARTY proposed** `trust-boundary-review` on #412; distinct general cross-source procedure, but incomplete persisted package-security evidence |
| P1 | Data lifecycle and privacy | `session-continuity` authorizes minimal durable capture; `agent-home-doctor` requires approval before deleting local files; `permissions-review` inventories credential reachability | **NEW FIRST-PARTY proposed** `data-lifecycle-review` on #412; differentiated source-to-derived/backups/third-party disclosure lifecycle; incomplete persisted package-security evidence |
| P1 | Delivery/release evidence | `repo-doctor` produces one-shot health punch list; `repo-pulse` surfaces cross-repo CI/PR debt, but neither binds artifact digest, tested baseline, rollback plan, explicit promotion permission, and observed production result | **NEW FIRST-PARTY proposed** `release-evidence-review` on #413; host-executed checklist only, not a release controller; independent scan/review/catalog unfinished |
| P2 | Agent memory quality/lifecycle | `session-continuity` covers recall, provenance, contradictory statements and authorized write-back; `memory-pulse` is vendor news. Neither measures recall precision, stale fact suppression, deletion propagation or conflicting memory graphs | **ADAPT/COMPOSE first**, using `session-continuity`, proposed `data-lifecycle-review` and separately governed external memory methods; a dedicated skill requires specific user demand and scenario evidence. Status: partial, further whole-corpus third-party overlap needed |
| P2 | Agent workflow cost/reliability/observability | `automation-receipts` verifies scheduled status; `agent-postmortem` captures cost-runaway lessons; `finance-review` analyzes supplied bank exports, not model/tool invocation spend | **CHECKLIST / COMPOSE first**. Missing per-task price/latency/token/quality attribution and recovery/SLO contract; gather real task budgets and host telemetry before choosing a new skill. Status: partial |
| P2 | Accessibility and multilingual quality | `fact-check`, `compare`, `deep-dive` evaluate general factual claims, not WCAG or language/locale usability; third-party coverage unverified in this review | **GOVERNED THIRD-PARTY OVERLAP REVIEW** before any original skill. Candidate approach: accessible-output and localization acceptance checklist backed by current standards, no invented conformance. Status: unknown until exact records reviewed |
| P2 | Incident response and recovery | `agent-postmortem` is retrospective; `repo-doctor` inspects repository health, and `permissions-review` recommends access tightening | **ADAPT/COMPOSE plus host incident-runbook checklist first**; first-party real-time containment/triage, incident communications authorization, restoration proof are partial/absent. User-specific incident ownership and existing enterprise procedures must govern. Status: partial |

## Macro conclusions

- Count imbalance is real (17 vendor-monitoring / 44 vs 3 software/repositories / 44), but does not prove all monitoring skills are unnecessary or that every software capability needs its own new skill.
- **Four P1 proposals already have scoped PRs** (#412 and #413). Avoid further parallel feature branches that would duplicate their semantic and catalog modifications.
- P2 research is best treated as one bounded whole-corpus overlap tranche for memory quality, cost/reliability, accessibility/localization, and incident recovery, with evidence from exact registered sources. Unknown third-party coverage cannot be asserted absent.
- No ongoing runner, monitor, CI, scheduler, memory database, telemetry pipeline, or automated controller belongs in this repo. Any security and behavioral proof is produced by authorized external hosts.
- First-party expansion from 44 to 46/48 is strictly conditional: source/version/security/semantic readiness, actual merge, and atomic README / SYSTEM_STATE / CURATION_QUEUE / INDEX / index.json reconciliation. No public counts are incremented here.
- `verified` is structured semantic review; `validated` requires actual external host execution. PR #413 has no behavioral outcomes, and its former repository-owned scanner is not a valid passive architecture prerequisite.

## Specific acceptance plan for PR #413

1. Compare against first-party `fact-check`, `agent-postmortem`, `automation-receipts`, `repo-doctor`, and `repo-pulse` at exact current version. Confirm differentiated mechanisms above.
2. Confirm candidate SKILL.md blob fingerprints `ceb0e562a70d6848e56d2641306eeac619d5f60f` (behavior) and `d236826daad241afbfc5c8867221c066b7ff5044` (release) remain valid at merge head; invalidate otherwise.
3. Obtain exact-version authorized external security reviews with reusable report evidence. Existing green workflow is historical CI evidence, not authority to introduce repo-owned CI or assert behavioral validation.
4. Review PR #413's modifications to `registry/local-verification.json` for canonical ordering and duplicate keys/entries, and reconcile `registry/categories.yaml` with public index.
5. Do independent acceptance, then five-surface atomic accounting; account for #412 if it merges first.

## Next bounded gap tranche

Reconcile the four P2 topics against admitted and tracked sources, using exact provenance/verification records and user-fit evidence before NEW/ADAPT/CHECKLIST/NO CHANGE decisions. Keep #406 open until all eight have final coverage/disposition evidence, but do not hold completed P1 plans hostage to P2 research.
