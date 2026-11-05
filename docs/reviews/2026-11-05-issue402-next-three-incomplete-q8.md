# Issue #402: three more pinned Q8 scanner-incomplete packages

**Date:** 2026-11-05. **Method:** direct static inspection of exact pinned upstream Git content and relevant license terms, with reasoned misuse/non-trigger cases. **No source scripts, web servers, mail connectors, third-party installers or agent-host behavior were executed.** The exact source and package-tree fingerprints, findings and ten-axis scores appear in the [machine review ledger](../../registry/security/q8-three-incomplete-privacy-and-code-static-dispositions-20261105.json).

This tranche adds 3 full package reviews (13 material owned files) to the 3 previous scanner-INCOMPLETE reviews. Together with the already completed 7 scanner-FAILED reviews, the targeted Q8 risk-content frontier is now **13 of 40**. This changes **none** of the historical scanner states: 10 PASS, 7 FAIL, 33 INCOMPLETE among the 50 selected study references. The 10 past PASS receipts do not mean these are installed or behaviorally accepted. None of the 13 new static content decisions grants unchanged execution.

## Results

| Skill, pinned source | Direct file count | Current static score | Review disposition |
|---|---:|---:|---|
| [Daily Focus Board](https://github.com/github/awesome-copilot/tree/f11a4e441c5ff061b4f8ae37952be8c602e4034e/skills/daily-focus-board) | 7 | **14/20** | Reference-only: fix privacy/retention and day-to-day carryover expectations before general reuse |
| [Build Evidence Map](https://github.com/github/awesome-copilot/tree/f11a4e441c5ff061b4f8ae37952be8c602e4034e/skills/build-evidence-map) | 5 | **16/20** | Reference-only: accurate evidence method; clarify validation limits and fix timestamp contract |
| [Email Voice](https://github.com/agentskillexchange/skills/tree/a6017b4af9d0298b7be3af7a6ec7485943d2c3e7/skills/email-voice) | 1 | **18/20** | High-quality bounded static procedure, but no installation, mailbox access, send, or behavioral approval |

**All three pinned complete Git trees match both the original Q12 security register and their latest upstream default-branch package trees at the review checkpoint.** A source repository gaining commits is not itself a changed package; exact package-tree identity is the review-freshness boundary. Source code and references remain unexecuted data.

### Daily Focus Board

**Package tree:** `b6816f5d51874b15b852090ad9d2880515dde640`. **SKILL.md blob:** `ca4f9c93f966bc57ba2be7418dace757c4189b4b`. Full owned scope: `SKILL.md`, the template and sample HTML, three supporting Markdown files, and `serve-board.ps1`. Root GitHub, Inc. MIT license must be preserved if copying expression. Original SkillSpector state: **INCOMPLETE**, with incomplete-reference/parse and content-pattern flags, unchanged here.

The source correctly separates personal task planning from an agent's ability to read browser-local state; it recommends escaping injected JSON and the UI includes basic text/attribute escaping. Its server example binds to `127.0.0.1` and the PowerShell launcher gives a PID-based stop instruction. These are legitimate safeguards and should not be erased in a risk-only summary.

**Material findings:**

- **High, privacy and retention:** `assets/board.template.html:271–274,301,389–404` stores progress, notes and personal brain-dump content in day-keyed `localStorage`, indefinitely until manual/browser deletion. Notes can be deleted individually, but there is no disclosed retention schedule or comprehensive clear/export-and-delete control. Use of a general scratch-directory HTTP server should not expose unrelated private files, even when loopback bound.
- **Medium, misleading next-day carryover:** `assets/board.template.html:271,403,413` changes `state.t[id].carried` for **today's** date key but does not import that task into a **new** date key. The recap identifies deferred items, so manual transfer is possible, but descriptions promising a working “move to tomorrow” feature overstate the implementation.
- **Medium, silent state failure:** `save()` swallows storage exceptions and an agent cannot read the browser's actual saved state, so a user can believe progress persisted when it did not. The tutorial should plainly describe backup and manual restart.

**Next acceptance work:** Add a visible full privacy reset, retention/export guidance and warning on failed storage; implement real next-day transfer or explicitly label the feature as recap-only; serve only a dedicated directory and close the server when finished.

### Build Evidence Map

**Package tree:** `e5de9060f2171ee6f1b6d7dae5e30402aad9eb4d`. **SKILL.md blob:** `3d0ff9385a5603242e39989cbfc6e7a8d856d6cc`. Full owned scope: SKILL, `references/evidence-ladder.md`, `references/map-schema.md`, `scripts/contract.mjs` and `scripts/validate.mjs`. GitHub root MIT terms retained on copying. Previous scanner state: **INCOMPLETE**, not rescanned.

The source is unusually careful about evidence: a directed acyclic reasoning graph, counterevidence, bounded excerpts, dates and explicit missing facts are part of the local contract. It warns that JSON validation proves graph integrity rather than factual truth and prohibits unsolicited third-party installation and source fetching.

**Material findings:**

- **Medium, contract contradiction:** The map schema and `retrievalDate()` permit `retrievedAt` as an ISO UTC timestamp, but when a `verification` block exists, `contract.mjs` compares the **entire** timestamp to `verification.checkedAt.slice(0,10)`, an ISO date-only string. A same-day valid timestamp form can fail validation despite being allowed by the public schema.
- **Medium, source verification provenance:** `scripts/validate.mjs` computes a receipt over the supplied map and excerpt hashes. `contract.mjs` checks the shape of supplied verification metadata but cannot independently prove that an external source fetch/normalized excerpt match actually happened. An offline `VALID` receipt is therefore structural evidence only, and the tool must not infer a remote verification from an untrusted user-authored `verification` object.
- **Low, explicit external dependency:** Rendering uses optionally installed `doubt-ai@0.8.0`, and remote source verification may contact listed URLs. The SKILL explicitly requires separate network permission; no such permission or result is inferred from reading it.

**Next acceptance work:** Make timestamp parsing and equality semantics match the documented schema; distinguish attested source retrieval from user-supplied verification claims; regression-test the accepted date forms before recommending unchanged use.

### Email Voice

**Package tree:** `11cd6421647e0551cf1579c663bd1478c94d5394`. **SKILL.md blob:** `b36152d130ff9e3de7ddc41a3ae96b3b215fb176`. Its whole package is a single Markdown source with an **inline MIT grant and copyright notice for Rohit Motwani**. The previous scanner state was **INCOMPLETE**, with one missing-reference flag. No runnable supporting components were found inside this pinned package.

**Positive findings:** It explicitly asks which Sent folders or supplied samples the user authorized; bounds Quick/Balanced/Deep sampling; reserves independent threads for held-out evaluation; avoids full-mailbox and attachment overcollection; treats mail text as untrusted data; keeps checkpoints and style profiles private; suppresses raw-email export by default; and refuses to infer permission to send or change a mailbox from a request to draft. It also labels unavailable validation rather than inventing results. Those are good static design decisions, not behavioral proof.

**Boundaries that remain:**

- Optional ZIP/`npx skills@1.7.4` setup instructions involve download/installation, not passive text reading. Explicit separately authorized installation, provider verification and a suitable sandbox/host flow are still required.
- The method can read 40–300 private sent messages plus reserved replies if asked. Its consent and deidentification language is strong, but the host must actually honor account, retention and source-scope restrictions.
- No live connected mailbox or held-out user response was inspected. The proposed 4/5 validation threshold is a method, **not a measured pass**.

**Recommendation:** Preserve the method as a particularly useful, source-reviewed reference. It needs no invented source defect merely to justify being held from unapproved installation or private mailbox access. A source-level positive judgment does **not** authorize those side effects.

## Review accounting and next priority

- Historical Q8 security scanner outcomes: **10 PASS / 7 FAIL / 33 INCOMPLETE**, unchanged.
- Direct exact-source risk reviews for historically FAILED: **7/7**.
- Direct exact-source risk reviews for historically INCOMPLETE: **6/33**.
- Targeted historically flagged content reviewed: **13/40**; **27** historically incomplete Q8 packages still await direct risk-content review.
- Agent behavioral tests, new hosted scans, and unchanged-use permissions during this tranche: **0**.

The [README progress graphic](../../docs/assets/q8-direct-static-risk-review-progress.svg) is regenerated from these pinned ledgers by [the deterministic Node renderer](../../scripts/build-q8-static-review-progress.mjs), not manually painted. It reports **source-review work** separately from the older scanner graphic and does not change capability-domain totals. The broader corpus and other issues remain open until independently resolved.
