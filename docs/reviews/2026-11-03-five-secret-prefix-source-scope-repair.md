# Five first-party evidence-scope repairs: implementation receipt (2026-11-03)

**Disposition: candidate implementation, HOLD.** This is an independently owned bounded repair of [issue #491](https://github.com/Knapp-Kevin/skillz/issues/491). It changes five existing first-party instructions, not inventory, and is disjoint from open drafts #673, #677 and #682. Base main: `0045bb24cc5aeff047c8b9964765ebef23dd951f`. All commits use `[skip ci]`.

## Why this matters

A reader using these methods to compare products, verify a claim, research a topic, write a brief or learn from an agent failure should never see fragments of a password or token in the answer. Private inboxes and session logs should not be read merely because a connector exists. The five methods are preserved, but their safety boundaries are explicit.

## Exact changed SKILL.md identities

| Existing method | Base Git blob | Candidate Git blob | Safety change |
|---|---|---|---|
| `skills/brief-writer/SKILL.md` | `0eb629e92e53a03c26df0ebef15662e1888c25b0` | `bdc5411eec2eb268955c677f0b0c7c6bdba171e3` | No credential fragments; scoped email/calendar evidence |
| `skills/compare/SKILL.md` | `b933a8266b8eda18807de9b9717436c54af0362d` | `37b5d493dfa87ff1ce20e7b44d7d095e2eeed700` | No credential fragments or identifying source excerpts |
| `skills/deep-dive/SKILL.md` | `b518f172abce491d979cf8f8ef854a61605b2790` | `44d59d8b890d5b5ca3dc2497aada03f0ff70ad99` | No credential fragments or identifying source excerpts |
| `skills/fact-check/SKILL.md` | `e58dea59671c8a7c537e27403d6f52e466bf8d86` | `d83c43282d525682f3e13b8296111d7fe7de46f0` | No credential fragments or identifying source excerpts |
| `skills/agent-postmortem/SKILL.md` | `fb8777d18a27a89f47f9e8a022385b480d49f7c0` | `dde789e87da090b92021b3e55304299244f62ac2` | No credential fragments; scoped transcript/log/cost access |

All five candidates forbid exposing prefixes, suffixes, hashes, signed URLs, query parameters or identity-bearing excerpts. They report safe category/location only, recommend secure rotation when actual exposure is confirmed, and treat source text/logs as untrusted evidence. External writes, private exports, installations and communications require separate action-specific approval.

**Scope:** five original source-neutral first-party packages, no new positive recommendations. This is not a promotion, not a regrade, not a governed exact-version verification and not unchanged-use clearance. Source and per-file terms stay unchanged, subject to full package audit. The base skill Git blob does not identify the whole package tree. Exact package-tree IDs, alias exposure, bundled dependencies, revised provenance and verification companions, and consolidated first-party registry fingerprints must be reconciled before integration.

**Static implementation readback:** candidate file SHA matrix above is from GitHub update responses; independent final refetch still required. No external SkillSpector run, adversarial execution, host behavior test, CI or workflow result is claimed. Security: NOT RUN. Behavior: NOT RUN. Exact-version governed review: STALE/NOT REQUALIFIED. Promotion: NONE. Authority: safe text changes do not themselves authorize any read, installation, scheduled action or write.

**Integration gate:** reconcile this five-file repair with the 44-entry first-party registry and any current shared ownership. Independently verify all five exact candidate blobs and source/provenance/verification companions, obtain pinned final-package security and representative adversarial host evidence, then integrate with expected-main-head protection. Keep #491 open until qualified merge. Do not modify five public accounting surfaces or the 33-domain graph for an unqualified repair. Preserve original README banner and discovery routes.

**Accounting:** five repaired instructions, zero new distinct eligible packages, zero new grades, zero new selected Valuable References or Recommended for Use, zero source-family admissions. Global eligible denominator UNKNOWN. Existing historical 1,039 governed records and 4,813 raw paths are different populations and remain unchanged.
