# Static source and conformance-oracle reconciliation

## Why this stage exists

A normalized CI Guard simulator takes caller-provided workflow, job and
conformance policy declarations. Even a perfectly successful graph
simulation can represent **stale or wrong source**. Before recommending
expensive CI redesign, compare those declarations to the actual
workflow files and the source-level checker expectations that police them.

The optional [source reconciliation tool](../scripts/ci_source_reconcile.py)
is a **read-only, Python standard-library-only textual binding** to
the existing normalized v3 simulator schema. It does **not** implement
a second CI policy engine, run repository programs, parse arbitrary YAML
into GitHub semantics, authorize host actions or authenticate provider
workflow receipts.

It is conservative by design: a **pass** means supplied source files,
hashes, literal job and guard declarations, and declared Python test
assertion anchors match within the supported subset. It is **not**
a compiled-checker result, proof of effective conditional semantics, or
permission to change CI.

## Invocation

From the CI Guard package root, using a complete exact-source checkout
of the **consumer repository**:

```sh
python3 scripts/ci_source_reconcile.py \
  --root /path/to/authorized/repository \
  --scenario-input /path/to/ci-scenario-v3-input.json \
  --source-map /path/to/source-map-v1.json \
  --require-pass

python3 -m unittest discover -s examples -p 'test_ci_source_reconcile.py' -v
```

No automatic source-map synthesis or untrusted script execution occurs.
The source-map is a *caller-supplied inventory* and must be independently
bound to a real Git revision. Treat guessed paths/guards as a HOLD, not
as a final inventory. The tool never reads a network location and has
no GitHub token requirement.

## Source-map schema v1

Top-level fields: `schema_version:1`, `source_revision`,
`design_id`, `workflow_files`, `oracle_files`.

Each item in `workflow_files` declares `workflow` (matching a v3
design workflow ID), `path` (direct file under `.github/workflows/`),
a complete lowercase `sha256` of the **exact source bytes**,
`events` (literal GitHub event names), and all `jobs`.
A job entry declares `job` (normalized v3 ID),
`source_job` (literal workflow YAML job key),
`if` (exact single-line condition value or `null`),
`needs` (literal source job IDs in order), and
`runs_on` (literal runner label).

An `oracle_files` item declares Python `path`, source `sha256`,
and `checks`: one normalized job ID plus a `test_*` function name
for **each** normalized job. The checker function must contain an
AST-visible `workflow_text = ...read_text()`-style operation
and `assert "<literal>" in workflow_text` for the literal job header
and, where applicable, its literal `needs` and `if` lines.
The same function must include the workflow file path as a literal.
That detects a stale closed allowlist or missing guard assertion
as **source drift**. This is AST *presence analysis*, not an
interpretation of the test's semantics or proof the function ran.

The tool requires every `.github/workflows/*.yml|*.yaml` file in the
checkout to be listed exactly once and every declared candidate job
to map to exactly one source job and one oracle check. It reconciles
source `needs` to the normalized v3 job graph using the existing
simulator's validation entry point.

## Explicitly supported literal subset

The simple parser accepts:

- root `on: [push, pull_request]`, `on: push` or unfiltered
  `on:` with two-space-indented literal event keys;
- `jobs:` with two-space-indented job names;
- four-space-indented, single-line scalar `if`, `runs-on`,
  and `needs: [a, b]` or `needs: a` declarations;
- ordinary `steps` text as **opaque source**.

It **rejects** filtered triggers, multiline YAML guards,
aliases/anchors in guards, reusable-workflow job `uses`,
dynamic `strategy` matrices, dynamic runner labels, duplicate
job identities, changed or missing source digest, unknown or
unmapped workflow files, and unsupported checker AST shapes.
Those cases require a trusted host YAML/expression interpreter
and actual compiled/shell/Rust conformance tests; they do
not become verified because this subset cannot understand them.

Source job condition strings are compared literally: the tool does
**not** claim they mean `success`, `always`, or another normalized
condition in GitHub's real evaluator. Matrix/shard expansion,
workflow permissions, nested/composite job commands, required
branch contexts, token exceptions, release authority and dispatch
causality are not interpreted by this source scanner.

## Result and mandatory evidence boundary

The output `STATIC_SOURCE_RECONCILED` is an offline textual result,
with each workflow SHA-256, normalized job/source ID and checker
assertion reference. This state always includes:

- `source_git_head_authenticated:false` (the source map *claims*
  a revision; only a trusted checkout and Git object verification
  can bind those bytes to a provider commit);
- `yaml_effective_semantics_verified:false`;
- `compiled_oracle_execution_verified:false`;
- `nested_commands_reconciled:false`;
- `provider_job_dispatch_verified:false`;
- `branch_rules_verified:false`;
- `automatic_cutover_authorized:false`.

The required next steps are to run the real repository's conformance
tests on the exact checked-out revision and reconcile provider
run/attempt jobs using the existing
[host-reconciliation component](host-reconciliation.md), plus
independent branch/release/seeded-failure review.
This source checker never upgrades an apparent pass into
`PROVED_IMPROVEMENT`, measured savings, or release authorization.

## Planted falsifiers

The bundled [27 tests](../examples/test_ci_source_reconcile.py) create
ephemeral, entirely fictional workflow files and Python conformance
checkers. They plant stale literals, old allowlists, missing guards
and dependencies, duplicate/missing jobs, unlisted workflows,
unsupported YAML, symlink/path traversal, a program that would throw
if executed, and invalid source revisions. No consuming source is
included in the public skill package, and no consumer code is run.

Where parser coverage is insufficient, prefer a **specific HOLD**
over modifying or deleting the test checker. Evidence of a passing
static oracle is not evidence that the actual host test suite ran.
