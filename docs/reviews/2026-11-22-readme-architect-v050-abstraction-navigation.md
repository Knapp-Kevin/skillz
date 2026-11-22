# README Architect v0.5.0: abstraction-first portfolio navigation

Date: 2026-11-22. First-party standalone skill package. No consumer
README edits, external source experiments, deployed preview, or CI runs
are implied by this source review.

## Problem and generalizable answer

A flat repository inventory can tell a newcomer what projects are called
without conveying how they fit a conceptual stack or where to start.
Version 0.5.0 adds a **conditional** abstraction-first lens, especially
for multi-project ecosystem and organization-profile READMEs:

1. Inventory the authorized canonical project set and previous README.
2. Explain layers from human-facing experiences through coordination
   and shared capabilities toward foundations, but only where evidenced
   as useful for actual reader discovery.
3. Keep **conceptual abstraction** distinct from tested integration,
   declared build/runtime prerequisites and planned relationships.
4. Preserve unrelated and uncertain-role work rather than inventing
   a dependency tree; offer independent audience entry paths.
5. Reconcile unique project coverage, local anchors, link identity,
   source claims, rendered presentation and novice/maintainer tasks.
   Flat/outcome-first grouping may be better if a hierarchy is artificial.

All implementation guidance, examples and tests are inside the skill
package. No external consumer identities or borrowed organization
structure are needed to use it offline.

## Actual work added

- Complete normative decision and preservation method in `SKILL.md`.
- In-package portable technical criteria in
  `references/readme-quality-contract.md`.
- Nine-project, fully fictional, `example.invalid` portfolio mapping
  in `examples/abstraction-portfolio-example.md`.
- Adversarial cases for misleading project names, unsupported arrows,
  unowned destinations, missing/cross-cutting projects and inaccessible
  image-only maps.
- Seven new Python unittest methods in
  `tests/test_abstraction_portfolio.py` for bounded local links,
  complete nine-entry inventory, ordered headings and negative controls.
- Existing historical evaluation/docs references identifying unrelated
  consumer repositories redacted. Source observations are explicitly
  **no longer independently reproducible from public redacted records**,
  not falsely relabeled as anonymous executed tests.

## Targeted source review matrix

| Control | Result | Evidence limit |
| --- | --- | --- |
| Unique fictional inventory | SOURCE_PASS | 9/9 entries, no duplicate primary listing |
| Layer order | SOURCE_PASS | Five headings in intended order |
| Local navigation anchors | SOURCE_PASS | Referenced headings match expected slugs |
| Remote identity | SOURCE_PASS | All illustration URLs use reserved invalid domain; no live URL tested |
| Reader journeys | SOURCE_PRESENT | Two task-oriented entry points; no real reader observed |
| Misleading dependencies | SOURCE_PRESENT | Conceptual versus proven dependence explicitly distinguished; semantic accuracy not measured |
| Unrelated projects | SOURCE_PRESENT | Separate independent/unclassified path |
| Existing source preservation | NOT_RUN | No real consumer README rewrite in this source PR |
| New Python suite | NOT_RUN | Seven tests authored, not run on exact v0.5 source |
| Independent agent/host test | NOT_RUN | No external consuming agent available or required |
| Render/visual/readability | NOT_RUN | No actual organization/profile README deployed or rendered |
| Rights/disclosure | SOURCE_REVIEWED | Fictional example and deliberate historical redactions, source history remains public in Git |

## Strict outcome and follow-up

The compiled structural assertions show source layout and consistency,
not successful GitHub Markdown rendering, accessible real-user workflow,
correct cross-project architecture, or live external links. The
regression tests are real Python test code but have no current-version
execution receipt until actually run; older results cannot be imported.

After source merge, user-facing acceptance still requires a real
authorized consumer portfolio, editorial reading task and verified
canonical links when available. This is **not** a prerequisite for
publishing a complete portable skill source, but it remains a
behavioral-validation HOLD under the authored corpus review.

A PR or branch is not delivered work until merged and verified on main.
