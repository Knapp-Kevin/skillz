# Capability quickstart: start with useful outcomes

**Purpose:** A short, populated shelf of **actual indexed skill examples**, followed by a complete name-search fallback. This is a **discovery aid**, not a source-ownership ranking, a list of install-approved packages, or a claim to cover the ecosystem.

If the user only shared the repository and said **“take a look”**, first deliver the [memory-grounded value brief](agent-value-discovery.md). Use this page to turn those needs into concrete candidate files. If they already named a capability, skip the full interview and search directly.

## Start from a task, not a source

| What the agent needs to do | Actual repository examples | Evidence and caution |
|---|---|---|
| Verify a consequential claim before reporting it | [Fact Check](../skills/fact-check/SKILL.md) | [First-party exact-version static verified](../registry/verification/local-skills/fact-check.yaml); behavioral `not-run` |
| Learn from a failed agent run | [Agent Postmortem](../skills/agent-postmortem/SKILL.md) | [Static verified](../registry/verification/local-skills/agent-postmortem.yaml); report/propose only |
| Recover relevant decisions across sessions | [Session Continuity](../skills/session-continuity/SKILL.md) | [Static verified](../registry/verification/local-skills/session-continuity.yaml); host-memory dependent; durable writes require authorization |
| Review code quality or a specification | [Code Review and Quality](../registry/verification/addyosmani-agent-skills/code-review-and-quality.yaml); [Code Review](../registry/verification/mattpocock-skills/code-review.yaml) | Both third-party **static verified**; review actual package, host fit, license, security; behavior `not-run` |
| Investigate a repository's problems | [Repo Doctor](../skills/repo-doctor/SKILL.md); [TODO Harvester](../skills/todo-harvester/SKILL.md) | First-party [Repo Doctor review](../registry/verification/local-skills/repo-doctor.yaml) and [TODO Harvester review](../registry/verification/local-skills/todo-harvester.yaml); no autonomous mutation implied |
| Produce traceable API documentation | [Authoring API Reference](../registry/verification/bm629-agent-skills/authoring-api-reference.yaml) | Third-party **static verified**; bundled references matter; publication and live API requests are separately gated |
| Produce a compact decision brief or investigate a subject | [Brief Writer](../skills/brief-writer/SKILL.md); [Deep Dive](../skills/deep-dive/SKILL.md) | First-party [brief evidence](../registry/verification/local-skills/brief-writer.yaml) and [research evidence](../registry/verification/local-skills/deep-dive.yaml); no claim of executed validation |
| Create a reliable handoff for another agent | [Handoff Writer](../skills/handoff-writer/SKILL.md) | [Static verified](../registry/verification/local-skills/handoff-writer.yaml); doesn't authorize modifying persistent state |
| Reduce authorization or MCP integration risk | [Permissions Review](../skills/permissions-review/SKILL.md); [MCP Vetting](../skills/mcp-vetting/SKILL.md) | First-party [permissions](../registry/verification/local-skills/permissions-review.yaml) and [MCP vetting](../registry/verification/local-skills/mcp-vetting.yaml) evidence; read-only reviews |
| Improve search-engine discoverability | [SEO Audit](../registry/verification/corey-haines-marketing-skills/seo-audit.yaml) | Third-party **static verified**, read-only SEO evaluation; website changes need separate approval |
| Develop a fiction setting or plot | [Worldbuilding](../registry/verification/jwynia-agent-skills/worldbuilding.yaml); [Plot Structure](../registry/verification/danjdewhurst-story-skills/plot-structure.yaml) | Both third-party **static verified**; source terms and any mutating operations still matter |
| Evaluate career options | [Career Radar](../skills/career-radar/SKILL.md) | [Static verified](../registry/verification/local-skills/career-radar.yaml); relies on current accessible market sources |
| Plan a presentation | [Deck Outline](../skills/deck-outline/SKILL.md) | [Static verified](../registry/verification/local-skills/deck-outline.yaml); outline is not an exported deck |
| Assess a software release or browser UI | [Release-readiness reference](../registry/verification/aws-agent-toolkit/analyzing-release-readiness.yaml); [Browser-testing reference](../registry/verification/addyosmani-agent-skills/browser-testing-with-devtools.yaml) | Both **rejected unchanged** on authority/safety grounds. Useful reference ideas, **not approved installs** |
| Find task/skill overlaps in an existing user system | [Task Surface](../skills/task-surface/SKILL.md); [Week in Review](../skills/week-in-review/SKILL.md) | First-party static review only; write/approval boundaries differ by host |

**Key distinction:** an existing exact-version review is not an install permit. `verified` above refers to **static semantic review**, not a security scan, behavioral test, distribution license or compatibility assurance. The third-party links point to evidence companions; read the companion's full package path, provenance, license/NOTICE obligations and its specific security context before adoption. These examples are not ranked by authorship.

## Find beyond these examples

1. **Browse [the capability directory](../registry/capability-directory.json)** by domain → subdomain. Its `matched_skill_ids` are evidence-linked seed examples; `name_only_review_candidate_ids` are **uninspected name-token leads** from the reviewed-record index. Those leads may be rejected, candidate-only or semantically irrelevant. An empty list is **unknown coverage**, never absence.
2. **Search [all 1,039 governed review companion names](../registry/governed-review-name-index.json)**, including 44 first-party and 995 third-party records. For an ID `source/skill`, read `registry/verification/source/skill.yaml` and `registry/skills/source/skill.yaml`. Use task synonyms, not just exact filename.
3. **Expand to [pinned dynamic discovery manifests](../registry/discovery/dynamic-four-source-frontier-20261101.json)** when governed records don't cover the task. These are wider unqualified `SKILL.md` path/blob leads, **not** verified or reusable packages. No fixed count is the product's success criterion.
4. **Decide with the [consumer contract](consumer-discovery-and-installation.md)** whether existing host capabilities suffice, whether safe and licensed reuse/adaptation is justified, or whether independent creation is better. Reading a candidate is not activating it. Only a separate authorized installation changes the user's host.

A cold agent with no memory can still name concrete **provisional examples** from the table and distinguish them from user-specific fit. An agent with memory should rank examples against *observed repeated work, error-prevention needs, existing skills and host capabilities*, not invent a profile. The output for a vague first look is the value brief itself, **not an offer to provide one later**.
