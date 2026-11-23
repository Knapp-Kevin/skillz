# Organization, Archive and Mutation Rules

Read this before presenting a physical reorganization, export, archive or any cleanup proposal. This skill has **no built-in file system executor**; all effects are host-authorized actions.

## Action-state vocabulary

- `PROPOSED`: a plan only; no authority or mutation.
- `APPROVED`: user/owner approved a specific scope and action class; still not executed.
- `EXECUTED`: tool reported performing an operation; not yet integrity-verified.
- `VERIFIED`: a read-back or source/destination inspection supports the expected effect.
- `FAILED`: attempted operation did not satisfy success criteria.
- `BLOCKED`: authority, source, collision, storage, privacy or retention prerequisite unresolved.
- `ROLLED_BACK`: rollback action was performed and its result checked; never infer from a suggested undo.
- `UNKNOWN`: no reliable observation.

Do not collapse these states into "done." A visual folder tree, completion
percentage, planned "after" shape, generated image or chart is not
an additional action state and never proves execution. See the
[three-view visual contract](visual-progress-contract.md).

## Dry-run plan

For every proposed file mutation or archive batch, report the following before seeking approval:

| Field | Required evidence |
|---|---|
| Source | Stable ID, original locator, observed version and verified digest when available |
| Destination | Intended locator, parent root, collision policy, sensitivity/access inheritance |
| Operation | Rename, move, copy, export, index-persist, tag-edit, archive-create, restore, delete or permission-change |
| Rationale | Human task and intended benefit, including non-mutating alternative |
| Safety | Expected link breakage, protected folders, cross-volume behavior, symlinks, hidden and read-only files |
| Preconditions | Ownership/authority, destination writable, sufficient space/cost where observable, same-file drift checks |
| Recovery | Backup or reversible copy, restore test/limitation, conflict handling and partial failure plan |
| Approval | Named scope, approval timestamp/context, operation class and explicit exceptions |
| Result | Per-record attempted status, observed tool receipt, integrity/ACL read-back and follow-up |

`Copy` is not automatically safe: unintended disclosure to the destination is a side effect. A persistent index and embeddings can likewise expose private content.

## Before applying an approved batch

1. Re-read the approved source set; compare stable identities, versions and full-byte hashes when available. Source drift requires a revised proposal. Do not follow unapproved symlinks or cloud shortcuts.
2. Enumerate destination collisions, case-insensitive/path-normalization conflicts, reserved names, maximum path issues, ACL inheritance and link breakage. Unknown behavior blocks risky moves.
3. For each file, prefer reversible **copy + verify** over move when originals or linked references matter. Do not call a copy a backup until recovery is checked.
4. Keep a transaction journal outside the source material only when that storage is approved. Journal both successes and failures. Abort dependent operations after failure; do not retry unboundedly.
5. Read back destination bytes/metadata and compare to the correct source snapshot when supported. No inferred success from a zero-error message alone. Record changed permissions and unexpected metadata loss.
6. Never delete originals solely because move/copy/archive reports success. Destructive disposal requires a separate approved policy decision, verified recovery path where applicable and protected-hold resolution.

## Archive decision table

| Evidence | Recommended disposition |
|---|---|
| Inactive, no retention decision | Propose archive; retain original; ask owner about retention |
| Version superseded but still referenced | Keep version chain and links; archive candidate only |
| Legal hold, unknown regulatory retention or ongoing investigation | HOLD; no deletion, no auto-expiration |
| Restricted file and destination has broader access | BLOCK archive/export until permissions are safe and explicitly approved |
| Recoverable read-back verified but no disposal approval | Archive may be VERIFIED; original remains |
| Archive extraction unreadable or integrity check fails | FAILED; retain original and restore tested state |
| Owner authorizes disposal with retention and backup safeguards | Separate deletion batch, never inferred from general organization approval |

Common archive formats can omit ACLs, timestamps, extended attributes, version history, links or cloud-provider sharing context. Report such losses before authorizing. Do not promise legal records compliance, tamper-proof storage, indefinite preservation or successful restore without observed evidence.

## Retrieval and ongoing freshness

Resolve a search query using available authorized index data, quote the actual file/section locator, show the index capture date, and mark a result stale when the source revision has changed. Metadata similarity is not equivalent to content verification. If permanent indexing, scheduled refresh, notifications or archival checks are requested, those are separate automations subject to explicit ongoing scope and consent.
