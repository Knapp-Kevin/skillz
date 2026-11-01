# OpenAI Google Drive and Dropbox: eleven exact-source candidate decisions

**Date:** 2026-11-01  |  **Intake issue:** [#586](https://github.com/Knapp-Kevin/skillz/issues/586)  |  **Source:** [openai/plugins](https://github.com/openai/plugins/tree/0722921d5542fc593105c27bd52630babd8b8c2a)  |  **Registered revision:** `0722921d5542fc593105c27bd52630babd8b8c2a`

## Scope, denominator, and provenance

This is **dynamic-discovery source vetting**, not an admitted-source semantic review. Pinned Git trees establish exactly **5** direct, front-mattered `SKILL.md` packages under `plugins/google-drive/skills/` and **6** under `plugins/dropbox/skills/`: **11/11 terminal decisions**. The two source families share file-management use cases but have distinct connector contracts, manifest identities, provenance and authorization patterns. No aliases, symlinks, duplicate exposure paths or independently first-class nested manifests were found in these two inspected skills trees. Ordinary reference Markdown, upstream scripts, host helpers, runtime modules, agent config and images are dependencies, **not** extra skills.

- Google Drive plugin `0.1.15`, manifest declares MIT (see pinned [plugin manifest](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/google-drive/.codex-plugin/plugin.json)). Plugin tree `14ec4043bb90d3ea4effe27dcf215effb87cd8d4`, skills tree `17a1ac3986361a4cf6ce1d1efe133cd8d5340e56`.
- Dropbox plugin `5.0.1`, [manifest](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/dropbox/.codex-plugin/plugin.json) has **no declared license field**, and links Dropbox terms/privacy. Plugin tree `71d222e051fe240afa78a211185c768c87415bd6`, skills tree `0b6dd74c1d79a31c48a3e6e975a522889e9c6158`.
- No controlling LICENSE text was found at repository root, either plugin root, or the inspected first-class package roots at the pinned revision. Google Drive's manifest MIT label alone does not establish a controlling redistribution grant; Dropbox has no skill-level grant established. **NOASSERTION for copying.** No material is vendored or installed.
- Individual last-change dates below come from GitHub's commit history filtered to each exact `SKILL.md` path at the pinned revision. They are **skill-path freshness**, not a claim that every bundled dependency changed on that date.

## Exact candidate register

| Canonical package | Package tree SHA | SKILL.md blob SHA | Last SKILL change | Decision / candidate score |
|---|---|---|---|---|
| `google-drive/google-docs` | `cc80605d8d4a9dd1ba87e7998f8b18224954782e` | `32095d7ebf5fbdc9787b7b50c357c381f4537fe0` | 2026-08-27 | **REJECT unchanged** 13/20 |
| `google-drive/google-drive-comments` | `de6d7d556dd5493d1c3c8642aa47ecc5d89a6f68` | `f4124a337f276bd1b23213f91bdf3994f27f25d7` | 2026-04-07 | **REJECT unchanged** 13/20 |
| `google-drive/google-drive` | `fc0453cb068d6c4fb0601384e4bc56167b558a39` | `418efac481d4bfb9dc770d170a7d499df4522bb5` | 2026-08-26 | **REJECT unchanged** 12/20 |
| `google-drive/google-sheets` | `d8d14972cbdb8b6b433fe6affd8f5b1ec4862fb1` | `5f7f744a9b849c4f0028849b60505e7cf4094da9` | 2026-08-27 | **REJECT unchanged** 14/20 |
| `google-drive/google-slides` | `38c10de3ad2157852a530b4cc8fef2a96823ddc9` | `d576f9907487e092b99689b34603fb1a9b5eab03` | 2026-08-27 | **REJECT unchanged** 11/20 |
| `dropbox/clean-up-dropbox-content` | `7827bb319a79f8b4d22b820a1df6bd5955568410` | `d482f3231116b22890436b8b9d3572563e0ae9b7` | 2026-08-26 | **REFERENCE-ONLY** 16/20 |
| `dropbox/collect-files-with-request` | `c96ccf61c1394b4a738c6ad08eacb2828d71d6a9` | `90cd5f61ded00b45e2b3fb14816ff7e14ebb0071` | 2026-08-26 | **REJECT unchanged** 14/20 |
| `dropbox/find-dropbox-content` | `8ff629d50b35b865212f3ca719e4c6c3e9f5049d` | `3bbe938de1dd20749334bd537bff987fadb00687` | 2026-08-26 | **REFERENCE-ONLY** 17/20 |
| `dropbox/inspect-dropbox-file` | `b1688c81825b4aa3cbd7620bd572a7a2d88a0568` | `912d12d57473dee919e312ad2f8870262848beb1` | 2026-08-26 | **REFERENCE-ONLY** 16/20 |
| `dropbox/organize-dropbox-folder` | `86ceb9ca28d68347c0da3a1af269b2b7821a67e5` | `b43fcffc7c5fe1644d185352089032ac7b2ec204` | 2026-08-26 | **REFERENCE-ONLY** 16/20 |
| `dropbox/share-dropbox-content` | `140482b4ec9d2b2d8f1af02212dc24c76441485d` | `e022bcf0f7174bed40aa8a7742404e595c1728d4` | 2026-08-26 | **REFERENCE-ONLY** 16/20 |

## Individual reviews

### 1. `google-drive/google-docs`

- **Canonical identity:** `plugins/google-drive/skills/google-docs/SKILL.md`; manifest name `google-docs`; package tree `cc80605d8d4a9dd1ba87e7998f8b18224954782e`; SKILL blob `32095d7ebf5fbdc9787b7b50c357c381f4537fe0`. Last SKILL-path change: 2026-08-27 UTC at or before pin.
- **Purpose / trigger and non-trigger:** Create/edit native Docs, preserve tabs, chips, layout and template structure; do not route ordinary file discovery here.
- **Dependencies / portability:** 18 reference Markdown files; 5 host helpers, 5 scripts and 6 runtime modules; Google Docs connector, optional dropdown-specific connector actions and local code-mode host. Portability **medium**; all bundled helpers are upstream source-owned reference material.
- **Authority and privacy finding:** Automatically creates or reuses a `ChatGPT` Drive-root folder; trusted-read bridge persists full private document content to local artifacts; native copying and batch writes lack a separately bounded disclosure, retention and destination approval. Strong revision, target and protected-control checks are correctness guards, not consent.
- **Controlled tags:** `documentation`, `implementation`, `external-side-effect` (use case/characteristic/authority as applicable). Candidate score **13/20**, **REJECT unchanged** for unchanged use; preserve selective adaptation/checklist evidence.
- **Evidence:** Static source inspection only; behavioral validation **not-run**, adversarial execution **not-run**, pinned package-security scan **not-run**, redistribution **not cleared**.

### 2. `google-drive/google-drive-comments`

- **Canonical identity:** `plugins/google-drive/skills/google-drive-comments/SKILL.md`; manifest name `google-drive-comments`; package tree `de6d7d556dd5493d1c3c8642aa47ecc5d89a6f68`; SKILL blob `f4124a337f276bd1b23213f91bdf3994f27f25d7`. Last SKILL-path change: 2026-04-07 UTC at or before pin.
- **Purpose / trigger and non-trigger:** Write, reply or resolve comments on specific Drive files; not for content editing or general discovery.
- **Dependencies / portability:** Google Drive/Docs/Sheets/Slides read tools and bulk_update_file_comments; sibling file-type skills; no bundled scripts. Portability **high**; all bundled helpers are upstream source-owned reference material.
- **Authority and privacy finding:** One bulk call can create replies and resolve threads visible to collaborators. Exact evidence fields and IDs prevent wrong anchors, but no distinct pre-send approval for comment text, target audience, and thread-resolution side effects. Quoted private content may be disclosed in collaborator-visible comments.
- **Controlled tags:** `code-review`, `communication`, `external-side-effect` (use case/characteristic/authority as applicable). Candidate score **13/20**, **REJECT unchanged** for unchanged use; preserve selective adaptation/checklist evidence.
- **Evidence:** Static source inspection only; behavioral validation **not-run**, adversarial execution **not-run**, pinned package-security scan **not-run**, redistribution **not cleared**.

### 3. `google-drive/google-drive`

- **Canonical identity:** `plugins/google-drive/skills/google-drive/SKILL.md`; manifest name `google-drive`; package tree `fc0453cb068d6c4fb0601384e4bc56167b558a39`; SKILL blob `418efac481d4bfb9dc770d170a7d499df4522bb5`. Last SKILL-path change: 2026-08-26 UTC at or before pin.
- **Purpose / trigger and non-trigger:** Router for Drive search, fetch, export, share, move and delete; dispatch Docs/Sheets/Slides edits to sibling skills.
- **Dependencies / portability:** 4 Slides reference files; Drive revision/download/export/move tools; Google Docs, Sheets, Slides and comments sibling skills. Portability **medium**; all bundled helpers are upstream source-owned reference material.
- **Authority and privacy finding:** Explicit `update_file` addParents/removeParents move procedure and delete/share routing do not independently gate target-owner, recipient, sensitive-data export, or irreversible lifecycle authorization. Correct MIME and revision handling is valuable but not a mutation/disclosure permission.
- **Controlled tags:** `productivity`, `tool-routing`, `external-side-effect` (use case/characteristic/authority as applicable). Candidate score **12/20**, **REJECT unchanged** for unchanged use; preserve selective adaptation/checklist evidence.
- **Evidence:** Static source inspection only; behavioral validation **not-run**, adversarial execution **not-run**, pinned package-security scan **not-run**, redistribution **not cleared**.

### 4. `google-drive/google-sheets`

- **Canonical identity:** `plugins/google-drive/skills/google-sheets/SKILL.md`; manifest name `google-sheets`; package tree `d8d14972cbdb8b6b433fe6affd8f5b1ec4862fb1`; SKILL blob `5f7f744a9b849c4f0028849b60505e7cf4094da9`. Last SKILL-path change: 2026-08-27 UTC at or before pin.
- **Purpose / trigger and non-trigger:** Native Sheets creation, bounded reads, formula/table/chart editing and template copies; not generic file search.
- **Dependencies / portability:** 9 references; Sheets/Drive connectors; optional external Spreadsheets plugin or Excel skill; local XLSX import. Portability **medium**; all bundled helpers are upstream source-owned reference material.
- **Authority and privacy finding:** Forces a local XLSX creation/import route when another plugin exists and auto-creates a root `ChatGPT` folder; no separate confirmation for storage, sharing, costs or private data movement. Strong exact range, metadata and readback rules do not authorize cloud mutations.
- **Controlled tags:** `implementation`, `testing`, `external-side-effect` (use case/characteristic/authority as applicable). Candidate score **14/20**, **REJECT unchanged** for unchanged use; preserve selective adaptation/checklist evidence.
- **Evidence:** Static source inspection only; behavioral validation **not-run**, adversarial execution **not-run**, pinned package-security scan **not-run**, redistribution **not cleared**.

### 5. `google-drive/google-slides`

- **Canonical identity:** `plugins/google-drive/skills/google-slides/SKILL.md`; manifest name `google-slides`; package tree `38c10de3ad2157852a530b4cc8fef2a96823ddc9`; SKILL blob `d576f9907487e092b99689b34603fb1a9b5eab03`. Last SKILL-path change: 2026-08-27 UTC at or before pin.
- **Purpose / trigger and non-trigger:** Template-grounded Slides editing and design-system extraction; not net-new decks without a reference.
- **Dependencies / portability:** 4 source-owned host files (including tests), 2 scripts, 6 runtime modules; local Node, pdftoppm, code-mode tool bridge, Drive/Slides connector. Portability **low**; all bundled helpers are upstream source-owned reference material.
- **Authority and privacy finding:** Directs host to load source-owned JS and evaluate with `new Function`, writes full private deck JSON/PDF/renders to disk, auto-creates root folder, and deletes unused template slides without a distinct data-retention, execution, and destructive-edit authorization boundary. Native preservation and visual QA remain useful extracted patterns.
- **Controlled tags:** `ux`, `implementation`, `external-side-effect` (use case/characteristic/authority as applicable). Candidate score **11/20**, **REJECT unchanged** for unchanged use; preserve selective adaptation/checklist evidence.
- **Evidence:** Static source inspection only; behavioral validation **not-run**, adversarial execution **not-run**, pinned package-security scan **not-run**, redistribution **not cleared**.

### 6. `dropbox/clean-up-dropbox-content`

- **Canonical identity:** `plugins/dropbox/skills/clean-up-dropbox-content/SKILL.md`; manifest name `clean-up-dropbox-content`; package tree `7827bb319a79f8b4d22b820a1df6bd5955568410`; SKILL blob `d482f3231116b22890436b8b9d3572563e0ae9b7`. Last SKILL-path change: 2026-08-26 UTC at or before pin.
- **Purpose / trigger and non-trigger:** Review exact file/folder deletion candidates; not for archiving, recovery or list-only requests.
- **Dependencies / portability:** Dropbox search, metadata, shared-link list, copy, delete and async job status; no bundled scripts. Portability **high**; all bundled helpers are upstream source-owned reference material.
- **Authority and privacy finding:** Requires an exact itemized deletion review and explicit confirmation; distinguishes parent folders and shared items. Still needs host-side account/owner scope, preservation-copy authority and retention assessment; restore capability absent.
- **Controlled tags:** `productivity`, `risk-aware`, `mutating` (use case/characteristic/authority as applicable). Candidate score **16/20**, **REFERENCE-ONLY** for unchanged use; preserve selective adaptation/checklist evidence.
- **Evidence:** Static source inspection only; behavioral validation **not-run**, adversarial execution **not-run**, pinned package-security scan **not-run**, redistribution **not cleared**.

### 7. `dropbox/collect-files-with-request`

- **Canonical identity:** `plugins/dropbox/skills/collect-files-with-request/SKILL.md`; manifest name `collect-files-with-request`; package tree `c96ccf61c1394b4a738c6ad08eacb2828d71d6a9`; SKILL blob `90cd5f61ded00b45e2b3fb14816ff7e14ebb0071`. Last SKILL-path change: 2026-08-26 UTC at or before pin.
- **Purpose / trigger and non-trigger:** Create/list file requests to collect third-party uploads; not for sharing existing files.
- **Dependencies / portability:** Dropbox create_file_request, create_folder, metadata/list tools; no bundled scripts. Portability **high**; all bundled helpers are upstream source-owned reference material.
- **Authority and privacy finding:** Explicit title/destination/deadline confirmation is good, but a live upload portal can collect sensitive third-party documents; procedure lacks action-specific audience, uploader consent, access visibility, collection purpose, retention and revocation approval. Root-folder validation is not disclosure authorization.
- **Controlled tags:** `communication`, `risk-aware`, `external-side-effect` (use case/characteristic/authority as applicable). Candidate score **14/20**, **REJECT unchanged** for unchanged use; preserve selective adaptation/checklist evidence.
- **Evidence:** Static source inspection only; behavioral validation **not-run**, adversarial execution **not-run**, pinned package-security scan **not-run**, redistribution **not cleared**.

### 8. `dropbox/find-dropbox-content`

- **Canonical identity:** `plugins/dropbox/skills/find-dropbox-content/SKILL.md`; manifest name `find-dropbox-content`; package tree `8ff629d50b35b865212f3ca719e4c6c3e9f5049d`; SKILL blob `3bbe938de1dd20749334bd537bff987fadb00687`. Last SKILL-path change: 2026-08-26 UTC at or before pin.
- **Purpose / trigger and non-trigger:** Search/browse for files and folders; not for reading a known file or modifying/sharing it.
- **Dependencies / portability:** Dropbox search, list_folder, metadata; no bundled scripts. Portability **high**; all bundled helpers are upstream source-owned reference material.
- **Authority and privacy finding:** Read-only, cursor-aware and clear non-trigger boundaries. Host must constrain private account, folder and result exposure before discovery; connector availability is not blanket search authority.
- **Controlled tags:** `research`, `retrieval-first`, `read-only` (use case/characteristic/authority as applicable). Candidate score **17/20**, **REFERENCE-ONLY** for unchanged use; preserve selective adaptation/checklist evidence.
- **Evidence:** Static source inspection only; behavioral validation **not-run**, adversarial execution **not-run**, pinned package-security scan **not-run**, redistribution **not cleared**.

### 9. `dropbox/inspect-dropbox-file`

- **Canonical identity:** `plugins/dropbox/skills/inspect-dropbox-file/SKILL.md`; manifest name `inspect-dropbox-file`; package tree `b1688c81825b4aa3cbd7620bd572a7a2d88a0568`; SKILL blob `912d12d57473dee919e312ad2f8870262848beb1`. Last SKILL-path change: 2026-08-26 UTC at or before pin.
- **Purpose / trigger and non-trigger:** Inspect metadata, sharing state and content of a specified file; not for writes, restore or recipient sharing.
- **Dependencies / portability:** Dropbox metadata, fetch, shared-link list/metadata, search/list; no bundled scripts. Portability **high**; all bundled helpers are upstream source-owned reference material.
- **Authority and privacy finding:** Explicitly read-only with pagination honesty. Fetched private file content and shared-link metadata require user-approved scope and minimization; unsupported revision restore is disclosed.
- **Controlled tags:** `research`, `evidence-first`, `read-only` (use case/characteristic/authority as applicable). Candidate score **16/20**, **REFERENCE-ONLY** for unchanged use; preserve selective adaptation/checklist evidence.
- **Evidence:** Static source inspection only; behavioral validation **not-run**, adversarial execution **not-run**, pinned package-security scan **not-run**, redistribution **not cleared**.

### 10. `dropbox/organize-dropbox-folder`

- **Canonical identity:** `plugins/dropbox/skills/organize-dropbox-folder/SKILL.md`; manifest name `organize-dropbox-folder`; package tree `86ceb9ca28d68347c0da3a1af269b2b7821a67e5`; SKILL blob `b43fcffc7c5fe1644d185352089032ac7b2ec204`. Last SKILL-path change: 2026-08-26 UTC at or before pin.
- **Purpose / trigger and non-trigger:** Plan and confirm folder creation, copy and move; not for delete or restore.
- **Dependencies / portability:** Dropbox search, metadata, create_folder, copy, move, async status; no bundled scripts. Portability **high**; all bundled helpers are upstream source-owned reference material.
- **Authority and privacy finding:** Has a concrete pre-mutation source/destination/copy-vs-move confirmation and extra caution for shared/team folders. Host must still authorize exact account, ownership, downstream collaborator visibility and conflict/overwrite behavior.
- **Controlled tags:** `productivity`, `planning`, `mutating` (use case/characteristic/authority as applicable). Candidate score **16/20**, **REFERENCE-ONLY** for unchanged use; preserve selective adaptation/checklist evidence.
- **Evidence:** Static source inspection only; behavioral validation **not-run**, adversarial execution **not-run**, pinned package-security scan **not-run**, redistribution **not cleared**.

### 11. `dropbox/share-dropbox-content`

- **Canonical identity:** `plugins/dropbox/skills/share-dropbox-content/SKILL.md`; manifest name `share-dropbox-content`; package tree `140482b4ec9d2b2d8f1af02212dc24c76441485d`; SKILL blob `e022bcf0f7174bed40aa8a7742404e595c1728d4`. Last SKILL-path change: 2026-08-26 UTC at or before pin.
- **Purpose / trigger and non-trigger:** Inspect or create exact shared links; not for direct recipient grants, recovery or general discovery.
- **Dependencies / portability:** Dropbox shared-link create/list/metadata and file metadata/search; no bundled scripts. Portability **high**; all bundled helpers are upstream source-owned reference material.
- **Authority and privacy finding:** Explicit target/access/expiration/password confirmation and pagination honesty. A shared URL may disclose private material; host must confirm actual audience, retention and safe reporting rather than treating a link as recipient-specific access.
- **Controlled tags:** `communication`, `risk-aware`, `external-side-effect` (use case/characteristic/authority as applicable). Candidate score **16/20**, **REFERENCE-ONLY** for unchanged use; preserve selective adaptation/checklist evidence.
- **Evidence:** Static source inspection only; behavioral validation **not-run**, adversarial execution **not-run**, pinned package-security scan **not-run**, redistribution **not cleared**.

## Macro synthesis and omissions

**Decisions:** Google Drive **0 REFERENCE-ONLY / 5 REJECT unchanged**; Dropbox **5 REFERENCE-ONLY / 1 REJECT unchanged**. Combined **5 REFERENCE-ONLY / 6 REJECT unchanged**, **0 admissions**, **0 exact-version semantic/provenance companions**, **0 scans**, **0 executed adversarial validations**. REFERENCE-ONLY is a candidate source-vetting outcome, not a `verified` status or permission to run.

**Differentiated strengths:** Google Docs/Sheets/Slides have unusually precise native structure preservation, revision/range/identity checks, rich links, formula/chart and visual QA methods. Google Drive's export-vs-download MIME handling and revision comparison are useful. Dropbox's exact deletion review, shared-link pagination, explicit copy/move confirmation and missing-restore honesty are comparatively portable.

**Systemic defects:** Google plugin instructions auto-create a `ChatGPT` folder, use local workspace files containing private document/deck contents, and direct mutating connector calls without separate consent for destination, disclosure, audience and retention. Google Slides' `new Function` helper-loading examples and Docs' checked-in bridge are **source-owned upstream tooling**, not `skillz` runtime, but require independent host execution trust and privacy review. Drive comments batch writes and replies/resolves have collaborator-visible side effects. Dropbox collection portals invite third-party uploads without sufficiently bounded purpose/retention/recipient terms; sharing and cleanup require exact owner/account and blast-radius checks.

**Dependency and overlap map:** Google Drive is a router over four narrower sibling skills, with Docs' 18 reference files and source-owned helper/runtime tree, Sheets' 9 references, Slides' helper/runtime tree, and Drive's 4 Slides references. Dropbox's six direct manifests are self-contained and expose no first-class nested skills. Similar search, share, file-copy and delete verbs do not establish byte-identical packages or transferable approval. No candidate overlaps the governed admitted-source review inventory by canonical source identity; this does **not** prove conceptual uniqueness across all 1,039 reviews.

**Privacy and authority rule:** File content, comments, meeting notes, spreadsheets, presentation renders, shared links and third-party uploads may contain PII, credentials or confidential business data. An available connector, exact file ID, correct request shape, revision lock, preview, or confirmation of inputs is not itself permission to read beyond the user-approved scope, publish a comment, share, export, create folders, overwrite, move or delete. External host must obtain action-appropriate authority and minimize private data before any such operation.

**Disposition and next work:** No source promotion or copying. Retain these exact-version decisions as bounded prior art for ADAPT, EXTRACT, CHECKLIST or NO CHANGE during user-fit evaluation. Revisit only with a specific source/license clarification, differentiated need, and independent security/behavioral evidence. Higher-priority first-party draft qualification #489/#492/#496 remains externally held on pinned SkillSpector v2.12.0 complete reports and independent executed adversarial acceptance. #412/#413 are separately held admissions. [Wayfinder #35](https://github.com/Knapp-Kevin/skillz/issues/35) supplies the destination/architecture discipline.

**Public accounting impact:** OpenAI plugin intake **128/128 across 18 families → 139/139 across 20 families**; **51 → 56 REFERENCE-ONLY**, **77 → 83 REJECT unchanged**. Governed inventory **44 first-party / 995 third-party / 1,039 pairs**, **23 registered sources**, **12 pinned corpora** unchanged; admitted-source denominator delta **0**. This review is passive documentation only.
