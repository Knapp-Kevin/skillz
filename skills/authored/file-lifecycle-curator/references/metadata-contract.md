# Metadata and Index Contract

A **record** corresponds to one source file or one explicitly identified version. A **metadata deck** renders one card per eligible record from these fields. Values not observed must be null or labeled unknown, never guessed. Store approved material only in an approved destination.

## Portable JSON record shape

The following is a descriptive template, not a claim that an index database was created:

```json
{
  "schema_version": "1.0",
  "record_id": "src-a:doc-002:v1",
  "source_id": "src-a",
  "source_locator": "approved-root/docs/meeting-brief.txt",
  "source_revision": null,
  "source_context": null,
  "display_name": "meeting-brief.txt",
  "observed_media_type": "text/plain",
  "detected_media_type": null,
  "size_bytes": null,
  "modified_at": null,
  "captured_at": "2026-11-18",
  "fingerprint": {"algorithm": null, "value": null, "coverage": "not-computed"},
  "extraction": {"status": "partial", "method": "supplied-excerpt", "coverage": "excerpt-only", "warnings": []},
  "primary_category": "work/meetings",
  "subjects": ["planning"],
  "keywords": ["agenda", "milestone"],
  "tag_basis": "inferred-from-supplied-excerpt",
  "tag_confidence": "medium",
  "summary": {"short": "A proposed agenda.", "detailed": null, "status": "excerpt-limited"},
  "evidence_locators": ["section:agenda"],
  "version_family_id": null,
  "duplicate_class": "UNRESOLVED",
  "related_record_ids": [],
  "retention": {"classification": "unknown", "hold": "unassessed", "review_owner": null},
  "access": {"visibility": "unknown", "sensitivity": "not-assessed"},
  "organization": {"proposed_path": null, "action_state": "not-proposed"},
  "archive": {"recommendation": "not-assessed", "destination": null, "action_state": "not-proposed"},
  "limitations": ["file bytes and full contents not observed"]
}
```

## Required rules

- **Federated extension (v1.1):** When records are selected by Federated Source Catalog, populate `source_context` with `catalog_id`, `provider`, `principal_scope`, `approved_root`, `native_resource_id`, `revision_kind`, `observed_at`, `coverage_state`, `viewer_check` and permitted audience. Keep the original `catalog_id` as `record_id` or an explicitly recorded one-to-one alias. This object is **null for standalone files** without federated context. Never represent stale permission checks as active authorization. Preserve current viewer checks and extraction evidence through cards/derived indexes. See [federated-intake.md](federated-intake.md) and [the synthetic intake cases](../examples/federated-intake-cases.md).
- **Identity:** Record IDs must remain stable within the declared source namespace; do not derive cross-user global IDs from a private path. Keep original locator immutable in the plan. Include an authorized source link only when one exists; no invented URL.
- **Fingerprint:** Mark `complete-byte-verified`, `source-provided-unverified`, `partial`, or `not-computed`. A partial checksum, size or filename is not EXACT identity. Hashes do not replace a safe content or version comparison in collision-sensitive operations.
- **Content:** Separate one-line description, detailed summary, quoted source snippet and inference. Record extraction coverage and citation locator; unknown should stay unknown.
- **Tag taxonomy:** Normalized lowercase, Unicode normalization where tools support it, singular/plural and synonym reconciliation; avoid making sensitive tags discoverable to broader audiences. Use a small human-reviewed vocabulary, optional subject subcategories, and an exceptions queue. Do not combine multiple inconsistent taxonomies silently.
- **Evidence:** Observed fields need source IDs; inferred fields need confidence and justification. A title/date in body text is not necessarily file author or creation date. A `modified_at` timestamp is not a retention decision.
- **Security:** Record ACL/visibility only if available and authorized. Metadata/search indexes inherit at least source visibility constraints; expanding access is a separately approved action. Indexing should not leak raw secrets into public titles, cards or logs.
- **Lifecycle:** Treat proposed location, staged operation, executed operation and verified read-back as distinct fields. Update an archive disposition only when an authorized retention policy exists. Preserve tombstone/supersession references only within approved storage and retention rules.

## A metadata deck card

```text
FILE: <record_id> — <display_name>
SOURCE: <observed locator or redacted label> | VERSION: <observed / unknown>
TYPE: <observed / inferred> | COVERAGE: <readable / partial / inaccessible>
CATEGORY: <primary> | KEYWORDS: <controlled tags> | TAG BASIS: <evidence>
ONE-LINE SUMMARY: <source-grounded or unavailable>
DETAIL: <optional, with locator>
RELATED: <verified record IDs + relationship>
DUPLICATE: <EXACT / LIKELY / RELATED / UNRESOLVED + basis>
RETENTION: <policy / unknown / hold> | ARCHIVE: <proposal only or actual receipt>
NEXT ACTION: <optional permissioned proposal>
```

A deck is a readable view of the index, not an irreversible alteration to source files. If the card or index is exported, include the generation scope, observed snapshot, redaction status and data-owner permission.
