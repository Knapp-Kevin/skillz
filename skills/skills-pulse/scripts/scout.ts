#!/usr/bin/env bun
/**
 * Skills Pulse — scans the agent-skills source watchlist for new activity
 * and prints a markdown skeleton for intake review.
 *
 * Usage (Bun or Node 22.18+):
 *   node scripts/scout.ts               # default: last 7 days
 *   node scripts/scout.ts --since 30d
 *
 * Sources: GitHub repos on the watchlist (commits + latest release).
 * Marketplaces without APIs (skills.sh, mcpmarket, etc.) are covered by
 * the web-search step in SKILL.md, not this script.
 */

import { parseArgs } from "node:util";

const { values } = parseArgs({
  options: {
    since: { type: "string", default: "7d" },
    help: { type: "boolean", default: false },
  },
});

if (values.help) {
  console.log(`Skills Pulse — watchlist activity scan

Usage:
  node scripts/scout.ts [--since Nd] [--help]
`);
  process.exit(0);
}

const sinceDays = parseInt(values.since!.replace(/d$/, ""), 10) || 7;
const sinceDate = new Date(Date.now() - sinceDays * 24 * 60 * 60 * 1000);
const sinceISO = sinceDate.toISOString();
const sinceStr = sinceISO.split("T")[0];

// GitHub repos on the watchlist. vendored: true means the repo is a
// submodule under vendor/ and stale activity implies `git submodule
// update --remote` + index regeneration.
const WATCHLIST = [
  { repo: "anthropics/skills", vendored: true },
  { repo: "anthropics/knowledge-work-plugins", vendored: true },
  { repo: "vercel-labs/agent-skills", vendored: true },
  { repo: "microsoft/skills", vendored: true },
  { repo: "microsoft/azure-skills", vendored: true },
  { repo: "aws/agent-toolkit-for-aws", vendored: true },
  { repo: "hashicorp/agent-skills", vendored: false },
  { repo: "obra/superpowers", vendored: false },
];

async function gh(path: string): Promise<any> {
  const resp = await fetch(`https://api.github.com${path}`, {
    headers: {
      "User-Agent": "SkillsPulse/1.0",
      Accept: "application/vnd.github+json",
      ...(process.env.GITHUB_TOKEN ? { Authorization: `Bearer ${process.env.GITHUB_TOKEN}` } : {}),
    },
  });
  if (!resp.ok) {
    console.error(`[scout] WARN: ${path} returned ${resp.status}`);
    return null;
  }
  return resp.json();
}

interface RepoActivity {
  repo: string;
  vendored: boolean;
  commitCount: number;
  commitSubjects: string[];
  latestRelease: string | null;
  releaseDate: string | null;
}

async function scan(entry: { repo: string; vendored: boolean }): Promise<RepoActivity> {
  const [commits, release] = await Promise.all([
    gh(`/repos/${entry.repo}/commits?since=${sinceISO}&per_page=50`),
    gh(`/repos/${entry.repo}/releases/latest`),
  ]);
  const list = Array.isArray(commits) ? commits : [];
  return {
    repo: entry.repo,
    vendored: entry.vendored,
    commitCount: list.length,
    commitSubjects: list.slice(0, 8).map((c: any) => (c.commit?.message ?? "").split("\n")[0]),
    latestRelease: release?.tag_name ?? null,
    releaseDate: release?.published_at?.split("T")[0] ?? null,
  };
}

async function main() {
  console.error(`[scout] Scanning watchlist since ${sinceStr} (${sinceDays}d window)\n`);
  const results = await Promise.all(WATCHLIST.map(scan));
  const today = new Date().toISOString().split("T")[0];

  let out = `# Skills Pulse — ${sinceStr} to ${today}\n\n## Watchlist repo activity\n\n`;
  for (const r of results) {
    const badge = r.vendored ? " (vendored)" : "";
    out += `### ${r.repo}${badge}\n\n`;
    if (r.commitCount === 0) {
      out += `_No commits in window._`;
    } else {
      out += `**${r.commitCount} commit(s)** in window:\n`;
      for (const s of r.commitSubjects) out += `- ${s}\n`;
      if (r.commitCount > r.commitSubjects.length) out += `- …and ${r.commitCount - r.commitSubjects.length} more\n`;
    }
    if (r.latestRelease) out += `\nLatest release: **${r.latestRelease}** (${r.releaseDate})`;
    out += `\n\n`;
  }

  const staleVendored = results.filter((r) => r.vendored && r.commitCount > 0);
  if (staleVendored.length > 0) {
    out += `## Vendored submodules with upstream activity\n\n`;
    out += `Refresh and re-index:\n\n\`\`\`\ngit submodule update --remote\nnode scripts/build-index.ts\n\`\`\`\n\n`;
    out += staleVendored.map((r) => `- ${r.repo}`).join("\n") + "\n";
  }

  console.log(out);
}

main().catch((err) => {
  console.error("[scout] FATAL:", err);
  process.exit(1);
});
