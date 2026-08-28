# Evaluation Evidence

This directory contains behavioral evaluation plans and captured evidence for the `skillz` user experience.

## Initial alpha

The initial implementation is proven through five representative first-visit and returning-user scenarios.

Use these files together:

- [`initial-alpha-matrix.md`](initial-alpha-matrix.md) — human-readable purpose and evidence expectations;
- [`fixtures/initial-alpha-scenarios.json`](fixtures/initial-alpha-scenarios.json) — frozen synthetic scenario inputs and prewritten pass/fail criteria;
- [`run-initial-alpha.md`](run-initial-alpha.md) — execution, isolation, scoring, and evidence-recording procedure;
- [`results/`](results/) — captured run evidence only after scenarios are actually executed.

The five scenarios are:

1. governed unchanged reuse;
2. refusal of unverified or stale unchanged reuse;
3. custom creation when reuse would distort user fit;
4. returning-user minimal refinement;
5. returning-user `NO CHANGE NEEDED`.

Static tests can verify routing, selection mechanics, schema, and repository contracts. They do **not** count as behavioral proof for these scenarios. Each scenario must contain captured run evidence before alpha lock.

The fixtures deliberately use synthetic user evidence. Do not replace them with real private user history merely to make the evaluation feel realistic.

After alpha lock, this directory can grow with broader skill-level and corpus-level evaluations without changing the initial product boundary.
