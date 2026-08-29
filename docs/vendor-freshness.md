# Pinned Source Freshness

`skillz` includes pinned third-party source corpora under `skills/sources/`.

A pin establishes the exact source revision represented by the repository. It does **not** establish that upstream has not moved, that the newer upstream version is better, or that every skill inside the source is individually trustworthy.

This is a passive review policy. `skillz` does not poll upstream repositories, run freshness checks, update submodules, schedule scans, or execute a refresh workflow. An external agent may inspect upstream state when the user or an authorized curation task calls for it.

## Authoritative source state

Do not duplicate mutable source pins in this document.

The current source identity, role, class, license, inclusion mode, local path, and pinned/reference revision belong in:

- `.gitmodules` for included git submodules;
- `registry/sources.yaml` for governed source metadata;
- `registry/skills/` for skill-specific provenance;
- `registry/verification/` for exact-version individual quality decisions;
- `registry/source-signals.yaml` for timestamped source-level activity/adoption context.

When these disagree, investigate and reconcile the records. Do not choose whichever value looks most convenient.

## Freshness principles

- **Pins are exact-version evidence.** They identify what source revision is currently represented.
- **Newer is not automatically better.** Upstream movement is a reason to inspect, not a command to update.
- **Source freshness is not skill quality.** A newly refreshed official source can still contain rejected or unverified individual skills.
- **Individual quality is version-bound.** When material skill content changes, prior exact-version review no longer proves the changed version.
- **Provenance survives review.** License, authorship, notices, source path, dependencies, and relationship changes remain material facts.
- **Popularity is contextual.** Stars, forks, and activity may inform discovery or source context but do not prove an individual skill is good.
- **No automatic refresh exists.** Every source change incorporated into the corpus should be an intentional external-agent decision.

## External-agent review method

When an external agent has a reason to examine source freshness:

1. Read the current governed source record and represented revision.
2. Inspect the upstream source using capabilities legitimately available in the host.
3. Determine whether upstream materially changed since the represented revision.
4. Classify relevant change as one or more of:
   - documentation;
   - skill content;
   - dependency/shared-resource;
   - tooling supplied by the upstream source;
   - security/authority;
   - license/provenance;
   - structural/path change.
5. Decide whether the current pin should remain, whether the newer revision should be represented, or whether more evidence is needed.
6. If represented skill content changes, identify affected characterized skills and treat prior exact-version quality evidence conservatively.
7. Reconcile source/provenance/verification/source-signal records only where facts changed.
8. Reconcile static navigation snapshots when their paths, counts, or descriptions became stale.
9. Record the reason for accepting, rejecting, or deferring the source change.

If the host cannot establish upstream state, record freshness as unavailable or not checked. Do not invent a comparison.

## One source at a time

Prefer reviewing one source independently rather than updating many sources merely because they all have newer commits.

This keeps evidence attributable and makes it possible to answer:

- what changed;
- which skills were affected;
- whether dependencies or licensing changed;
- why the new revision was accepted or rejected;
- which exact-version quality records need reconsideration.

## Changed individual skills

For every characterized skill whose canonical content materially changed, the external agent should:

1. establish the new exact content identity when possible;
2. inspect the relevant delta and dependencies;
3. update skill-specific provenance/freshness evidence;
4. treat the prior quality conclusion as stale for unchanged reuse until review is complete;
5. apply the structured verification standard to the changed version;
6. revisit behavioral evidence only when previous evidence may no longer apply;
7. preserve rejection or limitation reasons when they remain true.

## Shared resources and dependencies

Do not reason about a `SKILL.md` in isolation when it depends on shared references, templates, assets, hooks, packages, scripts supplied by the upstream project, or host-specific capabilities.

Those dependencies may be important to the skill's usefulness or safety even though `skillz` itself executes none of them.

## Catalog reconciliation

`INDEX.md` and `index.json` are passive navigation snapshots. When source review changes paths, inclusion, counts, names, or quality summaries, an external agent may update those snapshots directly from the evidence available to it.

There is no required generator, idempotency script, materialization preflight, or CI gate.

If an exact corpus count cannot be established from the accessible evidence, use an explicitly approximate or pending count rather than claiming false precision.
