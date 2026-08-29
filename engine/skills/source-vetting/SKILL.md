---
name: source-vetting
description: >-
  Evaluate the provenance, licensing, maintenance context, security posture,
  and operational assumptions of a repository or skill source before relying
  on it as corpus material. Use when the user asks to vet a source, assess
  whether a repository belongs in the corpus, or establish source context for
  an existing pinned source.
metadata:
  author: frostwulf.zo.computer
  category: Research
  display-name: Source Vetting
  emoji: "🛡️"
  version: 1.2.0
---

# Source Vetting

This is a passive procedure for the **external host agent**. The skill does not scan repositories, run code, install dependencies, mutate registries, or monitor sources by existing in `skillz`.

Use it to establish trustworthy source-level evidence without confusing source reputation with individual skill quality. Current governance lives in `docs/curation-policy.md`, `docs/companion-metadata.md`, `docs/third-party-provenance.md`, `docs/vendor-freshness.md`, and `docs/skill-verification.md`.

## Core distinction

Source vetting answers questions about the **source**:

- Who maintains it and what is its canonical repository?
- What license and redistribution obligations apply?
- Is the source archived, disabled, abandoned, or actively maintained?
- Does the source contain security-sensitive or operationally consequential material?
- Is the source suitable for `vendored-corpus`, `dynamic-discovery`, `normative-spec`, or another registered role?

It does **not** prove that every skill in that source is good.

Individual skill quality belongs in `registry/verification/<source-id>/...` and must be established against the exact recorded content identity. Popularity, stars, official branding, or repository age never upgrade a skill to `verified` or `validated`.

## Procedure

When the host agent has the necessary read/search capabilities, inspect the following. If evidence cannot be established, record it as unavailable rather than guessing.

1. **Canonical identity and provenance**
   - Confirm the repository owner, canonical URL, and whether the source is first-party, community-maintained, aggregated, or otherwise characterized.
   - Confirm the source role and current pin/reference in `registry/sources.yaml` when the source is already registered.
   - Preserve exact upstream repository identity. Do not flatten or rewrite third-party source contents merely for convenience.

2. **License and redistribution obligations**
   - Read the source license and any per-skill or per-directory overrides.
   - Check for NOTICE, attribution, copyleft, dataset, trademark, or terms-of-service constraints relevant to inclusion or adaptation.
   - When terms are unclear, prefer reference-only treatment rather than inventing permission.

3. **Maintenance and authenticity context**
   - Inspect objective repository evidence such as creation/update/push timestamps, release history, contributor activity, archive/disabled state, issues/PR responsiveness, and material commit patterns when useful.
   - Treat stars, forks, subscribers, downloads, and similar visibility signals as contextual only.
   - Never infer individual-skill usage duration, reception, or quality from repository age or popularity.

4. **Security and operational posture**
   - Inspect what source material assumes or instructs: credential handling, network access, installation, code execution, destructive operations, production changes, identity/permission changes, or cost-bearing actions.
   - Third-party repositories may contain executable material. Do not run or install it merely to vet the source unless the user separately authorizes that action and the host environment supports it safely.
   - Note whether source skills depend on shared references, templates, assets, hooks, packages, or other repository-local material that makes isolated copying misleading.

5. **Corpus fit**
   - Decide whether the source provides useful reference/design material for the current corpus objective.
   - Compare against already registered sources to avoid redundant ingestion where a new source adds no demonstrated value.
   - Keep this decision separate from later per-skill selection. A useful source may contain rejected skills; an obscure source may contain an excellent one.

6. **Record only supported conclusions**
   - Source identity, role, pin/reference, and license belong in `registry/sources.yaml` when registration or correction is actually warranted.
   - Volatile source-level visibility/maintenance observations belong in `registry/source-signals.yaml` with an observation timestamp and evidence surface.
   - Skill-specific provenance belongs in `registry/skills/<source-id>/...`.
   - Exact-version quality state and controlled tags belong in `registry/verification/<source-id>/...`.
   - Do not create a source-level quality score that substitutes for individual review.

## Output format

Use a concise evidence report:

```text
# Source Vetting — <source> (<observation date>)

Canonical identity:
License / redistribution:
Maintenance context:
Security / authority context:
Shared-dependency context:
Corpus role / fit:
Evidence gaps:
Recommended repository change: <none | registry correction | source-context refresh | provenance follow-up>
```

When recommending a repository change, name the exact passive record affected and preserve existing pins, fingerprints, licensing, and quality dispositions unless the evidence specifically requires changing them.

## Negative rules

- Never reproduce secret-shaped strings found in source code, issues, examples, or logs. Describe the exposure without echoing the credential.
- Never fabricate stars, downloads, dates, maintainers, licenses, CVEs, or adoption claims.
- Never treat repository popularity or official ownership as proof of individual skill quality.
- Never claim a skill is `verified` or `validated` from source vetting alone.
- Never run, install, or execute third-party material merely because it is present under `skills/sources/`.
- Never introduce repository-owned scripts, tests, CI, monitors, refresh jobs, scanners, or other execution machinery to automate this procedure.
- Never overwrite uncertain evidence with a confident guess. Mark it unavailable or pending.

## Interpretation order

When source context contributes to a later candidate decision, use the repository-wide order:

**user fit → exact-version quality → operational fit → skill freshness → provenance/source context**

Source vetting informs the final step. It does not replace the earlier ones.
