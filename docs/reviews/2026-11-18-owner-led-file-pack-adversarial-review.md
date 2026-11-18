# Independent first-party adversarial review: file and federated skill packs

**Date:** 2026-11-18. **Reviewer:** ChatGPT performing the Skillz first-party source review. **Disposition:** Individual v1.0.0 packages retain their existing exact-version *static-reviewed* labels. **Cross-skill end-to-end composition: HOLD pending normative handoff contract and independent observed acceptance.** This review is itself independently performed, not supplied by an outside implementer.

## Owner acceptance policy

Skillz owns quality and evidence. We inspect, challenge, and, where tools support it, test our own instructions. **No external tester's report, attendance, contact, verbal feedback or delivery is required.** Informal feedback can create an investigation lead but cannot change a rubric score, validate behavior, close a gap, or excuse missing our own verification. If no agent host with necessary capabilities is available, leave the relevant behavior `NOT RUN` and move independent static/refinement work forward.

## Independently verified exact baselines

| Package | Source blob | Complete tree | Static review |
|---|---|---|---|
| [File Lifecycle Curator](../../skills/authored/file-lifecycle-curator/SKILL.md) | `63577971773ae0d923f6d38165c13c34f36b8f72` | `12e7f8d07bdd1553f7ed78e377ebc7b5e9742a84` | 18/20 static, behavior not-run |
| [Federated Source Catalog](../../skills/authored/federated-source-catalog/SKILL.md) | `4d028afe00921af05f8258e0c7f50707d2ebb68c` | `130b199cc7c5549d8905196d62f54617198d1976` | 18/20 static, behavior not-run |

**Checks actually performed in this review:** Read back both entire SKILL.md files, required supporting references, original fixtures, and their authored-index records from live GitHub `main`. For **11 files across two complete packs**, checked entry blob identity against authored index, package file counts, frontmatter names, relative internal links, and executable file absence. **Both Markdown JSON examples were parsed successfully.** No broken internal SKILL.md links were found. Original package fingerprints were not modified. These are source/contract integrity observations; they do not prove any model follows instructions.

## Adversarial static findings

| ID | Finding | Assessment | Why it matters / independent response |
|---|---|---|---|
| IR-01 | **Federation-to-curator identity contract is not normative.** One record uses `catalog_id/native_locator/revision/permissions`; the other uses `record_id/source_locator/source_revision/access`. | **GAP, P0 for composed use** | Both skills demand provenance retention, but a compatible field mapping and authorization envelope are not specified within either v1.0 package. Proposed [handoff contract](2026-11-18-file-pack-composition-contract.md) now specifies mapping, revision binding and viewer authority. Composed use is not independently qualified. |
| IR-02 | Shared/permissioned search would need per-viewer ACL checks and revocation propagation. | **Unproven operational control, P0** | The federated skill instructs an agent to filter before snippets, counts and graph edges. There is no bundled ACL enforcement or shared index; never infer tenant safety from wording. Independently test an authorized two-viewer synthetic scenario if a host permits. |
| IR-03 | Connector pagination, source completeness and GitHub/Drive revision semantics are not behaviorally proven. | **Unproven operational control, P0** | Text specifies PARTIAL on truncation, 403 and stale branch; actual connector action behavior is host-specific. Run source-scoped synthetic/bounded tests ourselves, or record NOT RUN. |
| IR-04 | Cross-provider EXACT_BYTES is a high-risk identity claim. | **Conditional, P1** | The prose correctly restricts equality to complete comparable bytes/trusted digest evidence, but the two metadata records lack a shared typed comparison envelope. Proposed mapping must preserve algorithm, byte scope, representation and revision; don't deduplicate native Docs/exports by title. |
| IR-05 | Curator schema lacks a dedicated normalized `catalog_id` field and a portable per-field permission/provenance structure. | **Gap, P1** | Generic `access`, `evidence_locators` and `tag_basis` may not preserve record-level source audience, provenance and inferred-vs-observed evidence across a handoff. Use an explicit sidecar until a reviewed v1.1 schema exists; do not silently drop fields. |
| IR-06 | Archive creation vs tested recoverability vs disposal are deliberately separate. | **Static design check passes, behavior not-run** | The curator requires a separate deletion authorization and archive read-back/restore evidence. Any real archive integrity or ACL test remains unobserved. |
| IR-07 | File bodies and README instructions are untrusted, including prompts to exfiltrate data. | **Static design check passes, behavior not-run** | Both packs explicitly reject embedded instructions; tests must independently observe that behavior in a supported host, not infer it from the text. |
| IR-08 | Incomplete/unreadable content must be visible as gaps. | **Static design check passes, behavior not-run** | Both packages prohibit fabricated full-content summaries, exact dedup conclusions and zero-result claims when files or pages are missing. |
| IR-09 | Search relevance, keyword taxonomy portability, metadata-deck usefulness and scale are not evaluated. | **Unproven effectiveness, P1/P2** | Create small synthetic ground truth, human-readable expected answers, source-cited tag/summary checks and repeatable comparisons against baseline prompts. Do not call a schema useful merely because JSON parses. |
| IR-10 | Third-party comparison and taxonomy promotion remain incomplete. | **Discovery/evaluation backlog, P2** | The 14 proposed file-management subdomains are **not** canonical, qualified behavior. Inspect complete exact third-party packages with rights, dependency, safety and outcome comparison before wider claims. |

No observed runtime defect or actual data leak is asserted by this static review. It finds **one concrete missing interoperability contract**, supporting schema limitations, and a set of operational/effectiveness claims we have not proven. The existing 18/20 scores apply to individual exact packages, **not** a tested composed product.

## First-party owned qualification lanes

**Lane A: Static and contract quality (can do without external access).** Maintain exact source version and required-file checks; independently review triggers/non-triggers, untrusted-data treatment, privilege boundaries, error outcomes, schema validity, and data minimization. This lane is the source of the P0 composition finding. The proposed [composition contract](2026-11-18-file-pack-composition-contract.md) defines 12 new synthetic cases (H01-H12) with expected decisions, not observed passes.

**Lane B: Synthetic host-agent behavior (our responsibility).** When we have a suitable user-authorized agent host, construct own fictional file/connector fixtures and run positive, negative and adversarial prompts. Record exact skill blob/tree, model/host/tool configuration, the actual messages/actions/output, expected result, observed result, PASS/FAIL/NOT RUN and limitations. Start with read-only tests; require no personal data, outside implementer or scheduled service. We must not count static reasoning as host behavior.

**Lane C: Connector/runtime integration (separate capability, not claimed by these passive skills).** If we have a functioning connector and a narrow expressly authorized source, test real listing/search/pagination and version/permissions only within that scope. Don't turn a connector's mere presence or an observed GitHub file read into a full cross-provider integration result. No shared index, cross-account ACL enforcement, sync or archive mutation is claimed.

**Lane D: Effectiveness and documentation.** Run independent synthetic retrieval/tagging evaluation and account for precision, coverage, unsupported formats, cost and error cases. Update full-package fingerprints and static review upon actual source change. Preserve v1.0 tested identity and label next versions honestly.

## Required publication rule

- **Static reference eligibility:** individual v1.0 reviewed packages may remain discoverable with exact fingerprints and `validation_status: not-run`.
- **Composed federated workflow:** still **HOLD** for any claim of end-to-end ready-to-run identity-safe pipeline until its mapping and authority rules are incorporated and re-reviewed in exact future skill versions and our observed test evidence exists.
- **Word-of-mouth feedback:** may be attached as `informal-unverified-feedback` with date and exact claim if voluntarily received, but is not a prerequisite, evidence substitute, automatic defect or acceptance.
- **Do not invent a test:** if an independent host test is unavailable, publish the source/contract review and a precise remaining evidence gap; never ask for external test results just to proceed.

**Next independent development decision:** produce a reviewed v1.1 composition amendment after the new handoff contract is challenged against cases H01-H12; keep source identities and authority scopes intact. This is future work, not an unearned completion claim.
