# Reference-edge and verification contract

A relationship audit is not an exhaustive graph unless the specified
source/target scope was actually enumerated with completeness evidence.

## Logical edge fields

```json
{
  "edge_id": "session-a:edge-001",
  "source": {
    "source_id": "github-a",
    "native_resource_id": "docs/plan.md",
    "revision_kind": "git-commit",
    "revision_value": "example-commit-abc",
    "evidence_locator": "line:12"
  },
  "reference": {
    "kind": "relative-markdown",
    "raw_locator": "../notes/old-plan.md",
    "anchor": "scope",
    "followed": false
  },
  "target": {
    "source_id": "github-a",
    "native_resource_id": null,
    "revision_kind": "unknown",
    "revision_value": null,
    "access_state": "not-checked"
  },
  "coverage": {
    "source_enumeration": "bounded-partial",
    "target_lookup": "NOT RUN"
  },
  "disposition": {
    "state": "UNRESOLVED",
    "evidence": "source link only",
    "repair": "PROPOSED-NOT-AUTHORIZED"
  }
}
```

## Required status semantics

| Status | When justified |
|---|---|
| `VERIFIED_CURRENT` | Authorized actual target resolution at the declared source revision with anchor/path validation as supported |
| `BROKEN_CONFIRMED` | Complete authorized resolution shows required target or anchor absent at the bound revision; no permission ambiguity |
| `STALE_VERSION` | Verified mutation/branch drift invalidates prior revision-bound source or target |
| `MOVED_OR_REDIRECT` | Provider explicitly reports an alias/move/redirect; target still requires access and resolution |
| `INACCESSIBLE` | Explicit source permission denial; existence or title not disclosed |
| `UNRESOLVED` | Missing connector, unsupported resolver, ambiguous locator, partial enumeration or uncheckable access |
| `ORPHAN_CANDIDATE` | No inbound edges **within enumerated approved scope only**, not proof of globally unreferenced object |
| `BLOCKED` | Unsafe target, unapproved network call, out-of-scope object, untrusted redirect or permission mismatch |

## Resolution contracts

- Relative Markdown links resolve from the observed source file's directory,
  not the repository root. GitHub path semantics at a branch are mutable;
  commit-bound references require exact commit context.
- A heading anchor requires the **actual rendering/slug convention** of
  the target document. Do not invent a universal slug algorithm.
- A Drive shortcut is its own resource; metadata visibility of the shortcut
  does not authorize target access. Different account IDs and exports
  are not interchangeable.
- An HTTP 404/410 may mean absent, filtered or unauthorized depending on
  provider/authentication. Report uncertainty when access is not verified.
- URL redirect hosts, query strings and signed links may be sensitive.
  Strip credentials from reports and don't follow new hosts by default.
- External links are NOT CHECKED without explicit destination/network
  authorization; no private-resource probes based only on embedded URLs.
- A graph edge from an authorized item to a hidden target can itself
  reveal target identity. Filter both endpoints and relationship.
- A missing inbound edge is not evidence of deletion eligibility. Keep
  unknown external dependents and source coverage in the result.

## Bounded repair proposal

Provide `source_revision`, `old_locator`, `proposed_new_locator`,
evidence, impact, collision/ACL concerns, owner approval, rollback
expectations and revalidation requirement. Any proposed link update
must remain PROPOSED until separately executed and independently
verified by authorized tools.
