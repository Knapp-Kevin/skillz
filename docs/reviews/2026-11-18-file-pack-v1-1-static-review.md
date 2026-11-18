# File and federation skills v1.1.0: independent exact-package static review

**Date:** 2026-11-18. **Reviewer/method:** first-party ChatGPT full-text static review and deterministic schema/contract fixture checks. **Not** a model-agent behavior validation or observed real connector acceptance. No outside tester report was used or required.

## Reviewed source identities

| Skill | Git blob for SKILL.md | Complete package tree | Package files |
|---|---|---|---:|
| File Lifecycle Curator v1.1.0 | `4d9387a3698252c7f92c0a4cbed415f789155c79` | `31f63a762ead720db8c390017c235e6602f3ffd8` | 7 |
| Federated Source Catalog v1.1.0 | `5f4859515de5d073a939d439f1d75e1084d4404e` | `b9add6ba4162fb1ad190dca20aa3fdee67d3e1c1` | 8 |

**Complete source boundary:** Curator: `SKILL.md`, `LICENSE`, `references/metadata-contract.md`, `references/operation-and-archive-rules.md`, `references/federated-intake.md`, `examples/synthetic-corpus-and-cases.md`, `examples/federated-intake-cases.md`. Federation: `SKILL.md`, `LICENSE`, `references/federated-record-contract.md`, `references/provider-adapter-matrix.md`, `references/authority-and-freshness.md`, `references/curator-handoff.md`, `examples/federated-cases.md`, `examples/federated-handoff-cases.md`. All are original MIT text, no bundled executable, OAuth client, service, account or external copied asset.

The original v1.0.0 reviews and hashes in the November 18 historical reviews are **retained as history**, not silently overwritten. The current package is a materially new exact version and has been read and re-adjudicated.

## Resolution of confirmed composition gap

A v1.0 federated file used `catalog_id`, `native_locator`, `revision`, `permissions`; v1.0 curator used `record_id`, `source_locator`, `source_revision`, `access`. Neither prescribed the full typed handoff.

**v1.1 addition:** federation produces a bounded handoff (source ID, principal/root, native object ID/locator, revision kind/value, observed time, permission basis and audience, extraction status/coverage/citations and explicit no-persistence defaults). Curator consumes only authorized content and preserves these as `record_id`, `source_locator`, `source_revision` and optional `source_context`. If data is missing, stale, unauthorized or impossible to preserve, the workflow BLOCKS or emits an incomplete result, not a fabricated success. A standalone curator needs no federation tool. Both sources own local reference/examples, not just an outside documentation link.

**Contract-level remediation: COMPLETE.** This does not prove that a live agent executes the handoff correctly. Real cross-provider access/revocation, content ingestion, file effects and per-viewer ACL isolation remain NOT RUN.

## Static rubric (each skill)

| Dimension | Curator /2 | Federation /2 | Reason |
|---|---:|---:|---|
| Trigger precision | 2 | 2 | Single-collection vs multi-source activations and non-triggers |
| Procedural clarity | 2 | 2 | Named phases and explicit optional bounded handoff |
| Authority/safety | 2 | 2 | Source principal/viewer, no implicit persistence/egress/mutation |
| Failure handling | 2 | 2 | Absent connector, mismatch, stale revision, private shortcut, denied source |
| Evidence discipline | 2 | 2 | Typed revisions, original IDs, observed vs inferred, partial extraction |
| Dependency coherence | 2 | 2 | All complete-package references and synthetic cases present |
| Portability honesty | 2 | 2 | Text-only core; host connector execution conditional |
| Usefulness/differentiation | 1 | 1 | Practical scoped workflows; no full ecosystem comparative or uptake evidence |
| Adversarial resilience | 2 | 2 | Embedded prompt and cross-user leakage rules, conservative handoff |
| Effectiveness design | 1 | 1 | Checkable contracts and fixtures, but real agent effectiveness unmeasured |
| **Total** | **18/20** | **18/20** | **Exact-version static verified, behavior NOT RUN** |

No unresolved static hard-fail identified in these bounded read-only scopes. Actual mutation, remote read, automated sharing and any connected app usage remain separately authorized host actions.

## Independently performed checks and limitations

- Re-read the complete 7-file and 8-file packages, including all new references; checked entry frontmatter version, internal links, exact file list, MIT license, and prohibited assumption about executable tools.
- Parsed JSON metadata records and the federated handoff example; both retained their status/identity boundaries and explicit missing data.
- Ran **12/12 deterministic synthetic policy-oracle checks** in an isolated first-party JS evaluation, using fictional case flags H01–H12. These exercised the *oracle's decisions* for matching identity, revision mismatch, 403, shortcut, second viewer, malicious text inertness, branch drift, export vs native, partial excerpt, no persistence, tenant mismatch and missing reader. Their passing result is **NOT** an invocation of either skill through an LLM host, an integration test, privacy enforcement proof, or behavioral validation. The synthetic policy helper was not added as a skill runtime.
- Retain `validation_status: not-run`; no claims of actual tested connector, archive restore, index freshness, source permission isolation or real-model obeying the contract.

## Remaining own-team acceptance

**P0:** A suitable authorized host must exercise the exact v1.1 complete trees against negative viewer/revocation tests, revision drift, incomplete provider pagination and cross-source handoff; report prompts, actual action trace, observed output, and PASS/FAIL/NOT RUN. **P1:** Independently benchmark source retrieval and tagging/metadata quality against a synthetic ground-truth corpus, and archive restore/ACL if a genuine authorized file runtime is present. Neither task depends on external tester reports.

**Completion boundary:** v1.1 static source/contract remediation is complete; product-level execution/behavioral validation is not. Changes to any required package file must invalidate and renew this exact-version review.
