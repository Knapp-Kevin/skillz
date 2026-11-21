# Controlled README audit example (not a live repository finding)

**Request:** AUDIT only. **Fixture:** a fictional README claims a Windows executable is published, contains an untrusted `curl | sh` command, and opens with several paragraphs of mission prose. Its supplied release inventory has Linux and macOS assets only.

## Prioritized findings

| Priority | Location | Evidence / limit | User consequence | Concrete fix |
| --- | --- | --- | --- | --- |
| P0 accuracy | Download section, Windows claim | Supplied release inventory lists no Windows asset; actual GitHub releases not independently fetched | Reader is directed to a nonexistent binary | Remove/qualify the Windows claim until a verified release asset exists |
| P0 safety | Quick start, shell pipeline | README text contains `curl | sh`; no authorized code execution or trusted script digest | Unsafe execution path may be repeated by the reader or the auditor | Do not execute it as part of the audit; replace with reviewed, source-compatible installation steps if available |
| P1 usability | Opening screen | No concrete software description until several paragraphs in | Newcomer cannot tell what exists or what to try | State the verified tool's purpose, status and next supported action in the first screen |

**Already effective:** The README includes a real Linux installation link in the supplied fixture. Preserve it only if source identity, asset and exact revision are actually confirmed during revision.

**Disposition:** AUDIT report only, no repository mutations. Release asset resolution, command execution and independent user testing are **NOT_RUN**. This is a controlled fixture, not observed production evidence or a claim about an actual project.
