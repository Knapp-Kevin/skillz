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


## Download your skill

1. Open the [authored skills catalog](../skills/authored/README.md), choose one skill and click its ZIP link. It downloads the complete canonical folder archive, not just the instructions.
2. Open the [published download manifest](https://github.com/Knapp-Kevin/skillz/releases/latest/download/authored-download-manifest.json). Locate the slug, source commit, exact package tree and SHA-256 of the selected file. Compare its hash before trusting the download (Windows PowerShell: `Get-FileHash .\skill-name.zip -Algorithm SHA256`; macOS/Linux: `shasum -a 256 skill-name.zip`).
3. Extract the archive into a temporary folder. Check that the named skill folder contains `SKILL.md`, its license and all supporting files. Review scripts as untrusted code; do not run anything merely because a file asks you to.
4. Select the appropriate host below. The catalog's canonical ZIP contains one enclosing skill directory. Microsoft upload packages have **SKILL.md at the ZIP root** and use the separate `-m365.zip` asset only if the manifest marks that exact target PACKAGE_READY. If that target is HOLD, use the documented safe fallback; do not strip mandatory files.
5. Confirm the skill is visible, then test a matching request on fictional or public data and a near non-trigger. Check that the intended output is correct and no unauthorized action occurs. A file copy or upload alone is not verification.

If a published snapshot is older than current main, inspect the exact published source or prepare the current full folder from source. Release assets are first-party MIT material only; no third-party corpus is bundled.

## Manual installation steps by environment

### GitHub Copilot (IDE, CLI and cloud)

1. Extract the canonical ZIP. From the intended repository root create `.github/skills/` if needed, and copy the whole named skill folder into it. For personal CLI/IDE scope use `~/.copilot/skills/` where the current host supports it. Do not overwrite an existing folder without review.
2. Reload the supported Copilot surface if necessary. Cloud and code-review discovery use repository content; a personal local folder is not automatically available in the cloud. Commit through your normal approved repository process only if repository sharing is intended.
3. Check discovery and run a matching task. [Official GitHub instructions](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills).

### Claude Code

1. Extract the ZIP and place the named folder under project `.claude/skills/` or personal `~/.claude/skills/`.
2. Open Claude Code in the intended project and check whether the skill is available; invoke it or try an appropriate request.
3. Review any requested tools, permissions and bundled scripts before authorizing them. [Official Claude Code guide](https://code.claude.com/docs/en/skills).

### Claude web, desktop and Cowork

1. Keep the canonical ZIP intact. In eligible Claude accounts enable code execution/file creation if required and permitted.
2. Open Customize > Skills, use the plus/create menu, select the upload option and choose the complete ZIP.
3. Confirm the skill is listed and enabled. Test it in the intended Claude surface; organization sharing requires separate consent. [Official Claude guide](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

### ChatGPT

1. Download and inspect the canonical ZIP. In an eligible account open Plugins > Skills, then Create > Upload from your computer.
2. Select the supported package in the upload picker. If the picker requires a different supported layout, retain all required files and follow the current official help; do not silently downgrade to a bare instruction file.
3. Wait for scanning and review any Needs Review or Blocked state. Check the skill in the installed list and try an appropriate task. If Skills is not available in this account, use portable handoff only. [Official ChatGPT Skills help](https://help.openai.com/en/articles/20001066-skills-in-chatgpt).

### OpenAI Codex

1. Extract the ZIP. Copy the named folder under the intended repository's `.agents/skills/` or personal `~/.agents/skills/`.
2. Open Codex in that scope; check discovery and test explicit or relevant invocation. Local filesystem and cloud workspaces differ. [Official Codex skills documentation](https://developers.openai.com/codex/skills).

### Gemini CLI

1. Extract and copy the folder to project `.gemini/skills/` (or the documented shared `.agents/skills/`) or personal `~/.gemini/skills/`.
2. In Gemini CLI run `/skills list`, reload if needed using `/skills reload`, and confirm the skill appears.
3. Try a matching task and inspect any requested tool actions. [Official Gemini CLI guide](https://geminicli.com/docs/cli/skills/).

### Gemini Apps (web and supported desktop/mobile)

1. Open Gemini's Customize > Skills page. Choose Create, then Upload.
2. Select the extracted skill folder containing `SKILL.md` and references, or the ZIP if the current picker supports that layout. Review and save the skill.
3. Verify reference support, particularly any scripts: internet-requiring scripts are not supported. Test an appropriate prompt. [Official Gemini Apps guide](https://support.google.com/gemini/answer/17094296).

### Hermes Agent

1. Extract the ZIP. Copy the named folder into the documented personal skills location, usually `~/.hermes/skills/`, or the authorized project/external skills directory.
2. Run `hermes skills list` in the actual environment, resolve any duplicate precedence, and test a matching request. [Official Hermes guide](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills).

### Microsoft 365 Copilot Chat (personal skills)

1. Find the slug in the manifest. If `m365-copilot-chat` is PACKAGE_READY, download the listed `-m365.zip` asset. It has `SKILL.md` at the root and preserves the license as `LICENSE.txt`. Do not use the enclosing-folder archive directly.
2. In eligible Copilot Chat open Agents > More agents, use the drop-down beside Add, then Upload skill. Choose the ZIP and upload.
3. Verify enablement, included resources and a matching prompt. Check tenant policy and script/runtime restrictions. [Official Microsoft guide](https://learn.microsoft.com/en-us/plugins/build-copilot-chat-skills).

### Microsoft 365 Agent Builder

1. Check the manifest specifically for `m365-agent-builder`; Chat readiness is not sufficient. Download its listed root-level `-m365.zip` only when PACKAGE_READY.
2. Open or create the intended declarative agent. On Configure, expand Skills, select Add and upload the ZIP.
3. Review included files and run a matching prompt on Try it. Do not publish or share the agent without separate authority. [Official Agent Builder guide](https://learn.microsoft.com/en-us/plugins/agent-builder-add-skills).

### Microsoft 365 Agents Toolkit

1. Check `m365-agents-toolkit` in the manifest. If PACKAGE_READY, use the root-level Microsoft ZIP, extract into a directory named exactly for the skill and copy that complete directory into the agent's `appPackage/skills/` location.
2. Follow the official manifest registration steps for your declarative agent, then validate its complete app package. Deploy only with separate authorization.
3. Verify discovery and invocation in that agent. [Official Toolkit guide](https://learn.microsoft.com/en-us/plugins/build-declarative-agents-add-custom-skills).

### OpenClaude and other environments

Identify the actual product/project, version and official maintained import instructions first. Download the complete canonical ZIP and inspect it. If native skill support, required references or permission cannot be established, use a portable read-only handoff rather than inventing an upload location. No verified native installation is claimed.


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
| ChatGPT | Plugins > Skills > Create > Upload from your computer, where available; see detailed steps above. | Check the connected skill in the current host and run a task. |
| Gemini Apps | Customize > Skills > Create > Upload; select the supported folder or archive. This is **not Gemini CLI** | Confirm it is available in Skills and actually applied in a test. |
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
