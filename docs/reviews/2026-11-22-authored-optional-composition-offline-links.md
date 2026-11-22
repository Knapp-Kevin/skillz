# Authored corpus review: optional composition without broken standalone links

**Date:** 2026-11-22. **Review scope:** three complete first-party
MIT packages. Reproducible source issue: published SKILL.md and
hand-off references linked to a sibling skill folder outside their own
downloadable package despite advertising independent offline use.
There is no need to download the sibling for a single-skill task.

## Source repairs (exact version)

| Package | Exact changed SKILL blob | Entire new package tree | Files | Outcome |
| --- | --- | --- | ---: | --- |
| File Lifecycle Curator v1.1.1 | `3e35bdf625b617fea62d9758501d5fc61c444dca` | `33a8e598e64478a763e335a2dea9f6eef34a7528` | 7 | Removed linked sibling SKILL, and linked sibling contract in reference |
| Federated Source Catalog v1.1.1 | `8d218771193ccefa162479e1a57fd08e9b4ba60a` | `68978717ac4bdb9766ebeab1616feec2196c8573` | 8 | Removed linked sibling SKILL, and linked sibling intake in reference |
| Metadata Taxonomy Steward v1.0.1 | `4e4f7c0c4595e95c9628d933146cd253afa41fbd` | `dee7107d9886e44e9afca4d985db9a5fb92d5b56` | 4 | Removed two sibling hyperlinks and embedded standalone taxonomy explanation |

The published `SKILL.md` now defines the optional composition boundary in
plain text. Required handoff fields, source version, read authority, viewer
and content coverage remain in each package's own references. No source or
connector access is granted by the explanatory sibling name.

## Actual executable source checks

A read-only JS structural scan was run over every bundled Markdown file
in all three **candidate** package trees using the GitHub connector. It
enumerated relative Markdown link targets, resolved parent segments
against the source file's directory, and compared resolved paths against
the exact indexed package file list.

- File Lifecycle Curator: **10/10** local relative links resolve inside
  its seven-file package.
- Federated Source Catalog: **13/13** local relative links resolve inside
  its eight-file package.
- Metadata Taxonomy Steward: **3/3** local relative links resolve inside
  its four-file package.
- Three complete MIT LICENSE files exist inside their folders; identical
  original MIT text blob `3ef83cc9480c9ac96b0e17d79ba6cf5f5beda1f0`
  (source SHA must be compared to the full blob ID recorded by Git).
- All three SKILL source paths lack `../sibling/` Markdown links, and
  current provenance/verification/index pins match new trees.
- **This is not an executed agent-host task**, a rendered Markdown browser
  review, external URL check, private connector test, or filesystem
  modification of any consumer installation.

## Adversarial and positive-preservation cases

**Curator:** H01 authorized excerpt retains original `catalog_id`,
native object identity, principal/root, version type and access scope.
A private H03/H05 document cannot leak through cards, counts or inferred
relationships. New H13 copies **only curator folder**: local collection
tagging, safe index proposal and in-folder handoff contract remain
usable, no required catalog import, no auto-archive/delete.

**Federation:** H01 produces a bounded current-viewer source map from
approved inputs. H04 shortcut to private target must not be
dereferenced, H12 missing reader yields NOT_RUN, and H13 **only
federated folder** with curator absent returns source map and
non-executed optional handoff without fictitious enrichment, storage
or connector authorization.

**Taxonomy:** roadmap term comparison proposes qualified canonical map;
homonymous `draft` stays separate, aliased categories cannot form
cycles, and private HR-private source must not become discoverable to
another viewer. T13 **only taxonomy folder** with other skills absent
produces source-based crosswalk proposals but no actual retag, migration,
ACL change, scheduled task or provider call.

Each added H13/T13 is a **planted static expected negative case**;
a real consuming agent has NOT been run. Existing positive examples and
source permissions were preserved. No mandatory host, standard,
script, network or additional skill was introduced.

**Disposition:** ADAPT source portability, not a false `NO_CHANGE`.
Source package publication is completed only once the PR is merged
and its pinned source reverified on `main`; behavioral qualification
and real consumer task outcomes remain NOT_RUN.
