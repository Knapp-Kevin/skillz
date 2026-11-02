# Robotics source: 43 pinned entrypoint identity and rights recovery (2026-11-02)

**Purpose:** preserve a bounded, source-pinned subset of held [discovery PR #590](https://github.com/Knapp-Kevin/skillz/pull/590) without merging its stale shared registries or claiming admission, grade or runtime execution.

## Exact provenance

- Source: [graph-robots/open-robot-skills](https://github.com/graph-robots/open-robot-skills), pinned commit `752dfbd96968d4d08379f8111765efbf6457800b`.
- **43/43 pinned SKILL.md entrypoint Git blob SHA identities independently fetched and matched**, zero mismatches, through GitHub source API on 2026-11-02.
- [43-row evidence ledger](../../registry/discovery/robotics-43-entrypoint-reconciliation-20261102.csv) preserves each original path, entrypoint SHA, prior directory tree SHA, and historical supporting-file count (158 supporting blobs observed in archived ledger).
- **Directory/package tree SHAs and the 158 supporting blobs were NOT independently reverified** in this pass. Entrypoint equality alone does not establish complete-package identity or rights. All 43 remain `DISCOVERED_UNGRADED`.
- Source categories: 33 entries under `skills/`, eight under `tools/`, two under `policies/` (the latter are **policy bundles**, not necessarily independent user-facing skills; confirm first-class eligibility before counting).
- Archived source ledger at PR #590 head `f9567bc4f7489621c1597fa5bed58ac9f101a24b` is evidence only, not current-main source admission.

## Rights and execution risks

- Complete pinned root [LICENSE](https://github.com/graph-robots/open-robot-skills/blob/752dfbd96968d4d08379f8111765efbf6457800b/LICENSE) independently fetched: **Apache License 2.0**, Git blob `d645695673349e3947e8e5ae42332d0ac3164cd7`. Retain required copyright, license and NOTICE notices where applicable, preserve changes and comply with patent and trademark boundaries. No root `NOTICE` file found at the pinned revision; this is not evidence that package-local files or external model weights lack separate terms.
- README at exact pin explicitly describes robot manipulation subgraphs, tool bundles and closed-loop VLA policy packages, with executable `scripts/` and external GaP graph execution. **These are upstream package dependencies, not permission to add scripts or a runtime to skillz.**
- Robotics is high-authority: physical motion, grasping, actuation, object handling, model-driven perception and policy execution can affect people, equipment, property and external systems. Any agent adaptation must require explicit action-specific operator authorization, hardware safety boundaries, human supervision, dry-run/simulation and stop/recovery criteria appropriate to the real host. No live robot, simulation, scanner or adversarial behavior was executed.
- Upstream references to GaP, model weights, tools and external datasets require their own rights, privacy, safety and dependency review. No bundled material has been copied into the repository.

## Accounting and follow-up

- The 43 archived paths are **outside** the pinned four-source 4,813 raw-path snapshot and outside the 1,039 existing governed review records. They do not increase either denominator or numerator; distinct eligible identities remain UNKNOWN.
- Next: inspect all 43 full package directories and dependency trees, independently reverify each package tree, resolve the two `policies/` entries' eligible identity status, per-file licensing and hardware authority gates; then perform individual static reviews/grades and clearly mark behavioral validation NOT-RUN unless real external evidence exists.
- This is a passive provenance/rights recovery only. Keep PR #590 open until its other uniquely valuable evidence is reconciled.

