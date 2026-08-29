# Make Your AI Better at Helping You

You do not need to understand skills, write code, or browse hundreds of files.

**Give your AI the GitHub link to this repository. That is enough to start.**

A local clone, shell, Git executable, Node/Bun runtime, initialized submodules, or GitHub Actions are **not required for normal bootstrap or refinement**. If the current host can read this repository through a connector, API, browser, or equivalent tool, use the connector-native path in [`AGENT_START_HERE.md`](AGENT_START_HERE.md) and continue.

Local execution is useful for repository-maintainer duties such as deterministic catalog generation and alpha preflight. It is not a prerequisite for helping a user.

There are two normal ways to arrive here.

## First visit: build a fitted skill set

If the user supplied this repository or its URL without a different task and does not already have a fitted skill set to review, **start first-visit bootstrap now**. Do not stop after describing the repository.

Your job is to build the smallest skill system that best fits this user.

Read [`AGENT_START_HERE.md`](AGENT_START_HERE.md), [`engine/skills/skill-bootstrap/SKILL.md`](engine/skills/skill-bootstrap/SKILL.md), and [`AGENTS.md`](AGENTS.md).

Start with relevant evidence the host already exposes: interaction history, persistent memory, the current conversation, recurring corrections, workspace/project instructions, repeated tool combinations, existing skills, and definitions of "done." Do not make the user repeat accessible information. Do not invent inaccessible history or sweep unrelated private connectors.

Then:

1. Identify durable working methods and latent skills.
2. Compare those needs against the complete governed search surface: local/imported skills, approved indexed vendor skills, and individually characterized tracked external skills whose exact source records are available.
3. For third-party candidates, inspect provenance, controlled tags, authority, portability, freshness, fingerprint, and verification status.
4. Prefer unchanged reuse only when the exact characterized version is `verified` or `validated`, its fingerprint matches, and it genuinely fits.
5. Treat `unverified` and legacy `trusted-baseline` records as design evidence until a current individual structured review is completed.
6. Adapt, supplement, or compose when that produces a better fit.
7. Create a new custom skill whenever the user's real workflow is not adequately represented.
8. Evaluate and adversarially review the fitted system.
9. Install it when the host supports installation and authority exists. Otherwise package it or provide the shortest correct portable handoff.

## Returning visit: review, refine, and improve

If the user already has skills from `skillz`, a prior bootstrap, or another compatible source and asks to review, update, refine, improve, audit, or revisit them, **do not restart from zero**.

Treat the current set as evidence about the user's working system.

1. Inventory the current skills, their intended jobs, installation state, and available fingerprints or versions.
2. Compare the current set with relevant recurring behavior and the user's present definitions of done.
3. Detect stale, overlapping, conflicting, unused, underperforming, over-broad, or missing capabilities.
4. Check whether any referenced upstream skill changed since the recorded fingerprint or freshness check.
5. Search the current governed surface for materially better fits or useful new patterns, including exact-version tracked external records when indexed material is inadequate.
6. Preserve custom behavior that still fits instead of resetting it to a generic upstream version.
7. Refine, replace, supplement, compose, or retire only where evidence supports change.
8. Re-run appropriate structured verification and behavioral evaluation for materially changed behavior.
9. Update installation state and the portable skill profile when applicable.
10. Return the smallest improved set plus a concise change log explaining what changed and why.

A returning review should be capable of concluding **no change needed**. More skills are not inherently better.

## Governed candidate shortlisting

Use the strongest lookup path the host supports.

### Local execution path

When you have local execution access to a fully materialized copy of this repository:

1. Regenerate the catalog with `node scripts/build-index.ts` when `index.json` is stale or older than schema version 2.
2. Translate the user's needs into controlled tags from [`registry/taxonomy.yaml`](registry/taxonomy.yaml).
3. Run [`engine/skills/skill-bootstrap/scripts/select-candidates.ts`](engine/skills/skill-bootstrap/scripts/select-candidates.ts) with relevant tag filters.
4. By default the selector returns indexed exact-version candidates eligible for trusted unchanged consideration under the current verification policy.
5. Use `--include-unverified` only when you intentionally want unverified material as **design evidence**.
6. Never bypass `stale`, `rejected`, or `retired` exclusions merely to produce a result.
7. For tracked external sources that are intentionally not part of the generated vendor index, inspect their exact provenance and verification companions through `registry/skills/` and `registry/verification/` instead of assuming the generated selector is exhaustive.
8. Treat every shortlist as evidence. Final user fit still determines `ADOPT`, `ADAPT`, `SUPPLEMENT`, `COMPOSE`, `CREATE`, or `DO NOT CREATE`.

### Connector/API/web path

When local execution is unavailable, **do not stop**.

1. Use [`CURATED.md`](CURATED.md), local category pages, `registry/verification/`, and registered tracked-source companions to locate relevant characterized candidates.
2. Read the verification companion for status, tags, source snapshot revision, and expected canonical content blob SHA.
3. Read the provenance companion in `registry/skills/` to resolve the upstream repository and canonical source path.
4. Fetch that upstream `SKILL.md` at the exact recorded snapshot revision through the connector/API/browser when possible.
5. If the host exposes a Git blob/content SHA, compare it to `content_blob_sha` before calling the exact version fingerprint-matched.
6. If exact identity cannot be established, lower confidence. Use the material as design evidence, adapt/create conservatively, or choose another candidate. Do not invent a match.

A stale generated index is a maintainer concern, not a reason to abandon a user bootstrap when the relevant live records can be inspected directly.

## Browse by purpose

Humans can browse the locally maintained portion of the library through [`skills/categories/`](skills/categories/), including planning, writing, research, software/repository work, agent operations/security, monitoring/intelligence, and business/career categories.

The complete indexed library also includes approved third-party sources under [`vendor/`](vendor/). Individually characterized tracked external sources remain outside that generated vendor index but are available to governed selection through their exact-version registry companions.

## What counts as the library?

The indexed library includes:

- user-facing skills under [`skills/`](skills/), and
- approved indexed user-facing skills from pinned sources under [`vendor/`](vendor/).

In addition, `registry/sources.yaml` may register **tracked external corpora** that are intentionally not vendored wholesale. An individual tracked external skill becomes a governed selection candidate only after it has provenance under `registry/skills/`, an exact fingerprint-bound companion under `registry/verification/`, and a decisive current quality state. Tracked source admission by itself does not add every upstream skill to trusted library inventory.

Repository machinery under [`engine/skills/`](engine/skills/) is excluded from the library count.

A third-party skill can be available as reference without being verified. Availability answers "can we find/use this as reference?" Verification answers "has this exact version earned trusted unchanged selection?"

## How skill quality works

Every characterized third-party skill receives an exact-version quality state under the repository's quality policy.

- `verified`: passed the current individual structured skillz quality/effectiveness rubric and is eligible for unchanged selection when fingerprint and user fit match.
- `validated`: also has representative behavioral evidence and is the strongest quality state.
- `unverified`: useful as design evidence, but not silently trusted for unchanged installation.
- `trusted-baseline`: legacy characterization retained for historical/schema compatibility; **not eligible for current unchanged selection** until replaced by an individual structured review.
- `stale`: the underlying skill/evidence changed and must be reviewed again.
- `rejected` / `retired`: excluded from normal selection.

Individually characterized skills have a companion under [`registry/verification/`](registry/verification/) bound to the exact canonical `SKILL.md` Git blob SHA.

Tags from [`registry/taxonomy.yaml`](registry/taxonomy.yaml) characterize use case, lifecycle phase, workflow characteristics, authority, and portability. Use those dimensions to refine matching rather than selecting by name alone.

## Compare before creating. Fit the user before reusing.

Existing skills are valuable reference evidence, not a cage.

A good result may use an existing skill unchanged, adapt one, supplement one, compose several, create something entirely new, use a smaller checklist/helper, retire something that no longer helps, or decide that no durable skill change is warranted.

The goal is not maximum reuse or maximum skill count. The goal is the **smallest dependable skill set that matches the user's actual workflow now**.

## Installation is part of the result

A bootstrap or returning refinement pass is not complete merely because Markdown exists.

Finish with an explicit host-level state such as `INSTALLED + VERIFIED`, `READY TO UPLOAD`, `USER ACTION REQUIRED`, or a clearly explained compatibility blocker. See [`docs/installation-handoff.md`](docs/installation-handoff.md).

A host that cannot write files may still produce a complete portable artifact or exact handoff. Do not convert "cannot install here" into "cannot use skillz here."

## What the human should receive

For a first visit:

1. The durable working patterns inferred from legitimate evidence.
2. The fitted skill set and why each skill exists.
3. Which pieces were reused, adapted, composed, or newly created.
4. The quality/evidence state of selected third-party skills.
5. Evaluation results and remaining uncertainty.
6. A portable skill profile when useful.
7. A concrete installation or handoff result.

For a returning visit, also include:

1. what changed since the prior set;
2. which skills stayed unchanged and why;
3. which skills were refined, replaced, added, or retired and why;
4. any stale fingerprints, upstream drift, or evidence that requires follow-up;
5. the updated installation/evaluation state.

The human should always be able to tell what is done, what is trusted, what is merely promising, what changed, what still needs proof, and what action remains.