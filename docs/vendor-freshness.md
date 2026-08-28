# Vendored-Source Freshness

Seven skill reference ecosystems are currently vendored as pinned submodules and indexed into INDEX.md / index.json: six official sources and one community-vetted source. Pins go stale silently; this document keeps staleness visible and chosen rather than accidental.

## Posture

- **CI validates the pinned state only.** `.github/workflows/ci.yml` checks out submodules recursively and proves the index regenerates cleanly against the pinned trees. CI never treats upstream drift as a blocking PR check.
- **Drift detection is scheduled/manual**, through `skills-pulse` or an ad-hoc check.
- **Refresh is reviewed, never automatic.** A pin bump lands only after a human has looked at what changed.
- **Source class remains visible.** Official sources are authoritative references for their own platforms but are not blanket-trusted for write-tier operations. Community-vetted sources are included for comparative/supplemental value and never gain platform authority by being vendored.
- **Provenance survives refresh.** License or attribution changes are review-significant. See `docs/third-party-provenance.md` and `registry/sources.yaml`.

## Refresh workflow

Run when skills-pulse flags upstream activity, or before any adoption/adaptation decision touching a vendored source.

1. **Check drift** (read-only):

   ```bash
   git submodule foreach --quiet 'echo "$name  pinned=$(git rev-parse --short HEAD)  upstream=$(git ls-remote origin HEAD | cut -c1-9)"'
   ```

2. **Refresh the drifted source** (one at a time, never blanket):

   ```bash
   git submodule update --remote vendor/<source>
   ```

3. **Review upstream changes before anything else**:

   ```bash
   git -C vendor/<source> log --oneline --stat <old-pin>..HEAD
   ```

   Classify the delta as:

   - **docs-only**: README/prose churn
   - **skill-content**: SKILL.md bodies added/changed
   - **tooling**: scripts/CI/runtime behavior
   - **security**: permission, credential, execution, or network posture changed
   - **license/provenance**: licensing, authorship, notices, or redistribution conditions changed

   If the review raises concerns, reset the pin and record why rather than normalizing the change because upstream shipped it.

4. **Re-index**: `node scripts/build-index.ts`. INDEX.md/index.json must reflect the new pin in the same commit.

5. **Registry check**: if the delta is skill-content, tooling, security, or license/provenance, re-read affected `registry/candidates.yaml` entries and the source entry in `registry/sources.yaml`. An upstream change can alter adoption rationale, permission tier, source class, or whether vendoring remains appropriate.

6. **Derived-skill check**: if a local skill records the source as `copied`, `adapted`, or `inspired-by`, determine whether the upstream change invalidates assumptions or merits a re-evaluation. Do not automatically re-copy upstream changes into the local skill.

7. **Commit** the pin bump + regenerated index + any registry/provenance updates together, with the classification in the message. Update the table below.

## Freshness table

Updated at every check or refresh.

| Source | Class | Pinned | Upstream (last checked) | Last checked | Last refreshed | Status |
|--------|-------|--------|-------------------------|--------------|----------------|--------|
| vendor/knowledge-work-plugins | official | ca3e3fb | ca3e3fb (2026-07-04) | 2026-07-04 | 2026-07-04 | current at last check |
| vendor/anthropic-skills | official | 9d2f1ae | 9d2f1ae (2026-07-04) | 2026-07-04 | 2026-07-02 | current at last check |
| vendor/vercel-agent-skills | official | f8a72b9 | f8a72b9 (2026-07-04) | 2026-07-04 | 2026-07-02 | current at last check |
| vendor/microsoft-skills | official | 32cad4e | 32cad4e (2026-07-04) | 2026-07-04 | 2026-07-02 | current at last check |
| vendor/azure-skills | official | 8f8c72b | 8f8c72b (2026-07-04) | 2026-07-04 | 2026-07-02 | current at last check |
| vendor/aws-agent-toolkit | official | ff1481a | ff1481a (2026-07-04) | 2026-07-04 | 2026-07-02 | current at last check |
| vendor/mattpocock-skills | community-vetted | 6654f6b | 6654f6b (2026-08-28) | 2026-08-28 | 2026-08-28 (initial vendoring) | current; MIT provenance recorded |

## Reporting contract (skills-pulse)

Each skills-pulse run reports, per vendored source: source class, current pinned SHA, latest upstream SHA/release where detectable, refresh-needed verdict, and likely delta classification. For community-vetted sources, changes do not inherit trust from prior versions; material behavioral changes may require a new sandbox evaluation.
