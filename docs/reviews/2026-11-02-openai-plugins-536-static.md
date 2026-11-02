# OpenAI Plugins: all 536 pinned paths at current standard (2026-11-02)

**Source:** `openai/plugins` at `0722921d5542fc593105c27bd52630babd8b8c2a`. There is no root license; terms are declared per plugin in `.codex-plugin/plugin.json`.
**Scope:** source-vetting candidate decisions only. No admission, governed review, security scan, behavioral validation or installation.

## Coverage

This tranche covers all 502 direct paths and all 34 nested or internal skills, each reviewed with its plugin manifest. Exact package records are in the [ledger](../../registry/discovery/openai-plugins-536-current-standard-static-20261102.json), and the [capability index](../../registry/discovery/openai-plugins-capability-index-20261102.json) lists them by domain and subdomain.

| Measure | Before | After |
|---|---:|---:|
| OpenAI Plugins current-standard exact-path decisions | 0 / 536 (41 historical candidate-only matches) | **536 / 536** |
| Four-source current-standard exact-path decisions | 3,718 | **4,254 / 4,813** |
| Raw paths without a current-standard decision | 1,095 | **559** (j4flmao 555; AgentSkillExchange 3 DEFER + 1 template) |

Results: **422 REFERENCE-ONLY / 114 REJECT unchanged**, 0 DEFER. **92** packages meet the static threshold signal; this is not verification, and rights-restricted plugins are excluded from it.

The 41 historical candidate-only matches were re-reviewed independently. Each record carries `historical_candidate_record` for traceability; the historical grades were not reused.

## Largest plugin families

| Plugin | Paths | REFERENCE-ONLY | REJECT |
|---|---:|---:|---:|
| `twilio-developer-kit` | 55 | 51 | 4 |
| `vercel` | 54 | 34 | 20 |
| `zoom` | 53 | 43 | 10 |
| `life-science-research` | 50 | 47 | 3 |
| `public-equity-investing` | 23 | 23 | 0 |
| `shopify` | 20 | 2 | 18 |
| `ngs-analysis` | 18 | 18 | 0 |
| `build-web-data-visualization` | 18 | 18 | 0 |
| `data-analytics` | 18 | 14 | 4 |
| `codex-security` | 15 | 15 | 0 |
| `superpowers` | 14 | 12 | 2 |
| `expo` | 13 | 11 | 2 |
| `nvidia` | 12 | 5 | 7 |
| `remotion` | 12 | 6 | 6 |

## Hard-fail flags

| Flag | Packages |
|---|---:|
| `unauthorized-consequential-action` | 47 |
| `self-update-or-remote-code` | 18 |
| `private-data-egress` | 18 |
| `embedded-agent-instruction` | 6 |
| `secret-logging` | 5 |
| `license-conflict` | 3 |
| `credential-in-url` | 3 |
| `solicits-secret-in-chat` | 2 |
| `capability-content-mismatch` | 1 |

## Macro findings

- All 536 pinned SKILL.md paths across 36 vendor/partner plugin families were reviewed as packages by 26 parallel read-only reviewers, including 34 nested/internal skills treated as their own identities (parents noted) and plugin manifests (.codex-plugin/plugin.json, .mcp.json, .app.json). The 41 historical candidate-only exact matches were independently re-reviewed at current standard and cross-linked, not inherited.
- Rights: the repository has no root license; terms come from each plugin.json. 189 paths sit in plugins declaring Proprietary, UNLICENSED, vendor terms (Figma Developer Terms) or nothing; those are capped at reference/discovery use and never receive the static threshold signal. Most MIT/Apache-declared plugins ship no license text (notice unavailable). Two genuine conflicts (Apache-2.0 text shipped inside Proprietary-declared ChatGPT-app skills) and one unattributed near-verbatim copy of Anthropic documentation were flagged; MIT-declared plugins shipping Apache-2.0 text were recorded as permissive mismatches.
- Authority: 47 packages direct consequential vendor-account actions without per-action confirmation: production deploys/rollbacks and DNS/billing changes (Vercel CLI/API, Wrangler), Marketplace provisioning, live store mutations and checkout (Shopify CLI, UCP), Terraform -auto-approve and billable endpoints (NVIDIA physical-AI), message sends and number purchases (twilio-send-message, WhatsApp senders), shared-workspace edits and notifications (Notion, Mixpanel), automatic Sites publishing (data-analytics Work Mode), EULA acceptance on the user's behalf (Omniverse) and unconfirmed Zotero restarts.
- Privacy: 18 packages send private data without consent, most notably 11 Shopify skills whose mandatory search/validate scripts send the user's code, queries and agent identity to vendor telemetry by default (env-var opt-out only), audio/transcript egress and CAD uploads.
- Strong reusable gates exist and are recorded as salvage: Boltz fresh cost estimate + explicit go-ahead before each billable job, Adobe before/after preview-confirm, Dropbox confirm-before-action, Temporal list-then-approve, vercel-firewall stage-then-user-publishes, SendGrid/voice confirmation rules.
- Six embedded-instruction hard fails include a session-start skill that tells the agent to trust it over its own knowledge, instructions to conceal vendor/model identity and evade moderation (faceless-channel), and a locus-to-gene script that reports sources as queried when they were not (fabricated evidence).
- Quality: version-sensitive content drifts quickly (Shopify, Vercel, Zoom, Stripe, Expo); several plugins contradict themselves across sibling skills; many skills depend on plugin-level shared references, scripts or Codex-only host tools outside the package directory, which reviewers checked at the pin. 38 records honestly state partial coverage of very large generated/reference files.
- Quality controls: 21 integration overrides (3 permissive license mismatches cleared, 11 hard fails or REJECTs added by a four-way second pass over 253 REFERENCE-ONLY records with privacy/authority/rights notes, REFERENCE-ONLY floor, threshold withdrawals). 92 packages meet the static threshold signal; this is not verification.

## Coverage honesty

38 records state that some very large generated, reference or data files were characterised by structure and targeted scans rather than read line by line. The same honesty correction is applied retroactively to 11 records in the [Awesome Copilot ledger](../../registry/discovery/github-awesome-copilot-remaining-313-static-20261102.json), whose earlier scope text overstated full reading.

## Next

j4flmao: 555 packages are under review in 44 batches.
