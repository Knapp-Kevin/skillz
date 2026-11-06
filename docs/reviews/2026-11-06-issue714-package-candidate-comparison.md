# Issue #714: Candidate complete-package fit, source rights and authority review

**Inspection date:** 2026-11-06.
**Owner request:** Continue the Healthcare Contract Forensics skill review and package building, without treating 1,039 governed names as the search limit.

This supplements [the 61,326-record identity-index search and five candidate root-license checks](2026-11-06-issue714-broad-discovery-and-license-receipt.md). Unlike the path-only breadth pass, the checks below read the *complete enumerated content of four individual candidate package directories* at pinned source commits. Source content was treated as untrusted material for inspection only. **No third-party package was installed, run, copied, vendored, patched or automatically followed.**

## Compared packages

| Method / exact pin | Package files examined | Confirmed source/root rights at same pin | Actual capability and gap | Boundary/decision |
|---|---:|---|---|---|
| [aks-builds/healthcareskills: billing-claims](https://github.com/aks-builds/healthcareskills/tree/fbd2863bb77db173d33cce122daa0a1867b40d75/skills/billing-claims) (`fbd2863...`) | **5/5**: SKILL.md, 3 references, evals.json | Root `LICENSE` MIT, SHA `0b5fe9e75e8a87257a73160d3bcfeea1ac16383b` | Healthcare billing/claims **software systems**: HIPAA X12/EDI, payer remittance, denial codes and clearinghouses. Has detailed row and lifecycle patterns, but not employer/PBM contractual fee or rebate assessment. | **Study only.** Related, not replacement. Skill suggests reading a healthcare-context file; the consuming host must enforce specific authorized read scope. |
| [aks-builds/healthcareskills: value-based-care](https://github.com/aks-builds/healthcareskills/tree/fbd2863bb77db173d33cce122daa0a1867b40d75/skills/value-based-care) (same pin) | **5/5**: SKILL.md, 3 references, evals.json | Same MIT root observed, not a nested-rights grant | VBC claims, capitation, attribution, risk adjustment, quality measures, savings benchmarks and value-based contracts. Contract-by-contract cautions are applicable as general reasoning, but this is **provider/ACO/VBC economics**, not a PBM compensation audit. | **Adjacent only.** Do not copy model-specific rate formula, clinical HCC logic or unverified dated CMS requirements into PBM analysis. |
| [Autter-dev/agentic-sales-skills: contract-reviewer](https://github.com/Autter-dev/agentic-sales-skills/tree/ed5191cb340be3100c9c7f33ed54584eea1f7823/04-proposals-and-close/skills/contract-reviewer) (`ed5191c...`) | **2/2**: SKILL.md, README.md | Root `LICENSE` MIT, SHA `593d62d3cfc489ad1d9a054a4678e807303b4d3d` | Sales MSA/order form risk, renewals, termination, SLA and negotiation suggestions. No PBM rebate definition, settlements, affiliate fees or claim-level reconciliation. | **Generic complement.** Uses qualitative recommendations without the precise financial evidence gate required here. |
| [takusaotome/claude-skills-library: contract-reviewer](https://github.com/takusaotome/claude-skills-library/tree/dd1fb14d0fc6937104657c9ff1770abc57e81683/skills/contract-reviewer) (`dd1fb14...`) | **13/13** enumerated files: SKILL.md, assets 2, docs 1, references 5, scripts 2, script tests 2 | Root `LICENSE` MIT, SHA `1d3316873bc75c676c76022840410006dc2f1369` | Broad business contract clause/risk classification. Bundled Python regex classifier, optional PyPDF2, report generation with an output-path write, fixed numeric score and automatic "approve/reject" thresholds. Its bundled historical code review and tests are **not** proof current script behavior was executed here. | **No unchanged-use recommendation** for the PBM need. Its risk-score thresholds cannot establish healthcare contract breach, and optional script writes/PDF dependency require separate authority/security qualification. |

The exact pinned SKILL.md hashes checked were `eecd39d69957bcd5950ab25fd8ead1e5a543e601` (aks billing), `154d730a041d9679b2dcd4b2d62767f30e2fee67` (aks VBC), `34dc492a8b47c02c7d65adf3170b51de483bf775` (Autter) and `46bcd9e58b0c66ffa1e08df12f9d3896ee694086` (takusaotome). Supporting file structure and full content were fetched at the same pinned commits; no source changed during inspection in this session. The previous broader receipt also inspected [aiunlocked1412 insurance-advisor](https://github.com/aiunlocked1412/claude-skill-unlock/blob/f40e6c332784b7bd66999dd52aafa58cfd4c3816/skills/05-business/insurance-advisor/SKILL.md), a Thai consumer product-comparison workflow whose root `LICENSE` was unavailable. Its reuse rights remain unknown; no import.

## Licensing decision

**CREATE / independently author**, not ADAPT an upstream skill. Our healthcare package and all fixture text are original first-party content covered by the repository's MIT license. Inspecting source methods did **not** import protected expression or satisfy a license gate for later borrowing.

For *any* subsequent partial adaptation, repeat exact-source inspection of (a) the original publisher and package path, (b) root and nested licenses/third-party excerpts, (c) modification/attribution notices, (d) code and bundled data rights, and (e) the requested distribution destination. MIT/Apache at a repository root is evidence of *a license*, not a substitute for inspecting material and terms. No root LICENSE found is **rights unknown**, not public domain.

## Concrete review conclusions

1. **Substantive novelty in inspected packages is a matter of fit, not a market-exclusive claim.** None of the four complete directories performs the combined employer/PBM defined-rebate, affiliate-compensation, claim-invoice reconciliation and evidence-led negotiation analysis required for issue #714.
2. **Software/clinical VBC workflows are adjacent but can contaminate contract analysis.** Claims engineers need X12/CARC/RARC/clinical context; PBM sponsor auditors need the signed defined terms, settlement records and plan fee schedules. Do not make a clinical diagnosis, assume every claim export is authorized, or recycle dated regulatory assertions.
3. **Third-party scripts are a separate action boundary.** An imported "contract reviewer" that installs Python libraries, reads arbitrary contract paths or writes reports is not equivalent to a passive read-only skill. Static scripts were inspected here, not run or cleared for execution.
4. **Score thresholds are not evidence.** Numeric "contract risk 78/100 => reject" is not a verified legal or economic conclusion without task-specific rationale and supplied benchmark.
5. **Open limitations:** Four complete packages were inspected, not all 233 lexical leads; 61,326 records were path-indexed, not all source bodies reviewed. Nested rights/third-party excerpts in candidate packages were not independently cleared for material reuse. No model-host behavior test or comparative accuracy study was performed.

## Local package improvements informed by the review

- Retain read-only authority, anti-injection source treatment and qualified counsel boundary.
- Keep scope to employer/PBM contract economics rather than insurance buying or clinical software.
- Show a complete fictional worked report; trace each case amount to a source row and contract clause.
- Add explicit later-amendment precedence, duplicate paid-claim and untrusted contract-note counterfactuals, with expected outcomes.
- Keep **verified arithmetic variance** and **verified money owed** explicitly distinct, including an **underbilling** scenario where the old fee is superseded.

**Outcome:** Four complete pinned packages materially characterized for this specific fit question, no observed license authorization for copied content needed because nothing was copied, and no new behavioral-validation claim. Additional specialist-source review remains open.
