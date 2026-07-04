# Vendored-Source Freshness

Six official skill ecosystems are vendored as pinned submodules and indexed into INDEX.md / index.json. Pins go stale silently; this document is the workflow that keeps staleness *visible and chosen* rather than accidental.

## Posture

- **CI validates the pinned state only.** `.github/workflows/ci.yml` checks out submodules recursively and proves the index regenerates cleanly against the *pinned* trees. CI never checks upstream and upstream drift is never a blocking PR check.
- **Drift detection is scheduled/manual**, through `skills-pulse` (weekly) or an ad-hoc run of the check below.
- **Refresh is reviewed, never automatic.** A pin bump lands only after a human has looked at what changed. Vendored official sources are not blanket-trusted for write-tier operations (registry `permission_tier` still governs adoption).

## Refresh workflow

Run when skills-pulse flags upstream activity, or before any adoption decision touching a vendored source.

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

   Classify the delta: **docs-only** (README/prose churn), **skill-content** (SKILL.md bodies added/changed — affects the index and possibly adoption decisions), or **tooling** (scripts/CI — affects trust posture). If the review raises concerns, reset the pin (`git submodule update vendor/<source>`) and record why here.

4. **Re-index**: `node scripts/build-index.ts` — INDEX.md/index.json must reflect the new pin in the same commit.

5. **Registry check**: if the delta is skill-content or tooling, re-read the affected `registry/candidates.yaml` entries — an upstream change can alter adoption rationale or `permission_tier`. Update entries with the review date.

6. **Commit** the pin bump + regenerated index + any registry updates together, with the classification in the message. Update the table below.

## Freshness table

Updated at every check or refresh (initial data: live `git ls-remote`, 2026-07-04).

| Source | Pinned | Upstream (last checked) | Last checked | Last refreshed | Status |
|--------|--------|------------------------|--------------|----------------|--------|
| vendor/knowledge-work-plugins | ca3e3fb | ca3e3fb (2026-07-04) | 2026-07-04 | 2026-07-04 | current — last delta docs-only/metadata (partner-plugin pointer bumps: fastly, carta, wix; marketplace.json only; index diff zero) |
| vendor/anthropic-skills | 9d2f1ae | 9d2f1ae (2026-07-04) | 2026-07-04 | 2026-07-02 (initial vendoring) | current |
| vendor/vercel-agent-skills | f8a72b9 | f8a72b9 (2026-07-04) | 2026-07-04 | 2026-07-02 (initial vendoring) | current |
| vendor/microsoft-skills | 32cad4e | 32cad4e (2026-07-04) | 2026-07-04 | 2026-07-02 (initial vendoring) | current |
| vendor/azure-skills | 8f8c72b | 8f8c72b (2026-07-04) | 2026-07-04 | 2026-07-02 (initial vendoring) | current |
| vendor/aws-agent-toolkit | ff1481a | ff1481a (2026-07-04) | 2026-07-04 | 2026-07-02 (initial vendoring) | current |

## Reporting contract (skills-pulse)

Each skills-pulse run reports, per source: current pinned SHA · latest upstream SHA/release where detectable · refresh-needed verdict · likely classification (docs-only / skill-content / tooling, inferred from upstream commit paths). See `skills/skills-pulse/SKILL.md` §Submodule freshness.
