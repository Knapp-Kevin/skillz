# Issue #714: current authored Healthcare Contract Forensics package review

**Reviewed:** 2026-11-06, exact 10-file v1.1.0 first-party authored package based on the first-party source introduced in [PR #715](https://github.com/Knapp-Kevin/skillz/pull/715), with this v1.1.0 fingerprint reviewed separately.

**Review verdict: structured semantic static review 19/20.** Observed agent-host behavioral testing **NOT RUN**; no external scanner run; no public legal certification or real savings evidence; unchanged use with confidential contracts/PHI **not cleared**.

## Exact source, copyright and rights

- Canonical folder: [`skills/authored/healthcare-contract-forensics/`](../../skills/authored/healthcare-contract-forensics/).
- Skill entrypoint Git blob `5a304a552678ad88f4fa239abf28fe52b20bbab6`.
- Full 10-file package Git tree SHA `587d29e9a1275efcb8f20437bbc5479d36d1f5b3`, assembled from the exact blobs below. Moving the package to `skills/authored/` does not alter package-relative Git tree identities.
- First-party MIT (SPDX `MIT`), copyright (c) 2026 Kevin Knapp, repository [LICENSE](../../LICENSE). No third-party original skill text, real healthcare contracts, protected records or patient PHI are vendored.
- Exact version facts also recorded in the [authored skills license index](../../registry/authored-skills-index.json), [provenance companion](../../registry/skills/local-skills/healthcare-contract-forensics.yaml), [verification companion](../../registry/verification/local-skills/healthcare-contract-forensics.yaml), and [local summary](../../registry/local-verification.json).
- Historical 9-file tree `0d1d9f2838691fcf7963472ea8b62c52b2a273ed` and old SKILL blob `02d7d645d6a6856d01165e01da9014f9cf43309c`, plus historical 7-file tree `3974f153ac39bd27895c4f0365ee50e0ef1527a9` and earlier SKILL blob `6ea8dda7b85b399a252f9b97295d54e536a3f897` are **superseded** and not valid current verification pins.

## Full package: static content identity

| Path under `skills/authored/healthcare-contract-forensics/` | Git blob SHA | Role |
|---|---|---|
| README.md | 37e1ffe85ca3b2479f4349d766e3083d748d8aff | User-facing shared-package overview and synthetic demo |
| SKILL.md | 5a304a552678ad88f4fa239abf28fe52b20bbab6 | Precise triggers, read-only authority, workflow and fail-closed behavior |
| references/clause-review.md | 9ea8e183bfa04b712a36db2e66b4e65e50385da3 | Definitions, economics, opposing readings, law-source navigation |
| references/financial-reconciliation.md | 52f370555cfb15af8dccf5fe5eb774ec72ba2b70 | Decimal arithmetic, units, reconciliation stop criteria |
| references/report-template.md | ac9a4709cbc0d94c8dc2e89008d3c779cb65964d | Evidence ledger/report output contract |
| examples/synthetic-pbm-case.md | b8c50e998c426747926267d4090ec6191c2ee4d1 | Fictional master, amendment, fees and manufacturer ledger |
| examples/claims-synthetic.csv | d4b01ddbed0a860f4676171383c6df1878bf363b | Four invented claims, incl. reversed status |
| examples/expected-case-review.md | 639cb9d8a45d18c0b362f2ff48b36da46e219eec | Base-case arithmetic and non-overclaim interpretation |
| examples/filled-report-synthetic.md | 2a89bdb9831ec7c86035055310cf182ca0068c9e | Filled fictional source-linked report, **not** model output |
| examples/negative-scenarios.md | a8c92f4e4f1a17ed892dddf537d0047ccd29e379 | Nine fictional adversarial/counterfactual cases |

All package-relative source/report reference links were checked against these ten blobs; no scripts, binaries, network calls or model-host adapters are bundled. Five previously malformed Markdown files were corrected for escaped backticks.

## Review score and evidence

| Static rubric dimension | Score | Evidence |
|---|---:|---|
| Trigger precision | 2 | Employer/PBM contract analysis triggered, personal plan shopping excluded |
| Procedure and workflow | 2 | Bound authority → source map → defined economics → opposing reading → reconciliation → report |
| Authority and confidentiality | 2 | Limited explicitly authorized reads, no vendor action or PHI egress |
| Failure and uncertainty | 2 | Missing precedence, duplicate claims, OCR, absent rates and unsupported statutes block conclusions |
| Source traceability | 2 | Section/row/contract version citations and contrary readings |
| Package completeness | 2 | All 10 files, source-linked report and fixture referenced/resolved |
| Portability honesty | 1 | Real hosts vary in PDF parsers, decimal arithmetic and confidentiality controls |
| Domain usefulness | 2 | PBM exclusions, affiliate remuneration, claim settlement and negotiating questions |
| Adversarial design | 2 | Injection, false benchmarks, later fees, sensitive data, missing contract and duplication |
| Evaluation readiness | 2 | Filled report, source-linked answer key and precise expected-failure scenarios |
| **Total** | **19/20** | **STATIC ONLY; NO OBSERVED HOST RUN** |

**Executed deterministic arithmetic/structural inspection (not model behavior):** parsed base synthetic CSV, confirmed 4 rows and 3 settled claims, expected $6.00 fee vs observed $7.25 yields +$1.25; $360 sponsor vs $310 pharmacy paid yields $50 observation; $50 defined rebates and $20 manufacturer service fees that are explicitly **excluded** from defined rebates. Later-amendment scenario at $2.50 × 3 = $7.50 gives **−$0.25** relative to $7.25 invoice. A duplicated `RX-002` in the counterfactual input triggers an unresolved count gate. All SKILL-relative links resolved; all nine variant IDs present; backtick formatting corrected. An initial overly literal phrase assertion against the worked example was rechecked by equivalent meaning: it explicitly says no overpayment proved and the amount is not recoverable on existing evidence. No production-billing validation, model accuracy metric or baseline superiority was established.

**Candidate and rights review:** [61,326 G1–G3 path identity receipt](2026-11-06-issue714-broad-discovery-and-license-receipt.md) and [four fully enumerated candidate-package inspections](2026-11-06-issue714-package-candidate-comparison.md). The broader search found 233 lexical leads; reading four adjacent complete packages established differing domains and authority needs, **not** proof that no more suitable skill exists. Third-party material was **not copied**. Root licenses observed at inspected source pins do not clear every nested asset.

## LinkedIn comment expectation: direct clause quotes and bounded impact

[Detailed v1.1.0 commenter-acceptance audit](2026-11-06-issue714-commenter-acceptance-audit.md) documents: four worked clause scrutiny cards, **eight original excerpts matched exactly** against the supplied synthetic source after removing Markdown emphasis, explicit source-file links, separate evidence-state labels for the $1.25 invoice variance, $20 excluded manufacturer fees and $50 contract-permitted price difference, plus concrete verification requests and negotiations questions on each card. Added a top-level human README because the shared GitHub folder must be understandable on arrival. These are **static source checks and deterministic fixture arithmetic**, **not** actual LLM-host or real-contract validation.

## Legal-context and behavioral boundaries

Current-law claims must be refreshed against the correct effective date, plan year, jurisdiction and primary source. The supplied 2025 fictional fixture is not determined unlawful by a later PBM disclosure rule. The exact source contains no authority to email contracts, infer PHI access, run a script or accuse a vendor of misconduct. An **external host** still needs independent tested enforcement.

## Outstanding evidence

- Run actual trigger/nontrigger/injection/OCR/duplicate/PHI/adversarial tests with the exact 10-file fingerprint on a selected authorized host.
- Run a matched baseline prompt comparison, capture transcripts and source citation precision rather than assume superiority.
- Verify any consequential regulation, applicable plan type, rights and dates with current primary authority and qualified counsel.
- Reconcile authored index and regenerated domain/dashboard counts before claiming a synchronized total.
- Independent reviewer/owner decision before any user-facing production promotion. PR #715 already merged the earlier passive reference version; this review does not imply behavioral sign-off.

The fact that this skill is marked `verified-static` does not mean behavioral or security validation, and the repository holds passive documents rather than active protection controls.
