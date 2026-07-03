# Agent Skills Long-List Research

## Purpose

This document is a broad horizon scan of reusable AI agent skills, skill collections, and adjacent capability modules for consideration. It is intentionally wider than the current engineering/governance scope so the repository can serve as a durable intake list before narrowing into evaluation, adoption, or product-opportunity decisions.

This is not an endorsement list. Most public skills are not independently evaluated. Treat every skill as an untrusted dependency until it has been reviewed, scoped, tested, and versioned.

## Working definition

An agent skill is a reusable capability package that gives an AI agent procedural knowledge, workflows, scripts, references, and guardrails for a specific class of work. In the Anthropic-style format, a skill is usually a folder containing a `SKILL.md` plus optional scripts, resources, examples, templates, or test assets.

Useful agent skills should provide one or more of the following:

- Repeatable workflow guidance.
- Deterministic checks or scripts.
- Project-specific or domain-specific constraints.
- Tool-use instructions.
- Verification procedures.
- Structured outputs.
- Reduced context burden through progressive disclosure.

Weak skills are often just vague markdown advice with no execution boundary, no tests, no version compatibility, and no clear trigger conditions.

## Source categories reviewed

The current ecosystem can be grouped into four discovery layers:

1. Official or vendor-backed ecosystems.
   - Anthropic Skills.
   - Vercel Agent Skills.
   - Microsoft Skills and Azure Skills.
   - AWS Agent Toolkit for AWS.

2. Marketplaces and directories.
   - Skills.sh.
   - MCP Market.
   - Awesome Claude.
   - Skills Directory.
   - Composio-style skill/plugin indexes.

3. Community collections.
   - Superpowers.
   - Matt Pocock skills.
   - Caveman skills.
   - Taste/UI/design skills.
   - Marketing and developer-relations collections.
   - Research and academic workflow collections.

4. Research and benchmark literature.
   - SWE-Skills-Bench.
   - Skill ecosystem/security analyses.
   - CUA-Skill.
   - SkillWiki-style provenance and lifecycle research.

## Top-level caution

The ecosystem does not yet have a universal quality metric.

Most directories rank by activity, installs, stars, or visibility. Those signals are useful for discovery, but they do not prove that a skill improves task success, safety, determinism, or maintainability.

Public research indicates that many software-engineering skills provide no measurable improvement on real-world tasks, and some can degrade performance when their advice conflicts with project context. This makes skill governance, evaluation, and scoping a first-class requirement rather than a nice-to-have.

## Strategic interpretation

The most important finding is not that there are many skills. The important finding is that skill ecosystems are becoming operational surfaces.

That creates a governance problem:

- Skills can encode policy.
- Skills can override project norms.
- Skills can trigger tool use.
- Skills can introduce outdated assumptions.
- Skills can carry malicious or careless instructions.
- Skills can create false confidence.
- Skills can bloat context.
- Skills can conflict with repo-level rules, `AGENTS.md`, `CLAUDE.md`, Cursor rules, MCP policies, or human decisions.

For Qortara, Bicameral, FailSafe, and related governance work, skills should be treated as versioned, auditable, testable artifacts.

---

# 1. Core agent-skill discovery, authoring, and governance

These are meta-skills: skills for finding, writing, auditing, improving, or managing other skills.

| Skill or collection | Use case | Evaluation notes |
|---|---|---|
| find-skills | Discover and install skills from the Skills.sh ecosystem. | Useful discovery layer. Needs allowlist and review gate. |
| skill-creator | Create new Anthropic-style skills. | Strong candidate for internal skill authoring. |
| write-a-skill | Authoring skills with repeatable structure. | Useful for standardizing in-house skill creation. |
| rules-distiller | Extract reusable rules from installed skills or project docs. | Product-relevant for governance and drift control. |
| agnix | Linter for agent configs, `SKILL.md`, `CLAUDE.md`, hooks, MCP configs, and related files. | Strong fit for agent-governance tooling. |
| Context Engineering Skills | Context engineering, multi-agent systems, production agent patterns. | Worth reviewing for memory/context architecture. |
| Claude Skills collections | Broad cross-domain skill packs. | Treat as untrusted until scoped and audited. |
| Agent Almanac | Large bundle of skills, agents, and teams across domains. | Good discovery input, not adoption-ready by default. |
| OpenPaw | Personal-assistant bundle with git, Telegram, Discord, Obsidian, briefings, and automation. | Useful outside coding, but requires permission hygiene. |
| claude-starter | Production Claude Code configuration template with auto-activating skills and token patterns. | Useful for comparing repo-level config patterns. |
| AgentSkills.io spec | Portable skill structure reference. | Useful for internal format decisions. |
| SkillWiki | Research direction for provenance-aware skill lifecycle and execution-driven evolution. | Strong product-opportunity signal. |

## Governance questions

- Does the skill declare when it should be used?
- Does it declare when it must not be used?
- Does it require tools, network access, secrets, or filesystem writes?
- Does it include scripts or only instructions?
- Does it conflict with repo-level rules?
- Can it be evaluated with before/after task success?
- Can it be versioned and pinned?
- Can it be signed or provenance-tracked?
- Can it be disabled by policy?

---

# 2. Coding workflow, planning, and agent discipline

These skills focus on slowing agents down, forcing planning, improving code review, and reducing chaotic implementation behavior.

| Skill or collection | Use case | Evaluation notes |
|---|---|---|
| Superpowers | Full agentic software-development operating method. | High value for complex tasks, heavy for small work. |
| brainstorming | Structured idea generation before implementation. | Useful when requirements are vague. |
| writing-plans | Convert intended work into executable implementation plans. | Good fit for planning gates. |
| executing-plans | Force plan-following discipline. | Useful if paired with verification. |
| test-driven-development | Red/green/refactor workflow. | Good if the repo has reliable tests. |
| subagent-driven-development | Delegate implementation/review across subagents. | Needs strong orchestration rules. |
| dispatching-parallel-agents | Parallel task execution. | High power, high coordination risk. |
| using-git-worktrees | Isolated branch/worktree workflows for agent work. | Strong for parallel coding agents. |
| finishing-a-development-branch | Cleanup and completion before merge or handoff. | Good pre-PR gate. |
| requesting-code-review | Structured review request creation. | Useful for human/agent handoff. |
| receiving-code-review | Handles review feedback systematically. | Useful for closing review loops. |
| systematic-debugging | Root-cause debugging before changes. | Very useful to prevent thrashing. |
| verification-before-completion | Requires verification before declaring done. | Strong governance fit. |
| handoff | Produces clear continuation context. | Strong for multi-agent or interrupted work. |
| to-prd | Turns ideas into product requirements. | Useful for product planning. |
| to-issues | Converts requirements/plans into implementation issues. | Strong GitHub workflow fit. |
| prototype | Rapid prototype workflow. | Useful when isolated from production paths. |
| diagnose | Diagnostic framing for unclear technical problems. | Good for triage. |
| zoom-out | Higher-level architectural/context review. | Useful when agents overfocus locally. |
| grill-me | Adversarial critique of a plan or implementation. | Very useful for decision hardening. |
| grill-with-docs | Critique grounded in project docs. | Better than generic critique. |
| request-refactor-plan | Requires plan before refactor. | Important for risky changes. |
| improve-codebase-architecture | Architecture improvement guidance. | Needs strong scope control. |
| ubiquitous-language | Domain language extraction and alignment. | Useful for product/domain modeling. |

## Evaluation priority

Adopt or test first:

1. verification-before-completion.
2. systematic-debugging.
3. writing-plans.
4. executing-plans.
5. handoff.
6. grill-with-docs.
7. to-issues.
8. test-driven-development.

---

# 3. Verification, QA, testing, security, and safety

This is the highest-overlap category for governance tooling.

| Skill or collection | Use case | Evaluation notes |
|---|---|---|
| Verification Loop | Multi-phase quality gate: build, type check, lint, tests, security scan, diff review. | Strong adoption candidate. |
| Verification Loops | Output verification, schema checks, graders, pass@k patterns. | Strong for agent eval design. |
| Santa Method Verification | Multi-agent adversarial review. | Useful, but needs cost/token control. |
| Security Review | Security audit across common web/app risks. | Strong candidate for pre-PR checks. |
| Bug Detection and Logic Review | Finds logic errors, race conditions, null references, async issues. | Good review augment. |
| Bug Review | Structured defect analysis and fix workflow. | Useful for bug triage. |
| Systematic Dev Debugger | Four-phase investigate/analyze/hypothesize/fix workflow. | Good against random-change behavior. |
| Writing Tests | Outcome-driven tests and edge-case coverage. | Useful when test framework is clear. |
| Go Testing Code Review | Table-driven Go test review, subtests, cleanup, idioms. | Language-specific. |
| Swift Testing Code Review | Swift Testing framework review. | Language-specific. |
| Spring Boot Verification Loop | Java/Spring build, tests, static analysis, Testcontainers, security. | Useful for enterprise Java stacks. |
| React Code Fix and Linter | Formatting/linting/CI compliance for React projects. | Useful for frontend hygiene. |
| AI Regression Testing | Regression detection for AI behavior changes. | Strategic for governed AI products. |
| Automated Compliance Auditor | Compliance-oriented review automation. | Needs policy grounding. |
| Advisor Brief Review and Verification | Verifies inbound advisor-agent briefs for authorized cross-agent coordination. | Product-relevant for agent networks. |
| Safety Guard | Guardrail/safety workflow category candidate. | Needs source review. |
| openclaw-secure-linux-cloud | Secure Linux/cloud workflow. | Useful if scope is clear. |
| sentry-cli | Sentry CLI diagnostics and observability. | Useful if connected to real Sentry setup. |
| full-output-enforcement | Forces complete output rather than lazy partials. | Useful for artifact completion. |

## Security review checklist for skills

Before adopting any skill in this category:

- Inspect all scripts.
- Inspect bundled resources.
- Check for external network calls.
- Check for secret handling.
- Check for destructive file operations.
- Check for dependency installs.
- Verify version compatibility.
- Run in a sandbox first.
- Record expected tool permissions.
- Add allow/deny policy.

---

# 4. Rust, systems, backend, and language-specific engineering

Relevant for systems-level projects, local inference runtimes, backend services, and compiled-language correctness.

| Skill or collection | Use case | Evaluation notes |
|---|---|---|
| Rust Best Practices and Patterns | Ownership, borrowing, safe concurrency, error handling, crate organization. | Strong GG-Core fit. |
| Rust Best Practices | Idiomatic, efficient, memory-safe Rust guidance. | Compare overlap with other Rust skills. |
| Rust Coding Standards | Clippy, ownership, borrowing, shallow nesting, standards enforcement. | Good style gate. |
| Rust Development Guidelines | Production Rust best practices. | Useful if not too generic. |
| Rust Development Best Practices | Naming, type safety, newtypes/builders, error handling. | Good modeling guidance. |
| Pragmatic Rust Development | Idiomatic Rust lifecycle guidance. | Useful for real-world constraints. |
| Rust Anti-Pattern Refactor | Finds excessive cloning, unsafe unwraps, inefficient structures. | Very useful for review. |
| Bevy Game Engine Development | ECS/game development patterns in Rust. | Niche, useful if Bevy appears. |
| Python Patterns and Best Practices | Pythonic idioms, PEP 8, modern type hints. | Useful for scripts/tooling. |
| Go Testing Code Review | Go test quality. | Useful for Go services. |
| Swift Testing Code Review | Swift Testing framework guidance. | Useful for Apple ecosystem. |
| Bun Runtime and Toolkit | Bun runtime, package, and test guidance. | Useful for JS tooling. |
| Coding Standards and Best Practices | Universal TypeScript/JavaScript/React/Node standards. | Needs project-specific override. |
| MCP Server Development Patterns | Node/TypeScript MCP server development. | Strategic for agent tool ecosystems. |
| Backend Architecture Patterns | Backend architecture review and design. | Useful but must be scoped. |
| API Design | API design and consistency. | Useful for service contracts. |
| Docker Patterns | Containerization guidance. | Useful for deployment hygiene. |
| GitHub Actions Docs | CI/CD workflow guidance. | Useful for automation reliability. |

## Rust-specific adoption notes

For Rust-heavy projects, prioritize skills that include concrete rules around:

- Error type strategy.
- `anyhow` vs `thiserror`.
- `Result` propagation.
- Ownership and borrowing simplification.
- `Arc`, `Mutex`, `RwLock`, Tokio, channels.
- Avoiding unnecessary clones.
- Avoiding `unwrap` and `expect` outside narrow contexts.
- Module and crate boundaries.
- Benchmarking and profiling.
- FFI or unsafe boundaries if applicable.

---

# 5. Frontend, UI, design, and product experience

This category is large and strategically relevant because agents increasingly create production UI surfaces.

| Skill or collection | Use case | Evaluation notes |
|---|---|---|
| frontend-design | General frontend design guidance. | High activity, needs quality review. |
| vercel-react-best-practices | React and Next.js performance rules. | Strong for modern React apps. |
| vercel-composition-patterns | Scalable React composition patterns. | Useful for maintainability. |
| vercel-react-native-skills | React Native performance and architecture. | Mobile-specific. |
| next-best-practices | Next.js file conventions, RSC boundaries, data patterns. | Version-sensitive. |
| next-cache-components | Next.js 16 Cache Components and PPR patterns. | Highly version-sensitive. |
| next-upgrade | Upgrade Next.js using official guides/codemods. | Useful when framework version is known. |
| cra-to-next-migration | Convert Create React App to Next.js. | Useful for legacy CRA projects. |
| turborepo | JavaScript/TypeScript monorepo guidance. | Useful for repo scale. |
| web-design-guidelines | Accessibility, UX, performance, forms, theming, i18n, animation. | Strong QA input. |
| building-components | Accessible, composable UI components. | Useful for design systems. |
| shadcn | shadcn/ui usage. | Useful for modern app UI. |
| sleek-design-mobile-apps | Mobile visual design. | Evaluate for taste and specificity. |
| ui-ux-pro-max | High-end UI/UX skill. | Needs skeptical review. |
| design-taste-frontend | Frontend taste/design critique. | Useful as critique layer. |
| high-end-visual-design | Visual polish and product design. | Useful for marketing/product surfaces. |
| minimalist-ui | Minimalist UI patterns. | Style-specific. |
| industrial-brutalist-ui | Industrial/brutalist design. | Style-specific. |
| stitch-design-taste | Design-style transfer/review. | Useful for design consistency. |
| extract-design-system | Extract design system from existing UI. | Very useful for existing products. |
| brandkit | Brand system creation/maintenance. | Useful for product/marketing consistency. |
| image-to-code | Convert visual references to code. | Needs strong accessibility review. |
| imagegen-frontend-web | Generate frontend visuals for web. | Useful for ideation, not final code alone. |
| imagegen-frontend-mobile | Generate frontend visuals for mobile. | Useful for ideation. |
| design-an-interface | Interface design workflow. | Broad candidate. |
| emil-design-eng | Design-engineering guidance. | Worth reviewing. |

## UI/design adoption notes

Frontend/design skills should be evaluated against:

- Accessibility outcomes.
- Component reusability.
- Responsiveness.
- Dark mode behavior.
- Theming consistency.
- Form usability.
- State/error/loading behavior.
- Performance impact.
- Design-system alignment.
- Avoidance of generic SaaS visual sameness.

---

# 6. Browser, scraping, web automation, and computer-use skills

These skills enable agents to interact with live websites, browser sessions, GUIs, screenshots, and web data.

| Skill or collection | Use case | Evaluation notes |
|---|---|---|
| agent-browser | Browser navigation, form filling, screenshots, data extraction. | High utility, needs permission control. |
| before-and-after | Screenshot comparison for UI state changes. | Useful for visual QA. |
| just-scrape | Web scraping and data extraction. | Legal/robots/rate-limit review needed. |
| develop-userscripts | Browser userscript development. | Useful for personal automation. |
| xget | Fetch/download utility workflow. | Check network boundaries. |
| xdrop | File/drop workflow. | Check file-handling safety. |
| tzst | Utility skill from community collection. | Review source before use. |
| webapp-testing | Browser-driven web app testing. | Useful for QA. |
| CUA-Skill | Research-backed skill base for computer-using agents. | Important research direction. |
| Agent Reach-style browsing tools | Internet/social platform access for research agents. | Requires strong auth and data boundaries. |
| OpenPaw daily briefing | Personal briefing and browser/social integrations. | Useful for assistant workflows. |

## Governance concerns

Browser and computer-use skills are high-risk because they may:

- Submit forms.
- Access authenticated sessions.
- Scrape private data.
- Trigger purchases or account changes.
- Leak screenshots.
- Download unsafe files.
- Circumvent intended access boundaries.

These should always run under explicit permission policies.

---

# 7. Cloud, DevOps, infrastructure, and enterprise platform skills

Official vendor-backed skills matter more in this category because cloud operations can affect production state, security posture, and spend.

| Skill or collection | Use case | Evaluation notes |
|---|---|---|
| Microsoft Azure Skills Plugin | Azure workflows, decision trees, guardrails, MCP-backed execution. | Strong enterprise signal. |
| microsoft-foundry | Microsoft Foundry model/agent workflows. | Strategic for Microsoft ecosystem. |
| azure-prepare | Prepare Azure architecture/deployment. | Good planning gate. |
| azure-validate | Validate Azure configuration before deployment. | Strong pre-deploy gate. |
| azure-deploy | Deployment workflow. | Requires approval policy. |
| azure-upgrade | Upgrade Azure resources/apps. | Requires version/safety checks. |
| azure-enterprise-infra-planner | Enterprise infrastructure planning. | Useful for architecture. |
| azure-hosted-copilot-sdk | Hosted Copilot SDK workflow. | Relevant for agent products. |
| azure-kubernetes | AKS/Kubernetes workflow. | Requires cluster safety rules. |
| airunway-aks-setup | AKS setup. | Review before use. |
| azure-diagnostics | Troubleshooting and diagnostics. | Useful if scoped read-only. |
| appinsights-instrumentation | Application Insights instrumentation. | Useful for observability. |
| azure-compliance | Azure compliance checks. | Strong governance relevance. |
| azure-resource-lookup | Resource inventory/lookup. | Useful read-only workflow. |
| azure-quotas | Quota checks/planning. | Useful planning workflow. |
| azure-cost | Cost review. | Useful for spend control. |
| azure-cost-optimization | Cost optimization. | Needs approval before changes. |
| azure-compute | Compute/service selection. | Useful planning guidance. |
| azure-resource-visualizer | Resource visualization. | Useful for architecture understanding. |
| azure-cloud-migrate | Migration planning. | Useful for enterprise migration. |
| azure-ai | Azure AI workflows. | Relevant for agent products. |
| azure-aigateway | AI gateway patterns. | Governance-relevant. |
| azure-storage | Storage patterns. | Useful architecture input. |
| azure-kusto | Kusto/log analytics. | Useful for telemetry. |
| azure-messaging | Messaging/eventing. | Useful architecture input. |
| azure-rbac | Role-based access control. | Strong security relevance. |
| entra-app-registration | Entra app registration. | Sensitive, approval required. |
| entra-agent-id | Agent identity. | Strategic governance relevance. |
| azure-observability | Observability workflow. | Useful reliability input. |
| azure-reliability | Reliability review. | Good architecture review. |
| AWS Agent Toolkit for AWS | Official AWS skills/plugins/MCP layer. | Strong vendor-backed ecosystem. |
| aws-core | Service selection, CDK/CloudFormation, serverless, containers, storage, observability, billing, SDK usage, deployment. | Broad AWS baseline. |
| aws-agents | Bedrock/AgentCore agent-building workflows. | Relevant for agent products. |
| aws-data-analytics | S3 Tables, Glue, Athena, ETL/data lake workflows. | Useful for data products. |
| aws-agents-for-devsecops | Incident investigation, code review, UAT, vulnerability scans, pen testing. | Strong governance/security fit. |
| HashiCorp agent-skills | Terraform/infrastructure automation. | Critical if IaC is in scope. |
| Firebase basics | Firebase project guidance. | Useful for app backends. |
| Firebase auth basics | Firebase authentication guidance. | Security-sensitive. |
| Firebase hosting basics | Firebase hosting guidance. | Deployment-oriented. |
| Supabase | Supabase workflow. | Useful app backend. |
| Supabase Postgres Best Practices | Postgres/Supabase database best practices. | Useful schema/query guidance. |

## Cloud governance requirements

Cloud skills should be classified by permission tier:

- Read-only inventory and diagnostics.
- Planning and recommendation.
- Code/config generation.
- Staging deployment.
- Production deployment.
- Identity/RBAC changes.
- Cost-impacting changes.
- Destructive changes.

Only the first two should run without explicit human approval.

---

# 8. Data, analytics, databases, and BI

Relevant for dashboards, product telemetry, attribution, reporting, and decision support.

| Skill or collection | Use case | Evaluation notes |
|---|---|---|
| xlsx | Spreadsheet manipulation, formulas, charts, transformations. | High office utility. |
| Data Analysis skills | General analysis workflows. | Needs source review. |
| Supabase Postgres Best Practices | Database schema/query/project guidance. | Useful for app data. |
| Supabase | Backend/database workflows. | Useful for product apps. |
| Firebase basics/auth/hosting | Backend, auth, and hosting workflows. | Useful for app prototypes. |
| Azure Kusto | Log analytics and Kusto query patterns. | Useful for telemetry/observability. |
| AWS data analytics | S3 Tables, Glue, Athena, ETL. | Useful for analytics/data lakes. |
| Polaris DataInsight Doc Extract | Structured extraction from Office/HWP documents. | Good document intelligence candidate. |
| Paper Context Resolver | Resolves paper context for academic reproduction. | Research-specific. |
| Repo Intake and Plan | Research/codebase intake. | Useful for reproduction. |
| Minimal Run and Audit | Reproducibility/audit workflow. | Useful for scientific/code eval. |
| Env and Assets Bootstrap | Environment setup for reproduction tasks. | Useful setup workflow. |
| AI Paper Reproduction skill family | Paper/code reproduction workflows. | Good research automation candidate. |
| Data and Analysis category skills | Broad category. | Review individually. |
| Scientific and Research Tools category | Research-oriented extraction/analysis. | Review individually. |

## Data skill review criteria

- Does it preserve data provenance?
- Does it separate raw data from transformed output?
- Does it document assumptions?
- Does it avoid hallucinated values?
- Does it support reproducible notebooks/scripts?
- Does it handle PII safely?
- Does it avoid writing back to source systems without approval?

---

# 9. Documents, slides, PDFs, spreadsheets, and office workflows

High utility for pitch decks, SOWs, RFQs, reports, PRDs, customer docs, and internal planning.

| Skill or collection | Use case | Evaluation notes |
|---|---|---|
| docx | Word document creation, editing, formatting, tracked changes. | Strong artifact utility. |
| pdf | PDF extraction, merge, annotate, form workflows. | Useful for contracts/RFQs/reports. |
| pptx | Slide generation, layout editing, template handling. | Strong pitch/deck utility. |
| xlsx | Spreadsheet formulas, charts, data transforms. | Strong ops utility. |
| revealjs-skill | HTML/Reveal.js presentation generation. | Useful for technical decks. |
| doc-coauthoring | Collaborative document authoring workflow. | Useful for shared drafts. |
| polaris-datainsight-doc-extract | Structured extraction from office docs. | Useful for intelligence extraction. |
| lark-doc | Lark document workflows. | Team productivity. |
| lark-slides | Lark slide workflows. | Team productivity. |
| lark-markdown | Markdown conversion/workflow in Lark. | Team productivity. |
| lark-base | Lark base/database workflows. | Team productivity. |
| lark-drive | Lark drive workflows. | Team productivity. |
| lark-mail | Lark mail workflows. | Team productivity. |
| Google Workspace CLI Assistant | Gmail, Calendar, Drive, Sheets terminal workflow. | Useful with permission controls. |
| career-ops | Resumes, JD evaluation, ATS, interviews, negotiation. | Personal/career utility. |

## Artifact workflow notes

Document skills should be evaluated for:

- Layout stability.
- Template reuse.
- Citation handling.
- Track changes support.
- Table fidelity.
- PDF extraction accuracy.
- Slide theme consistency.
- Spreadsheet formula correctness.
- Non-destructive editing.

---

# 10. Collaboration, project management, and team operations

These skills connect agents to team workflows and collaboration platforms.

| Skill or collection | Use case | Evaluation notes |
|---|---|---|
| GH Issues Auto-Fixer | Automates issue lifecycle, code fixes, PRs, review comments. | High value, high write-risk. |
| GitHub Integration | GitHub PRs, issues, CI/CD via CLI. | Needs repo permission policy. |
| Community PR Reviewer | PR review workflow. | Useful for open source. |
| Discord Integration | Messaging, reactions, channel management. | Requires careful channel permissions. |
| Google Workspace CLI Assistant | Gmail/Calendar/Drive/Sheets workflows. | Sensitive data risk. |
| lark-approval | Approval workflows. | Useful team governance. |
| lark-okr | OKR workflows. | Useful planning. |
| lark-im | Instant messaging workflows. | Sensitive comms risk. |
| lark-vc-agent | Video conferencing/workflow agent. | Meeting data risk. |
| lark-attendance | Attendance workflows. | HR/sensitive data risk. |
| lark-apps | Lark app workflows. | Review individually. |
| lark-note | Notes/work notes. | Useful if scoped. |
| OpenPaw | Personal/team assistant workflows. | Broad, review permissions. |
| Advisor Brief Review and Verification | Secure cross-agent coordination. | Strategic governance relevance. |
| handoff | Cross-person or cross-agent handoff. | Strong collaboration fit. |
| to-issues | Project planning into issues. | Useful GitHub workflow. |
| to-prd | Product planning. | Useful product workflow. |

## Collaboration risks

These skills frequently touch:

- Private messages.
- Email.
- Calendar.
- Files.
- Issues.
- PRs.
- Customer data.
- Internal planning.
- HR or attendance data.

They should require source-specific permission and logging.

---

# 11. AI app, agent, MCP, and LLM product development

Directly relevant for agent-native products, MCP servers, governance layers, and AI application surfaces.

| Skill or collection | Use case | Evaluation notes |
|---|---|---|
| ai-sdk | Vercel AI SDK agent/chatbot/RAG development. | Useful for AI product apps. |
| ai-elements | shadcn/ui component library for AI-native apps. | Useful frontend layer. |
| streamdown | Streaming React Markdown with security. | Useful AI chat rendering. |
| MCP Server Development Patterns | Building MCP servers. | Strategic for tool ecosystems. |
| microsoft-foundry | Foundry model/agent workflows. | Enterprise AI platform relevance. |
| aws-agents | Bedrock/AgentCore agent development. | Enterprise AWS AI relevance. |
| workflow | Durable async workflows, retries, orchestration. | Useful for agent orchestration. |
| json-render-core | Generative UI schema/catalog/spec streaming. | Agentic UI relevance. |
| json-render-react | JSON-to-React rendering. | Useful dynamic UI pattern. |
| json-render-react-native | JSON-to-React Native rendering. | Mobile dynamic UI. |
| json-render-remotion | JSON-to-video timelines. | Generative video/UI crossover. |
| vercel-deploy | Framework-aware Vercel deployments. | Useful deployment workflow. |
| vercel-cli | Vercel CLI deployment/management. | Useful if Vercel is used. |
| autoship | Automated releases and npm publishing. | Requires release approval. |
| ucp | Universal Commerce Protocol checkout/payment operations. | Sensitive commerce action. |
| rules-distiller | Extract project rules from skills/docs. | Strong governance relevance. |
| Context Engineering Skills | Context architecture and multi-agent production systems. | Strong memory/agent systems relevance. |

## Product opportunity notes

This category reinforces the need for:

- Agent capability manifests.
- Skill permission scopes.
- Skill provenance.
- Runtime policy enforcement.
- Eval harnesses.
- Skill registry metadata.
- Skill conflict detection.
- Context-budget accounting.
- Decision memory alignment.

---

# 12. Media, video, audio, and creative production

Useful for demos, pitch assets, product videos, launch collateral, and creative workflows.

| Skill or collection | Use case | Evaluation notes |
|---|---|---|
| remotion-best-practices | Remotion video creation in React. | Useful for code-driven video. |
| remotion-render | Render Remotion videos. | Operational utility. |
| remotion-to-hyperframes | Convert Remotion workflows to Hyperframes. | Niche workflow. |
| hyperframes | Video/media generation workflow. | Review provider dependency. |
| hyperframes-cli | CLI workflow. | Review install/execution behavior. |
| hyperframes-registry | Registry integration. | Review dependency trust. |
| hyperframes-media | Media workflow. | Review provider trust. |
| video-edit | Video editing. | Useful creative workflow. |
| ai-video-generation | AI video generation. | Provider/model dependent. |
| kling-3-0 | Video model workflow. | Provider/model dependent. |
| seedance-v2 | Video generation workflow. | Provider/model dependent. |
| wan-2-7 | Video model workflow. | Provider/model dependent. |
| video-extend | Extend videos. | Creative utility. |
| video-inpainting | Edit/mask video regions. | Creative utility. |
| video-outpainting | Extend video frame/canvas. | Creative utility. |
| image-to-video | Generate video from image. | Creative utility. |
| ai-image-generation | Image generation. | Provider/model dependent. |
| gpt-image-2 | Image generation/editing. | Provider/model dependent. |
| gpt-image-edit | Image editing. | Provider/model dependent. |
| image-edit | General image editing. | Creative utility. |
| image-inpainting | Fill/edit image regions. | Creative utility. |
| image-outpainting | Extend image canvas. | Creative utility. |
| controlnet-pose | Pose-guided image/video generation. | Useful for character consistency. |
| flux-2-klein | Flux image model workflow. | Provider/model dependent. |
| flux-kontext | Kontext image workflow. | Provider/model dependent. |
| nano-banana-edit | Image edit workflow. | Provider/model dependent. |
| nano-banana-2 | Image generation/edit workflow. | Provider/model dependent. |
| face-swap | Face swap workflows. | Sensitive/consent risk. |
| relight | Relighting images/video. | Useful creative workflow. |
| lipsync | Lip-sync video. | Consent and authenticity risk. |
| ai-avatar-video | Avatar video generation. | Consent and representation risk. |
| ai-music | Music generation. | Rights/licensing review needed. |
| elevenlabs-music-generation | ElevenLabs music workflow. | Provider/licensing review. |
| ace-step | Music/audio generation workflow. | Provider/model dependent. |
| runcomfy-cli | RunComfy CLI integration. | Review workflow execution. |
| codex-pet | Entertainment/agent companion skill. | Low strategic priority. |

## Creative governance concerns

Creative-generation skills should be reviewed for:

- Copyright risk.
- Likeness and consent.
- Model/provider terms.
- Watermark/provenance.
- Prompt retention.
- Output licensing.
- Brand consistency.
- Style consistency.
- Data leakage through uploaded media.

---

# 13. Marketing, content, growth, and developer relations

Useful for founder-led distribution, developer marketing, launch planning, technical content, and product positioning.

| Skill or collection | Use case | Evaluation notes |
|---|---|---|
| devmarketing-skills | Developer marketing: HN, docs-as-marketing, tutorials, Reddit, onboarding, newsletters, SEO. | Strong for technical product GTM. |
| wondelai/skills | UX, marketing/CRO, sales, product strategy, growth. | Review for quality and specificity. |
| @clawfu/mcp-skills | Expert-sourced marketing skills based on classic frameworks. | Good strategy candidate. |
| seo-audit | SEO audit. | Useful if grounded in site data. |
| copywriting | Copywriting. | Needs voice control. |
| marketing-psychology | Persuasion and positioning. | Can become manipulative/sloppy. |
| content-strategy | Content planning. | Useful for editorial systems. |
| programmatic-seo | Programmatic SEO workflows. | Useful for scalable content. |
| viral-short-form | Short-form content. | High slop risk. |
| viral-captions-and-ctas | Social captions/CTA optimization. | Needs brand voice constraints. |
| developer-onboarding | Devtool onboarding content. | Strong for technical products. |
| technical tutorials | Tutorial creation. | Strong devrel utility. |
| Reddit engagement | Community response workflow. | Must avoid salesy tone. |
| newsletter strategy | Newsletter workflows. | Useful for recurring communications. |
| HN strategy | Hacker News launch/content strategy. | Useful but unpredictable. |
| docs-as-marketing | Documentation as acquisition channel. | Strong devtool fit. |
| product strategy | Product positioning and planning. | Useful for framing. |
| sales skills | Sales messaging and process. | Needs strong honesty constraints. |

## Marketing skill constraints

Marketing and devrel skills should be forced to:

- Avoid fake claims.
- Avoid fake urgency.
- Avoid synthetic authority.
- Preserve user voice.
- Cite real product facts.
- Separate hypothesis from proof.
- Avoid exaggerated AI-market language.
- Avoid pretending adoption or traction exists unless proven.

---

# 14. Commerce, payments, ordering, and business operations

Potentially useful for customer-facing agents or internal business automation.

| Skill or collection | Use case | Evaluation notes |
|---|---|---|
| ucp | Universal Commerce Protocol for checkout/payment/commerce operations. | Payment-sensitive. Requires approval gates. |
| ordercli | Food delivery/order management. | Low strategic priority unless assistant commerce is in scope. |
| Google Workspace CLI Assistant | Business productivity. | Sensitive data access. |
| lark-approval | Approval routing. | Useful team governance. |
| lark-okr | OKRs. | Useful planning. |
| lark-attendance | Attendance. | HR-sensitive. |
| career-ops | Job search and negotiation workflows. | Useful personal/career workflow. |
| Changelog Writer | Generates changelogs from commits. | Useful release hygiene. |
| autoship | Changesets, releases, npm publish. | Requires release approval. |
| Azure cost/cost optimization | Business cost control. | Useful if cloud spend matters. |
| AWS billing/observability via aws-core | Business/ops cost visibility. | Useful for FinOps. |

## Commerce/business ops risks

These skills can trigger:

- Purchases.
- Payments.
- Orders.
- Contract steps.
- Release publication.
- Customer communications.
- HR-sensitive workflows.

They should require explicit confirmation before state-changing actions.

---

# 15. Academic, research, education, and knowledge-work skills

Useful for agent education, research digestion, paper reproduction, structured learning, and knowledge synthesis.

| Skill or collection | Use case | Evaluation notes |
|---|---|---|
| AlterLab-Academic-Skills | 186+ academic research skills across 13 domains. | Large research candidate set. |
| AI Paper Reproduction skill family | Reproduce papers/codebases. | Useful for eval/research. |
| paper-context-resolver | Resolve paper/code context. | Useful for research grounding. |
| repo-intake-and-plan | Intake repository and form reproduction plan. | Useful for code/paper reproduction. |
| minimal-run-and-audit | Run/audit minimal reproduction. | Useful for reproducibility. |
| env-and-assets-bootstrap | Bootstrap environment/assets. | Useful setup workflow. |
| teach | Teaching/explanation workflow. | Useful education support. |
| Learning and Knowledge category | Broad educational workflows. | Review individually. |
| Scientific and Research Tools category | Research-focused skills. | Review individually. |
| Data and Analysis category | Research/data analysis. | Review individually. |
| Document extraction skills | Extract info from PDFs, docs, spreadsheets. | Useful for literature/document review. |
| SkillWiki | Governed skill lifecycle research. | Product-relevant. |
| CUA-Skill | GUI/computer-use skill bases. | Important research direction. |

## Research skill criteria

Research skills should require:

- Source citation.
- Distinction between claims and interpretation.
- Reproducibility notes.
- Dataset/provenance tracking.
- Limitation reporting.
- Versioned environment capture.
- No fabricated citations.
- No unsupported benchmark claims.

---

# 16. Personal assistant, notes, productivity, and daily operations

Useful, but many are convenience tools rather than strategic agent-governance assets.

| Skill or collection | Use case | Evaluation notes |
|---|---|---|
| OpenPaw | Personal assistant bundle. | Broad but permission-heavy. |
| Google Workspace CLI Assistant | Gmail, Calendar, Drive, Sheets. | Sensitive data risk. |
| Discord Integration | Messaging/community workflows. | Needs permission boundaries. |
| lark-im | Chat workflows. | Sensitive comms risk. |
| lark-note | Notes. | Useful if scoped. |
| lark-mail | Mail. | Sensitive data risk. |
| lark-drive | File storage. | Sensitive data risk. |
| lark-doc | Docs. | Useful productivity workflow. |
| lark-base | Databases. | Useful productivity workflow. |
| lark-slides | Presentations. | Useful productivity workflow. |
| daily briefing skills | Summaries and briefings. | Useful recurring workflow. |
| Obsidian-related skills | Personal knowledge management. | Useful memory workflow. |
| Telegram skills | Personal/team notifications. | Permission-sensitive. |
| career-ops | Job search workflow. | Useful personal workflow. |
| caveman family | Compact/strict communication and workflow tools. | Review for practical utility. |

## Personal productivity concerns

Assistant-style skills often require access to:

- Email.
- Calendar.
- Contacts.
- Notes.
- Messages.
- Files.
- Private documents.

They should be treated as privacy-sensitive even when they look harmless.

---

# 17. Recommended evaluation framework

Score each candidate skill from 0 to 3 on each criterion.

| Criterion | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Relevance | No clear workflow | Possible use | Clear recurring use | Critical recurring workflow |
| Source trust | Unknown/random | Known but unverified | Reputable community | Official/vendor/internal |
| Scope clarity | Vague | Some boundaries | Clear trigger | Clear trigger and non-trigger |
| Version compatibility | Unknown | Partially compatible | Mostly compatible | Explicitly compatible |
| Determinism | Vague advice | Checklist only | Scripts or structured checks | Reproducible tests/checks |
| Security posture | Unsafe/unknown | Risky but reviewable | Bounded | Sandboxed/read-only/safe |
| Token efficiency | Bloated | Neutral | Reduces repeated context | Strong progressive disclosure |
| Verifiability | No test path | Manual review only | Some measurable outcome | Clear before/after eval |
| Composability | Conflicts likely | Unknown | Mostly compatible | Explicitly compatible with repo governance |
| Drift risk | High | Medium | Low | Actively reduces drift |

## Suggested classification

| Classification | Meaning |
|---|---|
| Adopt now | Strong fit, low risk, clear workflow. |
| Sandbox evaluate | Promising but needs controlled test. |
| Track | Important market/product signal but not yet adoption-ready. |
| Reject | Too vague, risky, obsolete, redundant, or irrelevant. |
| Quarantine | Useful but dangerous without strict permissioning. |

---

# 18. Initial priority list

## Adopt or evaluate first

1. Verification Loop.
2. Security Review.
3. systematic-debugging.
4. verification-before-completion.
5. Rust Best Practices and Patterns.
6. Rust Anti-Pattern Refactor.
7. writing-plans.
8. executing-plans.
9. handoff.
10. grill-with-docs.
11. to-issues.
12. to-prd.
13. web-design-guidelines.
14. vercel-react-best-practices.
15. MCP Server Development Patterns.
16. azure-validate.
17. aws-agents-for-devsecops.
18. AI Regression Testing.
19. Automated Compliance Auditor.
20. Skill creator/write-a-skill/rules-distiller.

## Track as product opportunities

1. Skill governance.
2. Skill provenance.
3. Skill signing.
4. Skill security scanning.
5. Skill conflict detection.
6. Skill version pinning.
7. Skill eval harnesses.
8. Skill permission manifests.
9. Skill runtime policy enforcement.
10. Skill drift detection.
11. Skill decision-memory alignment.
12. Skill marketplace trust scoring.
13. Skill-to-AGENTS.md reconciliation.
14. Skill-to-MCP permission modeling.
15. Skill lifecycle observability.

## Deprioritize unless needed

1. Most generic best-practices skills.
2. Viral content skills.
3. Novelty/pet skills.
4. Personal assistant bundles without strict permission controls.
5. Media skills unrelated to product/demo needs.
6. Commerce/order skills unless commerce is in scope.
7. Broad marketing skills that do not preserve voice or proof.
8. Cloud deploy skills without approval gates.

---

# 19. Proposed repository structure

If this repository becomes a real skill-governance project, consider this structure:

```text
skillz/
  README.md
  docs/
    agent-skills-longlist.md
    evaluation-framework.md
    source-watchlist.md
    governance-model.md
    risk-taxonomy.md
  registry/
    candidates.yaml
    adopted.yaml
    rejected.yaml
    quarantined.yaml
  evaluations/
    templates/
      skill-eval-template.md
      security-review-template.md
      compatibility-review-template.md
    results/
  policies/
    permissions.md
    allowlist.md
    denylist.md
    source-trust-policy.md
  scripts/
    lint_skill_manifest.py
    score_candidates.py
  schemas/
    skill-candidate.schema.json
    skill-evaluation.schema.json
```

---

# 20. Candidate metadata schema

A candidate skill should eventually be represented with structured metadata:

```yaml
id: verification-loop
name: Verification Loop
source_url: ""
source_type: marketplace
maintainer: ""
category:
  - verification
  - qa
  - security
status: sandbox-evaluate
trust_level: medium
permission_tier: local-read
requires_network: false
requires_filesystem_write: false
requires_shell: false
requires_credentials: false
trigger_conditions:
  - before declaring implementation complete
  - before opening PR
non_trigger_conditions:
  - exploratory brainstorming
  - non-code writing
known_conflicts:
  - may duplicate repo CI checks
version_notes: ""
eval_plan:
  success_metric: pass rate and defect reduction
  sample_tasks: []
  baseline_required: true
risk_notes:
  - may create false confidence if test suite is weak
decision_notes: ""
```

---

# 21. Source watchlist

Track these regularly:

| Source | URL |
|---|---|
| Anthropic Skills | https://github.com/anthropics/skills |
| Anthropic skill engineering article | https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills |
| Anthropic Skills docs | https://docs.anthropic.com |
| Claude support: Skills | https://support.claude.com/en/articles/12512176-what-are-skills |
| Vercel Agent Skills docs | https://vercel.com/docs/agent-resources/skills |
| Vercel Agent Skills repo | https://github.com/vercel-labs/agent-skills |
| Microsoft Skills | https://github.com/microsoft/skills |
| Microsoft Azure Skills | https://github.com/microsoft/azure-skills |
| AWS Agent Toolkit for AWS | https://github.com/aws/agent-toolkit-for-aws |
| Skills.sh | https://www.skills.sh |
| MCP Market Agent Skills | https://mcpmarket.com/tools/skills |
| MCP Market Leaderboard | https://mcpmarket.com/tools/skills/leaderboard |
| Awesome Claude Skills | https://awesomeclaude.ai/awesome-claude-skills |
| Skills Directory | https://skills-directory.com |
| AgentSkills.io | https://agentskills.io |
| SWE-Skills-Bench paper | https://arxiv.org/abs/2603.15401 |
| Skill ecosystem/security paper | https://arxiv.org/abs/2602.08004 |
| CUA-Skill paper | https://arxiv.org |

---

# 22. Next-step recommendation

Treat this repository as a skill intake and governance registry, not just a list.

Recommended immediate next files:

1. `docs/evaluation-framework.md`
2. `docs/risk-taxonomy.md`
3. `registry/candidates.yaml`
4. `evaluations/templates/skill-eval-template.md`
5. `policies/source-trust-policy.md`

The main opportunity is not collecting skills. The opportunity is deciding which skills are allowed to influence an agent, under which conditions, with which permissions, and with what proof that they actually improve outcomes.
