# AgentSkillExchange: identity segmentation and two complete structural clusters (2026-11-02)

**Source:** `agentskillexchange/skills` at `a6017b4af9d0298b7be3af7a6ec7485943d2c3e7` (discovery-only; root MIT, Copyright (c) 2026 Agent Skill Exchange; linked upstream rights separate).
**Scope:** source-vetting candidate decisions only. No admission, governed review, security scan, behavioral validation or installation. Governed review records stay at **1,039**.

## What changed

| Measure | Before | After |
|---|---:|---:|
| AgentSkillExchange paths with exact blob/tree identity verified against a nontruncated checkout | 0 | **3,200 / 3,200** (0 mismatches) |
| AgentSkillExchange terminal exact-path static decisions | 0 | **545** (+3 DEFER) |
| Four-source terminal exact-path static decisions (current 10-dimension standard) | 209 | **754 / 4,813** |
| Four-source raw paths without such a decision | 4,604 | **4,059** |
| Distinct eligible denominator | unknown | **unknown** |

Evidence:
- [Identity segmentation](../../registry/discovery/agentskillexchange-identity-segmentation-20261102.json): structural segments for every path, exact duplicate exposures, shared upstream groups and the non-skill template exclusion.
- [Stub cluster ledger: 462 records](../../registry/discovery/agentskillexchange-catalog-stub-462-static-20261102.json).
- [Authored cluster ledger: 86 records](../../registry/discovery/agentskillexchange-authored-procedures-86-static-20261102.json).
- [Capability index](../../registry/discovery/agentskillexchange-capability-index-20261102.json): source-neutral domain → subdomain → package lookup, with negative evidence included.

## Identity map (Phase 1)

| Structural segment | Paths | Status after this tranche |
|---|---:|---|
| `catalog-stub-no-procedure`: description-only card that says no install/usage could be extracted | 462 | **all reviewed**: 458 REJECT unchanged / 4 REFERENCE-ONLY |
| `authored-procedure`: authored sections beyond the catalog template (14 multi-file) | 83 | **all reviewed**: see below |
| nested first-class DocsBot reference skills (other-shape) | 3 | **all reviewed** |
| `template/SKILL.md`: contributor placeholder template | 1 | **excluded as non-skill**; no grade |
| `catalog-card-install-pointer`: auto-extracted upstream install fragments only | 2,651 | **pending**: next frontier |

Other identity facts:
- **Exact duplicate exposures:** 3 pairs are identical apart from slug, self-URL and star counters (`draft-internal-status-updates-and-incident-comms`, `investigate-failing-github-actions-runs-with-ci-doctor`, `mailgun-javascript-sdk-email-delivery-and-domain-operations` and their `-2` twins). Each twin carries `duplicate_exposure_of`.
- **Same name, distinct content:** 2 pairs.
- **Shared upstream:** 201 groups covering 1,044 paths cite the same upstream URL; for example, 29 cards cite `hashicorp/terraform` and 28 cite `aws/aws-sdk-js-v3`. Shared upstream is a lead for reusing upstream-level facts, **not** proof of duplication.
- **Publisher labels:** 2,619 cards are labelled `security_reviewed` and 577 `listed`. No package contains evidence supporting the security label.

## Method and acceleration

- **Parallel review:** 16 parallel read-only reviewers were each assigned disjoint exact package identities. Each received the same rubric brief: the existing ten dimensions, the authority hard gate, privacy and secrets rules, and the controlled taxonomy.
- **Integration checks:** one integration owner validated every record. The checks covered exact blob/tree identity, taxonomy membership, rubric-rationale agreement, consistency between hard fails and dispositions, and double counting.
- **Adjudications:** 12 conflicts were resolved; each is recorded under `reconciliation_overrides` in the ledgers.
  - Four REFERENCE-ONLY results below the 10/20 floor used by earlier tranches were changed to REJECT.
  - Five authority or privacy gate failures were applied: `jev-social`, `darkmoon-pentest-mcp`, `openhook`, DocsBot `bot-builder` and `hypergrok-trading-desk`.
  - Three stubs whose content lives only in an unpinned upstream were normalized from DEFER to REJECT unchanged, matching the stub cluster.
- **Throughput:** 548 exact packages reached a decision in one integration cycle, against the earlier baseline of about eight packages per run. The gain came from three sources:
  - structural segmentation, so homogeneous clusters share one brief;
  - parallel disjoint review;
  - one atomic publication instead of many per-tranche accounting edits.
- **Spot checks:** high scorers (for example `clean-closed-issue-worktrees` 19/20) and every reviewer exception were checked by the integration owner against the package text.

## Macro findings

### Stubs
- None of the 462 stubs contains an executable procedure. Four have useful design prose and are REFERENCE-ONLY: `ralph-loop`, `cross-validate-research-with-sandbase-multi-source-search`, `turn-messy-datasets-into-auditable-reports-with-data-master` and `pangolinfo-amazon-scraper`.
- **Suspected misattribution (115 cards):** the author is named as the API vendor or monorepo owner with no evidence that the vendor published the card.
- **Capability not supported by content (79 cards).**
- **Consequential side effects with no gate (81 cards).**
- **Private-content egress with no gate (20 cards).**

### Authored packages
86 packages: 51 REFERENCE-ONLY, 32 REJECT unchanged, 3 DEFER.

- **Reusable mechanisms:**
  - exact-plan-ID scan-confirm-execute (`clean-closed-issue-worktrees`);
  - per-action confirmation for publishing and phone calls (`shipvela-publish`, `placecall`, `bulkpublish-social-publishing`);
  - privacy-preserving style learning (`email-voice`);
  - read-only bounded review loop (`gauntlet`).
- **Authority hard-gate failures (16):** unconfirmed USDC sales, metered checkout with a raw private key, `git push origin master` behind only a coordination lock, account creation and public profile publishing, webhook registration, unconfirmed pentest launch, trading with upstream-only gates, and harness security reconfiguration.
- **Remote or self-updating instructions (4 rejected):** for example, `datacircle` says "Read https://datacircle.dev/SKILL.md and follow it".
- **License conflicts (2):** `sandbase` claims Apache-2.0 without shipping the text, and the DocsBot `bot-builder` templates describe themselves as copies of vendor internal source.
- **DEFER (3):** an essential bundled client is missing from the pinned package: `live-search-console-data`, `brainiall-diarized-transcription`, `popnow-video`.

## Limits and next action

These are static candidate grades. None is approved for unchanged use, security-qualified or behaviorally validated.

The 2,651 install-pointer cards remain without decisions. **Next:** review them by category cluster, reusing upstream-level facts across the 201 shared-upstream groups while still reading every card.
