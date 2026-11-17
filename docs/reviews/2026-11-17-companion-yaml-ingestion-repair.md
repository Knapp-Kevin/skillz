# Governed companion ingestion repair

Baseline: `660da7ca95503a3756179cc3a725d4b667e110b3`. Checked November 17, 2026.

All **1,042 provenance and 1,042 verification companions** pass safe parsing and duplicate-key rejection. The baseline had **139 syntax failures**: 81 notes, 55 rationales, one dependency scalar, one relationship scalar and one dependency-list item. Each repair quotes exactly one original scalar, preserving its full text. No skill source, pin, fingerprint, score, disposition, license grant or behavioral state was revised.

Six additional Archie Indian provenance records contained repeated `license_terms_status` keys. The effective later value, `incomplete-pinned-license-issue-544`, remains; the earlier `incomplete-upstream-license` value is retained as a superseded comment. This removes ambiguous ingestion without resolving upstream issue #544.

[Machine-readable receipt](../../registry/maintenance/companion-yaml-ingestion-repair-20261117.json) records all 145 changed companions and before/after SHA-256 digests.

## Executed checks

- All 139 repaired scalar texts equal their original complete line values. Every other line in those files is unchanged.
- All 1,945 originally parseable records produce identical before/after safe-loaded objects, including the six duplicate-key repairs.
- The offline check passes 2,084 files, requires paired companions and matching declared identities, and rejects duplicate mapping keys. Directory aliases are allowed because paths can intentionally differ from upstream names.
- Nine temporary positive/negative fixtures exercised quoted and unquoted colons, top-level and nested duplicate keys, unsafe YAML tags, valid path aliases, mismatched paired identities, missing companions and an empty corpus. All matched expected results.
- Existing authored capability-link integrity and current capability graphic checks pass: **3 authored packages, 121 mapped identities, 74 linked subdomains**. The SVG is byte-identical because navigation counts did not change.

Maintainer command, explicitly invoked from the repository root:

```bash
python3 scripts/qa/check-registry-yaml.py
```

Requires Python 3 and PyYAML (already installed on the executed host). Reads local companions only; no network, installs, writes or candidate execution. Passing establishes ingestion integrity, not complete schema conformance, content accuracy, package completeness, licensing clearance or behavioral effectiveness.

Metadata ingestion is repaired. Follow the [balanced capability quality plan](../capability-quality-plan.md) for unfinished status normalization, fragmented routing, essential-outcome acceptance and domain qualification.
