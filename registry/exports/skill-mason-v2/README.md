# Skill Mason catalog handoff v2

**Exact source snapshot:** [`000de43c3a5e245d58aa9aa015c661d3288828a2`](https://github.com/Knapp-Kevin/skillz/tree/000de43c3a5e245d58aa9aa015c661d3288828a2)
(Git tree `74a57111957f4275e91860125d64080b74bf4c78`).

**Immutable predecessor:** [v1](../skill-mason-v1/README.md). Neither its manifest, governed records nor discovery artifact changed. This is a **passive metadata snapshot**, not permission to install, use, copy, combine or execute source packages.

## Inventory and verification

- Indexed governed records: **1047**, including any original retired semantic statuses.
- Additional historical-only retired companion pairs: **22**, represented in `manifest.json` and original source-file inventory, not selectable or silently lost.
- Tracked source file inventory: **3070**. Source Git submodule pins are recorded without materializing or executing contents.
- V1 comparison: **26 added**, **22 removed from governed index but historically retained**, **36 changed**, **985 byte-equivalent records**.
- Original `anthropic-skills/frontend-design` exact `SKILL.md` blob: `a5333457c414d20d625f307df945842c0952ecc3`; complete package Git tree: `d79e2a5bb4df4a386c2adcdd9ab8709bba28c3f6`.
- Producer source: `scripts/build-skill-mason-catalog.py` at the pinned snapshot. A standalone, offline Python/PyYAML producer, not a consumer activation instruction.

## Files

- [`manifest.json`](manifest.json): source commit/tree, per-source-file and generated artifact SHA-256 inventories.
- [`governed.ndjson`](governed.ndjson): all **1047** governed review identities. Preserve rejected, retired, unmapped and unknown evidence.
- [`discovery-manifests.json`](discovery-manifests.json): raw-discovery shard references and source-evidence pointers.
- [`delta-v1-v2.json`](delta-v1-v2.json): exact added/removed/changed/unchanged record identities, individual changed-record before/after SHA-256, changed top-level fields, and v1/v2 artifact receipts.

## Consumer boundary

Validate the `manifest.json` SHA-256 and byte lengths against its artifact entries, match every source-file hash against the pinned commit/tree, then import every line of `governed.ndjson`. Independently trust the source commit and manifest digest. The manifest does not authenticate itself. No exported record has composition admission, target-host permission, expanded source-license clearance, or observed behavioral acceptance merely because it is present. The upstream pinned original and the consumer's independent source/rights/host gates remain required. A downstream Skill Mason snapshot-pin update requires a **separate, reviewed accession**.

Full review history, limitations and old consumer procedure remain in [the original v1 guide](../skill-mason-v1/README.md). No third-party source packages are vendored into this handoff.
