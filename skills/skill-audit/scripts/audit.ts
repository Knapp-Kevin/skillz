#!/usr/bin/env bun
/**
 * skill-audit — validates this repo's skills, scripts, and intake registry.
 *
 * Usage (Bun or Node 22.18+, from repo root or anywhere):
 *   node skills/skill-audit/scripts/audit.ts
 *   node skills/skill-audit/scripts/audit.ts --skills-dir <path> --registry <path>
 *
 * Exit 0 = clean (warnings allowed). Exit 1 = one or more FAIL findings.
 * Registry parsing is a purpose-built block parser for candidates.yaml's
 * regular shape (see registry file header), not a general YAML parser.
 */

import { parseArgs } from "node:util";
import { readdirSync, readFileSync, existsSync, statSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";
import { spawnSync } from "node:child_process";
import { parseFrontmatter } from "../../../scripts/lib/frontmatter.ts";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..", "..", "..");
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

// ── Check 1: SKILL.md frontmatter conventions ────────────────────────

function checkSkillFile(dir: string, skillFile: string): void {
  const fm = parseFrontmatter(readFileSync(skillFile, "utf8"));
  if (!fm) { fail(`${dir}: SKILL.md frontmatter does not parse`); return; }
  if (fm.name !== dir) fail(`${dir}: frontmatter name "${fm.name}" != directory "${dir}"`);
  const desc = typeof fm.description === "string" ? fm.description : "";
  if (!desc.trim()) fail(`${dir}: description missing or empty`);
  else if (!desc.includes("Use when")) fail(`${dir}: description lacks "Use when" trigger guidance`);
  if (!fm.metadata?.version) fail(`${dir}: metadata.version missing`);
}

function checkSkills(skillsDir: string): string[] {
  const skillFiles: string[] = [];
  for (const entry of readdirSync(skillsDir, { withFileTypes: true })) {
    if (!entry.isDirectory()) continue;
    const skillFile = join(skillsDir, entry.name, "SKILL.md");
    if (!existsSync(skillFile)) { fail(`${entry.name}: no SKILL.md`); continue; }
    checkSkillFile(entry.name, skillFile);
    skillFiles.push(skillFile);
  }
  return skillFiles;
}

// ── Check 2: every skill + repo script answers --help with exit 0 ───

function checkHelp(file: string, label: string): void {
  const res = spawnSync(process.execPath, [file, "--help"], { timeout: 30_000, encoding: "utf8" });
  if (res.status !== 0) fail(`${label}: --help exited ${res.status}`);
}

function checkScripts(skillsDir: string): void {
  for (const entry of readdirSync(skillsDir, { withFileTypes: true })) {
    if (!entry.isDirectory()) continue;
    const scriptsDir = join(skillsDir, entry.name, "scripts");
    if (!existsSync(scriptsDir)) continue;
    for (const f of readdirSync(scriptsDir).filter((f) => f.endsWith(".ts"))) {
      checkHelp(join(scriptsDir, f), `${entry.name}/scripts/${f}`);
    }
  }
  // Repo-level tooling scripts share the same contract (FEATURE_INDEX FX07).
  const repoScripts = join(ROOT, "scripts");
  for (const f of readdirSync(repoScripts).filter((f) => f.endsWith(".ts"))) {
    checkHelp(join(repoScripts, f), `scripts/${f}`);
  }
}

// ── Check 2b: sources.json parses; engine consumers carry the fallback marker ──

function checkSources(skillsDir: string): void {
  for (const entry of readdirSync(skillsDir, { withFileTypes: true })) {
    if (!entry.isDirectory()) continue;
    const sources = join(skillsDir, entry.name, "sources.json");
    if (!existsSync(sources)) continue;
    try {
      JSON.parse(readFileSync(sources, "utf8"));
    } catch {
      fail(`${entry.name}: sources.json does not parse as JSON`);
    }
    const skillFile = join(skillsDir, entry.name, "SKILL.md");
    if (existsSync(skillFile) && !readFileSync(skillFile, "utf8").includes("engine is unavailable")) {
      fail(`${entry.name}: sources.json present but SKILL.md lacks the "engine is unavailable" fallback marker (LD-5)`);
    }
  }
}

// ── Check 3: registry lint ───────────────────────────────────────────

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

// ── Check 4 (WARN): index freshness by mtime ─────────────────────────

function checkIndexFreshness(skillFiles: string[]): void {
  const indexPath = join(ROOT, "INDEX.md");
  if (!existsSync(indexPath)) { warn("INDEX.md missing — run: node scripts/build-index.ts"); return; }
  const indexTime = statSync(indexPath).mtimeMs;
  const stale = skillFiles.some((f) => statSync(f).mtimeMs > indexTime);
  if (stale) warn("INDEX.md older than a SKILL.md — run: node scripts/build-index.ts");
}

// ── Main ─────────────────────────────────────────────────────────────

const skillFiles = checkSkills(values["skills-dir"]!);
checkScripts(values["skills-dir"]!);
checkSources(values["skills-dir"]!);
checkRegistry(values.registry!);
checkIndexFreshness(skillFiles);

for (const f of findings) console.log(`${f.level}: ${f.msg}`);
const failures = findings.filter((f) => f.level === "FAIL").length;
console.log(`\nskill-audit: ${skillFiles.length} skill(s), ${failures} failure(s), ${findings.length - failures} warning(s)`);
process.exit(failures > 0 ? 1 : 0);
