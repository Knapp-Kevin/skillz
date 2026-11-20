# Technology Change Intelligence v1.2.5: GitHub window parity and canonical routing pins

**Date:** 2026-11-20. **Scope:** read-only source-based change for issue #738 and canonical routing consistency for #588 and #402.

## Actual behavior change

The original GitHub Pulse default was 30 days. Consolidated Technology Change Intelligence v1.2.4 used a 14-day profile window. v1.2.5 restores the **30-day default**, without changing the other 16 profile default windows. The entrypoint and bundled execution gate now explicitly require the original 30-day behavior, and bundled negative fixtures cover a candidate created 15–30 days earlier, an explicitly requested shorter interval and missing source coverage. User-selected ranges still take precedence.

## Exact Git source records

- Prior v1.2.4 entrypoint blob: `da2ed091777ed05e7ac94454439c3404c824408d`; full 11-file package tree: `4514fd326d170a49be9f43fcfdcbcd4e2983f8fb`.
- New v1.2.5 entrypoint blob: `7a2a66d3de1147cb83fa42176d501b81b6338770`; full 11-file package tree: `7aa1d44926dc7eeda91ac71f7ddebd3cf34772b7`.
- New 17-profile catalog blob: `b715faa11057435e1a921d9058c2d6ca51e0a5c0`.
- CI Guard v1.2.0 unchanged: entrypoint blob `a98f04ad42fedec08d316605ba7d390c7de3b5f1`, package tree `950bf5db6b9740bdd3fa92721ffb5a8a0fb9c258`. The capability directory had older pins for CI Guard and TCI despite the authored index already being current. Those two entries are updated to the exact reviewed source identities.

## Actual deterministic checks and limitations

- Parsed complete 17-profile catalog; confirmed exactly one `github-discovery` and a 30-day default; deep-compared the other 16 profiles to ensure they are unchanged.
- Confirmed current source explicitly states default, override and `30_DAY_COVERAGE_NOT_CHECKED` behavior, including the first-day edge fixture.
- Audited all 30 authored skill identities against the capability directory; detected exactly the TCI and CI Guard stale source pins and repaired both. Counts, taxonomy and capability links unchanged.
- Static assertions do **not** demonstrate that any agent host used the skill, retrieved a full month of repositories, completed discovery, or met a 1.5× effectiveness target. Source license, authority and security classifications remain unchanged.
- The 17 historical retirement qualifications still record v1.2.4 as their evaluated replacement snapshot; their additional `current_replacement_pin` describes the new v1.2.5 package without retroactive host claims.

**Release implication:** restored default and precise routing metadata may be merged when branch checks pass; independent host and user-outcome qualification remains open under #738.
