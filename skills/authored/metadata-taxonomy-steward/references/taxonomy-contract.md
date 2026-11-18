# Metadata taxonomy contract

This reference is a **logical proposal**, not a provider schema or a
working database. Current source permissions must be established before
any record, category, usage count or alias is shared.

## Canonical term fields

| Field | Meaning |
|---|---|
| `taxonomy_version` | Explicit version, not file modified date |
| `term_id` | Namespace-qualified stable ID, not just display label |
| `preferred_label` | Human-readable label and language |
| `definition` | Inclusion/exclusion meaning and example when permitted |
| `parent_term_id` | Hierarchy; must be acyclic |
| `aliases` | Explicit language/source namespace and direction |
| `owner` / `decision_state` | Accountable authority and PROPOSED/ACCEPTED/REJECTED/HOLD |
| `source_crosswalk` | Native source, observed raw term, proposed key, source revision, evidence |
| `sensitivity` | Source permission and disclosure bounds, not a deduced personal trait |
| `revision_receipt` | Before/after semantics, compatibility concerns and rollback limits |

Synthetic example; no provider record has actually been read:

```json
{
  "taxonomy_version": "1.0-proposed",
  "term_id": "work:project-plan",
  "preferred_label": {"en": "Project plan"},
  "definition": "Future-oriented work-plan documentation, not a retrospective",
  "parent_term_id": "work:planning",
  "aliases": [
    {"namespace": "drive-A", "raw_term": "proj plan", "relation": "EXACT_SYNONYM", "state": "proposed"}
  ],
  "owner": "authorized-taxonomy-owner-needed",
  "decision_state": "PROPOSED",
  "source_crosswalk": [
    {"source_id": "drive-A", "native_term": "proj plan", "native_revision": "unknown", "mapping_confidence": "provisional"}
  ],
  "privacy": {"audience": "current-viewer", "cross_viewer_share_approved": false},
  "changes": {"provider_write": "NOT RUN", "index_refresh": "NOT RUN"}
}
```

## Transformation and compatibility

- `EXACT_SYNONYM` can be one-way proposed normalization without
  assuming source write. Ambiguous aliases must be `HOLD`.
- Distinguish `display_label`, `canonical_key`, `native_source_label`
  and `term_id`; changes to display text need not change stable ID.
- Detect two incompatible canonical keys sharing the same alias and
  a single source label mapping to two incompatible definitions.
- Parent/child edges form a DAG; detect cycles and reject as a proposed
  normalized taxonomy.
- Version semantic changes, deprecations and compatibility changes
  separately. Preserve retired IDs and source-native values for audit.
- For multilingual sources, preserve language/locale and original script;
  transliteration or translation cannot be assumed equivalent.
- A materialized translation table/index is a separately approved write.
  Never claim a taxonomy was migrated from a plan alone.

## Failure categories

`NO_SCOPE`, `NOT_READ`, `MISSING_DEFINITION`, `AMBIGUOUS_SYNONYM`,
`ALIAS_CYCLE`, `PARENT_CYCLE`, `SENSITIVE_LABEL`,
`SOURCE_PERMISSION_UNKNOWN`, `CONSUMER_BREAKAGE_RISK`,
`MIGRATION_NOT_AUTHORIZED`, `REVISION_CHANGED`.

Explicitly keep unresolved terms and blocked sources in the output.
