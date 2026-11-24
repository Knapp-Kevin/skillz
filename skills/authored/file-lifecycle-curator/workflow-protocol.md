# Required bundled procedure

The original detailed procedure below is normative. [SKILL.md](SKILL.md) determines activation, authorized scope, route, and mandatory closeout. Read the relevant phase in full before carrying it out. Missing or inaccessible guidance is a dependency hold: do not invent a procedure, execute a mutation, or assert completion. Relative links resolve from this package root.

## Workflow

### 1. Bound the collection

Record the intended outcome (findability, tidy folders, knowledge intake, archive, or all), source roots and snapshot time, privacy/retention constraints, expected consumer and output destination. Select one or more work modes: **inventory**, **index**, **summarize**, **tag**, **metadata deck**, **deduplicate**, **organization plan**, **archive assessment**, **retrieve**, **incremental refresh**, **maintenance audit**, **visual structure review**.

Set a stable snapshot policy. A changing source or inaccessible file is recorded as a gap, not silently ignored. For huge collections, process a scoped batch with deterministic continuation and report the unvisited remainder.

### 2. Inventory without changing source data

For each eligible file, capture a stable source-scoped record ID and observed locator, path/name, file type, source system, relevant version, size/date when available, readable state, and access/visibility limits. Record original path separately from any proposed destination. For federated input, keep the original `catalog_id` as `record_id` or record a verifiable one-to-one alias; preserve native IDs, source principal/root, revision type/value, observation time and current viewer permission in an optional `source_context` rather than replacing these with a filename or path. Identify symlinks, aliases, shortcuts, shared folders, links, containers and mount boundaries before following them; do not recursively cross boundaries without permission. Never interpret identical filenames as duplicate content.

Use a cryptographic content hash **only when the complete bytes have actually been read or a trusted source-provided digest is explicitly identified**. If bytes are not accessible, use a provisional identity, mark fingerprint unavailable, and do not assert exact duplicates. Preserve source IDs across resumed batches. Do not include secrets or raw private content in logs.

### 3. Extract and classify cautiously

Prefer the actual authorized document over filename or extension guesses. Separate declared MIME/type from detected format. Extract only the formats and portions the host supports safely; do not execute content or unapproved converters. Note extraction method, coverage (pages/rows/sections), errors, and whether OCR or multimodal inspection was actually performed. Password protection, encrypted archives and corrupted files remain unreadable until approved lawful access is supplied.

Assign **one primary category**, optionally multiple cross-cutting subjects, and a consistent controlled keyword set. Use the collection's approved taxonomy when supplied; otherwise propose a small, documented vocabulary. Normalize synonyms and case, avoid generic filler tags, distinguish asserted tags from inferred suggestions, and do not infer sensitive personal traits from document content. Maintain an exceptions list for unclassifiable or ambiguous items.

### 4. Produce source-grounded summaries and metadata decks

For readable documents produce, as relevant, a 1-sentence description, 3-5 sentence summary, key topics, key entities only when appropriate, temporal scope, version/revision cues, action items attributed to the source, and uncertainty. For tables and media summarize only inspected dimensions; do not claim to have heard audio or viewed frames without that access. Link every nontrivial finding to file ID and a real page/section/row locator where available.

A **metadata deck** is a collection of consistent human-readable per-file cards that expose useful fields and direct provenance, not a decorative presentation or a substitute for the machine-readable index. For federated cards, preserve source identity, version and authorized viewer context; category/tag/summary/graph edges can disclose private source existence and must be filtered before display. Cards must omit/redact sensitive fields as required. Use the structured fields in [metadata-contract.md](references/metadata-contract.md); publish both source links and card summaries only to authorized audiences.

### 5. Build a searchable, verifiable index

Produce an index with stable record IDs, file/source locators, accessible title/name, category, normalized tags, summary, modified/source dates when observable, version hints, fingerprint state, extraction coverage, and permissions/retention limits. Record the exact source snapshot or per-file revision when available. Support keyword/filter navigation without claiming full-text or semantic search when no actual search engine exists.

Optional semantic embeddings, vector database ingestion, permanent index storage or shared search service are separate integrations requiring tool capability, approved storage scope, data-residency/egress authority, and observed retrieval tests. Link index records to their metadata cards and original files. Keep original and normalized text distinguishable; include an explicit NOT INDEXED list.

### 6. Detect duplicates and propose organization

Classify duplicate candidates as **EXACT** (verified complete-byte digest), **LIKELY** (substantially similar, independently compared content), **RELATED** (topic/version family) or **UNRESOLVED**. Keep version chains, originals and derived files; never auto-delete or coalesce based on similarity, filename, embeddings or a truncated digest. Collision-resistant names and clear conflict handling are required for *proposed* relocations.

Propose a shallow navigable folder tree based on stable primary categories, ownership and use, not an unbounded hierarchy of tags. Supply a proposed old -> new mapping, reasons, collision list, link/reference breakage, access/permission risk, and rollback plan. Prefer labels/virtual collections to physical moves where shared links, version history or collaboration make relocation costly. Make no writes without approved per-batch execution; see [operation-and-archive-rules.md](references/operation-and-archive-rules.md).

### 6a. Visualize the original, proposed and verified structure

When a plan includes an organization change, or the operator wants to
understand progress, show a **clear before/after folder-tree preview**
and a compact progress indicator. Use three *explicitly distinct*
views, never a single ambiguous "after" state:

- **Observed:** actual source-scoped structure reported by the
  authorized host at a named snapshot and capture time, including
  PARTIAL/UNKNOWN coverage. File/folder counts and names can be
  sensitive; enforce the current viewer and source access rules
  before displaying any tree or change count.
- **Proposed:** desired categorized folder structure, still a
  hypothetical read-only plan, never the result of a file move.
  Show collision/permission/link holds and unplaced records. Do
  not treat an approved proposal as having been applied.
- **Verified:** only relocations with current observed destination
  and a host-checked source/plan/revision-bound readback receipt.
  EXECUTED but unverified, BLOCKED, FAILED, ROLLED_BACK and UNKNOWN
  remain separate. A visualization alone does not make a receipt
  trustworthy.

Progress means verified relocations / planned relocations **inside
the actually observed scope**, not "files scanned" or "tasks closed".
If scan coverage is partial, show counts but suppress a misleading
global completion percentage. If the diagram is truncated for
readability, say so and report the omitted count. Include accessible
text labels and a plain-text tree fallback rather than relying only
on color, image generation, or a particular charting app.

Read [visual-progress-contract.md](references/visual-progress-contract.md)
for full agent-lifetime safeguards: immutable plan identity/revision,
permission-bound visual recall, observed-vs-proposed-vs-verified
separation, progress accounting, replay/rollback, destination
collisions, safe display aliases, version drift, source omission,
scheduled runs, portability and adversarial failure conditions.
The optional [render_structure.py](scripts/render_structure.py)
accepts only explicitly supplied plan snapshots and produces
read-only Mermaid and plain-text views. Never claim it verified
real host operations or created private files. Any actual
interactive viewer, exported diagram or persistent visual
checkpoint requires separate supported host capability and
permission. The user may choose the preferred display style,
but a preference cannot remove provenance, protection or
status distinction.

### 7. Assess archive and retention safely

Separate **archive recommendation** from **archive creation**, **retention approval** and **deletion**. Identify reasons (inactive, superseded, completed, historical reference), proposed archive location/format, required metadata, immutability/holds, link preservation, owner, review date, future retrieval and restore expectations. Unknown legal, contractual or organizational retention is an OPEN HOLD, not an invitation to choose a guessed period.

Before an authorized archive action, require a recoverable destination with read-back/integrity verification, no unapproved external exposure, no permission broadening and an explicit retention disposition. An archive package is not a backup until recovery has actually been tested. Even when archival creation succeeds, do not delete originals without **separate** explicit disposal authority and safeguards.

