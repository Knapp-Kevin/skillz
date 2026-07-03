#!/usr/bin/env bun
/**
 * build-index.ts — regenerates the skill index for this repo.
 *
 * Scans skills/<name>/SKILL.md frontmatter plus the vendored
 * knowledge-work-plugins marketplace, and writes:
 *   - index.json  (machine-readable registry for agents/tooling)
 *   - INDEX.md    (human/agent-readable table with relative links)
 *
 * Usage (Bun or Node 22.18+):
 *   node scripts/build-index.ts
 *   bun run scripts/build-index.ts
 *
 * Zero dependencies. The YAML handling is a minimal parser that covers
 * the frontmatter shapes used in this repo and in Anthropic's plugins
 * (scalars, >- folded blocks, one nested map level, simple lists).
 */

import { readdirSync, readFileSync, writeFileSync, existsSync } from "node:fs";
import { join, relative, sep } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = fileURLToPath(new URL("..", import.meta.url));

// ── Minimal frontmatter parser ───────────────────────────────────────

function parseFrontmatter(md: string): Record<string, any> | null {
  const m = md.match(/^---\r?\n([\s\S]*?)\r?\n---/);
  if (!m) return null;
  const lines = m[1].split(/\r?\n/);
  const out: Record<string, any> = {};
  let i = 0;

  function parseBlock(indent: number): Record<string, any> {
    const obj: Record<string, any> = {};
    while (i < lines.length) {
      const line = lines[i];
      if (!line.trim()) { i++; continue; }
      const curIndent = line.length - line.trimStart().length;
      if (curIndent < indent) break;
      if (curIndent > indent) { i++; continue; } // stray deeper line; skip
      const kv = line.trim().match(/^([\w][\w.-]*):\s*(.*)$/);
      if (!kv) { i++; continue; }
      const key = kv[1];
      let val = kv[2];
      i++;
      if (val === ">-" || val === ">" || val === "|" || val === "|-") {
        // folded/literal block: collect deeper-indented lines
        const parts: string[] = [];
        while (i < lines.length) {
          const l = lines[i];
          if (l.trim() && l.length - l.trimStart().length <= indent) break;
          if (l.trim()) parts.push(l.trim());
          i++;
        }
        obj[key] = parts.join(" ");
      } else if (val === "") {
        // nested map or list
        if (i < lines.length && lines[i].trim().startsWith("- ")) {
          const arr: string[] = [];
          while (i < lines.length && lines[i].trim().startsWith("- ")) {
            arr.push(lines[i].trim().slice(2).replace(/^["']|["']$/g, ""));
            i++;
          }
          obj[key] = arr;
        } else if (i < lines.length && lines[i].length - lines[i].trimStart().length > indent) {
          obj[key] = parseBlock(lines[i].length - lines[i].trimStart().length);
        } else {
          obj[key] = "";
        }
      } else {
        obj[key] = val.replace(/^["']|["']$/g, "");
      }
    }
    return obj;
  }

  Object.assign(out, parseBlock(0));
  return out;
}

function relPosix(p: string): string {
  return relative(ROOT, p).split(sep).join("/");
}

// ── Local skills ─────────────────────────────────────────────────────

interface LocalSkill {
  name: string;
  displayName?: string;
  description: string;
  category?: string;
  version?: string;
  path: string;
  skillFile: string;
  scripts: string[];
}

function scanLocalSkills(): LocalSkill[] {
  const dir = join(ROOT, "skills");
  if (!existsSync(dir)) return [];
  const skills: LocalSkill[] = [];
  for (const entry of readdirSync(dir, { withFileTypes: true })) {
    if (!entry.isDirectory()) continue;
    const skillFile = join(dir, entry.name, "SKILL.md");
    if (!existsSync(skillFile)) continue;
    const fm = parseFrontmatter(readFileSync(skillFile, "utf8"));
    if (!fm?.name) {
      console.error(`[index] WARN: ${relPosix(skillFile)} has no parsable frontmatter name; skipped`);
      continue;
    }
    if (fm.name !== entry.name) {
      console.error(`[index] WARN: frontmatter name "${fm.name}" != directory "${entry.name}"`);
    }
    const scriptsDir = join(dir, entry.name, "scripts");
    const scripts = existsSync(scriptsDir)
      ? readdirSync(scriptsDir).map((f) => relPosix(join(scriptsDir, f)))
      : [];
    skills.push({
      name: fm.name,
      displayName: fm.metadata?.["display-name"],
      description: fm.description ?? "",
      category: fm.metadata?.category,
      version: fm.metadata?.version,
      path: relPosix(join(dir, entry.name)),
      skillFile: relPosix(skillFile),
      scripts,
    });
  }
  return skills.sort((a, b) => a.name.localeCompare(b.name));
}

// ── Vendored knowledge-work-plugins ──────────────────────────────────

interface VendorSkill { name: string; description: string; skillFile: string; }
interface VendorPlugin { name: string; displayName?: string; description: string; path: string; skills: VendorSkill[]; }

interface ExternalPlugin { name: string; description: string; }

function scanVendorPlugins(): { local: VendorPlugin[]; external: ExternalPlugin[] } {
  const base = join(ROOT, "vendor", "knowledge-work-plugins");
  const marketplaceFile = join(base, ".claude-plugin", "marketplace.json");
  if (!existsSync(marketplaceFile)) return { local: [], external: [] };
  const marketplace = JSON.parse(readFileSync(marketplaceFile, "utf8"));
  const plugins: VendorPlugin[] = [];
  const external: ExternalPlugin[] = [];
  for (const p of marketplace.plugins ?? []) {
    if (typeof p.source !== "string") {
      // Partner-built plugin hosted in an external repo; listed by name only.
      external.push({ name: p.name, description: p.description ?? "" });
      continue;
    }
    const pluginDir = join(base, p.source.replace(/^\.\//, ""));
    const skillsDir = join(pluginDir, "skills");
    const skills: VendorSkill[] = [];
    if (existsSync(skillsDir)) {
      for (const entry of readdirSync(skillsDir, { withFileTypes: true })) {
        if (!entry.isDirectory()) continue;
        const skillFile = join(skillsDir, entry.name, "SKILL.md");
        if (!existsSync(skillFile)) continue;
        const fm = parseFrontmatter(readFileSync(skillFile, "utf8"));
        skills.push({
          name: fm?.name ?? entry.name,
          description: fm?.description ?? "",
          skillFile: relPosix(skillFile),
        });
      }
    }
    plugins.push({
      name: p.name,
      displayName: p.displayName,
      description: p.description ?? "",
      path: relPosix(pluginDir),
      skills: skills.sort((a, b) => a.name.localeCompare(b.name)),
    });
  }
  return {
    local: plugins.sort((a, b) => a.name.localeCompare(b.name)),
    external: external.sort((a, b) => a.name.localeCompare(b.name)),
  };
}

// ── Emit ─────────────────────────────────────────────────────────────

const localSkills = scanLocalSkills();
const { local: vendorPlugins, external: externalPlugins } = scanVendorPlugins();

const index = {
  version: 1,
  generated: new Date().toISOString(),
  repo: "skillz",
  root: "https://github.com/Knapp-Kevin/skillz",
  skills: localSkills,
  vendor: {
    "knowledge-work-plugins": {
      source: "https://github.com/anthropics/knowledge-work-plugins",
      install: "/plugin marketplace add anthropics/knowledge-work-plugins",
      plugins: vendorPlugins,
      externalPartnerPlugins: externalPlugins,
    },
  },
};

writeFileSync(join(ROOT, "index.json"), JSON.stringify(index, null, 2) + "\n");

function truncate(s: string, n: number): string {
  const clean = s.replace(/\s+/g, " ").trim();
  return clean.length <= n ? clean : clean.slice(0, n - 1).trimEnd() + "…";
}

let md = `# Skill Index

> Generated by \`scripts/build-index.ts\` — do not edit by hand.
> Regenerate with \`node scripts/build-index.ts\` after adding or changing a skill.
> Machine-readable version: [index.json](index.json)

## How agents should use this

1. Read this file (or \`index.json\`) to find a skill by name/description.
2. Read the linked \`SKILL.md\` and follow its Execution Flow section.
3. Scripts listed for a skill run with Bun or Node 22.18+, zero install, from the skill's directory.

## Local skills (\`skills/\`)

| Skill | Category | Description | Scripts |
|-------|----------|-------------|---------|
`;

for (const s of localSkills) {
  const scripts = s.scripts.map((p) => `[${p.split("/").pop()}](${p})`).join(", ") || "—";
  md += `| [${s.name}](${s.skillFile}) | ${s.category ?? "—"} | ${truncate(s.description, 160)} | ${scripts} |\n`;
}

md += `\n## Vendored: [knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) (\`vendor/\`)

Anthropic's official knowledge-work plugin marketplace, vendored as a git submodule.
Install directly instead via \`/plugin marketplace add anthropics/knowledge-work-plugins\`.
`;

for (const p of vendorPlugins) {
  md += `\n### ${p.displayName ?? p.name}\n\n${truncate(p.description, 220)}\n\n`;
  if (p.skills.length === 0) {
    md += `_No skills directory._\n`;
    continue;
  }
  md += `| Skill | Description |\n|-------|-------------|\n`;
  for (const s of p.skills) {
    md += `| [${s.name}](${s.skillFile}) | ${truncate(s.description, 160)} |\n`;
  }
}

if (externalPlugins.length > 0) {
  md += `\n### External partner plugins (hosted outside the submodule)

Registered in the marketplace but sourced from partner repos — install via the marketplace command above, then \`/plugin install <name>@knowledge-work-plugins\`.

| Plugin | Description |
|--------|-------------|
`;
  for (const p of externalPlugins) {
    md += `| ${p.name} | ${truncate(p.description, 160)} |\n`;
  }
}

writeFileSync(join(ROOT, "INDEX.md"), md);

const vendorSkillCount = vendorPlugins.reduce((n, p) => n + p.skills.length, 0);
console.error(
  `[index] Wrote index.json + INDEX.md — ${localSkills.length} local skill(s), ` +
  `${vendorPlugins.length} vendored plugin(s) with ${vendorSkillCount} skill(s), ` +
  `${externalPlugins.length} external partner plugin(s).`
);
