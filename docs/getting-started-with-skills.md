# Getting started: put a Skillz skill into your AI

Skillz is a **library of instructions**, not software that silently installs
itself. You choose one skill for a task, check its source and permissions, and
place its **whole folder** where your AI can discover it. An agent with the
right tools can do some of these steps for you. A chat-only agent may be able
to prepare a file but cannot put it inside your editor or another account.

**The short route:** 1. Choose the skill. 2. Name the exact AI product and
surface (for example, GitHub Copilot in VS Code, not just "Claude model").
3. Let your agent assess package support and permission. 4. Install or upload.
5. Verify discovery. 6. Try a real task and verify its output.

## What a consuming agent must do

Before recommending an installation, the agent should:

1. **Identify the product, surface, and installation scope.** A model offered
   *inside* Copilot is still running in the Copilot host. Web, CLI, IDE,
   desktop, personal and project skill locations can differ.
2. **Find and review the full canonical package.** Preserve `SKILL.md`,
   references, scripts, assets, license/NOTICE and provenance. Inspect
   third-party rights and executable content. A catalog listing is not approval.
3. **Check host evidence:** current official installation method, plan or
   workspace entitlement, file/layout limits, dependency and sandbox support,
   permitted connectors/tools and whether the host can access all references.
   Run `python3 engine/builder/host_compat.py --skill <slug> --host <host>`
   when authorized local Python and the whole checkout are actually available.
   Otherwise inspect manually. The preflight **only** tests package shape.
4. **Choose the least burdensome executable route** from the actual tools:
   - `DIRECT-WRITE` only if a filesystem is writable, the exact host destination
     is known, and the current user authorizes installing that package.
   - `API-INSTALL` only through a supported, authenticated host API with
     current permission, followed by readback.
   - `UI-UPLOAD` when the user must complete an upload/enable action. Prepare
     the correct ZIP or instructions. Do not invent button labels.
   - `PORTABLE-HANDOFF` when a host cannot be reached or the method is unknown.
     A prompt pasted into a chat is **not** a successfully installed skill.
5. **Hand off one clear route:** what is already done, the file/path to use,
   numbered user actions (if any), official source, expected discovery result,
   one appropriate trigger test, and what evidence would complete verification.
6. **Record status per target:** `FORMAT_VALID`, `PACKAGE_READY`,
   `HOST_LOADED`, `BEHAVIOR_TESTED`, and `CONSUMER_ACCEPTED` are
   separate facts. Missing host observation is `NOT_TESTED`, never PASS.

**Do not auto-install merely because the user asked for a recommendation.**
Installing files, connecting accounts, enabling scripts, publishing to an
organization, updating existing skills, and accepting network costs have
different authority boundaries.

## Host-specific starting points

These are distinct products, not synonyms. Product documentation is the
source of truth; recheck it before a real install. The paths below describe
the usual project/user location or import shape, *not* verified access to
your own device, plan or organization.

| Target | Place or upload the complete skill | Verify it |
| --- | --- | --- |
| GitHub Copilot (IDE, CLI, cloud/review) | Project `.github/skills/<skill>/` (also `.agents/skills/` or `.claude/skills/`); personal `~/.copilot/skills/<skill>/` | Inspect skill discovery and try a matching request. Supported surfaces differ. |
| Claude Code | Project `.claude/skills/<skill>/`; personal `~/.claude/skills/<skill>/` | Check skill listing/invocation and a relevant task. |
| OpenAI Codex | Project `.agents/skills/<skill>/`; personal `~/.agents/skills/<skill>/` | Confirm discovered skill then test activation. |
| Gemini CLI | Project `.gemini/skills/<skill>/` (or `.agents/skills/`); user `~/.gemini/skills/<skill>/` | Use `/skills list` (and `/skills reload` if needed), then a task. |
| Hermes Agent | `~/.hermes/skills/<skill>/` or a supported project/external directory; `hermes skills install` can also install sources | Use `hermes skills list`; check source precedence and try a task. |
| Microsoft 365 Copilot Chat (personal) | Upload standalone `SKILL.md` only if there are no required support files; otherwise a ZIP with **`SKILL.md` at ZIP root**, not an enclosing folder | In Copilot Chat select **Agents → More agents → Add drop-down → Upload skill**, then check enabled and test; premium entitlement/tenant restrictions apply. |
| Microsoft 365 Agent Builder | Upload complete ZIP with `SKILL.md` at root, observing Agent Builder's limits | Confirm agent's skill is listed, can read bundled references, and executes an approved test. |
| Microsoft 365 Agents Toolkit | Add a complete skill *directory* under the relevant `appPackage/skills/` path, not a ZIP | Package/deploy with the intended agent and observe invocation. |
| ChatGPT / OpenAI Plugins | Use the current account's supported Skills/Plugin workflow, if exposed. Do not equate GPT knowledge attachments with installed skills | Check the connected skill in the current host and run a task. |
| Gemini Apps | Use the currently available Skills interface and its import flow for the account/surface; this is **not Gemini CLI** | Confirm it is available in Skills and actually applied in a test. |
| OpenClaude and other hosts | **Identify the exact project and official maintained installation docs first**. Names can be shared by unrelated products | Unsupported or unverified paths are handoff-only, not claimed compatible. |

Some host systems allow an agent to write files; others require a user to
click Upload. A source folder can be compatible with more than one host,
but installation and runtime behavior must be verified **independently**.

For a local installation into several coding agents, a shared
`.agents/skills/` project path is often a useful starting point where supported;
do **not** assume the agents share permissions, activation or runtime.

## What packaging checks actually prove

The optional offline command lives inside the **existing Skillz builder**
and does not execute skill scripts, invoke a model, access the network or
install anything:

```sh
python3 engine/builder/host_compat.py --all
python3 engine/builder/host_compat.py --skill effort-allocation-navigator --host m365-agent-builder
python3 engine/builder/host_compat.py --skill effort-allocation-navigator --host m365-copilot-chat --zip-output /path/outside/skillz/navigator-chat.zip
python3 engine/builder/host_compat.py --skill effort-allocation-navigator --host m365-agents-toolkit --directory-output /path/outside/skillz/navigator-toolkit-handoff
```

The ZIP command creates an uploadable archive at an explicitly chosen
new path, and the directory command creates a separate prepared handoff
folder. Neither command installs or uploads anything. The Microsoft adapter
preserves the canonical source while renaming an extensionless `LICENSE`
to `LICENSE.txt` **in the distribution artifact only**, rewriting valid
relative license links and checking transformed output digests. Unsupported
file types and missing references remain packaging HOLDs.

An actual host may still lack required Python modules, tool permissions,
connectors, network access or account features. In Microsoft's skill sandbox,
scripts cannot install packages or call external APIs directly. The agent
may use its own authorized connectors through host orchestration, but
script/network parity is **not** established by matching folder structure.

For non-native or unsupported hosts, provide a readable, source-attributed
manual procedure as an **adapter**, labeled clearly as a fallback. Preserve
the mandatory safety, evidence, privacy and decision controls. If a
required capability cannot be recreated safely, mark the host **BLOCKED**.

## Official instructions, checked 2026-11-24

- [GitHub Copilot Agent Skills](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills)
- [Gemini CLI Agent Skills](https://geminicli.com/docs/cli/skills/)
- [Hermes Skills](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills)
- [Microsoft 365 Copilot Chat skills](https://learn.microsoft.com/en-us/plugins/build-copilot-chat-skills)
- [Microsoft declarative agent skill requirements](https://learn.microsoft.com/en-us/plugins/declarative-agent-skills)
- [Microsoft Agent Builder upload](https://learn.microsoft.com/en-us/plugins/agent-builder-add-skills)
- [Microsoft Agents Toolkit](https://learn.microsoft.com/en-us/plugins/build-declarative-agents-add-custom-skills)
- [OpenAI Skills](https://developers.openai.com/plugins/concepts/skills)
- [Google Gemini Apps Help](https://support.google.com/gemini/answer/17094296)
- [Anthropic Claude Code Skills](https://code.claude.com/docs/en/skills)

**Completion rule:** a successfully formatted package is not a successful
user deployment. The handoff ends only when the intended target's current
installation status, next action and verification evidence are explicit.
