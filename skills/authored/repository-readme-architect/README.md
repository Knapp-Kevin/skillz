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

The checker is read-only and standard-library only. It checks common local links, file/heading anchors, reference definitions and explicitly delimited generated content. It never executes a README command, follows symlinks, calls a provider or validates a release claim. Complex Markdown, external URLs, factual accuracy, installability and actual reader success require separately reported evidence. The script is **optional**, not a requirement for users on weaker hosts or systems without Python.

## Qualification and boundaries

**Current version: 0.2.0.** A local Python 3.13.5 run passed **57/57 actual tests**, including controlled CREATE, UPLIFT and VERIFY exercises. The source-checkout CREATE example's documented command and unit test were executed against a controlled first-party fixture. This is bounded *method execution*, **not** independent model-host skill validation, verified third-party deployment or evidence that every generated README is production-ready.

Generated sections, canonical ownership, release evidence, licenses and historical signer identity must be preserved or corrected only from appropriate source evidence. The helper does not mutate files, and reading this skill never authorizes new permissions, CI runs, deployments, releases or unrelated repository changes.

A README succeeds when the actual reader can understand the project, take the correct first action (or understand why none is available), and verify consequential claims. Its job is not to become an ongoing PR diary.
