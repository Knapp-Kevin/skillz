# Capability-adaptive execution: offline-package closure correction

**Date:** 2026-11-19  
**Scope:** Universal authoring and review requirement; material correction to the independently authored CI Guard package.  
**Qualification:** Complete-package static path closure and simulated offline usability decision. This is **not** a cross-model host benchmark or independent agent-host behavioral validation.

## Owner finding and universal decision

A central repository-wide authoring standard cannot serve as a **mandatory runtime reference** for independently downloaded skills. Offline hosts, incomplete workspaces and Skill Mason exports may have only one skill directory. The universal standard remains normative to Skillz maintainers; each package must embody its required runtime instructions locally. External sources, online links and sibling skills may be optional informational references or explicit handoffs, never implicit requirements.

The following maintainer sources now codify this for **all existing and future authored skills**:

- `docs/capability-adaptive-skill-execution.md`: offline standalone package-closure requirement.
- `docs/skill-template.md`: authoring/example guidance and offline closure checklist.
- `docs/skill-verification.md`: dependency hard-fail for mandatory off-package content and honest complete-package verification.
- `skills/authored/README.md`: distribution policy.

No blanket existing-corpus certification, new required CI check or unreviewed third-party file change was performed.

## CI Guard v1.2 material correction

**Prior exact package:** entrypoint Git blob `29de6cb583efaca3edac1ea39fa557909b17807b`, six-file tree `6c9075636b92c6bddd601bcfdb8f975131a93ec1` (v1.1).  
**Reviewed current package:** entrypoint Git blob `a98f04ad42fedec08d316605ba7d390c7de3b5f1`, six-file tree `950bf5db6b9740bdd3fa92721ffb5a8a0fb9c258` (v1.2).

- Moved the full adaptive execution contract into the standalone `ci-guard/SKILL.md`: outcome, safety, authority, evidence, failure/acceptance and proportionate effort; direct/guided/fallback execution remains available.
- Removed the repository-relative governing dependency `../../../docs/capability-adaptive-skill-execution.md` from the entrypoint and `../../../../docs/capability-adaptive-skill-execution.md` from `components/diagnostic-paths.md`. The diagnostic component links only to its local `../SKILL.md`.
- A cross-skill handoff to Repository Delivery Assessor is **optional when separately installed**; CI Guard continues bounded CI analysis without that sibling package.
- Added local offline M7 adversarial expectation: using only the copied `ci-guard/` folder with no repository or network must not block an otherwise authorized CI assessment. This is a **test contract**, not proof a different model executed it.

## Static offline closure result

Inspected the **six package files** at the above exact tree: `SKILL.md`, three component Markdown files, `examples/acceptance.md`, and `LICENSE`. Resolved Markdown link targets using only relative paths within that six-file set. Results:

| Check | Observed |
| --- | --- |
| Complete tree | Six files, including all three optional components, cases and license |
| Markdown relative links | Seven occurrences; all resolved to existing files in this package |
| Escaping relative paths | Zero |
| HTTP(S) Markdown dependencies | Zero |
| Missing local Markdown targets | Zero |
| Other bundled executable dependencies | None declared |
| M7 offline scenario | Static contract examined, **not** model-host executed |

**Static package closure PASS for the documented Markdown dependencies.**
This does **not** establish that a host with no CI repository evidence can complete a CI review, only that missing Skillz policy files no longer prevent using a correctly installed package. Actual operation still depends on user-supplied CI data or authorized host tools and permissions.

## Corpus entrypoint scan: not a blanket pass

Read the current 30 authored `SKILL.md` entrypoints and classified Markdown references at the **entrypoint only**; auxiliary package files and exports outside CI Guard were **not** comprehensively audited. Nine entrypoints had at least one outbound link before remediation:

| Package | Observed outbound reference | Qualification still required |
| --- | --- | --- |
| `ci-guard` | mandatory repository-wide authoring-standard link | **Fixed in v1.2**, all six bundled files closure-checked |
| `character-motivation-interview` | external website and central discovery note | confirm informational provenance only; no operational dependency |
| `narrative-scene-gap-audit` | external website and central discovery note | confirm informational provenance only; no operational dependency |
| `healthcare-contract-forensics` | external issue and third-party source URL | confirm citation/provenance only; no mandatory runtime fetch |
| `federated-source-catalog` | sibling file curator skill link | confirm optional handoff or add local fallback |
| `file-lifecycle-curator` | sibling federated catalog skill link | confirm optional handoff or add local fallback |
| `metadata-taxonomy-steward` | sibling file-curator and catalog links | confirm optional handoff or add local fallback |
| `reference-integrity-auditor` | sibling catalog/curator/taxonomy skill links | confirm optional handoff or add local fallback |
| `repository-delivery-assessor` | sibling CI Guard link | confirm optional handoff or add local fallback |

A link's existence does **not** by itself mean a runtime dependency or a failed skill. The remaining eight need package-specific semantic inspection and, where material, a standalone remediation with version/fingerprint refresh. No other 21 entrypoints had outbound Markdown links in this bounded inspection; that is not a full package closure qualification.

## Preservation and next acceptance

CI Guard v1.2 stays at the established static rubric **18/20**, with `verification_status=verified` and `validation_status=not-run`. New exact blob and tree fingerprints are reconciled in the authored index, provenance and verification companions and local verification record. Historic v1.1 and its pinned GG-CORE field trial remain traceable and are **not** transferred as v1.2 behavioral evidence.

For future skill releases, verify the standalone folder closure before export and run a no-network, no-sibling-skill low-context scenario where behavioral evidence is needed. Do not create a universal mandatory test runner or inflate quality scores based on text changes.
