#!/usr/bin/env bun
/**
 * skill-sync — deploys this repo's portable library skills to local consumers.
 *
 * Dry-run by default (prints planned actions); --apply executes (LD-3).
 * Engine skills are structurally separate under engine/skills and are never
 * part of the deployable library inventory.
 *
 * Library skills may be organized under category folders inside `skills/`.
 * Installation remains flat by stable skill ID unless a target adapter says
 * otherwise, so repository browsing structure does not change host skill IDs.
 *
 * Targets (composable):
 *   --claude-user [--claude-user-root <path>]  junction per skill
 *                                              (default root: ~/.claude/skills)
 *   --dest <path>                              recursive copy per skill
 *   --coreforge <path>                         Synapse-style manifest.json + files
 */

import { parseArgs } from "node:util";
import {
  readdirSync, readFileSync, existsSync, mkdirSync,
  cpSync, rmSync, symlinkSync, realpathSync, writeFileSync,
} from "node:fs";
import { join, dirname, relative } from "node:path";
import { homedir } from "node:os";
import { fileURLToPath } from "node:url";
import { parseFrontmatter } from "../../../../scripts/lib/frontmatter.ts";
import { discoverSkillDirs } from "../../../../scripts/lib/skill-discovery.ts";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..", "..", "..", "..");

const { values } = parseArgs({
  options: {
    apply: { type: "boolean", default: false },
    "claude-user": { type: "boolean", default: false },
    "claude-user-root": { type: "string", default: join(homedir(), ".claude", "skills") },
    dest: { type: "string" },
    coreforge: { type: "string" },
    hosts: { type: "string" },
    help: { type: "boolean", default: false },
  },
});

if (values.help) {
  console.log("skill-sync — deploy portable library skills\n\nUsage: node sync.ts [--apply] [--claude-user] [--claude-user-root <path>] [--dest <path>] [--coreforge <path>] [--hosts <targetRepo>]");
  process.exit(0);
}

const mode = values.apply ? "apply" : "dry-run";

interface Skill { name: string; dir: string; fm: Record<string, any>; repoBound: boolean; }

function discoverSkills(): Skill[] {
  return discoverSkillDirs(join(ROOT, "skills")).map((skill) => {
    const fm = parseFrontmatter(readFileSync(skill.skillFile, "utf8")) ?? {};
    return {
      name: fm.name ?? skill.name,
      dir: skill.dir,
      fm,
      repoBound: fm.metadata?.["repo-bound"] === "true",
    };
  });
}

function listFiles(dir: string): string[] {
  const out: string[] = [];
  for (const entry of readdirSync(dir, { withFileTypes: true })) {
    const p = join(dir, entry.name);
    if (entry.isDirectory()) out.push(...listFiles(p));
    else out.push(p);
  }
  return out;
}

function copyDrift(src: string, dst: string): "create" | "update" | "up-to-date" {
  if (!existsSync(dst)) return "create";
  for (const file of listFiles(src)) {
    const counterpart = join(dst, relative(src, file));
    if (!existsSync(counterpart)) return "update";
    if (!readFileSync(file).equals(readFileSync(counterpart))) return "update";
  }
  return "up-to-date";
}

function syncDest(skill: Skill, destRoot: string): string {
  const dst = join(destRoot, skill.name);
  const action = copyDrift(skill.dir, dst);
  if (values.apply && action !== "up-to-date") cpSync(skill.dir, dst, { recursive: true, force: true });
  return action;
}

function junctionDrift(link: string, target: string): "create" | "update" | "up-to-date" {
  if (!existsSync(link)) return "create";
  try {
    return realpathSync(link) === realpathSync(target) ? "up-to-date" : "update";
  } catch {
    return "update";
  }
}

function syncJunction(skill: Skill, root: string): string {
  const link = join(root, skill.name);
  const action = junctionDrift(link, skill.dir);
  if (values.apply && action !== "up-to-date") {
    mkdirSync(root, { recursive: true });
    if (existsSync(link)) rmSync(link, { recursive: true, force: true });
    symlinkSync(skill.dir, link, "junction");
  }
  return action;
}

function buildManifest(skill: Skill): string {
  const meta = skill.fm.metadata ?? {};
  return JSON.stringify({
    skillId: skill.name,
    name: meta["display-name"] ?? skill.name,
    version: meta.version ?? "0.0.0",
    description: skill.fm.description ?? "",
    category: meta.category ?? "",
    entryPoint: "SKILL.md",
    runtime: "typescript",
    permissions: [],
  }, null, 2) + "\n";
}

function syncCoreforge(skill: Skill, destRoot: string): string {
  const dst = join(destRoot, skill.name);
  const manifestPath = join(dst, "manifest.json");
  const manifest = buildManifest(skill);
  const manifestCurrent = existsSync(manifestPath) && readFileSync(manifestPath, "utf8") === manifest;
  const fileAction = copyDrift(skill.dir, dst);
  let action: string;
  if (!existsSync(dst)) action = "create";
  else if (manifestCurrent && fileAction === "up-to-date") action = "up-to-date";
  else action = "update";
  if (values.apply && action !== "up-to-date") {
    cpSync(skill.dir, dst, { recursive: true, force: true });
    writeFileSync(manifestPath, manifest);
  }
  return action;
}

const HOST_DIRS = [".claude", ".kilo", ".codex"];

function syncHosts(skill: Skill, repoRoot: string): string {
  const actions = HOST_DIRS.map((h) => {
    const dst = join(repoRoot, h, "skills", skill.name);
    const action = copyDrift(skill.dir, dst);
    if (values.apply && action !== "up-to-date") cpSync(skill.dir, dst, { recursive: true, force: true });
    return action;
  });
  const unique = [...new Set(actions)];
  if (unique.length === 1) return unique[0];
  return actions.map((a, i) => `${HOST_DIRS[i]}:${a}`).join(" ");
}

const targets: Array<{ label: string; fn: (s: Skill) => string }> = [];
if (values["claude-user"]) targets.push({ label: `claude-user(${values["claude-user-root"]})`, fn: (s) => syncJunction(s, values["claude-user-root"]!) });
if (values.dest) targets.push({ label: `dest(${values.dest})`, fn: (s) => syncDest(s, values.dest!) });
if (values.coreforge) targets.push({ label: `coreforge(${values.coreforge})`, fn: (s) => syncCoreforge(s, values.coreforge!) });
if (values.hosts) targets.push({ label: `hosts(${values.hosts})`, fn: (s) => syncHosts(s, values.hosts!) });

if (targets.length === 0) {
  console.log("No targets given. Use --claude-user, --dest <path>, --coreforge <path>, and/or --hosts <path>.");
  process.exit(0);
}

for (const target of targets) {
  for (const skill of discoverSkills()) {
    const action = skill.repoBound ? "skip:repo-bound" : target.fn(skill);
    console.log(`[${mode}] ${target.label} ${skill.name}: ${action}`);
  }
}
