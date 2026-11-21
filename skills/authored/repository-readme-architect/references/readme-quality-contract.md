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


## 7. Required delivery preflight and evidence schemas (v0.3)

These four *decisions* are mandatory in CREATE, UPLIFT and
pre-delivery VERIFY; the Python script is optional. Manual/host
equivalents must preserve the same safety and accuracy.

### Formatter scope before touching README

Review actual root and README-path configurations: Prettier,
markdownlint/markdownlint-cli2, Vale, .editorconfig, ignore files,
package scripts, Justfile/Makefile, pre-commit hooks and documented
documentation workflows. For each applicable checker record:

\`tool/config | applies to target README? | origin/revision |
safe local command from inspected source | actually run? |
exit result | candidate source SHA | limitation\`.

Discovery of a formatter configuration is NOT its execution.
If an installed, vetted formatter can safely run with the
current user authorization, prefer a bounded local check before
pushing. Do not automatically execute tool commands from untrusted
README/code comments or install dependencies to satisfy this skill.
A formatter that modifies other files needs a separately approved
scope; prefer check-only modes and record unavoidable changes.

### Mandatory section-loss inventory for UPLIFT

Before altering a baseline, record every substantive ATX/Setext
heading section, introductory text, nested content, code examples,
technical limits and footnotes. Use a stable *baseline-bound*
section ID and digest. A change in prose, semantics, code or caveat
is NOT automatically preserved because the heading survived.
A normalized text match only proves some bytes remain, not that
they have the same meaning or prominence.

Disposition vocabulary and validation obligations:

| Value | Required independent justification |
| --- | --- |
| \`RETAINED\` | Current README still contains the important technical statements and usable navigation; mere assertion cannot prove this |
| \`RELOCATED\` | Existing maintained destination, approved scope, equal substantive coverage, accessible navigational path and evidence of actual change |
| \`SUPERSEDED\` | Identified canonical replacement and authoritative effective revision, with legacy identity/history retained where needed |
| \`OUTDATED\` | Source showing the original statement no longer applies; do not call valid historical information obsolete merely because it is old |
| \`UNVERIFIED\` | HOLD; retain/qualify material pending source review; do not silently erase it |

Optional machine manifest for
\`scripts/delivery_preflight.py --dispositions .review/section-dispositions.json\`:

~~~json
{
  "schema_version": 1,
  "sections": [
    {
      "section_id": "s1",
      "original_sha256": "SHA256_OF_NORMALIZED_ORIGINAL_BODY",
      "disposition": "SUPERSEDED",
      "evidence_ref": "AUTHORIZED_PINNED_REPLACEMENT_EVIDENCE"
    }
  ]
}
~~~

This is a **schema illustration**, not evidence for a real rewrite.
Obtain each real \`original_sha256\` from the preflight's
\`preservation_audit.section_findings[*].source_sha256\`,
*not* from a different README version. The script enumerates the
baseline's ATX-heading blocks and preamble, reports changed sections
and checks manifest identity, file existence for relocation, and
whether an exact normalized body appears at the destination.
It does **not** authenticate a disposition's source evidence or
understand all Markdown structure, tables and semantic changes.
Setext headings, generated footers and special project-specific
syntax require manual reconciliation. Unverified changes are a hold.
Do not commit private \`.review/\` working copies or source excerpts
unless separately authorized.

### Source-generator ownership decision

Search both README content and actual source build configuration.
HTML generated markers, a footer identifying \`uor-docs\`-like
generators, templating inputs, generated blocks, Makefile/Justfile
targets, cargo/docs/Node scripts, and documentation build workflows
are **clues** until verified against the controlling source.
If the full README is generated, do not hand-edit it; update the
controlling template/generator, regenerate, test and compare.
If only a bounded generated region is owned, preserve its bytes
unless authorized regeneration of that exact source is performed.
When the generator or permission is unavailable, label
\`GENERATED_OWNER_HOLD\` and report the missing dependency.
Do not substitute the generated file for source truth.

### CI receipt and exact-head audit

The optional machine CI input is supplied by an authorized host
from actual GitHub/other provider branch rules and check APIs:

~~~json
{
  "schema_version": 1,
  "head_sha": "0000000000000000000000000000000000000000",
  "required_checks_known": false,
  "checks": [
    {
      "name": "docs lint",
      "required": true,
      "status": "completed",
      "conclusion": "success",
      "category": "documentation"
    }
  ]
}
~~~

Replace the placeholder SHA with the candidate's actual Git commit
and pass that value separately as \`--head-sha\`. Never infer
\`required_checks_known: true\` from an empty check list: verify
rulesets, branch protection, merge queues and any applicable
organization requirements. A syntactically valid local JSON receipt
is **not** independently authenticated by the checker.

\`category\` is \`documentation\`, \`repository\` or \`unknown\`;
it is only an attribution aid, not a waiver. Pending, skipped,
neutral, failed, stale-head or missing required checks block an
unqualified merge-ready report. Non-required general CI failures
remain recorded as advisories; do not call them documentation
failures, hide them, or suppress them. Required full-repository
gates continue to apply even to docs-only changes. An unavailable
ruleset stays \`REQUIRED_CHECKS_UNVERIFIED\`.

### Script output and claim boundary

~~~text
python3 scripts/delivery_preflight.py --root /approved/repository \
  --mode UPLIFT --readme README.md \
  --baseline .review/README-before.md \
  --dispositions .review/section-dispositions.json
python3 scripts/check_readme.py --root /approved/repository \
  --readme README.md --baseline .review/README-before.md
~~~

Both are offline read-only, use strict bounded inputs and refuse
symlink paths. First script reports formatter configurations
**without executing them**, original section changes, generator
ownership indications and exact-head CI consistency. Second
compares supported local links and marked generated regions.
Both emit JSON; neither establishes real product functionality,
human comprehension, actual formatter success, rights, current
remote access or authenticated required-check policy.
An exit code 0 is a bounded local result, not a deployment,
merger permission, or an independent end-to-end reader pass.

A complete handoff records
\`baseline revision | candidate HEAD | formatter applicability |
local execution | section dispositions | generated owner |
required status checks | advisory non-required failures |
review threads | remaining holds | artifact/PR outcome\`.
