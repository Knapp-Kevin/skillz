# Issue #714: Healthcare Contract Forensics, exact-package static review

**Review date:** 2026-11-06
**Reviewer method:** Maintainer-directed, direct static reading of independently written source instructions and all included supporting text/data, plus separate decimal arithmetic check of fictional fixture.
**Finding:** **19/20 semantic static VERIFIED** for this exact seven-file passive package; **observed agent-host behavioral validation NOT RUN**, **external scanner NOT RUN**, no permission to process PHI or use unchanged in a regulated production workflow.

## Source identity and license

- Origin: [issue #714](https://github.com/Knapp-Kevin/skillz/issues/714); motivating [Mark Cuban LinkedIn post](https://www.linkedin.com/posts/mark-cuban-06a0755b_if-you-are-not-running-all-your-healthcare-share-7524530312345882624-FzV3/).
- First-party, independently authored under repository MIT license. Similar generic concepts were compared, but no third-party skill text, proprietary agreement, real insurer contract, paid data or private health records were copied into the package. Synthetic fixture is invented.
- Canonical source: \`skills/healthcare-contract-forensics/SKILL.md\`; exact Git blob \`6ea8dda7b85b399a252f9b97295d54e536a3f897\`.
- **Full seven-file package tree SHA:** \`3974f153ac39bd27895c4f0365ee50e0ef1527a9\` (separate Git tree created from the included file blobs, not a partial path listing).
- Review snapshot is this exact new work on the isolated issue branch. The final PR merge/rebase source commit must be recorded separately when it exists; this static source identity is content-based.

## Material files statically inspected

| Path relative to skill root | Blob SHA | Role |
|---|---|---|
| SKILL.md | 6ea8dda7b85b399a252f9b97295d54e536a3f897 | Triggers, scope, workflow, stop rules |
| references/clause-review.md | 3b5a0ff7ce050978c01f2fd192a185ade1c6e328 | Economic/legal question categories |
| references/financial-reconciliation.md | 6aae771da94e243280e70cdefa578fb06b3297dd | Arithmetic and admissibility rules |
| references/report-template.md | 0b005dcf746c3c36c680c6dad905c144249f8e07 | Evidence-led report contract |
| examples/synthetic-pbm-case.md | da1b5d44140a05f9d702e8a7c06a66f6da1a96b7 | Fictional clauses and invoice |
| examples/claims-synthetic.csv | d4b01ddbed0a860f4676171383c6df1878bf363b | Four fictitious claim status rows |
| examples/expected-case-review.md | e5f626830242ddf3e381dfb52f7ca538e75f2cfb | Ground-truth interpretations, failure tests |

Relative file links were checked against this exact manifest. There are **no scripts, network requests, runtime dependencies, installers or active model adapters inside the skill package**.

## Evidence behind independent creation

**Discovery scope correction (owner, 2026-11-06):** The **1,039** governed names (2026-11-01) are a *small reviewed-name index*, not a corpus search. The independent G1–G3 snapshot records **61,326 pinned package identity records across 942 repositories**, and additional separately maintained source-family indexes exist. Searching 1,039 names cannot establish the absence of a more relevant specialist skill. See the [full-corpus search contract](../discovery/full-corpus-search-contract.md).

**Expanded, still incomplete discovery evidence:** A source-pinned G1 `legal-contract-review` method-alternatives ledger (2026-11-03) records **7 examined rows, six on-family**, including independent methods for grounded contract markup, tracked changes, legal-document evaluation and contract version disputes. The ledger reports root-license observations such as Apache-2.0 and MIT for some sources, but also **no observed root license** for `HHHHHejia/awesome-legal-aiagent-skills` and `majiayu000/claude-skill-registry-data`. That absence is *not* permission to copy; source/package-specific rights, nested terms and original authorship require verification. This is a study of ledger evidence, **not** a fresh full-package read and **not** a complete cross-family sweep. Do not treat the original no-name-match as a novel-skill determination. Existing evidence-based adjacent methods include:
- \`anthropic-knowledge-work-plugins/review-contract\`: 18/20 verified static, generic contract workflow.
- \`.../legal-risk-assessment\`: 13/20 rejected unchanged for generic threshold/legal-action overreach.
- \`.../audit-support\`: 10/20 rejected unchanged for outdated prescriptive audit concepts.
- \`.../compliance-check\`: 10/20 rejected unchanged due to stale/static legal reference risks.
- \`local-skills/finance-review\`: 19/20 static verified, scoped statement digest rather than contract audit.

Relevant mechanisms (source location, alternate interpretation, arithmetic workpaper, risk/authority controls) are unprotected ideas and were expressed independently. **CREATE** is the disposition. A wider all-family source-pinned discovery sweep remains a **specific open acceptance item** before concluding no specialist alternative exists; do not claim exhaustive market novelty. No third-party protected content was copied into this independently authored skill, so the missing wider rights audit does not imply that its original source text has an unlicensed third-party dependency.

## Static quality rubric (ten dimensions)

| Dimension | Score | Reason |
|---|---:|---|
| Trigger precision | 2 | Employer/PBM contracting is explicit; diagnosis, personal plan selection and generic legal queries excluded |
| Procedure | 2 | Inventory -> definitions -> adversarial interpretations -> reconciliation -> report |
| Authority/safety | 2 | Approved input scope, PHI stop gate, no egress, no vendor action, untrusted contract text |
| Failure handling | 2 | Missing exhibits, OCR, unmatched claims, missing rates, law uncertainty block affected claims |
| Evidence discipline | 2 | Source IDs, exact clauses/rows, counterevidence, value-state distinctions |
| Dependency coherence | 2 | Seven files account for all required references, host math/parser conditional |
| Portability honesty | 1 | Different hosts vary in local PDF parsing, accurate decimal tools and regulated data controls |
| Differentiation | 2 | PBM-defined rebates, retained fees, affiliate disclosure, claims-level reconciliation and negotiation |
| Adversarial resilience | 2 | Explicit opposing readings, injection, overclaim and reversal counterexamples |
| Effectiveness design | 2 | Financial ledger and answer key make outcomes inspectable, not just persuasive text |
| **Total** | **19/20** | **Static semantic review only** |

## Arithmetic check and non-claims

Using the supplied invented claim rows, independent decimal calculation confirmed: three qualifying settled claims, $6.00 expected administration fee, $7.25 invoice fee, **+$1.25 arithmetic variance**; $360 sponsor charges vs $310 pharmacy settlements = **$50 observed price difference**; defined rebates **$50**, unrelated manufacturer admin fees **$20**. These checks validate arithmetic of fixture inputs only; **they do not measure LLM compliance with the skill or a baseline prompt**.

The contract explicitly excludes manufacturer admin fees from defined Rebates and permits plan-to-pharmacy charge differences. Thus neither $20 nor $50 is an established unauthorized retention/overpayment. Preserve that alternative reading and don't assert illegal behavior.

## Regulatory review and staleness

Checked primary public source leads 2026-11-06: [DOL PBM disclosure rule](https://www.dol.gov/agencies/ebsa/about-ebsa/our-activities/resource-center/fact-sheets/pharmacy-benefit-manager-fee-disclosure-final-rule), [Federal Register 91 FR 69092](https://www.govinfo.gov/app/details/FR-2026-11-02/2026-22306), [HHS de-identification](https://www.hhs.gov/hipaa/for-professionals/special-topics/de-identification/index.html), and [CMS Transparency in Coverage 2026](https://www.cms.gov/newsroom/fact-sheets/transparency-coverage-final-rules-cms-9882-f). DOL rule effective 2027-01-04, applicable to plan years starting 2027-07-01 for covered arrangements; therefore **not a basis for a March 2025 compliance assertion**. Sources are dated navigation references, not immutable legal requirements. Any actual audit must fresh-check primary authority and counsel.

## Findings / deliberate limitations

- **Material limitation:** Even correct synthetic arithmetic cannot establish a right to recover or a breach without complete contract and adjustment history.
- **Material limitation:** A one-time static review of instructional content is not actual host behavior with prompt injections or PHI.
- **Material limitation:** Member insurance-plan comparisons involve plan evidence and personal needs, not identical contract auditing. Keep separate until separately designed and validated.
- **Privacy:** Real documents may contain confidential prices and health details. The skill prohibits incidental external uploads and unapproved PHI reads; a specific runtime still must implement lawful and appropriate controls.
- **Corpus tracking:** Historic README/dashboard counts, governed name index and capability-directory snapshot predate this addition. Do not re-date or rewrite prior census evidence to fabricate a synchronized current corpus statistic. Index integration can occur in a separate genuine regeneration/update.

## Next qualification

Use an authorized external host on these invented files, run explicit trigger, non-trigger, injected-note, missing-document and baseline-vs-skill comparisons, record inputs/transcripts/actions and exact package fingerprint. Resolve observed failures before marking \`validated\`. No claims of superiority, monetized savings, endorsement by Cuban, operational clearance or security scanner PASS are supported now.
