#!/usr/bin/env bun
/**
 * pulse-run.ts — generic pulse collector driven by a per-skill sources.json.
 *
 * One engine for the whole pulse series (openai-pulse, gemini-pulse, ...):
 * the skill's sources.json declares WHAT to scan; this script fetches and
 * prints a markdown skeleton; the model does the synthesis per the skill's
 * SKILL.md. Zero dependencies, Bun or Node 22.18+.
 *
 * Usage:
 *   node scripts/pulse-run.ts --sources skills/openai-pulse/sources.json
 *   node scripts/pulse-run.ts --sources <path> --since 30d
 *
 * sources.json fields (all optional except name):
 *   name           display name
 *   github         ["org/repo", ...]        commits-in-window + latest release
 *   github_orgs    ["org", ...]             org repos pushed within window
 *   github_search  [{label, q}, ...]        repo search; "{SINCE}" in q -> date
 *   changelogs     [{label, url}, ...]      fetch text, surface dated lines
 *   subreddits     ["Name", ...]            recent posts (403 -> web-search note)
 *   keywords       ["term", ...]            relevance filter for subreddits
 *   pages          [{label, url}, ...]      echoed for the model to fetch
 *   searches       ["query", ...]           echoed for the model to web-search
 */

import { parseArgs } from "node:util";
import { readFileSync } from "node:fs";

const { values } = parseArgs({
  options: {
    sources: { type: "string" },
    since: { type: "string", default: "7d" },
    help: { type: "boolean", default: false },
  },
});

if (values.help || !values.sources) {
  console.log("pulse-run — generic pulse collector\n\nUsage: node scripts/pulse-run.ts --sources <sources.json> [--since Nd] [--help]");
  process.exit(0);
}

const spec = JSON.parse(readFileSync(values.sources, "utf8"));
const sinceDays = parseInt(values.since!.replace(/d$/, ""), 10) || 7;
const sinceDate = new Date(Date.now() - sinceDays * 24 * 60 * 60 * 1000);
const sinceStr = sinceDate.toISOString().split("T")[0];
const today = new Date().toISOString().split("T")[0];

console.error(`[pulse-run] ${spec.name}: scanning since ${sinceStr} (${sinceDays}d)\n`);

async function fetchText(url: string, headers: Record<string, string> = {}): Promise<string> {
  const resp = await fetch(url, { headers: { "User-Agent": "SkillzPulse/1.0", ...headers } });
  if (!resp.ok) {
    console.error(`[pulse-run] WARN: ${url} returned ${resp.status}`);
    return "";
  }
  return resp.text();
}

async function gh(path: string): Promise<any> {
  const token = process.env.GITHUB_TOKEN;
  const text = await fetchText(`https://api.github.com${path}`, {
    Accept: "application/vnd.github+json",
    ...(token ? { Authorization: `Bearer ${token}` } : {}),
  });
  try { return text ? JSON.parse(text) : null; } catch { return null; }
}

async function repoActivity(repo: string): Promise<string> {
  const [commits, release] = await Promise.all([
    gh(`/repos/${repo}/commits?since=${sinceDate.toISOString()}&per_page=30`),
    gh(`/repos/${repo}/releases/latest`),
  ]);
  const list = Array.isArray(commits) ? commits : [];
  let out = `### ${repo}\n\n`;
  if (list.length === 0) out += `_No commits in window._`;
  else {
    out += `**${list.length} commit(s)**:\n`;
    for (const c of list.slice(0, 6)) out += `- ${(c.commit?.message ?? "").split("\n")[0]}\n`;
    if (list.length > 6) out += `- …and ${list.length - 6} more\n`;
  }
  if (release?.tag_name) out += `\nLatest release: **${release.tag_name}** (${release.published_at?.split("T")[0] ?? "?"})`;
  return out + "\n";
}

async function orgActivity(org: string): Promise<string> {
  const repos = await gh(`/orgs/${org}/repos?sort=pushed&per_page=15`);
  if (!Array.isArray(repos)) return `### org:${org}\n\n_Unavailable._\n`;
  const active = repos.filter((r: any) => (r.pushed_at ?? "") >= sinceDate.toISOString());
  let out = `### org:${org} — ${active.length} repo(s) pushed in window\n\n`;
  for (const r of active.slice(0, 10)) out += `- **${r.name}** (★${r.stargazers_count}): ${r.description ?? ""}\n`;
  return out;
}

async function searchRepos(entry: { label: string; q: string }): Promise<string> {
  const q = entry.q.replace("{SINCE}", sinceStr);
  const data = await gh(`/search/repositories?q=${encodeURIComponent(q)}&sort=stars&order=desc&per_page=10`);
  let out = `### search: ${entry.label}\n\n`;
  if (!Array.isArray(data?.items)) return out + `_Search unavailable._\n`;
  for (const r of data.items) out += `- **[${r.full_name}](${r.html_url})** (★${r.stargazers_count}): ${(r.description ?? "").slice(0, 120)}\n`;
  return out;
}

async function changelogLines(entry: { label: string; url: string }): Promise<string> {
  const text = await fetchText(entry.url);
  let out = `### changelog: ${entry.label}\n\n`;
  if (!text) return out + `_Unavailable — fetch ${entry.url} manually._\n`;
  const dated = text.split("\n").filter((l) => {
    const m = l.match(/(\d{4}-\d{2}-\d{2})/);
    return m ? m[1] >= sinceStr : false;
  });
  if (dated.length > 0) {
    for (const l of dated.slice(0, 12)) out += `- ${l.trim().replace(/^[#*-]+\s*/, "")}\n`;
  } else {
    const headers = text.split("\n").filter((l) => l.startsWith("## ")).slice(0, 4);
    out += headers.length ? `_No dated lines in window; recent sections:_\n` : `_No dated lines found._\n`;
    for (const h of headers) out += `- ${h.replace(/^#+\s*/, "")}\n`;
  }
  return out;
}

const REDDIT_UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36";

function redditRelevant(post: any, keywords: string[]): boolean {
  if (keywords.length === 0) return true;
  const text = `${post.title} ${post.selftext ?? ""}`.toLowerCase();
  return keywords.some((k) => text.includes(k.toLowerCase()));
}

async function subredditPosts(sub: string, keywords: string[]): Promise<string> {
  const text = await fetchText(`https://www.reddit.com/r/${sub}/new.json?limit=40`, { "User-Agent": REDDIT_UA });
  let out = `### r/${sub}\n\n`;
  let data: any = null;
  try { data = text ? JSON.parse(text) : null; } catch { data = null; }
  if (!data?.data?.children) {
    return out + `_Reddit JSON API blocked or empty — use web search (see SKILL.md fallback)._\n`;
  }
  const posts = data.data.children.map((c: any) => c.data)
    .filter((p: any) => new Date(p.created_utc * 1000) >= sinceDate)
    .filter((p: any) => redditRelevant(p, keywords))
    .sort((a: any, b: any) => b.score - a.score)
    .slice(0, 8);
  if (posts.length === 0) return out + `_No relevant threads in window._\n`;
  for (const p of posts) out += `- **[${p.score}⬆ ${p.num_comments}💬]** ${p.title} — [link](https://www.reddit.com${p.permalink})\n`;
  return out;
}

async function main() {
  const sections: string[] = [`# ${spec.name} — ${sinceStr} to ${today}\n`];

  const repoResults = await Promise.all((spec.github ?? []).map(repoActivity));
  if (repoResults.length) sections.push(`## Repo activity\n`, ...repoResults);

  const orgResults = await Promise.all((spec.github_orgs ?? []).map(orgActivity));
  if (orgResults.length) sections.push(`## Org activity\n`, ...orgResults);

  const searchResults = await Promise.all((spec.github_search ?? []).map(searchRepos));
  if (searchResults.length) sections.push(`## GitHub repo search\n`, ...searchResults);

  const changelogResults = await Promise.all((spec.changelogs ?? []).map(changelogLines));
  if (changelogResults.length) sections.push(`## Changelogs\n`, ...changelogResults);

  const redditResults = await Promise.all(
    (spec.subreddits ?? []).map((s: string) => subredditPosts(s, spec.keywords ?? [])),
  );
  if (redditResults.length) sections.push(`## Community\n`, ...redditResults);

  if (spec.pages?.length) {
    sections.push(`## Pages for the model to fetch\n`);
    for (const p of spec.pages) sections.push(`- ${p.label}: ${p.url}`);
    sections.push("");
  }
  if (spec.searches?.length) {
    sections.push(`## Web searches for the model to run\n`);
    for (const s of spec.searches) sections.push(`- \`${s}\``);
    sections.push("");
  }
  console.log(sections.join("\n"));
}

main().catch((err) => {
  console.error("[pulse-run] FATAL:", err);
  process.exit(1);
});
