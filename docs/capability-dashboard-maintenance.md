# Capability and qualification dashboard maintenance

Skillz uses **generated charts and spreadsheet-ready CSV files**. Do not redraw the SVGs or edit their README tables by hand. Both views are snapshots grounded in dated ledgers. They do not run agent skills or approve installations.

## 1. Capability coverage: what the catalog contains

The existing [capability dashboard](../README.md#capability-dashboard) is generated from `registry/capability-dashboard-sources.json`. That manifest identifies the historical research-link audit, the **current catalog in the checked-out branch**, and the non-additive qualification pipeline. The Q8 proposal selects **44 Valuable References across 33 domains**. The last merged-main baseline was **20 across 10 domains** at commit `e083c47`; do not call Q8 merged until its PR is actually merged.

```sh
node scripts/build-capability-dashboard.mjs --self-test
node scripts/build-capability-dashboard.mjs
node scripts/build-capability-dashboard.mjs --check
```

These commands update or check the generated `README.md` capability block, `docs/assets/capability-dashboard.svg`, `docs/data/capability-dashboard.csv` and `docs/data/qualification-pipeline.csv`. The renderer uses two columns so all 33 domain names remain inside the SVG. The README table and CSV expose the precise numbers when a graphic is harder to read.

## 2. Workstream progress: what is actually finished

The new `registry/curation-workstream-status-20261103.json` captures exact GitHub PR heads and the deliberately separate **merged, draft, discovered, statically reviewed, and approved** populations. It is a **snapshot**, not a live API or merger. The progress chart shows Q8, Q9 and Q10 without summing overlapping counts.

```sh
node scripts/build-workstream-progress.mjs --self-test
node scripts/build-workstream-progress.mjs
node scripts/build-workstream-progress.mjs --check
```

That generator owns only the `SKILLZ_WORKSTREAM_PROGRESS` block in `README.md`, `docs/assets/qualification-workstream-progress.svg`, and `docs/data/qualification-workstream-progress.csv`. The separate dashboard generator owns the `SKILLZ_CAPABILITY_DASHBOARD` block. **Neither generator should overwrite the other's section.** Both use only built-in Node.js 20+ modules: no packages, network calls, or GitHub Actions required.

The progress generator checks its snapshot against the locally present Q7 and Q8 reference catalogs and Q8 qualification pipeline. It also verifies that Q9's **eight pinned leads** reconcile to Q10's **eight source-static reviews and zero original leads still waiting for that stage**, and that all known scanner pass/fail/incomplete records sum to the featured denominator. The ROS 2 Engineering source now has a **completed source-static review and a 118-file identity manifest** drawn from its 204-file repository, but no security, installation, ROS runtime, plugin-hook or real hardware acceptance. Source-static completion must never be displayed as unchanged-use approval. The Q9/Q10 evidence is on **separate draft branches**; its source head SHAs and ledger paths are recorded for inspection. The generator does not pretend it can live-fetch those branches or prove their merge status. If any PR changes, re-read the new pinned evidence and update this manifest **before** regeneration.

## 3. Before publication

1. Verify source identities, exact upstream revisions, license conditions, user authority boundaries, and the governing reviewer decision. Update machine ledgers first. **A research lead or a high static grade alone is not an approval.**
2. Update the relevant manifest(s) and regenerate both views when their source numbers change. Keep the historical review receipts and their dates.
3. Run each script with `--self-test` and `--check`. Both must pass against the checked-out branch. Review SVG header spacing, all domain labels, readable legend text, **SVG title/description accessibility text**, CSV headers/row counts, and README links in GitHub preview. Render the **exact committed Git blob** and verify its SHA before treating a local PNG as a visual acceptance record.
4. Make sure the progress view explicitly distinguishes `main` from Q8/Q9/Q10 drafts. Never add the overlapping Q9 discoveries and Q10 reviews. Keep failed/incomplete security results distinct from passes, and **0 behavioral validations / 0 unchanged-use approvals** unless new exact-package evidence justifies changing them.
5. Get independent review. Merge only with the owner's authorization and after resolving conflicts with the active Q8 branch. GitHub reporting `mergeable=true` is not a substitute for these checks.

**Limits:** Historical research links may include rejected candidates; featured references are methods worth studying, not safe packages to install. A successful static security scan does not prove runtime safety. All-corpus unique eligible/approved totals remain **UNKNOWN** unless a separate rigorous reconciliation establishes them.
