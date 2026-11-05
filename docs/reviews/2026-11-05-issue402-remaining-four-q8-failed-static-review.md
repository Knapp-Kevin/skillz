# Issue #402: the remaining four failed Q8 featured packages

**Direct static-source review on November 5, 2026.** This is a bounded exact-version review under [static content and freshness governance](../static-review-and-freshness.md), not execution, installation, a new SkillSpector run, a behavior test or an independent signature verification.

**Machine-readable complete-package and shared-reference identities:** [four-package static disposition ledger](../../registry/security/remaining-q8-four-failed-static-dispositions-20261105.json). Paired with the [preceding three-package review](2026-11-05-issue402-three-third-party-failed-static-review.md), **all 7/7 historically FAILED Q8 featured packages have now been independently reviewed as pinned static content**. No source has been approved for unchanged adoption.

## Results

| Exact pinned skill | Direct-owned files read | Static score | Current recommendation |
|---|---:|---:|---|
| [Scenario Storyboards](https://github.com/scenario-labs/skills/tree/7f4b801c7248d51b093ec365aceb114bd06139e6/skills/scenario-storyboards) | 1 | 11/20 | Study only; paid image generation/upload held |
| [Scenario Identity Library](https://github.com/scenario-labs/skills/tree/7f4b801c7248d51b093ec365aceb114bd06139e6/skills/scenario-identity-library) | 1 | 11/20 | Study only; likeness uploads/remote mutation held |
| [Geospatial and Cartographic Visualization](https://github.com/openai/plugins/tree/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/build-web-data-visualization/skills/geospatial-and-cartographic-visualization) | 11 | 16/20 | Study only; licensing and provider/privacy authority held |
| [Dynamo Interconnect Check](https://github.com/openai/plugins/tree/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/nvidia/skills/dynamo-interconnect-check) | 8 | 10/20 | Hold execution; live cluster access and false-clear verdict risk |

These four packages total **21 exact owned files** and the geospatial review additionally read **5 repository-root shared foundation documents** referenced outside its own package. The Scenario upstream root MIT LICENSE and the two OpenAI plugin manifests were read separately as source terms. Each pinned package Git tree was resolved directly from the corresponding upstream commit. These are source-review fingerprints, **not proof of executable or live agent behavior**. Historical Q8 scanner verdicts remain **FAILED**, including findings which a human reader can now characterize more precisely.

## Scenario Storyboards

**Pinned source:** `scenario-labs/skills@7f4b801c7248d51b093ec365aceb114bd06139e6`, package tree `b0b029258172a8a46a5e9187306e1606fa0585f5`; `SKILL.md` blob `9275b402c74f0165c1ea8c5a2ca3764cf327f367`. The root MIT LICENSE applies to Scenario-authored material, not necessarily user-supplied likenesses, images, output models or third-party assets.

The reported scanner `P9` “Whitespace Padding” at `SKILL.md:23` is part of an ordinary Markdown quick-reference table. Static inspection finds no covert command at that location, but **no formal scanner reclassification or new PASS has occurred**.

**Actual blockers:** The procedure authorizes a noninteractive fallback where a prompt description stands in for user approval of a character; then it selects a model and issues a sequence of `model_run` operations without an explicit bounded service-cost gate. It can upload reference art and persist panel collections without a specific user-approved destination, asset scope or retention agreement. It also recommends changing a moderation-blocked combat panel and retrying; any retry must comply with applicable safety constraints, not route around them. Named sibling skills remain outside this exact one-file review.

**Reusable technique:** Storyboard as a shot-by-shot beat table; preserve character baselines and camera geography; separate readable text overlay from art. These concepts can be expressed independently without installing Scenario tools or paying for generation.

## Scenario Identity Library

**Pinned source:** same upstream revision, package tree `d514d323fcd601d43551250e38809862d294e719`, `SKILL.md` blob `e36509de1f00a9b4114b437ae53f1c4b689b8c23`.

The historical `P9` matched another Markdown table. The same scanner-status distinction applies.

**Actual blockers:** A user-supplied drawing or personal photo is treated as a cloud-upload anchor without separately bounding where private likeness data will be transmitted. `collection_create`, `collection_add_assets` and `collection_remove_assets` alter persistent vendor state, potentially deleting or replacing existing collection members during redesign. The procedure does not establish item-by-item authorization, rollback or namespace isolation for these operations. Paid models and unreviewed sibling tools are additional constraints.

**Reusable technique:** Write a stable character/prop description and a named set of approved viewpoints; compare new images against the baseline before treating them as canonical. Keep planning read-only unless authorized to upload or mutate external collections.

## Geospatial and Cartographic Visualization

**Pinned source:** `openai/plugins@0722921d5542fc593105c27bd52630babd8b8c2a`, package tree `420de6234f1d7b9fb180e6072303a392655577d9`, `SKILL.md` blob `51b926ba198cf89b4776a483de5534f596a4521e`.

**Important reference correction:** The five shared foundation files formerly described as missing **do exist at the pinned plugin repository root** under `plugins/build-web-data-visualization/references/foundations/`, and were directly inspected. They were merely outside the one-skill tree supplied to the historical scanner. Existence and content review resolve that narrow source-reference uncertainty, but **do not convert the original historical scan into PASS**. Another ten material owned files are in the pinned complete package along with `SKILL.md`; exact fingerprints are in the machine ledger.

The scanner's `AR2` “Anti-Refusal Statement” at `references/deckgl-d3-geo-stack-selection.md:25` matches a caution against animated depictions of sensitive human movement without caveats, static fallback and restraint. That is not a refusal-bypass instruction. The previous `failed` state is preserved.

**Actual blockers:** The plugin manifest declares MIT, but the pinned repository root does not contain full LICENSE terms, so protected-text copying/redistribution remains unverified. Recommended services can incur provider charges and disclose coordinates, geolocation, camera or search data. A map-design request alone does not authorize vendor account use, location transmission or paid APIs. Other sibling references remain individually governed.

**Reusable technique:** Choose map versus chart by analytical purpose; keep coordinate systems, attribution, time and uncertainty in a visible source ledger; use responsive and low-bandwidth fallbacks. Do not copy protected source-specific text without resolving rights.

## NVIDIA Dynamo Interconnect Check

**Pinned source:** `openai/plugins@0722921d5542fc593105c27bd52630babd8b8c2a`, package tree `24748c47b449ad8081ba50063ca70f1907f775f0`, `SKILL.md` blob `a9c9d46228fed0439b76ed74d36fd128358c5f1f`. All eight owned files, including `scripts/check_interconnect.py`, `BENCHMARK.md`, `skill.oms.sig`, references, interface YAML and eval cases, were inspected **as static content only**.

The historical scanner findings `MP3`, `AS3`, `LP3` and `AST4` are **not dismissed wholesale**. Mentions of KV cache or skill benchmarking are not themselves evidence of memory poisoning, but the Python script really does call `subprocess.run` and `kubectl exec` and reads recursively under a caller-specified manifest directory. “Read-only” does not supply cluster authorization or guarantee that values logged from transport environments are safe to disclose.

**Concrete correctness defect:** `summarize()` counts `ok`, `warn`, and `fail`, but not `skipped` or `unknown`. With essential tests skipped and other checks returning OK, it can report **“no transport gaps detected by read-only checks”** without actually proving NIXL cross-pod transfer. This is a source-code risk finding, not a demonstrated live exploit. Require a fail-closed `inconclusive` outcome for missing essential probes and a real pairwise transfer before trust in high-consequence inference-readiness decisions.

**Other holds:** `kubectl exec` against production-like pods and recursive YAML reads require explicit cluster context, namespace, pod and content scope, plus safe output handling. The bundled `BENCHMARK.md` claims overall PASS despite no available Tier 3 live-agent record; it cannot justify behavioral validation. A bundled signature exists, but its chain and artifact digest were **not independently verified**. The plugin declares Apache-2.0 for code and CC-BY-4.0 for prose; source copying/redistribution requires terms and attribution verification.

## Exact-content freshness and remaining backlog

At this review checkpoint the Scenario upstream HEAD is **seven commits beyond** the deliberately pinned revision and `openai/plugins` is **one commit beyond** its pin. The upstream comparison returned no changed paths for these four selected packages and inspected shared foundation files. The pinned content was not silently updated; its direct review remains current for that exact content, while future source changes require a new decision. Do not call a pinned review stale merely because upstream develops further.

| Status | Count |
|---|---:|
| Historically FAILED Q8 featured packages with new direct static review evidence across both November 5 tranches | **7/7** |
| Historically INCOMPLETE Q8 featured packages still needing separately scoped risk/freshness adjudication | **33** |
| New scanner passes or behaviorally observed approvals | **0** |
| New unchanged-use authorizations | **0** |

The remaining #402 work is **not** satisfied by correcting these seven bounded findings. It includes the 33 historically incomplete Q8 featured packages, additional in-scope governed third-party identities and content changes, and any credible unresolved security findings. Next prioritize packages with actual credential, filesystem, network, privileged process, cloud, or exfiltration consequences. Treat reference-only study as distinct from copying or installation.
