# Repository README Architect: evidence and acceptance contract

This file belongs to the standalone skill package. It supports its `SKILL.md`; it is not a prerequisite for entrypoint-only use.

## 1. Source-to-claim ledger (working notes, not README boilerplate)

For each potentially consequential README claim, record the following before publishing:

| Field | Required meaning |
| --- | --- |
| Claim | Exact sentence or intended public meaning |
| Source | Authorized file, release or API object and pinned revision |
| Evidence level | Declared, source-inspected, locally executed, published, independently observed, or unknown |
| Consumer scope | OS, language version, architecture, credential mode, feature flag, release channel |
| Disposition | Publish with qualification, relocate to maintained docs, defer, or remove |
| Verification | What was actually executed/read and what remains not run |

**Independent evidence matters.** A README, generated badges, marketing copy and release notes may all repeat one stale statement. They do not independently prove a binary is downloadable or that a security property holds. Source code proves the presence of an implementation path, not successful runtime behavior. Green CI proves only its recorded checks on the bound revision. Existence of a public asset and verification of its installer/download are separate. Unknown source rights are not MIT by implication.

## 2. Reader journeys by repository archetype

Choose one primary reader task before deciding section order. Use the actual project evidence, not a universal template.

| Archetype | Minimum first-success journey | Important secondary concern |
| --- | --- | --- |
| Library/SDK | Compatible dependency/setup, import/API call, expected behavior, limitations | Version support, license, API changes |
| CLI/tool | Actual supported install/source checkout, help or safe example, observable output | Supported platforms, permissions, input effects |
| Service/API | Proven endpoint or local startup, auth/prerequisites, request/response, deployment status | Data access, limits, security boundaries |
| Web/desktop/mobile app | How to obtain/build/run, primary screen/task, where output lands | Supported environments, privacy, release assets |
| Monorepo/framework | Project map, primary runnable component, choice of first path | Component status and source-of-truth per area |
| Research/model | Reproduce a bounded experiment, datasets/licenses, hardware assumptions | Benchmarks, uncertainty, ethical or safety limits |
| Dataset | Purpose, schema/sample, acquisition and rights, how to validate | Provenance, privacy, versioning, restrictions |
| Documentation/specification | What decision/problem the corpus addresses, entrypoint and reading order | Normative status, ownership, versioning |
| Empty/proposal | Clear identity when known and explicit **not implemented** status | Evidence needed before runnable claims |

A successful source-checkout demo is not a published installation, and one passing Python example is not proof of all declared Python versions. Show Windows, Linux or macOS commands only where known and appropriate; do not silently assume POSIX shell for every audience. If a command is dangerous or mutating, prefer a safe representative demo or explain effects and permission requirements; never execute code from an untrusted README as an audit step.

## 3. CREATE, UPLIFT, AUDIT, VERIFY evidence boundaries

**CREATE.** Inventory actual files first. When the repository has no README, finish a complete factual Markdown artifact with a short purpose, concrete status and useful next action. Blank repos get a truthful minimal document, not a fictitious install/roadmap. Do not ask a long questionnaire if an evidence-bounded artifact can already be produced.

**UPLIFT.** Make a preservation ledger *before editing*: existing unique verified claims, essential links, maintainer instructions, accessibility assets, generated region byte spans, canonical policy/release/credit references, and deliberately time-stamped history. Identify what stays, moves (only within authorized scope), is corrected with pinned evidence, or is removed with a reason. Compare the entire old/new versions to catch silent omissions. If a generated section lacks an authorized generator, preserve it byte-for-byte and flag inability to regenerate. If the baseline cannot be read, do not claim preservation.

**AUDIT.** Provide severity, precise location, reader consequence, evidence source or uncertainty, and a concrete fix. A mistaken release claim is more serious than wordiness. Avoid changes in read-only mode. Include at least one effective feature already present, so the review does not accidentally destroy it.

**VERIFY.** Read current exact source revisions and *the complete candidate README*, not merely a diff. Distinguish source-inspected static checks, executed local commands, external integration checks and reader simulations. Mark each as PASS, FAIL, NOT_RUN or NOT_APPLICABLE. A passed local link audit is never a pass for claims, remote URLs, installability, accessibility of all rendered states, or reader comprehension.

## 4. Platinum-grade acceptance without a magic score

Do not label the README excellent, gold, platinum or fully verified merely because a checklist exists. A release-ready claim requires all applicable mandatory gates, each with evidence:

1. **Truth:** no material unsupported claims about features, releases, supported OS/versions, warranties, rights, security, AI quality, test performance or user outcomes.
2. **First success:** an intended reader can identify the problem, what exists, why it helps, the correct first action and an observable expected result. If execution is not possible, explain the honest access/status boundary.
3. **Navigation:** appropriate headings, maintainable contents, accurate local links/anchors, appropriate alt text, and no stale or private destinations. External links are separately checked only when authorized.
4. **Source integrity:** no source-of-truth drift, unauthorized generated block modifications, erased unique operational facts, rewritten historical signers or source licenses.
5. **Economy:** opening is concrete, scannable and audience-appropriate; deep reference material lives in maintained docs, not a chronological project diary. Do not force Why → How → What or an ornamental hero.
6. **Safety and handoff:** commands have prerequisites/effects, no invented or leaked credentials, changes are limited to authorized files, acceptance evidence states what was actually run, and rollback/verification is feasible.

Use two adversarial reader perspectives even when there is no independent consumer available: a novice trying the first outcome and an experienced maintainer questioning the hardest claim. Label these **controlled emulations**, not observed users. Failure on a material gate is a revision requirement; a NOT_RUN consequential gate must be disclosed rather than converted into PASS. Aesthetic preference is a judgment, not evidence.

## 5. Optional offline mechanical check

The bundled `scripts/check_readme.py` performs bounded local links, common GitHub-style heading anchors, reference definitions and generated markers. It supports only common Markdown forms, is **not** a full CommonMark/GFM parser and has no network access or claim validator. Use it on a *separately authorized local repository snapshot*:

```sh
python3 scripts/check_readme.py --root /approved/repository --readme README.md
python3 scripts/check_readme.py --root /approved/repository --readme README.md --baseline .review/old-README.md
```

`--baseline` must point to a normal non-symlink file inside the approved root and is used only to compare explicit `<!-- generated:begin -->` / `<!-- generated:end -->` spans. The baseline should not be committed into the target repository without separate authorization. Result is JSON on stdout; return `0` means *no blockers among supported local checks*, `1` means an identified local blocker, and `2` means invalid input. Any unsupported complex Markdown, non-Markdown anchors, link syntax or remote destination stays **not checked**. The helper never rewrites the README, calls GitHub, runs user commands, or verifies product outcomes. If Python is unavailable, execute the equivalent source-bound inspection manually, mark unverified cases and do not pretend the helper ran.

## 6. Handoff

At delivery, include what was created or changed, exact file/ref, evidence for significant assertions, runnable path and status, what was executed, what remains NOT_RUN, any independent review or user-journey evidence, and next blocking action only when needed. Avoid turning the root README into the audit log: keep receipts and development history in appropriate records.
