# Skill Mason catalog handoff v1

**Ready for inventory/catalog ingestion at the declared snapshot.** This is a
passive metadata export, not a package-reuse grant, universal capability coverage,
composition contract, generator or Prism proof.

**The library is much larger than its governed review subset:** G1–G3 contains
**61,326 pinned path observations across 942 repositories**, with **57,715 distinct
package-tree hashes**. The separate four-source frontier contains **4,813 paths**.
The **1,043 paired-companion records are one review population**, not the library
size or all prior candidate-evaluation decisions. These populations overlap;
neither adding them nor calling each tree a unique useful method is justified.

Source snapshot: [`31a8c518dd97b7828adcc728202fa41388a306d7`](https://github.com/Knapp-Kevin/skillz/tree/31a8c518dd97b7828adcc728202fa41388a306d7),
Git tree `e6d5dfeb42bcd7777ddff52605922fead62135ff`.
The snapshot pin is intentionally independent of the later commit publishing
this handoff, avoiding a self-referential commit hash.

| File | Purpose |
|---|---|
| [manifest.json](manifest.json) | Pinned origin, format, counts, generated-file digests, 2,825 source-file hashes and 12 upstream submodule pins |
| [governed.ndjson](governed.ndjson) | All 1,043 governed review records, one JSON object per line, including every unmapped, rejected and retired record |
| [discovery-manifests.json](discovery-manifests.json) | Direct access to G1–G3 shards, four-source path parts and all other discovery/evidence artifacts at the pin |

## What is represented

- **48 first-party + 995 third-party governed review identities**, with path-based
  record IDs kept distinct from declared upstream names/aliases.
- **122 mapped and 921 explicitly unmapped** records. Confirmed capability links
  and lexical hints are separate. An unmapped method remains searchable through
  its source identity, review tags and original evidence.
- Original semantic states: **337 verified, 702 rejected, 3 retired and 1
  verified-with-portability-caveats**. The nonstandard label is preserved; it must
  not be silently treated as verified. Behavioral/security evidence is separate.
- The **61,326 G1–G3 package observations** and **4,813 four-source paths** remain
  in their exact existing shards rather than being copied into a misleading
  combined unique-skill count. The populations overlap.
- **170 discovery artifacts** and every other tracked registry artifact are
  referenced losslessly, including Q-series reviews, rights observations,
  provenance, source registries, security receipts and taxonomy extensions.
- Complete local file inventories and defined SHA-256 package digests for all
  **48 first-party packages**. All 48 entrypoint fingerprints match the recorded
  review identities at this snapshot. Third-party full-package bytes are not
  materialized or implicitly licensed by these metadata files.
- All **seven engine/maintenance entrypoints** are listed separately from the
  user-facing first-party corpus. Their presence does not add seven governed
  user-facing skills or authorize engine instruction execution.

## Consumer procedure

1. Resolve the manifest and its digest through an independently trusted channel.
   Pin the stated upstream commit/tree. A manifest that hashes itself consistently
   is not proof of publisher identity. Verify the commit-to-tree binding against
   the trusted upstream repository; this exporter does not authenticate it.
2. Materialize the declared source snapshot separately from this export when
   necessary. Verify each source file against `source_files`, plus both generated
   artifacts against the manifest's byte counts and SHA-256. Exclude generated
   exports from future source-input inventories to prevent recursive handoffs.
3. Parse **every line** of `governed.ndjson`; verify unique `record_id` values and
   exact equality with the pinned governed companion/name-index populations.
   Never filter to capability-linked or static-verified records during inventory
   import. Preserve rejects, unknowns, historical states and unmapped records.
4. Read G1–G3 `/records` arrays and the four-source `/entries` arrays from the
   manifest-listed source files. Four-source entries retain their original array
   encoding; root manifests document its meaning. Use the complete artifact list
   for other ledger schemas, preserving their raw records and evidence pointers.
   Discovery observations are not governed reviews or generation permissions.
5. Use the original YAML companions whenever a normalized field is insufficient.
   The export preserves pointers to **complete original evidence**, rather than
   discarding nuanced rationales, rights restrictions, dependencies or findings.
   Do not substitute a nearby similarly named revision for the pinned identity.
6. Apply Skill Mason's separate target-specific rights, full-package, freshness,
   dependency, host, authority and essential-outcome gates before any selection,
   copying or composition. Every exported record starts with composition
   eligibility **not assessed** and no composable-method contract. Do not turn a
   static score, local SHA-256 or successful import into an eligibility verdict.

Hashes are byte-integrity evidence. `sha256-of-canonical-file-list-v1` hashes
canonical UTF-8 JSON plus LF of the path-sorted array of `{path, sha256}` objects;
the per-file hashes cover original file bytes. This is **not** SHA-256 of a tarball
or of a Git tree hash. Use the algorithm label when verifying. Legacy Git blob,
Git tree and mixed fingerprint algorithms remain explicitly labeled and must not
be conflated.

`original_review_date` is null when a specific original review date is absent.
Recorded last-verification, characterization and source-check dates remain
separate; the export does not invent an original date from another timestamp.
Additional package-security evidence may live in the pinned security registry.
Upstream HEAD freshness and target-host fit are not inferred.

## Explicit refresh, not automatic activation

An authorized maintainer may run the reviewed exporter from a clean source
snapshot, supplying an independently resolved commit/tree pair:

```bash
python3 /path/to/build-skill-mason-catalog.py \
  --source-root /path/to/clean-source-snapshot \
  --source-commit 31a8c518dd97b7828adcc728202fa41388a306d7 \
  --source-tree e6d5dfeb42bcd7777ddff52605922fead62135ff
```

Add `--check` to compare without writing. The producer needs Python 3, PyYAML and
local Git; these are maintenance dependencies, not normal Skillz consumer
prerequisites. It reads pinned source files without following skill instructions,
has no network/model calls, and writes only the three named handoff artifacts.
It adds no scheduler, CI or candidate execution to Skillz.

## Remaining qualification work

The handoff eliminates inventory omission at this snapshot. It does **not**
finish the 921 evidence-grounded capability mappings, essential-workflow
decomposition, third-party package/asset rights decisions, composable building
block definitions, or observed generated-skill behavior. The recognized and
proposed taxonomy surfaces remain separately available through `manifest.taxonomy`.
Skill Mason can begin its catalog adapter against this input now and should
refuse generation when its separate evidence requirements are unmet.

Skill Mason's active implementation and Prism integration remain in its own
repository. This handoff does not assert downstream implementation or approval.
