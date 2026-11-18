# Provider capability matrix

A connected provider account is not automatically available or authorized for a blanket scan. Produce a row **per independently scoped account, tenant, drive, repository or local root**, not merely one row per vendor. Every capability must be observed through available host actions or marked UNKNOWN.

| Field | What to record |
|---|---|
| source_id | Distinct, scoped, opaque identifier, not a password/token |
| provider and principal | Observed provider, authenticated user/tenant if available, or UNKNOWN |
| root | Approved folder/shared drive/repository/branch/local path and exclusions |
| object kinds | Files, native Docs, issues/PRs, shortcuts, attachments, directories, etc. |
| available operations | List, search, read, metadata, revisions, permissions, change token, write, independently observed or UNKNOWN |
| pagination | Page/cursor state, end-of-list proof, incomplete flags, budgets |
| source identity | Stable ID, path, revision/commit, alias/shortcut semantics |
| privacy | Authorized viewer, sensitive metadata, source disclosure/egress restrictions |
| freshness | Observation time, revision marker, delta support, invalidation |
| coverage | BOUNDED-COMPLETE / PARTIAL / SAMPLED / INACCESSIBLE / NOT-CONNECTED / NOT-RUN |
| exceptions | Denied scope, revoked grant, missing reader, unsupported export, rate limit |

## Provider-specific interpretation

**Google Drive:** A native Google Doc, its exported PDF and a shortcut have
different identities. Shared drives and multiple accounts have distinct scope.
File listing can be paginated or incomplete; a result of zero items in one
page is not proof of exhaustive listing. Permissions and current-user
capabilities vary by item. Connector metadata, revisions and exports are
not always equivalent to a complete native file byte stream. Read the
connected action's actual response, not a presumed SDK shape.

**GitHub:** Repository contents have paths, commits, blobs, trees, symlinks
and submodules; issues, PRs and releases are separate artifact types.
A branch-relative path is mutable, a pinned commit is a snapshot. A Git
blob SHA is not a universal cross-provider digest. Search results do not
guarantee full-tree enumeration, and repository access depends on the
connected app's installation and viewer authority.

**Local storage:** Files can be renamed or replaced at the same path;
symlinks and mounts may escape approved roots. User-supplied path names
do not prove local read access or that metadata is current.

**Other providers:** For OneDrive, Dropbox, Notion, Slack, email, object
storage or document-management providers, determine native object kind,
parent/container, stable identifier, principal scope, change/permission
model, and operation support from the *actual* authorized connector.
Do not hallucinate a plugin, API or complete permission map.

## Coverage rules

- A scope is BOUNDED-COMPLETE only when its actual enumeration terminates,
  all requested pages and segments were covered, and no incomplete/denied
  results remain within that scope.
- A missing count or cursor stays unknown. An intermediate empty page may
  still have continuation. A rejected/expired cursor invalidates the
  apparent completeness of the interrupted pass.
- If one source fails or lacks search, do not silently omit it from a
  cross-source answer. Report its status and limits.
- Sum counts only with a raw-object denominator. Copies, shortcuts,
  aliases and versions should not be described as unique logical documents.
- No provider reference grants permission to call its API or access files.

## Provider references (external documentation, not host capabilities)

- Drive files.list, pagination and incompleteSearch:
  https://developers.google.com/workspace/drive/api/reference/rest/v3/files/list
- Drive shared-drive search:
  https://developers.google.com/workspace/drive/api/guides/enable-shareddrives
- Drive file types and shortcuts:
  https://developers.google.com/workspace/drive/api/guides/about-files
- Drive permission behavior:
  https://developers.google.com/workspace/drive/api/guides/manage-sharing
- GitHub repository content:
  https://docs.github.com/en/rest/repos/contents
- GitHub Git trees:
  https://docs.github.com/en/rest/git/trees
