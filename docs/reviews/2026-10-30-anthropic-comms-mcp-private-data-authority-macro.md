# Anthropic Skills: private-source and evaluation authority macro review

**Date:** 2026-10-30  
**Registered source:** `anthropics/skills` at `8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4`  
**Scope:** 19 existing pinned exact-version companion pairs screened for disposition/risk; two high-risk packages deeply inspected, including bundled instructions and evaluation implementation. Static semantic inspection only. No behavioral execution, security scan, source-pin movement, package edit or new source admission.

## Family map and selection

The registered Anthropic Skills family has **19 eligible first-class packages**, **19/19** individual provenance/verification pairs, **zero genuine static gaps**, and **zero denominator delta**. The Git-tree inventory contains **911 verification YAML and 911 provenance YAML** across the whole repository. Candidate-only records are separate from admitted source identities. No additional alias or nested package is counted in this family.

Existing family decisions before this review were **10 VERIFIED semantic only / 9 REJECT unchanged**. Risk clusters include private-source retrieval in company communications; model-backed MCP evaluation with private tool outputs, cost and retained reports; mutable external SDK documentation; executable upstream helpers; restricted package licenses; and browser/tool mutation. The latter clusters already have explicit rejections where applicable. This bounded pass concentrates on two false unchanged-use approvals, while retaining 17 existing decisions without claiming to re-execute or independently requalify them.

| Package | Exact package tree | Exact SKILL.md blob | Previous → current | Decisive boundary |
|---|---|---|---|---|
| `internal-comms` | `9869687dcf6deb6802ca88ac11e67b6f7278017a` | `56ea935b74f371bfeb4c7d3c19d5139df866e73b` | VERIFIED 15/20 → **REJECT unchanged 13/20** | Bundled 3P, company newsletter and FAQ guides direct broad Slack, email, Google Drive and calendar retrieval when tools are available; no independently approved account, audience, time, sensitivity, minimization or cross-audience disclosure boundary |
| `mcp-builder` | `b866bcfb57b780c10b587c7b543e871a91661ce0` | `8a1a77a47d141967b246adb4da4f91037578ff7d` | VERIFIED 16/20 → **REJECT unchanged 13/20** | Required evaluation phase and bundled evaluation guide invoke real MCP tools; source-owned `scripts/evaluation.py` passes question/tool-result context to external Anthropic inference and produces detailed reports, without separate approval for private reads, provider disclosure, budget or retention |

## Source-specific evidence

**Internal communications.** `skills/internal-comms/SKILL.md` instructs the host to load `examples/3p-updates.md`, `examples/company-newsletter.md`, `examples/faq-answers.md` or `examples/general-comms.md`. The first three are not merely formatting templates: they explicitly instruct collection from company Slack, email, Drive/documents and calendars, with the FAQ guide encouraging holistic company-wide reading. Tool availability and an instruction to draft an update do not authorize broad private-source access or disclosure into a wider audience. The general-comms template has an audience-clarification step, but that step does not govern the other three procedures. Preserve format discipline, evidence linking and concise writing as adaptation/checklist material.

**MCP builder.** The parent `SKILL.md` includes a Phase 4 evaluation requirement; `reference/evaluation.md` requires direct read-only exploration and solving tasks against an MCP server. Read-only here constrains mutation, not confidentiality or paid API use. The bundled `scripts/evaluation.py` uses `Anthropic().messages.create` with task questions and tool results, prints task questions, and builds an answer/feedback report. It can transmit private service data to a model provider and incur inference charges; the package does not require action-specific approval of source accounts/fields, provider, budget, minimization or report destination/retention. It is **source-owned upstream tooling**, not repository-owned runtime. Preserve design patterns, MCP security guidance, tool schema methods and bounded evaluation-question construction.

## Systemic synthesis

The shared failure is **availability or read-only labeling being mistaken for private-data and external-inference authority**. A requested written deliverable does not automatically authorize rummaging through every connected company source. A non-destructive MCP tool does not authorize disclosure of its output to a separate model provider, paid calls or durable report storage.

For unchanged use, an adapted host procedure must establish approved source/workspace/time/data fields and recipients; use minimum-necessary reads; distinguish private context from publishable output; approve external inference provider, cost and retention separately; and fail closed if the needed scope cannot be established. This is a proposed adaptation boundary, not a claim that the pinned packages were modified or behaviorally validated.

## Accounting and lifecycle

Anthropic Skills: **19/19** static reviewed, **10 VERIFIED / 9 REJECT → 8 VERIFIED / 11 REJECT**. Two existing verification records and two provenance records refreshed; **0** new review identities, **0** admitted-source denominator change. Public accounting remains **44 first-party / 867 third-party / 911 total**, with **911/911** persisted companion pairs. No candidate admission, new scanner evidence, behavioral validation or source pin changes. Existing first-party repair and admission PRs remain governed by their own external qualification holds. All five public surfaces were reconciled in this tranche.
