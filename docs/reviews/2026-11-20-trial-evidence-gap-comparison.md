# Skill Trial Evidence Auditor v0.1: capability gap, bounded prior art, and exact-package assessment

**Date:** 2026-11-20. **Scope:** Skillz first-party source review, local checker execution, and a deliberately bounded outside-ecosystem comparison. **No independent agent-host effectiveness trial performed.**

## Decision: create a narrow evidence adjudicator, not another benchmark runner

The seven repository-bound engine procedures already provide static/source/license quality review, discovery and repository skill authoring. Specifically `engine/skills/skill-eval/SKILL.md` at `3c1068f408f4f7d7a03bcdab0347c9b8e7069187` explicitly disclaims multi-model benchmarking and measured behavioral effects. Authored `agent-failure-boundary-analysis` diagnoses failed execution boundaries and `research-methods-appraiser` addresses literature/reproducibility; neither is an exact evidence-adjudication protocol for a skill-enabled baseline/treatment experiment.

Three independently located **public upstream README / GitHub repo metadata** surfaces were read and source-pinned. These are *not complete code/package audits* or installation recommendations:

| Source | Checked pinned HEAD | Exact README blob | Observed README claims | Assessment |
| --- | --- | --- | --- | --- |
| [SkillBenchmark](https://github.com/TiesPetersen/SkillBenchmark) | `6ba8132fd5a7def75e2c57545c9c158e01cfdda8` | `08ebd703e70630daea13c3e9460ec711483494e6` | text-input treatment/control runner, blinded judge, intervals | potential **runner**; output and evaluation-method quality not independently proven by this reading |
| [agent-skill-eval](https://github.com/tardigrde/agent-skill-eval) | `536101b7bf3f6395c8d4ece03d1b412862b660e4` | `db89de19443369cf97e9caec8f069e4d6238abe6` | actual agent harnesses, isolated/container runs, trigger negative-controls, state-delta grading, token/time metadata | potential **runner**; host/version and artifact authenticity still independently required |
| [Kalaris research-agent-skills](https://github.com/KalarisLabs/research-agent-skills) | `a74b0dbe5fa865d73b9f250ba5b0c9f107bd1baa` | `f2277a58665a59472992e6f840f371deb9a7140d` | wide research skills catalog with benchmark/validation references | separate publisher/source lead, actual nested license terms not assessed; root API license metadata NOASSERTION despite README MIT badge |

**What was not searched exhaustively:** the G1–G3 61,326 pinned path identity dataset, the full 4,813-path dynamic four-source frontier, each of 995 governed external reviewed packages, other live GitHub repositories and the complete code of the three sources above. This is **no suitable identical in-package evidence-auditor among inspected methods**, not a claim that the open ecosystem has no equivalent. No external expression, code or assets were copied. External root MIT or an ambiguous badge does not automatically license all nested source files.

**Distinct deliverable:** source-agnostic, offline review of already-produced *paired-trial evidence* that enforces comparable arms, separate positive/nontrigger controls, leakage holds, independent grader assertions, host-run versus synthetic distinction, source/package pins, and bounded statistical reporting. It is not a model-runner, grading service, personal scheduler, skill selection engine or new source discovery service. Domain paths: `agent-mcp-development/evaluation` and `research/reproducibility`, both existing domains. Creating a new taxonomy domain would dilute the current hierarchy without new evidence of a distinct domain-level collection.

## Exact delivered package

- `skills/authored/skill-trial-evidence-auditor/SKILL.md` Git blob `4ab57ef3003285b7e6807776d7bfbc5a51118f97`.
- Full original eight-file Git tree `22dc96c351ffcf9c77b81c613415d9010b16984f`.
- Optional original Python 3.10+ stdlib method Git blob `cac8a94b40ce1aa6b24b99e85428050b42c426d9`.
- Actual executed test suite Git blob `3b78bd31d3babf7c5df52097a86d93dc2a715b34`.
- Eight individual uploaded source Git blobs matched locally computed `git hash-object`, byte for byte.
- Original MIT package license and explicit runnable/offline fallback. No sibling, internet, vendor API key, installed runner or external policy required.

## Executed bounded method results

**Python 3.13 standard library, `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -q`: 44/44 PASS, zero failures.** This exercises internally consistent registered positive pairs, independently verified-vs-self reported flags, hard evidence holds for unobserved execution, missing trigger telemetry, non-trigger firing or task regression, contamination, unequal agent/model/config/grader/snapshots, reused case IDs or receipt hashes, bogus identifiers, nonfinite JSON, missing fields, symlinks and excessive input. The deliberately synthetic 13-pair fixture has nominal 100 percentage-point recorded uplift, exact discordant-pair p ≈ .000488, yet the result is **WITHHELD_INSUFFICIENT_OR_UNQUALIFIED_EVIDENCE** because the runs are emulated, not preregistered and not isolated. This is an intentional negative control against false promotion.

The checker *cannot authenticate a declaration that an external trial was actually executed*. In even its best admissible metadata condition, it emits `RECORDED_POSITIVE_SIGNAL_NOT_AUTHENTICATED`, `source_authenticity_verified: false` and `actual_independent_host_validation_verified: false`. No modeled user acceptance, independently run host A/B, observed uplift, validated skill, achieved 1.5x ratio, production outcome, security scan or statistical generalization is proven here.

## Ten-dimension maintainer static rubric (not observed model-host success)

| Dimension | Score | Evidence |
| --- | ---: | --- |
| Trigger | 2 | exact compared-trial / design use, explicit runner/eval/scanner nontriggers |
| Procedure | 2 | staged preregistration, paired arms, leakage controls, rubric, verification, synthesis |
| Authority/safety | 2 | read-only, host action-specific approvals, privacy and untrusted records |
| Failure handling | 2 | missing baseline, untriggered skill, missing controls, incomparable arms |
| Evidence | 2 | complete package fingerprint, independent-vs-asserted receipt separation |
| Dependencies | 2 | in-package schema, executable/std-library tests, portable manual fallback |
| Portability | 2 | no external skill, service, network or model-tier dependence |
| Differentiation | 2 | method evidence checking rather than building benchmark infrastructure |
| Adversarial resilience | 2 | dedup receipts/cases, controls, leakage, invalid values, nontrigger errors |
| Effectiveness design | 1 | plausible improvement but no independent host trial / consumer result |

**Maintainer assessment 19/20; status static verified for this exact package only, behavioral validation NOT_RUN, source security not assessed by an external package scanner.** No formal mathematical proof that the checker itself is universally correct.

## Refinement priorities grounded by this pass

1. **skill-discovery / evaluation engine**: add representative *independently scored* source-neutral discovery tasks and false-duplicate negative controls, keeping observed runner outcomes separate from static catalogs. This amplifies through all authored packages and targets #599/#588.
2. **Federated Source Catalog**: make incomplete/paginated multi-source enumeration testable against real allowed connectors, with per-viewer existence-leak controls and actual source-handoff receipts. Distinguish a successful offline method from cross-tenant behavior.
3. **Scheduled Work Proof Auditor** and **Connector Capability Risk Review**: add robust real-provider receipt controls and adversarial tests, without creating scheduled tasks or autonomously granting tool authority.
4. **Underrepresented domains**: use the full source-family discovery frontier for robotics/IoT, 3D/CAD, accessibility, safety, scientific workflows and creative production before creating a domain-level category or implying novelty.

The first concrete step shipped in this tranche is the independently authored skill package **and** a user-facing authored catalog revision. This assessment does not pretend to exhaustively qualify the entire discovery corpus.

Related issues [#599](https://github.com/Knapp-Kevin/skillz/issues/599), [#588](https://github.com/Knapp-Kevin/skillz/issues/588) and [#738](https://github.com/Knapp-Kevin/skillz/issues/738) remain open.
