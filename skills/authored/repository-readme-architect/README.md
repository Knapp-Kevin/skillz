# Repository README Architect

Create a **complete, honest README from scratch**, materially improve one that already exists, audit its reader journey, or verify evidence and navigation without rewriting the repository.

The skill produces a finished Markdown artifact or an explicitly authorized focused change, not an empty template or a marketing checklist. It adapts to libraries, CLIs, applications, services, monorepos, research, datasets, documentation projects and repositories that have no implementation yet.

## Start here

**[Read the full standalone skill](SKILL.md)**. The normative CREATE, UPLIFT, AUDIT and VERIFY methods, authority boundaries, safe fallback and delivery criteria all live in its entrypoint. No Skillz repository, account connection, runtime, or sibling skill is required.

For deeper or repeatable work, this *optional in-package* material is available:

- [Quality and evidence contract](references/readme-quality-contract.md): source-to-claim traceability, project archetypes, preservation inventory, first-success checks and release-ready acceptance gates.
- [Controlled scenarios](examples/controlled-scenarios.md): realistic creation, revision, fact-checking, missing-permission and adversarial test cases.
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

## Qualification and boundaries

**Current version: 0.3.2 (generated-owner evidence attachment and heading-preservation fix).** Previous v0.3.0 Python 3.13.5 suites passed **101/101 actual tests** (57 existing link/README exercises plus 44 new delivery-preflight tests), including controlled CREATE, UPLIFT and VERIFY exercises. The source-checkout CREATE example's documented command and unit test were executed against a controlled first-party fixture. This is bounded *method execution*, **not** independent model-host skill validation, verified third-party deployment or evidence that every generated README is production-ready.

Generated sections, canonical ownership, release evidence, licenses and historical signer identity must be preserved or corrected only from appropriate source evidence. Neither helper mutates files, authenticates provider evidence or runs formatters/CI. A locally green report is not a merge-ready verdict. The helpers do not mutate files, and reading this skill never authorizes new permissions, CI runs, deployments, releases or unrelated repository changes.

A README succeeds when the actual reader can understand the project, take the correct first action (or understand why none is available), and verify consequential claims. Its job is not to become an ongoing PR diary.
