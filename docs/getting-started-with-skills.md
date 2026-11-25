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

1. Open the [authored skills catalog](../skills/authored/README.md), choose a skill and identify your exact host from the installation sections below. The catalog ZIP is the canonical source archive, not necessarily an uploadable host variant.
2. Open the [published download manifest](https://github.com/Knapp-Kevin/skillz/releases/latest/download/authored-download-manifest.json). Locate the skill slug, `source_commit`, exact package tree, and `hosts` entry for your target. A `PACKAGE_READY` entry specifies its `asset` and `sha256`; a HOLD, absent entry or null asset is not an installable host selection.
3. Download the selected asset from the same source-pinned release: `https://github.com/Knapp-Kevin/skillz/releases/download/authored-<source_commit>/<asset>`. Substitute only the manifest's exact commit and asset basename. You can also open that release's page and select the named asset. Do not fetch a second moving `latest` URL; a new snapshot could appear between requests. Compare the downloaded file's SHA-256 with the selected host entry (Windows PowerShell: `Get-FileHash .\skill-name.zip -Algorithm SHA256`; macOS/Linux: `shasum -a 256 skill-name.zip`). On mismatch or missing asset, stop and recheck the manifest; never bypass verification.
4. Inspect the full archive in a temporary location. Directory hosts use the enclosing skill folder; Claude Apps may select `-claude.zip`, while Gemini Apps and Microsoft select root-level `-gemini.zip` and `-m365.zip`. Preserve `SKILL.md`, license and all resources; review scripts as untrusted code. Follow your exact host instructions below, without stripping mandatory files. A held or unassessed host may use a portable read-only handoff, not an asserted native installation.
5. Confirm the skill is visible, then test a matching request on fictional or public data and a near non-trigger. Check that the intended output is correct and no unauthorized action occurs. A file copy or upload alone is not verification.

If a published snapshot is older than current main, inspect the exact published source or prepare the current full folder from source. Release assets are first-party MIT material only; no third-party corpus is bundled.

**Read your host's manifest status before installation.** `PACKAGE_READY` means the static package profile passed, not that the host loaded or ran it. `HOLD` means packaging is blocked or has not been assessed; read its `blockers` before proceeding. The `chatgpt` and `openclaude-other` entries deliberately remain HOLD until their exact host-specific packaging requirements can be established and assessed. Claude apps and Gemini Apps have separately checked static profiles; individual skills may still be held. A canonical source ZIP is still available for inspection and portable handoff, but a null host asset is not a validated upload package. Older manifests may omit these entries; an absent host means unassessed, never ready.

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

1. Check `claude-apps` in the manifest. If PACKAGE_READY, download and verify the exact listed asset. This is either the canonical folder-wrapped ZIP or a dedicated `-claude.zip` with a curated discovery description of at most 200 characters. The adapted archive preserves the original instruction body, full canonical activation scope, license and supporting files. Do not automatically truncate descriptions or substitute the canonical ZIP when the manifest selects an adapted archive. Changed, unmatched or unassessed source stays HOLD if it exceeds the limit. Enable code execution/file creation only if required and permitted.
2. Open Customize > Skills, use the plus/create menu, select the upload option and choose the complete ZIP.
3. Confirm the skill is listed and enabled. Test it in the intended Claude surface; organization sharing requires separate consent. [Official Claude guide](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

### ChatGPT

1. Download and inspect the canonical ZIP. The official help lists eligible Business, Enterprise, Healthcare and Edu accounts, subject to workspace settings. In an eligible account open Plugins > Skills, then Create > Upload from your computer. The exact upload profile remains HOLD; confirm the supported layout before proceeding.
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

1. Check `gemini-apps` in the manifest. If PACKAGE_READY, download and verify the listed `-gemini.zip` asset. It contains `SKILL.md` at the archive root with all resources and a lossless `LICENSE.txt` adaptation. Do not upload the folder-wrapped canonical archive as-is.
2. Open Gemini's Customize > Skills page, choose Create, then Upload. Select the Gemini ZIP or extract it into a single folder and select that folder. Review and save the skill.
3. Verify included references and test a matching prompt. Scripts cannot make external requests; the static profile does not prove runtime parity. For unsupported files or a HOLD, do not delete required resources to force upload. [Official Gemini Apps guide](https://support.google.com/gemini/answer/17094296) · [Transfer requirements](https://support.google.com/gemini/answer/18977944).

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
| Claude Apps (web, desktop, Cowork) | Use the manifest-selected folder-wrapped canonical or `-claude.zip` archive in Customize > Skills. | Verify enabled state, references and an appropriate task. |
| OpenAI Codex | Project `.agents/skills/<skill>/`; personal `~/.agents/skills/<skill>/` | Confirm discovered skill then test activation. |
| Gemini CLI | Project `.gemini/skills/<skill>/` (or `.agents/skills/`); user `~/.gemini/skills/<skill>/` | Use `/skills list` (and `/skills reload` if needed), then a task. |
| Hermes Agent | `~/.hermes/skills/<skill>/` or a supported project/external directory; `hermes skills install` can also install sources | Use `hermes skills list`; check source precedence and try a task. |
| Microsoft 365 Copilot Chat (personal) | Upload standalone `SKILL.md` only if there are no required support files; otherwise a ZIP with **`SKILL.md` at ZIP root**, not an enclosing folder | In Copilot Chat select **Agents → More agents → Add drop-down → Upload skill**, then check enabled and test; premium entitlement/tenant restrictions apply. |
| Microsoft 365 Agent Builder | Upload complete ZIP with `SKILL.md` at root, observing Agent Builder's limits | Confirm agent's skill is listed, can read bundled references, and executes an approved test. |
| Microsoft 365 Agents Toolkit | Add a complete skill *directory* under the relevant `appPackage/skills/` path, not a ZIP | Package/deploy with the intended agent and observe invocation. |
| ChatGPT | Plugins > Skills > Create > Upload from your computer, where available; see detailed steps above. | Check the connected skill in the current host and run a task. |
| Gemini Apps | Customize > Skills > Create > Upload; use the manifest-selected root-level `-gemini.zip` or its extracted folder. This is **not Gemini CLI** | Confirm it is available in Skills and actually applied in a test. |
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
folder. Neither command installs or uploads anything. The Microsoft and Gemini upload adapters
preserve the canonical source while renaming an extensionless `LICENSE`
to `LICENSE.txt` **in the distribution artifact only**, rewriting valid
relative license links and checking transformed output digests. Adapted ZIPs use sorted members, fixed archive timestamps and stable metadata so identical inputs rebuild identically under the same Python/zlib toolchain; this is not a claim of byte reproducibility across arbitrary toolchain versions. Unsupported
file types and missing references remain packaging HOLDs. Gemini's static profile also checks its documented file count, byte limits and description length; Claude apps check the separate description limit and select either the canonical folder archive or a source-pinned `-claude.zip` variant. Curated variants are generated only for explicitly maintained canonical source blobs; any changed source must be reassessed before its adapted variant can be published. Neither profile confirms account entitlement, upload scanning or model execution.

An actual host may still lack required Python modules, tool permissions,
connectors, network access or account features. In Microsoft's skill sandbox,
scripts cannot install packages or call external APIs directly. The agent
may use its own authorized connectors through host orchestration, but
script/network parity is **not** established by matching folder structure.

For non-native or unsupported hosts, provide a readable, source-attributed
manual procedure as an **adapter**, labeled clearly as a fallback. Preserve
the mandatory safety, evidence, privacy and decision controls. If a
required capability cannot be recreated safely, mark the host **BLOCKED**.
For example, Offline Hyper-V Qualification VM requires its original PowerShell scripts and a suitable owner-approved Windows Hyper-V environment. Gemini Apps and Microsoft upload profiles currently hold this package; use an authorized compatible host or a read-only manual planning handoff. Do not rename executable PowerShell scripts as text or strip them to force upload.

## Official instructions, checked 2026-11-24; app upload requirements rechecked 2026-11-25

- [GitHub Copilot Agent Skills](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills)
- [Gemini CLI Agent Skills](https://geminicli.com/docs/cli/skills/)
- [Hermes Skills](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills)
- [Microsoft 365 Copilot Chat skills](https://learn.microsoft.com/en-us/plugins/build-copilot-chat-skills)
- [Microsoft declarative agent skill requirements](https://learn.microsoft.com/en-us/plugins/declarative-agent-skills)
- [Microsoft Agent Builder upload](https://learn.microsoft.com/en-us/plugins/agent-builder-add-skills)
- [Microsoft Agents Toolkit](https://learn.microsoft.com/en-us/plugins/build-declarative-agents-add-custom-skills)
- [OpenAI Skills](https://developers.openai.com/plugins/concepts/skills)
- [Google Gemini Apps Help](https://support.google.com/gemini/answer/17094296) and [transfer requirements](https://support.google.com/gemini/answer/18977944)
- [Claude custom skill packaging](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)
- [ChatGPT Skills help](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)
- [Anthropic Claude Code Skills](https://code.claude.com/docs/en/skills)

**Completion rule:** a successfully formatted package is not a successful
user deployment. The handoff ends only when the intended target's current
installation status, next action and verification evidence are explicit.
