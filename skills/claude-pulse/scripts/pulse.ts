#!/usr/bin/env bun
/**
 * Claude Pulse — fetches official Claude releases + community commentary
 * and writes a synthesized markdown digest to stdout.
 *
 * Usage (Bun or Node 22.18+ — both run TypeScript natively):
 *   bun run scripts/pulse.ts              # default: last 7 days
 *   node scripts/pulse.ts --since 30d     # last 30 days
 *   bun run scripts/pulse.ts --since 3d   # last 3 days
 *
 * Sources:
 *   - Claude Code CHANGELOG.md (GitHub raw)
 *   - Claude Code GitHub Releases
 *   - Claude Dev Platform release notes
 *   - Anthropic blog (claude.com/blog)
 *   - Reddit: r/ClaudeAI, r/coding, r/LocalLLaMA (filtered to Claude-relevant)
 *
 * Output: markdown digest to stdout. Save to file or pipe onward.
 */

import { parseArgs } from "node:util";

const { values } = parseArgs({
  options: {
    since: { type: "string", default: "7d" },
    help: { type: "boolean", default: false },
  },
});

if (values.help) {
  console.log(`Claude Pulse — latest Claude updates digest

Usage (Bun or Node 22.18+):
  bun run scripts/pulse.ts [--since Nd] [--help]

Options:
  --since Nd   Time window: 7d (default), 3d, 14d, 30d, etc.
  --help       Show this help
`);
  process.exit(0);
}

const sinceDays = parseInt(values.since!.replace(/d$/, ""), 10) || 7;
const sinceDate = new Date(Date.now() - sinceDays * 24 * 60 * 60 * 1000);
const sinceStr = sinceDate.toISOString().split("T")[0];

console.error(`[pulse] Scanning since ${sinceStr} (${sinceDays}d window)\n`);

interface ChangelogEntry {
  version: string;
  date: string;
  changes: string[];
}

interface ReleaseEntry {
  tag: string;
  name: string;
  publishedAt: string;
  body: string;
  url: string;
}

interface RedditPost {
  title: string;
  subreddit: string;
  score: number;
  numComments: number;
  url: string;
  permalink: string;
  createdUtc: number;
  selftext: string;
}

// ── Helpers ──────────────────────────────────────────────────────────

async function fetchText(url: string, headers: Record<string, string> = {}): Promise<string> {
  const resp = await fetch(url, {
    headers: { "User-Agent": "ClaudePulse/1.0", ...headers },
  });
  if (!resp.ok) {
    console.error(`[pulse] WARN: ${url} returned ${resp.status}`);
    return "";
  }
  return resp.text();
}

const REDDIT_UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36";

async function fetchJSON(url: string, headers: Record<string, string> = {}): Promise<any> {
  const resp = await fetch(url, {
    headers: { "User-Agent": "ClaudePulse/1.0", ...headers },
  });
  if (!resp.ok) {
    console.error(`[pulse] WARN: ${url} returned ${resp.status}`);
    return null;
  }
  return resp.json();
}

// ── Source 1: Claude Code CHANGELOG.md ───────────────────────────────

function parseChangelog(md: string): ChangelogEntry[] {
  const entries: ChangelogEntry[] = [];
  // Matches: ## 2.1.199 (2025-07-02) or ## [2.1.199] ...
  const versionBlocks = md.split(/^## /m).slice(1);
  for (const block of versionBlocks) {
    const lines = block.split("\n");
    const header = lines[0].trim();
    // Extract version and date
    const versionMatch = header.match(/(\d+\.\d+\.\d+)/);
    const dateMatch = header.match(/(\d{4}-\d{2}-\d{2})/);
    if (!versionMatch) continue;

    const version = versionMatch[1];
    const date = dateMatch ? dateMatch[1] : "";
    const changes = lines
      .slice(1)
      .map((l) => l.trim())
      .filter((l) => l.startsWith("- ") || l.startsWith("* "))
      .map((l) => l.replace(/^[-*]\s+/, ""));

    entries.push({ version, date, changes });
  }
  return entries;
}

async function getChangelog(): Promise<ChangelogEntry[]> {
  const url = "https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md";
  const md = await fetchText(url);
  if (!md) return [];
  const all = parseChangelog(md);
  // The Claude Code CHANGELOG rarely carries dates, so --since can't filter
  // it. Entries are newest-first; cap undated ones so a short window doesn't
  // dump the entire version history.
  const undatedCap = Math.max(3, sinceDays);
  let undatedKept = 0;
  return all.filter((e) => {
    if (!e.date) return ++undatedKept <= undatedCap;
    return e.date >= sinceStr;
  });
}

// ── Source 2: GitHub Releases ────────────────────────────────────────

async function getGitHubReleases(): Promise<ReleaseEntry[]> {
  const url = "https://api.github.com/repos/anthropics/claude-code/releases?per_page=10";
  const releases = await fetchJSON(url, { Accept: "application/vnd.github+json" });
  if (!Array.isArray(releases)) return [];

  return releases
    .filter((r: any) => {
      if (!r.published_at) return false;
      return new Date(r.published_at).toISOString().split("T")[0] >= sinceStr;
    })
    .map((r: any) => ({
      tag: r.tag_name,
      name: r.name || r.tag_name,
      publishedAt: r.published_at,
      body: (r.body || "").slice(0, 500),
      url: r.html_url,
    }));
}

// ── Source 3: Dev Platform release notes ─────────────────────────────

async function getDevPlatformNotes(): Promise<string> {
  const url = "https://platform.claude.com/docs/en/release-notes/overview.md";
  return await fetchText(url);
}

// ── Source 4: Reddit (JSON API) ──────────────────────────────────────

const CLAUDE_KEYWORDS = [
  "claude", "anthropic", "opus", "sonnet", "haiku",
  "claude code", "claude.ai", "claudeai", "artifacts",
  "cowork", "computer use",
];

function isClaudeRelevant(text: string): boolean {
  const lower = text.toLowerCase();
  return CLAUDE_KEYWORDS.some((kw) => lower.includes(kw));
}

async function getRedditPosts(subreddit: string, limit = 25): Promise<RedditPost[]> {
  const url = `https://www.reddit.com/r/${subreddit}/new.json?limit=${limit}`;
  try {
    const data = await fetchJSON(url, {
      "User-Agent": REDDIT_UA,
      "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
      "Accept-Language": "en-US,en;q=0.9",
    });
    if (!data?.data?.children) {
      // fetchJSON returns null on HTTP errors (Reddit 403s data-center IPs)
      // rather than throwing, so surface the fallback note here too.
      console.error(`[pulse] NOTE: Reddit JSON API blocked or empty for r/${subreddit}. Use web search for Reddit discourse (see SKILL.md).`);
      return [];
    }

    const posts: RedditPost[] = data.data.children
      .map((c: any) => c.data)
      .filter((p: any) => {
        const created = new Date(p.created_utc * 1000);
        return created >= sinceDate;
      })
      .filter((p: any) => {
        // For Claude-specific sub, keep all. For others, filter by relevance.
        if (subreddit.toLowerCase() === "claudeai") return true;
        return isClaudeRelevant(`${p.title} ${p.selftext || ""}`);
      })
      .map((p: any) => ({
        title: p.title,
        subreddit: `r/${subreddit}`,
        score: p.score,
        numComments: p.num_comments,
        url: p.url,
        permalink: `https://www.reddit.com${p.permalink}`,
        createdUtc: p.created_utc,
        selftext: (p.selftext || "").slice(0, 200),
      }));

    return posts;
  } catch (e: any) {
    // Reddit blocks data-center IPs (403). Flag for web_search fallback.
    console.error(`[pulse] NOTE: Reddit JSON API blocked for r/${subreddit}. Use web search for Reddit discourse (see SKILL.md).`);
    return [];
  }
}

// ── Synthesis ────────────────────────────────────────────────────────

async function main() {
  const [changelog, releases, devNotes, rClaudeAI, rCoding, rLocalLLaMA] =
    await Promise.all([
      getChangelog(),
      getGitHubReleases(),
      getDevPlatformNotes(),
      getRedditPosts("ClaudeAI", 25),
      getRedditPosts("coding", 50),
      getRedditPosts("LocalLLaMA", 50),
    ]);

  const today = new Date().toISOString().split("T")[0];
  const rangeStr = `${sinceStr} to ${today}`;

  let out = `# Claude Pulse — ${rangeStr}\n\n`;

  // ── Official Releases ──
  out += `## Official Releases\n\n`;

  out += `### Claude Code\n\n`;
  if (changelog.length > 0) {
    for (const entry of changelog) {
      out += `- **v${entry.version}**${entry.date ? ` (${entry.date})` : ""}: ${entry.changes.slice(0, 5).join("; ")}\n`;
    }
  } else {
    out += `_No changelog entries in window._\n`;
  }
  out += `\n`;

  out += `### GitHub Releases\n\n`;
  if (releases.length > 0) {
    for (const rel of releases) {
      const date = rel.publishedAt.split("T")[0];
      out += `- **${rel.name}** (${date}): [release](${rel.url})\n`;
      if (rel.body) out += `  > ${rel.body.replace(/\n/g, " ").slice(0, 150)}...\n`;
    }
  } else {
    out += `_No GitHub releases in window._\n`;
  }
  out += `\n`;

  out += `### Models & Platform\n\n`;
  if (devNotes) {
    // Extract the first ~30 lines that mention dates or versions
    const lines = devNotes.split("\n").slice(0, 40);
    const relevant = lines.filter((l) => /20\d{2}|v\d|version|model|deprecat/i.test(l));
    if (relevant.length > 0) {
      for (const line of relevant.slice(0, 10)) {
        out += `- ${line.trim().replace(/^[#-]\s*/, "")}\n`;
      }
    } else {
      out += `_No dated entries in platform notes._\n`;
    }
  } else {
    out += `_Platform release notes unavailable._\n`;
  }
  out += `\n`;

  // ── Community Commentary ──
  out += `## Community Commentary\n\n`;

  out += `### r/ClaudeAI (${rClaudeAI.length} threads)\n\n`;
  if (rClaudeAI.length > 0) {
    const sorted = [...rClaudeAI].sort((a, b) => b.score - a.score).slice(0, 10);
    for (const post of sorted) {
      out += `- **[${post.score}⬆ ${post.numComments}💬]** ${post.title} — [link](${post.permalink})\n`;
    }
  } else {
    out += `_No threads in window._\n`;
  }
  out += `\n`;

  out += `### r/coding & r/LocalLLaMA (Claude-relevant)\n\n`;
  const combined = [...rCoding, ...rLocalLLaMA];
  if (combined.length > 0) {
    const sorted = [...combined].sort((a, b) => b.score - a.score).slice(0, 10);
    for (const post of sorted) {
      out += `- **[${post.score}⬆ ${post.numComments}💬]** ${post.subreddit}: ${post.title} — [link](${post.permalink})\n`;
    }
  } else {
    out += `_No Claude-relevant threads in window._\n`;
  }
  out += `\n`;

  // ── Sources ──
  out += `## Sources\n\n`;
  out += `- [Claude Code CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)\n`;
  out += `- [Claude Code Releases](https://github.com/anthropics/claude-code/releases)\n`;
  out += `- [Claude Dev Platform Notes](https://platform.claude.com/docs/en/release-notes/overview.md)\n`;
  out += `- [Anthropic Blog](https://claude.com/blog)\n`;
  out += `- [r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/)\n`;
  out += `- [r/coding](https://www.reddit.com/r/coding/)\n`;
  out += `- [r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/)\n`;

  console.log(out);
}

main().catch((err) => {
  console.error("[pulse] FATAL:", err);
  process.exit(1);
});
