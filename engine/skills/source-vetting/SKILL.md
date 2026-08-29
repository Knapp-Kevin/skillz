---
name: source-vetting
description: >-
  Evaluate whether an external skill source is worth tracking as prior art or
  discovery material by reviewing provenance, licensing, maintenance signals,
  package structure, safety concerns, and differentiated value. Use for curation.
metadata:
  author: frostwulf.zo.computer
  category: Research
  display-name: Source Vetting
  emoji: "🛡️"
  version: 2.0.0
  repo-bound: true
---

# Source Vetting

**Repository-curation procedure only.**

A source-level decision answers whether an upstream repository is useful enough to track. It does **not** verify every skill inside that source and does not grant blanket unchanged-reuse eligibility.

## Procedure

1. Establish source identity:
   - canonical repository or publisher;
   - maintainer/organization;
   - current revision when relevant;
   - root and per-skill licensing model;
   - whether the source is authoritative, official ecosystem material, community-maintained, aggregated, or normative specification material.
2. Inspect enough of the repository structure to understand:
   - what kinds of skills/components it contains;
   - whether skill packages include scripts, references, templates, fixtures, dependencies, or other supporting material;
   - whether provenance and licensing are clear at the package level;
   - whether the corpus is curated, generated, mirrored, aggregated, or mixed.
3. Review maintenance/authenticity signals when they materially affect confidence:
   - meaningful commit/release activity;
   - named maintainers or accountable organization;
   - issue/PR quality where useful;
   - suspicious bulk imports, mirrors, or provenance gaps.
4. Review security/authority characteristics of representative material without executing candidate code merely to vet the source.
5. Compare the source with what `skillz` already tracks. Favor differentiated value over another large pile of generic prompts wearing a new logo.
6. Decide the source role:
   - `tracked-corpus` for useful upstream prior art worth revisiting;
   - `normative-spec` for standards/specification authority;
   - `dynamic-discovery` for broad fast-moving discovery surfaces;
   - `reference-only` when useful context does not justify normal individual intake;
   - `do-not-track` when value, provenance, licensing, or quality is insufficient.
7. If tracking is justified, record canonical source identity, role, licensing context, rationale, and a pinned revision when one has actually been established.
8. Identify only a small number of individual skills/components worth separate semantic review. Do not bulk-promote the corpus.

## Output

```text
Source: <canonical source>
Maintainer/publisher: <identity>
Source class: <official / official-ecosystem / community-vetted / aggregated / normative / other>
License model: <root + per-skill caveats>
Revision: <exact revision if established>
Differentiated value: <what this source adds>
Material risks/ambiguities: <only meaningful findings>
Recommended source role: tracked-corpus | normative-spec | dynamic-discovery | reference-only | do-not-track
Individual follow-up candidates: <small selective list or none>
```

## Negative rules

- Never equate source admission with individual skill verification.
- Never require a local clone, submodule, vendored copy, repository script, CI job, or runtime execution.
- Never discard or penalize a skill package merely because it legitimately contains its own scripts or other supporting components; evaluate those components as part of the package when the individual skill is reviewed.
- Never fabricate stars, dates, licenses, revisions, maintainer identity, or security evidence.
- Never bulk-ingest a repository simply because it is official, popular, large, or easy to enumerate.
- If a signal cannot be established, record the uncertainty instead of inventing confidence.
