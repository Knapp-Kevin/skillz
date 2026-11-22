# Repository README Architect

Create a **complete, honest README from scratch**, materially improve one that already exists, audit its reader journey, or verify evidence and navigation without rewriting the repository.

The skill produces a finished Markdown artifact or an explicitly authorized focused change, not an empty template or a marketing checklist. For repository collections and organization profile READMEs, it also evaluates **abstraction-first navigation** when that serves the reader better than a flat inventory, while separating conceptual roles from proven dependencies. It adapts to libraries, CLIs, applications, services, monorepos, research, datasets, documentation projects and repositories that have no implementation yet.

## Start here

**[Read the full standalone skill](SKILL.md)**. The normative CREATE, UPLIFT, AUDIT and VERIFY methods, authority boundaries, safe fallback and delivery criteria all live in its entrypoint. No Skillz repository, account connection, runtime, or sibling skill is required.

For deeper or repeatable work, this *optional in-package* material is available:

- [Quality and evidence contract](references/readme-quality-contract.md): source-to-claim traceability, project archetypes, preservation inventory, first-success checks and release-ready acceptance gates.
- [Controlled scenarios](examples/controlled-scenarios.md): realistic creation, revision, fact-checking, missing-permission and adversarial test cases.
- [Abstraction-first portfolio example](examples/abstraction-portfolio-example.md): a wholly fictional, accessible multi-project navigation showing product-to-foundation conceptual layers, unrelated items, and an alternative first step for each audience. Semantic dependencies and external destinations are deliberately NOT_VERIFIED.
- [Source-checkout CREATE example](examples/create-python-library-output.md), [empty-repository CREATE example](examples/empty-repository-output.md) and [AUDIT example](examples/audit-output.md).
- [Offline local-link and generated-region checker](scripts/check_readme.py), with [its regression suite](tests/test_check_readme.py).

## Optional mechanical check

On a **separately authorized local repository snapshot**, using Python 3.9+:

```text
python3 scripts/check_readme.py --root /approved/project --readme README.md
python3 -m unittest discover -s tests -v
```

Before UPLIFT, follow the [four mandatory delivery safeguards](SKILL.md#four-mandatory-readme-delivery-safeguards) and, when a safe local Python interpreter is available, inspect the candidate with:

```text
python3 scripts/delivery_preflight.py --root /approved/project --mode UPLIFT --readme README.md --baseline .review/README-before.md
```

A UPLIFT that removes or substantively changes original content, including safety-critical headings and heading-only sections, requires an evidence-bound section disposition manifest; generated READMEs must be modified through their authorized generator, not by hand. Local documentation formatters should be identified before editing, then executed safely when available and authorized. Required CI gates must never be bypassed, and CI receipts must match the candidate commit.

For a generated README, the optional preflight also accepts
`--generated-evidence .review/generated-owner.json` with exact local
generator/template file fingerprints, output SHA-256 and a named required
CI drift-check receipt for the candidate HEAD. A locally consistent attachment
stays **blocked pending independent human review**, not authenticated generator execution
or permission to hand-edit generated files. Missing or mismatched evidence
stays blocked. The format and verification limits are documented in the
[bundled quality contract](references/readme-quality-contract.md).

The link checker is read-only and standard-library only. It checks common local links, file/heading anchors, reference definitions and explicitly delimited generated content. It never executes a README command, follows symlinks, calls a provider or validates a release claim. Complex Markdown, external URLs, factual accuracy, installability and actual reader success require separately reported evidence. The script is **optional**, not a requirement for users on weaker hosts or systems without Python.

## Reader-first Gold Standard

The first screen answers **Why → What → How**, in that order: reader
problem and significance, verified project value, and a practical way
to begin. A first-time visitor should understand purpose within
30 seconds. Introductory language targets approximately tenth-grade
accessibility, while deep technical content moves into linked references
without losing accuracy. The root README is a public-facing introduction,
not an automatically generated API manual.

Gold also requires a first-success path with a meaningful, observable
result; a generic test command alone does not qualify. Visual asset
inventory distinguishes verified existing artwork, newly committed
artwork, proposed placeholders and approved final branding. Structural
checks cannot replace independent editorial, rendered or newcomer
acceptance.

## Gold/Platinum quality acceptance

**Gold is the default quality benchmark for substantive repositories.**
Baseline is only appropriate when a compact artifact serves the reader
better, with an explicit justification. Different repository types will
need different onboarding and presentation designs, not different truth or
usability standards.

The skill sets the standard. Existing organization READMEs, brand assets
and style rules are **identity and provenance evidence**, not permission
to downgrade an explicitly requested Gold or Platinum outcome. The
selected profile makes appropriate banner, legitimate badges, working
table of contents, usable first-success example, technical navigation
and evidence-qualified claims binding requirements. Platinum also
requires independent reader and accessibility/responsive review.

Use the [read-only profile checker](scripts/profile_acceptance.py)
with a [project-specific contract](examples/gold-quality-profile.json)
to detect missing presentation requirements. Missing items are FAIL;
evidence-bound exceptions remain HOLD until independently adjudicated.
External badge legitimacy, rendered quality and actual reader outcomes
are never proven by a local string match. Both technical delivery
acceptance **and separate editorial quality acceptance** must pass.
Existing generated ownership and preservation safeguards remain intact.

## Offline Gold/Platinum regression

From this standalone skill package, exercise the 48 synthetic negative
and boundary cases with no network, provider or GitHub Actions budget:

~~~sh
python3 -m unittest discover -s tests -p 'test_profile_acceptance.py' -v
~~~

This is the **test command**, not a claim that the current v0.4.1 suite
has executed. The checker deliberately returns a HOLD even with all
mechanical conditions present because actual source authority,
generated-file parity, approved branding, rendered Markdown,
first-user comprehension and CI delivery require independent evidence.

## Qualification and boundaries

**Current version: 0.4.1 (binding quality profiles, generated-owner evidence, nested heading preservation).** Previous v0.3.0 Python 3.13.5 suites passed **101/101 actual tests** (57 existing link/README exercises plus 44 new delivery-preflight tests), including controlled CREATE, UPLIFT and VERIFY exercises. The source-checkout CREATE example's documented command and unit test were executed against a controlled first-party fixture. This is bounded *method execution*, **not** independent model-host skill validation, verified third-party deployment or evidence that every generated README is production-ready.

Generated sections, canonical ownership, release evidence, licenses and historical signer identity must be preserved or corrected only from appropriate source evidence. All bundled checkers are read-only. They do not authenticate provider evidence, execute README commands, render pages or run formatters/CI. A local check is not a merge-ready verdict and cannot certify the selected quality grade. Reading this skill never authorizes new permissions, CI runs, deployments, releases or unrelated repository changes.

A README succeeds when the actual reader can understand the project, take the correct first action (or understand why none is available), and verify consequential claims. Its job is not to become an ongoing PR diary.

**v0.4.1 source correction:** The profile checker's section reader now
retains nested `###` first-use/contents subheadings and ignores fake
headings inside fenced code. Five adversarial/preservation regression
methods are included in `tests/test_profile_acceptance.py`. A bounded
local method reproduction covered four cases, but the complete updated
package Python suite and any independent README reader acceptance are
**NOT_RUN**; historical v0.3 results cannot qualify new bytes.
