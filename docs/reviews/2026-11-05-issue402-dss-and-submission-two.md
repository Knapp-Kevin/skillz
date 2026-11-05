# Issue #402: Singapore accessibility and student-submission safety, exact static review

**Reviewed 2026-11-05 as passive source content.** [Machine-readable review ledger](../../registry/security/q8-two-incomplete-dss-and-student-privacy-static-dispositions-20261105.json) records 2 complete pinned Git package trees, 14 exact owned file blobs, 3 relevant sibling/shared upstream source blobs and 2 root MIT license notices. No government website was checked live for current standards, no Oobee/axe/browser test was run, no student files or sensitive academic data were transferred, and no third-party script or agent was executed. No installation or public/agency-facing action was approved.

| Package | Exact pinned package Git tree | Static score | Outcome |
|---|---|---:|---|
| [SG DSS Accessibility](https://github.com/kyleoliveiro/sg-gov-skills/tree/16892fc613263c3f835457cd23ae092d404979ca/skills/sg-gov-dss-accessibility) | `d616f58c9079b3b78a3e367873b2d3e7982c5d3a` | 15/20 | Reference-only; compliance certification and code/CI execution held |
| [Submission Auditor](https://github.com/YujxZJCN/teaching-skills/tree/fd0c486e61cb1f065b88133b599e8806dfaeac12/submission-auditor) | `9bfa23e2d497c948cf9dd41fbf02f2d66d56c30c` | 15/20 | Reference-only; identifiable student processing or report delivery held |

All current source pin package trees match their originally recorded Q12 scanner evidence and current upstream default-branch revision at this checkpoint. Both historical scanner states remain **INCOMPLETE**, not new passes. Source-content scoring and operational permission are separate dimensions.

## Singapore DSS Accessibility

**Source identity:** `SKILL.md` blob `ec0e8e20c2dce3f941395eb4eabb452a49b40da6`; six owned package files include the 53-control reference, two static JSON eval files and two intentionally flawed HTML fixtures. Root license MIT `4c827fc32ce43ebdadc16de241277918e2690113`, for source-authored work only.

The main source embeds Singapore Digital Service Standards text from **July 16, 2026**, relying on published pages that it says were last updated March 5, 2026. It describes 53 controls and two WOGAA traffic tiers, and labels its WCAG crosswalk as **inferred**, not government-issued. These are helpful source facts, but **no live current government-source verification was performed**. Issuing an authoritative compliance certificate from a dated snapshot would be unsafe. Confirm controlling DSS/SSP details with the responsible agency and current official sources before a current claim, especially decisions about Level 1/2 deviations and traffic-based tiers.

The substantial `references/wcag-controls.md` file reproduces government **control statements, recommendations and rationales**. The author's MIT root license does not by itself establish reproduction/relicensing rights for those embedded government text passages. Verify their original reuse terms separately. Linking/citing and independent high-level explanation is distinct from copying text wholesale.

The guide suggests Oobee and axe scanning and CI integration. Those operations could fetch private agency pages, process credentials or mutate repository CI, and need explicit target, policy and runtime permission. Its six JSON test cases and two HTML fixtures are **unexecuted evaluation inputs**, not accessibility acceptance receipts. The historical scanner's AR2/P3 alerts remain preserved, not reclassified by this review; the P3 location is inside a timeout-modal example, not an observed exfiltration command.

**Reusable value:** semantic HTML, labels, focus, screen-reader and live-region checks, contrast, reflow and scoped user testing with source-linked findings. Use a current official control matrix and real authorized accessibility tests before calling a service compliant.

## Submission Auditor

**Source identity:** `SKILL.md` blob `46adb631687ec846990cf3399476a8aeaaee9353`; eight owned files cover four worker agents, design guide and two templates. Root MIT `024003bb56236b1161c03c575372d0e97abd8fc4`, attributable to Jiaxing Yu.

This is a strong read-only *process* concept: require an instructor-confirmed specification, separate mechanical checks from subjective judgments, cite locations in student work, do a fairness consistency pass, and let the professor make decisions before sending any result. The instructions correctly prohibit autonomous grading, student-facing posting and speculative factual findings. Those strengths should carry forward.

Two material risks block unchanged adoption:

1. **Student privacy and institutional authority.** The package proposes handling many academic submissions, quoting portions of work, and generating per-student reports. Its pseudonymization rule is only *where feasible*, without an enforceable consent, host-model disclosure/retention, student-data minimization, identity-isolation or educational institution policy gate. A source review does not give permission to transmit identifiable student work to any AI provider.
2. **Prompt-injection boundary.** Professor templates, exemplars and student submissions are all untrusted input documents. The four-agent workflow does not expressly prevent instructions embedded within those documents from overriding the confirmed professor rubric, triggering tools, causing publication or modifying the audit's allowed scope. Instruction-bearing text within a submission must be evaluated as data only.

The original scanner logged eight missing-reference flags. An important scope correction: `shared/checkpoint_protocol.md` (Git blob `41e533bd540d397053a0807f4147da42344eb97c`), `shared/pedagogy_foundations.md` (blob `ab8172a092ba8812266e31443cc93e4802befe22`) and `student-mentor/references/feedback_principles.md` (blob `fb35d1d4629a35160815f05b5b4097bcc01a7160`) **do exist in the pinned upstream repository**, but **outside the individual eight-file skill package**. They were directly read during this tranche. A standalone distribution must include or identity-bind the required shared authority documents; source presence is not host permission. Historical scanner `INCOMPLETE` remains unchanged.

The declared multi-agent fairness pass is also not a measured fairness result: no actual student corpus, inter-rater review, institutional acceptance or agent workflow test occurred. All person-affecting reports remain professor-only drafts.

**Reusable value:** explicit confirmation checkpoints, located evidence, `NOT_EVALUABLE` and `NEEDS PROFESSOR REVIEW` alternatives, consistent batch severity, and no autonomous release.

## Progress and exact next work

These two packages raise current targeted historically flagged Q8 content-risk reviews to **18/40**, comprising **7/7 historically scanner-FAILED plus 11/33 historically scanner-INCOMPLETE**, leaving **22** incomplete sources for direct review. Historical Q8 scanner outcomes remain 10 PASS / 7 FAIL / 33 INCOMPLETE across the 50 study references. **Zero** new scanner runs, agent-host/clinical/institutional validations, paid operations, unchanged-use approvals, licenses cleared for embedded external text or capability admissions occurred.

The [README current Q8 progress graphic](../../docs/assets/q8-direct-static-risk-review-progress.svg) derives its counts from the original scanner register and explicit static source-review ledgers. It is not a live compliance dashboard or a claim that any studied skill can run unchecked. Issue #402 remains open for 22 still-unreviewed historically incomplete Q8 references and the wider governed corpus; prioritize consequential data egress, external account access and locally executable package code.
