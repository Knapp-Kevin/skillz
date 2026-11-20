# Federated record and relationship contract

A federated catalog is a logical **overlay** across authorized resource
systems, not a replacement for them. The JSON below is a synthetic
illustration, not evidence of actual access or persistent index storage.

```json
{
  "schema_version": "1.0",
  "catalog_id": "session-a:drive-a:doc-001",
  "source_id": "drive-a",
  "provider": "google-drive",
  "principal_scope": "approved-account-alias",
  "approved_root": "folder-alias",
  "native_resource_id": "example-doc-001",
  "native_kind": "document",
  "native_locator": "provider-supplied-or-redacted",
  "display_name": "Illustrative launch plan",
  "revision": {"kind": "unknown", "value": null},
  "observed_at": "2026-11-18T15:00:00-05:00",
  "coverage": {"state": "partial", "cursor_state": "unknown", "scope": "approved-folder"},
  "content": {"status": "not-read", "extraction_coverage": null},
  "permissions": {"viewer_checked": false, "current_state": "unknown", "safe_to_share": false},
  "metadata": {"category": "planning", "keywords": ["milestones"], "basis": "title-only", "confidence": "low"},
  "summary": {"state": "not-run", "text": null, "citations": []},
  "relationships": [{"target_catalog_id": "session-a:github-a:doc-007", "type": "REFERENCE", "basis": "source mentions target", "confidence": "unconfirmed"}],
  "freshness": {"state": "observation-only", "verified_at": null},
  "curator_handoff": {"state": "not-run", "contract_version": "1.1"},
  "actions": {"persist": "not-authorized", "copy": "not-authorized", "sync": "not-authorized"}
}
```

## Invariants

1. Namespace generated catalog IDs by source and audience/scope. Do not
   include secrets, credentials, raw OAuth grants or signed URLs.
2. Keep native resource ID separate from a title/path/URL, and keep
   revision identity separate from both. An object can move, rename
   or change content; two objects may share a name.
3. Distinguish immutable Git commit/blob/tree observations, branch
   pointers, Drive revisions/ETags, local hashes and file exports.
   A provider revision field/ETag is not automatically a byte digest.
4. Track authorized viewer and current permission checks. One user's
   past visibility cannot authorize another user's query.
5. Treat inferred tags, summaries and relationship confidence as
   derived attributes with evidence, not provider-native facts.
6. Relationship types are `ALIAS_OF`, `SHORTCUT_TO`, `REFERENCE`,
   `EXPORT_OF`, `VERSION_OF`, `COPIED_FROM`, `EXACT_BYTES`,
   `LIKELY_SAME_CONTENT`, `TOPIC_RELATED`, `UNKNOWN`.
7. `EXACT_BYTES` requires equal complete, comparable bytes or trusted
   same-algorithm complete-file digest evidence for specific revisions.
   Equal titles, semantic similarity and partial checksums are insufficient.
   Retain both source objects even when identical.
8. An edge to a confidential item can reveal its existence. Filter
   each endpoint and edge by the viewer's authorization before output.
9. A generated card, snippet, export or cached index does not
   automatically inherit provider ACL. Shared durable catalogs
   require actual proven per-user access enforcement.
10. Missing data stays UNKNOWN/null. Keep observation timestamp,
    extraction coverage, access-check evidence and source errors
    attached to every result.

## Curator handoff contract (v1.1)

A catalog record may be passed downstream only with an explicit scoped [outbound handoff](curator-handoff.md) containing `catalog_id`, `native_resource_id`, a source revision kind/value, principal/root, actual viewer permission basis, extraction coverage and the intended output audience. The curator may map `catalog_id` to `record_id`, and the source native locator to `source_locator`, but must preserve a separate `source_context` for identity, permission and revision type. Incomplete, revoked or mismatched access results in BLOCKED/NOT-RUN, not an inferred summary. See [synthetic handoff cases](../examples/federated-handoff-cases.md). A `curator_handoff.state` of `not-run` in this example is not evidence an agent host was exercised.

## Search result contract

Every permitted result should carry source-provided link/locator when
available, provider and approved source, artifact kind, native ID/revision
when safe, query/match evidence, observation time, entitlement check
and per-source coverage. If access cannot be checked, withhold
confidential cached content and disclose the access verification gap.
Include NOT-SEARCHED sources instead of presenting them as empty.
