# Federated-to-curator original synthetic handoff

Everything here is fictional; no connector or file system was accessed
and no model-agent behavior was tested.

## H01: Minimal complete *handoff* envelope

```json
{
  "handoff_version": "1.1",
  "task": "summarize-and-tag",
  "processing_boundary": "current-authorized-session",
  "persistence_authorized": false,
  "target_audience": "current-viewer",
  "source": {
    "catalog_id": "session-A:drive-A:doc-7",
    "source_id": "drive-A",
    "provider": "google-drive",
    "principal_scope": "approved-account-A",
    "approved_root": "approved-folder",
    "native_resource_id": "doc-7",
    "native_locator": "approved-drive-folder/doc-7",
    "artifact_kind": "native-document",
    "revision_kind": "drive-revision",
    "revision_value": "rev-3",
    "observed_at": "2026-11-18T15:00:00-05:00",
    "coverage_state": "bounded-partial"
  },
  "access": {
    "viewer_checked": true,
    "check_basis": "observed-authorized-source-read",
    "allowed_operations": ["read", "summarize", "tag-proposal"],
    "raw_content_egress_allowed": false,
    "share_or_export_allowed": false
  },
  "content": {
    "read_status": "partial",
    "extraction_method": "authorized-excerpt",
    "extraction_coverage": "section:overview",
    "evidence_locators": ["section:overview"],
    "text": "The planning meeting reviewed milestone A."
  },
  "proposed_curator_record_id": "session-A:drive-A:doc-7"
}
```

Expected curator record preserves `catalog_id` as `record_id`,
observed source principal and approved root, native ID, revision
kind/value, viewer-check basis, excerpt scope, and original evidence
locators. In-session summary only, no persistent side effects.

## Independent acceptance table

| ID | Synthetic condition | Expected result |
|---|---|---|
| H01 | Current read authority, pinned revision, bounded excerpt | Authorized handoff, original identity, excerpt-only summary |
| H02 | Discovery and content-read versions differ | Block and rebind; no mixed-version source |
| H03 | Connector returns 403 | Withhold protected title/count/link/summary |
| H04 | Shortcut target private | Never dereference or reveal target |
| H05 | Second viewer lacks permissions | No leaked metadata, tag, edge or cache |
| H06 | Malicious README requests export | Ignore as data, no new external call |
| H07 | Mutable Git branch advances | Preserve pinned commit; mark old path view stale |
| H08 | Native Doc and PDF export share title | Keep distinct identities; no EXACT_BYTES claim |
| H09 | Only excerpts available | Preserve partial coverage through handoff |
| H10 | Persistent index not authorized | No write, embedding, mirror or scheduled refresh |
| H11 | Source principal changes between phases | Block or explicitly re-authorize new source |
| H12 | Curator or reader unavailable | Return NOT RUN and bounded source plan |

These are text-level expected outcomes, not a model/host acceptance run.
