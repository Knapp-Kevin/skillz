# Third-Party Notices

The root [`LICENSE`](LICENSE) applies to first-party material authored for this repository.

Third-party repositories and third-party material keep their own copyright and license terms. A reference source, dependency, or git submodule does **not** become MIT-licensed merely because it appears inside this MIT-licensed parent repository.

## Vendored reference sources

| Source | Repository | License status |
|---|---|---|
| Anthropic Skills | `anthropics/skills` | **Mixed.** Many example skills are Apache-2.0. Anthropic's document skills (`docx`, `pdf`, `pptx`, `xlsx`) are source-available under separate terms and are not open source. Consult the upstream repository and per-skill license files before copying or adapting. |
| Anthropic Knowledge Work Plugins | `anthropics/knowledge-work-plugins` | Apache-2.0 |
| Vercel Agent Skills | `vercel-labs/agent-skills` | MIT |
| Microsoft Skills | `microsoft/skills` | MIT |
| Microsoft Azure Skills | `microsoft/azure-skills` | MIT |
| AWS Agent Toolkit | `aws/agent-toolkit-for-aws` | Apache-2.0 |
| Matt Pocock Skills | `mattpocock/skills` | MIT, Copyright (c) 2026 Matt Pocock |

Each vendored git submodule retains its upstream license files and repository identity.

## Local adaptations

A local skill under `skills/` may be covered by the repository's MIT license when it is independently authored from general ideas or patterns.

If a local skill copies or materially adapts third-party text, code, distinctive structure, or other copyrightable material, the applicable upstream license obligations still apply to that material. Preserve required copyright, attribution, permission, NOTICE, or other terms alongside the local adaptation.

Record those relationships using [`docs/third-party-provenance.md`](docs/third-party-provenance.md).

## Reference is not relicensing

Reading another skill, comparing its design, or independently implementing a general method does not by itself change the license of independently authored first-party material. Conversely, calling something "inspired by" does not erase license obligations when substantial protected material was actually copied.

When licensing is unclear, treat the source as reference-only until its terms are established.
