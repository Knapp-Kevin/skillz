# Evaluation Evidence

This directory contains behavioral evaluation plans and captured evidence for the `skillz` user experience.

## Initial alpha

Start with [`initial-alpha-matrix.md`](initial-alpha-matrix.md).

The initial matrix deliberately contains only five representative scenarios:

1. governed unchanged reuse;
2. refusal of unverified or stale unchanged reuse;
3. custom creation when reuse would distort user fit;
4. returning-user minimal refinement;
5. returning-user `NO CHANGE NEEDED`.

Static tests can verify routing, selection mechanics, schema, and repository contracts. They do **not** count as behavioral proof for these scenarios. Each scenario must eventually contain captured run evidence before alpha lock.

After alpha lock, this directory can grow with broader skill-level and corpus-level evaluations without changing the initial product boundary.
