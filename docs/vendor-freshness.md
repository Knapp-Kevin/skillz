# Vendored-Source Freshness

`skillz` currently carries **12 pinned third-party source corpora** under `vendor/`. Each gitlink records the exact upstream revision used by the repository. Two additional registered sources are reference/discovery-only and are not vendored corpora.

A pin establishes reproducibility. It does **not** establish that upstream has not moved, nor does source freshness establish individual skill quality.

## Current posture

- **Pins are exact.** `registry/sources.yaml`, `.gitmodules`, and the repository gitlinks identify the source and pinned revision.
- **Automatic GitHub Actions are disabled.** The workflow is manual-dispatch only while Actions budget is protected. Do not describe absent automatic CI as a freshness failure.
- **Upstream drift detection is manual or scheduled outside automatic PR CI.** It may be performed by ecosystem-intake tooling or an explicit review.
- **Refresh is reviewed, never automatic.** A pin bump lands only after relevant upstream changes are inspected.
- **Availability is separate from quality.** Updating a source pin never automatically promotes individual skills to a stronger quality state.
- **Characterization is exact-version bound.** If a characterized skill's canonical `SKILL.md` fingerprint changes, its prior characterization must be treated as stale until refreshed.
- **Provenance survives refresh.** License, authorship, notices, path, and relationship changes are review-significant. See `docs/third-party-provenance.md`, `registry/skills/`, and `THIRD_PARTY_NOTICES.md`.

## Current pinned corpora

Pins below are the gitlinks present in the initial-alpha implementation tree.

| Source path | Pinned revision | Notes |
|---|---|---|
| `vendor/knowledge-work-plugins` | `ca3e3fb2c4a1d3eea73fc003998faef6daa650b8` | pinned corpus |
| `vendor/anthropic-skills` | `9d2f1ae187231d8199c64b5b762e1bdf2244733d` | pinned corpus |
| `vendor/aws-agent-toolkit` | `ff1481a7bc1a04ee00ebf63d3a8a149aa6a2c546` | pinned corpus |
| `vendor/azure-skills` | `8f8c72bb9e22aee4366e07aadfd5766ef9add8f4` | pinned corpus |
| `vendor/vercel-agent-skills` | `f8a72b9603728bb92a217a879b7e62e43ad76c81` | pinned corpus |
| `vendor/microsoft-skills` | `32cad4ee689c95c309e61aeefcbc6af356f1e6a7` | pinned corpus |
| `vendor/mattpocock-skills` | `6654f6b60cd9d5be8b54c6fafe44346dabeb3b76` | pinned corpus; provenance records exist for characterized subset |
| `vendor/addyosmani-agent-skills` | `f63ec56a3cc936408d792956ae583c3c96a825bd` | pinned corpus; provenance records exist for characterized subset |
| `vendor/openhands-extensions` | `87959a7da3e75445647e77b2fbf5bf5b66fb037b` | pinned corpus |
| `vendor/cline-skills` | `26378461e978f2b4e2e6d67b57121b86b2a79ba5` | pinned corpus; characterized/verified subset exists |
| `vendor/cloudflare-skills` | `f96bff754e428838818017f75817f0f9428acd48` | pinned corpus; characterized/verified subset exists |
| `vendor/google-agents-cli` | `ef7808f33fc3038112b69d4ad488ce33b72699b1` | pinned corpus; characterized/verified subset exists |

The authoritative source URLs, source roles, classes, licenses, and inclusion modes live in `registry/sources.yaml`. Do not duplicate those fields here as independent truth.

## Reference/discovery sources

Registered sources that are not physically vendored are tracked in `registry/sources.yaml` with their appropriate source roles. They may inform discovery, specification compliance, or comparison without being silently counted as initialized local submodules.

## Drift-check workflow

Run when source-intake tooling flags meaningful upstream activity, before adopting an unreviewed upstream change, or during an intentional source refresh.

### 1. Check current pin versus upstream

Read-only example:

```bash
git submodule foreach --quiet 'echo "$name pinned=$(git rev-parse HEAD) upstream=$(git ls-remote origin HEAD | cut -f1)"'
```

A difference means **upstream moved**. It does not by itself mean refresh is desirable.

### 2. Review one source at a time

```bash
git submodule update --remote vendor/<source>
git -C vendor/<source> log --oneline --stat <old-pin>..HEAD
```

Classify relevant deltas as:

- documentation only;
- skill content;
- tooling/runtime;
- security/authority;
- license/provenance;
- structural/dependency changes.

If review raises concerns, restore the old pin and record the decision rather than normalizing upstream merely because it is newer.

### 3. Reconcile affected individual records

For every characterized skill whose canonical content changed:

1. compute/check the new canonical fingerprint;
2. mark the old characterization stale until reviewed;
3. refresh controlled tags if behavior/use case/authority/portability changed;
4. rerun structured verification when required by the quality policy;
5. do not retain behavioral-validation claims when the evidence no longer applies to the exact version.

### 4. Reconcile provenance and dependencies

Check:

- source/path changes;
- license or notice changes;
- bundled references/scripts/assets required by the skill;
- derived/imported local skills that may rely on old upstream assumptions.

Do not copy a lone `SKILL.md` while omitting required shared resources.

### 5. Regenerate the catalog

With all intended submodules materialized:

```bash
node scripts/verify-index-idempotency.ts
```

The first pass may refresh stale `INDEX.md` / `index.json`. The second pass must be byte-identical.

### 6. Commit one coherent refresh

Land together when applicable:

- gitlink change;
- source/provenance/notice changes;
- refreshed characterization/verification records;
- regenerated catalog;
- concise classification of what changed and why the refresh was accepted.

## Initial-alpha note

The exact current indexed skill count is intentionally pending the next fully materialized schema-v2 catalog generation. The source pins above are independently visible in the repository tree, but API-side path counts are **not** used as a substitute for the generator's deduplication/exclusion rules.
