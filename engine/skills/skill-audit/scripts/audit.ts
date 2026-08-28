#!/usr/bin/env bun
/**
 * skill-audit — validates this repo's library skills, scripts, and intake registry.
 *
 * Usage (Bun or Node 22.18+, from repo root or anywhere):
 *   node engine/skills/skill-audit/scripts/audit.ts
 *   node engine/skills/skill-audit/scripts/audit.ts --skills-dir <path> --registry <path>
 *
 * Exit 0 = clean (warnings allowed). Exit 1 = one or more FAIL findings.
 */

import { parseArgs } from "node:util";
import { readdirSync, readFileSync, existsSync, statSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";
import { spawnSync } from "node:child_process";
import { parseFrontmatter } from "../../../../scripts/lib/frontmatter.ts";
import { discoverSkillDirs } from "../../../../scripts/lib/skill-discovery.ts";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..", "..", "..", "..");
const STATUSES = ["adopted", "sandbox", "track", "rejected", "quarantined"];
const TIERS = [
  "read-only", "plan-only", "generate", "staging-write",
  "production-write", "identity", "cost", "destructive",
];

const { values } = parseArgs({
  options: {
    "skills-dir": { type: "string", default: join(ROOT, "skills") },
    registry: { type: "string", default: join(ROOT, "registry", "candidates.yaml") },
    help: { type: "boolean", default: false },
  },
});

if (values.help) {
  console.log("skill-audit — repo validator\n\nUsage: node audit.ts [--skills-dir <path>] [--registry <path>] [--help]");
  process.exit(0);
}

interface Finding { level: "FAIL" | "WARN"; msg: string; }
const findings: Finding[] = [];
const fail = (msg: string) => findings.push({ level: "FAIL", msg });
const warn = (msg: string) => findings.push({ level: "WARN", msg });

function checkSkillFile(name: string, skillFile: string): void {
  const fm = parseFrontmatter(readFileSync(skillFile, "utf8"));
  if (!fm) { fail(`${name}: SKILL.md frontmatter does not parse`); return; }
  if (fm.name !== name) fail(`${name}: frontmatter name "${fm.name}" != directory "${name}"`);
  const desc = typeof fm.description === "string" ? fm.description : "";
  if (!desc.trim()) fail(`${name}: description missing or empty`);
  else if (!desc.includes("Use when")) fail(`${name}: description lacks "Use when" trigger guidance`);
  if (!fm.metadata?.version) fail(`${name}: metadata.version missing`);
}

function checkSkills(skillsDir: string): string[] {
  const skillFiles: string[] = [];
  const names = new Set<string>();
  for (const skill of discoverSkillDirs(skillsDir)) {
    if (names.has(skill.name)) fail(`${skill.name}: duplicate local skill directory name`);
    names.add(skill.name);
    checkSkillFile(skill.name, skill.skillFile);
    skillFiles.push(skill.skillFile);
  }
  if (skillFiles.length === 0) fail(`no library skills discovered under ${skillsDir}`);
  return skillFiles;
}

function checkHelp(file: string, label: string): void {
  const res = spawnSync(process.execPath, [file, "--help"], { timeout: 30_000, encoding: "utf8" });
  if (res.status !== 0) fail(`${label}: --help exited ${res.status}`);
}

function checkScripts(skillsDir: string): void {
  for (const skill of discoverSkillDirs(skillsDir)) {
    const scriptsDir = join(skill.dir, "scripts");
    if (!existsSync(scriptsDir)) continue;
    for (const f of readdirSync(scriptsDir).filter((f) => f.endsWith(".ts"))) {
      checkHelp(join(scriptsDir, f), `${skill.relativeDir}/scripts/${f}`);
    }
  }
  const repoScripts = join(ROOT, "scripts");
  for (const f of readdirSync(repoScripts).filter((f) => f.endsWith(".ts"))) {
    checkHelp(join(repoScripts, f), `scripts/${f}`);
  }
}

function checkSources(skillsDir: string): void {
  for (const skill of discoverSkillDirs(skillsDir)) {
    const sources = join(skill.dir, "sources.json");
    if (!existsSync(sources)) continue;
    try {
      JSON.parse(readFileSync(sources, "utf8"));
    } catch {
      fail(`${skill.name}: sources.json does not parse as JSON`);
    }
    if (!readFileSync(skill.skillFile, "utf8").includes("engine is unavailable")) {
      fail(`${skill.name}: sources.json present but SKILL.md lacks the "engine is unavailable" fallback marker (LD-5)`);
    }
  }
}

function parseRegistry(path: string): Record<string, string>[] {
  const entries: Record<string, string>[] = [];
  let current: Record<string, string> | null = null;
  for (const line of readFileSync(path, "utf8").split(/\r?\n/)) {
    const start = line.match(/^  - id:\s*(.+)$/);
    const field = line.match(/^    ([\w_]+):\s*(.+)$/);
    if (start) { current = { id: start[1].trim() }; entries.push(current); }
    else if (field && current) current[field[1]] = field[2].trim();
  }
  return entries;
}

function checkRegistryEntry(e: Record<string, string>): void {
  const tag = `registry entry "${e.id}"`;
  if (!STATUSES.includes(e.status)) fail(`${tag}: invalid status "${e.status}" (expected one of ${STATUSES.join("|")})`);
  if (!TIERS.includes(e.permission_tier)) fail(`${tag}: invalid permission_tier "${e.permission_tier}"`);
  if (!e.rationale) fail(`${tag}: rationale missing`);
  if (e.status === "adopted" && e.resolved_path && !existsSync(join(ROOT, e.resolved_path))) {
    fail(`${tag}: resolved_path "${e.resolved_path}" does not exist`);
  }
}

function checkRegistry(path: string): void {
  if (!existsSync(path)) { fail(`registry not found: ${path}`); return; }
  const entries = parseRegistry(path);
  if (entries.length === 0) { fail(`registry has no parsable candidates: ${path}`); return; }
  for (const e of entries) checkRegistryEntry(e);
}

function checkIndexFreshness(skillFiles: string[]): void {
  const indexPath = join(ROOT, "INDEX.md");
  if (!existsSync(indexPath)) { warn("INDEX.md missing — run: node scripts/build-index.ts"); return; }
  const indexTime = statSync(indexPath).mtimeMs;
  const stale = skillFiles.some((f) => statSync(f).mtimeMs > indexTime);
  if (stale) warn("INDEX.md older than a library SKILL.md — run: node scripts/build-index.ts");
}

const skillFiles = checkSkills(values["skills-dir"]!);
checkScripts(values["skills-dir"]!);
checkSources(values["skills-dir"]!);
checkRegistry(values.registry!);
checkIndexFreshness(skillFiles);

for (const f of findings) console.log(`${f.level}: ${f.msg}`);
const failures = findings.filter((f) => f.level === "FAIL").length;
console.log(`\nskill-audit: ${skillFiles.length} library skill(s), ${failures} failure(s), ${findings.length - failures} warning(s)`);
process.exit(failures > 0 ? 1 : 0);
