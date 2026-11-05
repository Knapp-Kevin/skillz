# Capability browse improvement: eight governed IDs, fifty study-only methods (2026-11-05)

**Issue:** [#588](https://github.com/Knapp-Kevin/skillz/issues/588). **Implemented** in `registry/capability-directory.json` at commit `fc1845d9357f1f89b41bfd55dea60dd7d3bb6f1c`. The previously unmapped review IDs were read and matched to their exact pinned upstream `SKILL.md` Git blobs and existing `registry/verification/<id>.yaml` + `registry/skills/<id>.yaml` companions before creating evidence-based links.

## Eight newly mapped governed IDs

| Source ID / skill | Exact SKILL.md Git blob | Evidence-backed capability path | Existing semantic state | Important restriction |
|---|---|---|---|---|
| `anthropic-skills/algorithmic-art` | `634f6fa42e4e697fa6afd293acd7fb8246574876` | `illustration/digital-traditional-media` | verified 17/20 | p5.js runtime; package-local Apache-2.0 license was read at `skills/algorithmic-art/LICENSE.txt`, blob `4f881c52d1f72f4cfb720e339e2d35c3058d01a9`; no new security or host behavior pass |
| `jwynia-agent-skills/game-facilitator` | `1c1d51e56fd71a28add191966f4edb2d8cd570c9` | `game-design/tabletop-games` | rejected 13/20 | Unauthorized campaign canon mutation in unchanged instructions |
| `jwynia-agent-skills/interactive-fiction` | `956b8acba3618d49084cf08924911acf9fc1e841` | `game-design/narrative-design`; `fiction-narrative-worldbuilding/interactive-fiction` | verified 16/20 | Mutating/persistent artifacts need host-specific authorization; static review only |
| `microsoft-skills/azure-ai-transcription-py` | `a6fd15e733a567c832962e5c4dc71998cc2ebcde` | `audio-voice-sound/speech-voice` | rejected 11/20 | Remote audio disclosure, consent/recording law, cost and unpinned dependencies |
| `anthropic-skills/academy-guide` | `cefeaeb20cc29a803af0335d7c7155b066d8770f` | `education/learning-technology` | verified 17/20 | Claude Academy *course navigation*, **not** generic tutoring or lesson creation |
| `david-ondrej-skills/teach` | `4007a2b24d89340943d30f1d14eedfd2bd79238c` | `education/tutoring` | rejected 16/20 | Persistent teaching workspace writes lack separately authorized mutation gate |
| `anthropic-knowledge-work-plugins/review-contract` | `030204860ec70bf80254f9894721504df7c81bd5` | `law/contracts` | verified 18/20 | Playbook and qualified legal-review conditions govern actual reliance |
| `anthropic-knowledge-work-plugins/compliance-check` | `688d8c967870e6036c27e8fa2f1bc34ca5cf0896` | `law/regulatory-analysis` | rejected 10/20 | Static regulatory deadlines wrong/volatile; must retrieve jurisdiction-current law |

**No untrusted skill instructions were executed.** Existing semantic scores and rejected statuses were preserved; none received a new review grade, scanner pass, observed host validation, or unchanged-use approval. The crosswalk explicitly retains denied/held packages as *discoverable knowledge* rather than hiding failed reviews. Existing source license/provenance companions remain authoritative for rights.

## Curated methods, separate from governed identity mapping

All **50 previously accepted Q8 Valuable References** from `registry/consumer-positive-references-q8-20261103.json` are now attached to their exact matching domain/subdomain as `curated_q8_study_references`. They cover **33/33 domains**. A study record includes its exact source revision/blob, method, benefit, existing static candidate score and disposition, historic security gate, why unchanged use was held, and an explicit `unchanged_use_approved: false`.

These are **50 existing curated study-method links**, not 50 newly discovered/verified distinct skills, not a replacement for the 1,039 governed reviews, and not a claim of full source/domain maturity. The current featured security states remain 10 pass, 7 fail, 33 incomplete; 0 behavioral validations and 0 unchanged-use approvals.

## Actual before/after, verified after Git commit

| Measure | Before | After |
|---|---:|---:|
| Governed exact-version identities mapped to capability paths | 78 | **86** |
| Known governed denominator | 1,039 | **1,039** |
| Governed exact-version IDs still unmapped | 961 | **953** |
| Subdomains containing mapped governed IDs | 53 | **62** |
| Canonical subdomains | 247 | **247** |
| Curated Q8 method records in domain/subdomain browse | 0 in dedicated Q8 browse field | **50** |
| Domains with at least one Q8 study-method browse entry | 0 in dedicated Q8 browse field | **33** |

The full JSON is deliberately large because it is a read-only catalog, not a startup instruction: `registry/capability-directory.json`. A lightweight GitHub content reader may return an empty/truncated body for a file this large; fetch the full GitHub contents/raw representation before claiming it is empty. The indexed file's Git blob is `7cb6493472bd7d1c2b20ff7a7cb55abc00a2c9d0`.

## Remaining work

953 governed identities have no evidence-backed capability path yet. Some have name-only hints; those are not qualified mappings. Candidate-only sources remain a separate intake/vetting pool. Per-subdomain maturity still requires demonstrated breadth, independent evidence, freshness and actual usability, with stale/blocked flags separate; no domain is labelled mature merely because Q8 has a featured study method. The Tier 1/Tier 2 external SkillEvaluator evidence gate remains distinct and is not claimed complete. Do not close #588 on this tranche.
