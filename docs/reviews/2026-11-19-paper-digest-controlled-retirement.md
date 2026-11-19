# Paper Digest: independently authored replacement qualification

Date: 2026-11-19. Tracked under [issue #738](https://github.com/Knapp-Kevin/skillz/issues/738).

## Complete original and new package identity

- Historical original: [`skills/paper-digest/SKILL.md`](https://github.com/Knapp-Kevin/skillz/blob/285732d5390c7e309b5613f8afba06ce5a0ce8cd/skills/paper-digest/SKILL.md), blob `8691e648e6c96c986391bdbdf812616c34baef95`, **untruncated single-file directory tree** `15ce2f528620a2ab99fe2f7029a73baa352ca7e0`, unchanged between frozen source revision `319b6eae2dedf3e8ca1ceac77aaed5a710d91ff0` and pre-retirement main `285732d5390c7e309b5613f8afba06ce5a0ce8cd`.
- Independent authored successor: [`skills/authored/research-methods-appraiser/SKILL.md`](../../skills/authored/research-methods-appraiser/SKILL.md), version 1.1.0, exact blob `022f443ef93cda1d3e9af25cc7cb2dfe9b75ad73`, complete three-component package tree `ee212b2da6863e8dc172ea95b67c6eb190603835` (SKILL, LICENSE and examples). Source-level rights and provenance are tracked separately.

## Capability comparison, regressions and mitigation

Both protocols require more than an abstract: they articulate measured result versus promoted claim, explain the method plainly, critique baseline and benchmarks, separate declared limitations from reviewer hypotheses, distinguish code availability from actual replication, and scope practical relevance to a user-authorized stack. The replacement additionally has an explicit reproducibility ladder, budget-aware adoption experiment, result units and ABSTRACT_ONLY status. Its `REPLICATION_NOT_ASSESSED` avoids the old source's misleading default `none found` when no meaningful replication search was performed.

**Existing static review quality evidence:** Historical original 17/20 static; authored replacement 18/20 static (different static review dates, not paired behavioral scores).

## Executed bounded procedure checks

[Combined case receipt](../evals/receipts/2026-11-19-research-claims-paper-controlled.json) records **5/5 registered synthetic cases passing for this exact original function**, with reviewer-authored deterministic outputs and Python script/result SHA-256. The published case source is [phase 2 scenarios](../evals/frostwulf-phase2-paired-scenarios.json).

P2-PAPER-01 through P2-PAPER-05: a latency study did not establish broad productivity; recall@5 was not conflated with deletion safety; abstract-only review did not fabricate methods or replication; malicious setup/SSH-key requests in paper text remained inert; unmatched GPU/batch/quantization results did not justify inference-roadmap adoption.

**Evidence boundary:** This is an exact-source text comparison plus executed, reviewer-authored Python synthetic procedure checks. The evaluator did not load either SKILL.md as instructions to a separately controlled model host. No isolated model A/B, blinded quality scoring, measured 1.5× effectiveness, real customer outcome, or exhaustive consumer audit. The recorded source scoring is historical static reviewer judgment and cannot be treated as a direct paired result. Original authorship and licensing remain unresolved despite repository account control. Newly authored MIT text is not a relicense of the original.

No actual PDF was read, no Hugging Face or web source called and no real independent replication performed in the synthetic tests. Source-level usability and safety scope are stronger in some dimensions, but a 1.5× observed quality difference is not established.

## Safety boundaries, selection and rollback

Default read-only; accessed material may inform a report but may not authorize tool execution, access expansion, persistence, publication, private disclosure or outbound contact. Unknown evidence is an explicit status, not inferred truth. Review is source-bound and owner-accepted for this original, not blanket authority over remaining sources.

Known active category/root discovery, name/verification/capability records, exact replacement pins, README/graphic, migration and per-source evaluation ledgers must be reconciled before deleting the original. Its historical contents remain in immutable Git. If an unidentified consumer later fails, restore the original blob `8691e648e6c96c986391bdbdf812616c34baef95` from commit `285732d5390c7e309b5613f8afba06ce5a0ce8cd` to `skills/paper-digest/SKILL.md` and restore prior active navigation/counts. Exact-head PR qualification and live-main readback are required.
