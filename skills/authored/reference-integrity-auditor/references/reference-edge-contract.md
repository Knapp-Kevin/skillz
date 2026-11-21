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


## Optional offline machine receipt, schema version 1

The standalone Python standard-library method reads **only**
\`--input <authorized local JSON file>\`, not provider content.
See [the pinned public fixture](../examples/skillz-public-links-pinned.json)
for a full valid example and [the 60 executable regressions](../tests/test_audit_graph.py)
for negative cases.

Top-level fields (unexpected keys are rejected):
\`schema_version: 1\`, \`scope_id\`, \`snapshot_revision\`,
\`enumeration: {sources_complete: boolean, visibility_complete: boolean}\`,
\`nodes\` (1–300), \`edges\` (0–1000) and optional
\`changes\` (0–30). IDs are bounded, opaque, non-secret
handles, not file paths, signed URLs, credentials or display titles.

Each \`nodes[]\`: \`id\`, \`visible\` and \`revision\`.
Each \`edges[]\`: \`id\`, \`source\` (known node ID),
\`target\` (known node ID, unindexed opaque ID or null),
\`kind\` from RELATIVE_MARKDOWN / GITHUB_BRANCH /
GITHUB_COMMIT / HEADING_ANCHOR / CITATION /
DRIVE_SHORTCUT / METADATA_EDGE, \`evidence_ref\`
and \`lookup\`:

- \`state\`: FOUND, ABSENT, DENIED, NOT_RUN, UNKNOWN,
  REDIRECT or HTTP_404. **HTTP_404 never by itself confirms absence**.
- \`authorized\`, \`complete\`, \`absence_proven\`,
  \`redirect_verified\` and \`anchor_renderer_verified\`:
  explicit booleans, representing host-collected attestations.
  \`absence_proven\` is meaningful only with ABSENT; likewise
  \`redirect_verified\` only with REDIRECT.
- \`source_current\` and \`target_current\`: true, false or null
  (not assessed). An ABSENT target uses
  \`target_current: null\`; absence requires valid source-revision
  binding, authorized complete lookup and an affirmative provider
  absence receipt at that revision.
- \`anchor\`: VALID, MISSING, NOT_CHECKED or NOT_APPLICABLE.
  A heading's purportedly valid/missing anchor must be
  checked against the actual renderer or it remains UNRESOLVED.

Each \`changes[]\`: \`id\`, \`node\` (known approved node ID),
\`operation\`: MOVE / RENAME / DELETE_PROPOSAL. This is a **proposal**,
not a command. Changes only produce bounded reverse-graph impact
and a list of possible unresolved direct dependents.

The script does not authenticate these host assertions, compare
real repositories, follow symlinks, crawl, evaluate provider ACLs
or change anything. It withholds **all** source/target/edge identifiers
for edges involving non-visible nodes. If a user cannot see a
target, its existence and location must not leak through a
suggested repair, a summary count or an orphan list.
A target absent from the provided graph is **UNRESOLVED** even
if the input claims FOUND; do not silently repair the identity.

Output \`VERIFIED_CURRENT\` is only consistency with the supplied
bound receipt, **not** a claim that the script directly inspected
GitHub/Drive. Orphan candidates are scope-local and appear only
when the authorized inventory and its visibility are both complete;
they are never evidence of global deletion safety. Any further
write, CI action, network probe or sharing change requires an
independent, specific owner-authorized workflow.
