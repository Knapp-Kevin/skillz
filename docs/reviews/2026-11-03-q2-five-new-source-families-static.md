# Q2: five new source families, 127 exact packages at current standard (2026-11-03)

**Scope:** exact-pinned, 10-dimension static source-vetting candidate decisions. This is not governed review, admission, a security scan, behavioral validation or installation approval.

This tranche follows [Q1](2026-11-03-q1-four-new-source-families-static.md) and uses the same brief, rubric, hard gates and integration checks. The five sources are original-author repositories found and identity-verified in GitSkills discovery: [G1](../discovery/2026-11-03-gitskills-g1-source-diversity.md) found `trycomp-io/comp-skills` and [G2](../discovery/2026-11-03-gitskills-g2-second-wave.md) found the other four. They were chosen as unclaimed families in underserved domains.

The pins are unchanged since verification. Every package at each pin was reviewed, so every review cursor is complete.

## Sources and results

| Source (exact pin) | Domain focus | Packages | REFERENCE-ONLY | REJECT | Threshold signal | Ledger |
|---|---|---:|---:|---:|---:|---|
| `rvanshur/vertical-gtm-skills` @ `a9ee9d3547e1df59fe5b170b7fefc4ecff57350b` | sales / GTM | 29 | 29 | 0 | 23 | [ledger](../../registry/discovery/q2-rvanshur-vertical-gtm-skills-static-20261103.json) |
| `jirawatp/resume-career-toolkit` @ `85189e64c79dd544aa40d2d8b1a205517e6b0775` | career | 20 | 18 | 2 | 4 | [ledger](../../registry/discovery/q2-jirawatp-resume-career-toolkit-static-20261103.json) |
| `vl4dt/godot-skills` @ `1ae280d35f2cc3931d4d8eb63f4bac82d6acf4a0` | game development | 23 | 6 | 17 | 1 | [ledger](../../registry/discovery/q2-vl4dt-godot-skills-static-20261103.json) |
| `trycomp-io/comp-skills` @ `3bbe033b448243a46fb03fca63b7f426f852a3a1` | HR / compensation | 37 | 1 | 36 | 0 | [ledger](../../registry/discovery/q2-trycomp-io-comp-skills-static-20261103.json) |
| `kyleoliveiro/sg-gov-skills` @ `16892fc613263c3f835457cd23ae092d404979ca` | government (Singapore) | 18 | 18 | 0 | 17 | [ledger](../../registry/discovery/q2-kyleoliveiro-sg-gov-skills-static-20261103.json) |
| **Total** | | **127** | **72** | **55** | **45** | |

**Identity:**
- **Root licence.** Every repository has an MIT root LICENSE. The blob and holder are in each ledger.
- **Package-local licences.** No package carries one.
- **Shape.** All 127 SKILL.md paths are direct packages, recorded by blob and package-tree SHA.
- **Template path.** `docs/skill-template/SKILL.md` in `vl4dt/godot-skills` is an unfilled template. Its REJECT is annotated as a template path.

**Hard fails:**

| Flag | Packages | Why |
|---|---:|---|
| `literal-credential` | 36 | All 36 bundle the same vendor client with a hardcoded default API key. The value is not reproduced anywhere in this evidence. |
| `capability-content-mismatch` | 4 | Godot packages whose code targets Godot 3 or invented APIs while claiming Godot 4.x. |

The other 15 REJECTs are for low quality, including 3 moved below the 10/20 floor at integration.

**Scores:** 18 ×3, 17 ×12, 16 ×21, 15 ×10, 14 ×7, 13 ×11, 12 ×18, 11 ×20, 10 ×5, 9 ×9, 8 ×5, 7 ×1, 6 ×2, 5 ×1, 4 ×2.

**REFERENCE-ONLY by domain:**
- career 18, sales 14, security 10, software engineering 6, memory/context 5, cloud/devops 4
- 2 each: game design, marketing, product, UX
- 1 each: agent/MCP, audio, business, law, planning, testing, visual design

Routing entries are in the [capability routing file](../../registry/discovery/q2-new-source-families-capability-routing-20261103.json).

## Source-family findings

- **Sales/GTM (`rvanshur/vertical-gtm-skills`).** This is the strongest authority design of the tranche.
  - **Shared contract:** one contract applies across all 29 skills. They are draft-only and never send, enrol contacts or write to the CRM. CRM and call-recorder reads happen only after a yes and only for named records. Working another rep's account needs the owning rep's yes.
  - **Evidence discipline:** facts need evidence tags, unconfirmed elements are left out of scores, and only customer-confirmed proof points may go into talk tracks.
  - **Gaps:**
    - Only one skill checks opt-outs, and there is no CAN-SPAM or GDPR guidance for cold email.
    - No skill treats pasted CRM notes or transcripts as untrusted.
    - Contact email and phone are handled without minimisation.
    - The Discovery skill writes to the shared profile and knowledge base without an owner-approval step.
    - Two skills declare `mutating: false` but write files.
  - **Packaging:** rules specific to the cemetery/funeral-home vertical bleed into the generic core. SKILL.md files run 90–180 KB.
- **Career (`jirawatp/resume-career-toolkit`).** Advisory only; nothing is submitted or sent.
  - **Anti-fabrication is uneven.** It is strong in the resume-customizer and bullet-rewriter skills. It is missing in the case-study and cover-letter skills. One worked example adds an unsupported figure.
  - **Other gaps:** no minimisation of résumé personal data, no handling of instructions embedded in pasted job postings, and US conventions presented as universal.
- **Godot (`vl4dt/godot-skills`).**
  - **False compatibility:** the skills claim Godot 4.0–4.7 support, but much of the code is Godot 3 or invented API.
  - **Missing references:** references are missing at the pin, and advertised MCP tools are not defined.
  - **Harmful scaffold:** it ignores `*.godot`, including `project.godot`, and disables asset import.
  - **Insecure save loading:** `.tres` saves are loaded without warning about code execution.
  - **Attribution note:** the root licence names "RoboCat" while the skill metadata names vl4dt.
- **HR/compensation (`trycomp-io/comp-skills`).**
  - **Hardcoded vendor key** in 36 of 37 packages.
  - **Email re-sent without asking:** once a user's email is stored, it is re-sent to the vendor on the first run of each new skill. The README's "no tracking" and "network only if a key is configured" claims are misleading.
  - **Mandatory vendor branding.**
  - **Calculation and privacy defects:**
    - Decimal stripping turns 8500.50 into 850050.
    - INSS/IRPF tax tables are stale (2024).
    - There are re-identification leaks and named-individual risk lists.
    - Candidate screening has no fairness gate.
  - **Salvage** is recorded per package.
- **Singapore government (`kyleoliveiro/sg-gov-skills`).** Accurate, current integration and security-control guidance (scores 15–18), but Singapore-specific.
  - **Rights note:** embedded government documentation text is credited, but its reuse terms are not stated.
  - **No approval step:** infrastructure skills give no approval step before applying org-level guardrail, IAM or security-group changes (authority 1). The secure-pipeline skill directs visibility changes and Git history purges without confirmation, so its threshold signal is withdrawn.
  - **Credentials redacted:** vendor-published sandbox credentials and seeded fixture secrets are not hard fails, and are redacted here.
  - **Lapsed deadline:** the Myinfo v3/v4 migration deadline (end September 2026) has passed.

## Method and controls

- **Review.** 16 parallel read-only reviewers worked on disjoint, size-balanced batches. Coverage is stated per package. Several sales SKILL.md files over 60 KB were characterised within the allowance.
- **Credential redaction.** Reviewer output was redacted before integration. Two reviewers had copied an 8-character prefix of the hardcoded vendor key, and one had copied vendor sandbox and fixture passwords. Every published Q2 file was then scanned, and the key, its prefixes and those passwords are absent.
- **Overrides (5).** Listed in each ledger: 3 floor moves, 1 template annotation and 1 threshold withdrawal.
- **Nothing executed.** No package, script or test was run, installed or fetched. Security scans: **0**. Behavioral validations: **0**. GitHub Actions triggered: none.

## Proposed accounting delta for the integration worker (not applied here)

The five shared accounting surfaces, `registry/sources.yaml` and `registry/capability-directory.json` are deliberately not edited.

- **Current-standard exact-path decisions outside the four-source snapshot:** add 127 (72 REFERENCE-ONLY / 55 REJECT). Q1 + Q2 together give 240 (165 / 75).
- **New source families with a complete exact-pin cursor:** add 5 (9 with Q1). Registration is the integration worker's decision.
- **Capability directory:** 72 REFERENCE-ONLY examples are available. They notably raise career (4 → 22 candidate examples) and sales (2 → 16).
- **Unchanged:** governed review records (1,039), the four-source 4,809/4,813, admissions, scans and behavioral validation. The eligible denominator is still unknown.
