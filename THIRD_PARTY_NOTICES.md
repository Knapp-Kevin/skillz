# Third-Party Notices

The root [`LICENSE`](LICENSE) applies to first-party material authored for this repository.

Third-party repositories and third-party material keep their own copyright and license terms. A reference source, dependency, or git submodule does **not** become MIT-licensed merely because it appears inside this MIT-licensed parent repository.

## Vendored reference sources

| Source | Repository | License status | Pinned revision when recorded |
|---|---|---|---|
| Anthropic Skills | `anthropics/skills` | **Mixed.** Many example skills are Apache-2.0. Anthropic document skills may use separate source-available terms. Consult upstream and per-skill license files before copying or adapting. | gitlink is authoritative |
| Anthropic Knowledge Work Plugins | `anthropics/knowledge-work-plugins` | Apache-2.0 | gitlink is authoritative |
| Vercel Agent Skills | `vercel-labs/agent-skills` | MIT | gitlink is authoritative |
| Microsoft Skills | `microsoft/skills` | MIT | gitlink is authoritative |
| Microsoft Azure Skills | `microsoft/azure-skills` | MIT | gitlink is authoritative |
| AWS Agent Toolkit | `aws/agent-toolkit-for-aws` | Apache-2.0 | gitlink is authoritative |
| Matt Pocock Skills | `mattpocock/skills` | MIT, Copyright (c) 2026 Matt Pocock | `6654f6b60cd9d5be8b54c6fafe44346dabeb3b76` |
| Addy Osmani Agent Skills | `addyosmani/agent-skills` | MIT, Copyright (c) 2025 Addy Osmani | `f63ec56a3cc936408d792956ae583c3c96a825bd` |
| OpenHands Extensions | `OpenHands/extensions` | MIT | `87959a7da3e75445647e77b2fbf5bf5b66fb037b` |
| Cline Skills | `cline/skills` | Apache-2.0 | `26378461e978f2b4e2e6d67b57121b86b2a79ba5` |
| Cloudflare Skills | `cloudflare/skills` | Apache-2.0 | `f96bff754e428838818017f75817f0f9428acd48` |
| Google Agents CLI | `google/agents-cli` | Apache-2.0 | `ef7808f33fc3038112b69d4ad488ce33b72699b1` |

Each vendored git submodule retains its upstream license files and repository identity. The source registry records the intended role and quality-default policy for each source.

## Tracked reference sources

These sources are referenced for standards or discovery without being vendored into the repository:

| Source | Repository | License | Snapshot used for current review | Role |
|---|---|---|---|---|
| Agent Skills Specification | `agentskills/agentskills` | Apache-2.0 | `69ef37e9424c0a7ea9dd2293b559e43ec8176379` | normative specification |
| GitHub Awesome Copilot | `github/awesome-copilot` | MIT | `f11a4e441c5ff061b4f8ae37952be8c602e4034e` | dynamic discovery/comparison |

Tracked discovery does not imply endorsement, redistribution, or verification of individual contributions.

## Local adaptations

A local skill under `skills/` may be covered by the repository's MIT license when it is independently authored from general ideas or patterns.

If a local skill copies or materially adapts third-party text, code, distinctive structure, or other copyrightable material, the applicable upstream license obligations still apply to that material. Preserve required copyright, attribution, permission, NOTICE, or other terms alongside the local adaptation.

Record those relationships using [`docs/third-party-provenance.md`](docs/third-party-provenance.md).

## Reference is not relicensing

Reading another skill, comparing its design, or independently implementing a general method does not by itself change the license of independently authored first-party material. Conversely, calling something "inspired by" does not erase license obligations when substantial protected material was actually copied.

When licensing is unclear, treat the source as reference-only until its terms are established.
