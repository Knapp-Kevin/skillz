# Exact-reviewed technical documentation and UX capability crosswalk
Date: November 9, 2026

**Outcome:** The existing canonical capability directory now indexes **14** additional exact-pinned third-party `bm629/agent-skills` identities across **20** narrowly justified capability links. These skills remain third-party, live at their upstream repo, and are not copied into `skills/authored/`.

The previous structured static dispositions were **11 verified and 3 rejected unchanged**. These were NOT regraded and do NOT establish real-world agent behavior. [Machine-readable Git source and review receipt](../../registry/discovery/bm629-14-exact-source-technical-ux-routing-20261109.json).

## Pinned review identities and destinations

| Exact identity | Prior decision | Capability subdomain route(s) | SKILL.md Git blob |
|---|---|---|---|
| `bm629-agent-skills/authoring-user-guide` | VERIFIED 17/20 | `technical-writing/tutorials`, `technical-writing/reference-manuals` | `d2e35d05eb06fbec0981fb48b265dbb814f946ee` |
| `bm629-agent-skills/reviewing-user-guide` | VERIFIED 17/20 | `technical-writing/tutorials`, `technical-writing/reference-manuals` | `118b10b741fd73ac4588ab843e79cf024a4f2004` |
| `bm629-agent-skills/authoring-developer-guide` | VERIFIED 16/20 | `technical-writing/tutorials` | `b398179bc8f486917276d24d2e51ff3bc3ab41db` |
| `bm629-agent-skills/reviewing-developer-guide` | VERIFIED 18/20 | `technical-writing/tutorials` | `e03ef02d32aa5a473957156eaac5f75c22f6a70f` |
| `bm629-agent-skills/authoring-architecture-doc` | VERIFIED 16/20 | `technical-writing/architecture-records`, `software-engineering/architecture` | `a725d42406117d81e231a70415188236d5eb6feb` |
| `bm629-agent-skills/reviewing-architecture-doc` | VERIFIED 17/20 | `technical-writing/architecture-records`, `software-engineering/architecture` | `2cbafdf0b8ca06ead40c71518f58eaaeb8f16b26` |
| `bm629-agent-skills/authoring-technical-design` | VERIFIED 17/20 | `software-engineering/architecture` | `b5f414c338aca6b429c2f8fd2cbe9594622e905c` |
| `bm629-agent-skills/reviewing-technical-design` | VERIFIED 17/20 | `software-engineering/architecture` | `52a4eae308b86f89970e0b70d891dc5b489d8e45` |
| `bm629-agent-skills/authoring-design-system` | VERIFIED 16/20 | `ux-ui/design-systems` | `4fcb71f77d443023668b76a8a9237ad1821cb3c6` |
| `bm629-agent-skills/reviewing-design-system` | VERIFIED 16/20 | `ux-ui/design-systems` | `810f7c2fe684cba14022852f46c5d7a097818fa5` |
| `bm629-agent-skills/authoring-hi-fi` | REJECTED 14/20 | `ux-ui/prototyping` | `ea345e3e371a709f682b9f1e84227eb421b4fbfe` |
| `bm629-agent-skills/reviewing-hi-fi` | REJECTED 14/20 | `ux-ui/prototyping` | `3bacaaf008a3e48954b80db3099e783f687b5abb` |
| `bm629-agent-skills/user-research-prior-art-survey` | REJECTED 14/20 | `ux-ui/user-research`, `research/literature-review` | `b118c3444df28405daf2d8ab579f25e5d49cc8f6` |
| `bm629-agent-skills/reviewing-user-research-prior-art-survey` | VERIFIED 15/20 | `ux-ui/user-research`, `research/synthesis` | `69de5c70be0157135ab0583a5df7563c0b25bc99` |

## Source restrictions, not silently promoted

- `authoring-hi-fi`: **REJECT unchanged**. Existing static review found mandatory code generation and headless rendering with insufficiently bounded network, sandbox, private content and screenshot/output controls.
- `reviewing-hi-fi`: **REJECT unchanged**. Mandatory independent code rendering and screenshots lacked adequate isolation, egress and disclosure limits.
- `user-research-prior-art-survey`: **REJECT unchanged**. Required external research queries were not sufficiently gated against disclosure of private or sensitive product/user information.
- Eleven **VERIFIED** records are static-content decisions, not proof of host behavior, permission to execute code, release user data, write project files or contact services. The source and license terms apply independently.

## Count reconciliation and limits

- The governed review-name denominator is unchanged at **1,042**. The directory's **107 → 121** exact-reviewed mapped identities and **935 → 921** unmapped identities reflect only new crosswalk links.
- First-party mapped remains **47**. Third-party mapped becomes **74**. Distinct source identities added: **14**, mapping routes added: **20**, subdomains linked by exact-review evidence **68 → 74 of 247**.
- No new domains, local packages, first-party authored content, Q8 study references, security scanners, independent original rubric grades, host behavioral validations, approved unchanged installations or licensing permissions.
- All **14 exact pinned source `SKILL.md` blobs** were read. Supporting package-file review evidence is inherited **only as historical prior static review**, not a claimed fresh package re-review. Upstream `main` drift beyond the pinned snapshot was not checked.

## Public outputs

The README's [live capability graphic](../assets/current-capability-mapping.svg) is regenerated from `registry/capability-directory.json` using the [existing renderer](../../scripts/build-current-routing-graphic.mjs). The **prior graphic was byte-compared against this exact renderer** before generating the new one. Other dated, different-scope research and scanner graphics remain historical and are not conflated with current source mapping.

## Exact Git identity verification (pinned upstream tree)

Fetched the **GitHub tree at `f6a700ea94a16cf8e0b5e563d4d48d85503e41f6`**, then checked every listed `skills/<slug>/SKILL.md` Git blob and every entire package subtree SHA. **14/14 SKILL.md blobs match, 14/14 package trees match, zero mismatches, tree not truncated.** This proves source-pin consistency, **not** that the upstream's latest head is unchanged or that the prior static rubric was rerun.
