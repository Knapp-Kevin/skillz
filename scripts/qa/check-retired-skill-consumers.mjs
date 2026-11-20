#!/usr/bin/env node
// Full checkout consumer-route audit for 44 historical source packages.
// Passive, Node stdlib only: no commands, network, writes, installs or skill runs.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ARCHIVE_PREFIXES = [
  'docs/reviews/', 'docs/evals/', 'docs/history/', 'docs/archive/',
  'registry/', 'skills/archive/', 'skills/retired/'
];
const HISTORY_FILES = new Set(['CHANGES.md', 'MAINTAINER_WORKBOARD.md']);
const IGNORED_DIRS = new Set(['.git', 'node_modules', '__pycache__', '.venv', 'venv', 'dist', 'build', '.next']);
const TEXT_EXTENSIONS = new Set([
  '.md', '.markdown', '.mdx', '.rst', '.adoc', '.txt', '.json', '.jsonl',
  '.yaml', '.yml', '.toml', '.ini', '.cfg', '.js', '.mjs', '.cjs', '.ts',
  '.tsx', '.jsx', '.py', '.sh', '.ps1', '.html', '.xml', '.csv'
]);
const MAX_BYTES = 4 * 1024 * 1024;
const normalized = p => p.split(path.sep).join('/');
const safeInside = (root, abs) => abs === root || abs.startsWith(root + path.sep);

function traverse(root, directory, files, problems) {
  for (const entry of fs.readdirSync(directory, { withFileTypes: true })) {
    if (entry.name === '.git' || (entry.isDirectory() && IGNORED_DIRS.has(entry.name))) continue;
    const full = path.join(directory, entry.name);
    if (!safeInside(root, full)) { problems.push(`Path escapes checkout: ${full}`); continue; }
    const stat = fs.lstatSync(full);
    if (stat.isSymbolicLink()) {
      // Never resolve/read a symlink. An active consumer link to one also
      // fails via the retired-route parent audit.
      continue;
    }
    if (stat.isDirectory()) traverse(root, full, files, problems);
    else if (stat.isFile()) files.push(full);
  }
}

function isHistoricalEvidence(rel) {
  return ARCHIVE_PREFIXES.some(prefix => rel.startsWith(prefix))
    || HISTORY_FILES.has(rel);
}

function legacyTarget(link, current, root, retired) {
  let candidate = link.trim().replace(/^<|>$/g, '').split(/\s+"/)[0];
  if (!candidate || candidate.startsWith('#')) return null;
  try { candidate = decodeURIComponent(candidate.split(/[?#]/)[0]); }
  catch { return null; }
  // Immutable Git object URLs are archival citations, not active installs.
  if (/^https?:\/\//i.test(candidate)) {
    const m = /^https:\/\/github\.com\/Knapp-Kevin\/skillz\/(?:blob|tree)\/([^/]+)\/(skills\/([^/]+)(?:\/[^\s]*)?)/i.exec(candidate);
    if (!m || !retired.has(m[3])) return null;
    if (/^[0-9a-f]{40}$/i.test(m[1])) return null;
    return { target: m[2], mode: 'mutable-github-url' };
  }
  if (/^[a-z][a-z\d+.-]*:/i.test(candidate) || candidate.startsWith('//')) return null;
  const target = candidate.startsWith('/')
    ? path.resolve(root, '.' + candidate)
    : path.resolve(path.dirname(current), candidate);
  if (!safeInside(root, target)) return null;
  const rel = normalized(path.relative(root, target));
  const m = /^skills\/([^/]+)(?:\/|$)/.exec(rel);
  if (m && retired.has(m[1])) return { target: rel, mode: 'relative-link' };
  return null;
}

function markdownLinks(content) {
  const links = [];
  // Standard inline markdown; reference-definition links; HTML attr href/src.
  // This does not claim to fully parse nested Markdown expressions.
  for (const m of content.matchAll(/\[[^\]\n]+\]\((<?[^)\n]+>?)\)/g)) links.push({ url: m[1], offset: m.index });
  for (const m of content.matchAll(/^\s*\[[^\]\n]+\]:\s*(\S+)/gm)) links.push({ url: m[1], offset: m.index });
  for (const m of content.matchAll(/\b(?:href|src)\s*=\s*["']([^"'\n]+)["']/g)) links.push({ url: m[1], offset: m.index });
  return links;
}

export function auditRetiredSkillConsumers(rootDirectory, historicalIds) {
  const root = fs.realpathSync(rootDirectory);
  const retired = new Set(historicalIds);
  if (retired.size === 0) throw new Error('Retired skill identity set is empty');
  const problems = [];
  const files = [];
  traverse(root, root, files, problems);
  let textFiles = 0, markdownFiles = 0, markdownLinksInspected = 0;
  let historicalEvidenceFiles = 0, historicalEvidenceMentions = 0;
  let currentFilesWithLegacyMentions = 0, unclassifiedTextFiles = 0;
  const currentMentionExamples = [];
  const activeLegacyRouteLinks = [];
  const examplesLimit = 15;
  const idPattern = new RegExp(`\\bskills/(?:${[...retired].map(x => x.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')).join('|')})/(?:SKILL\\.md|README\\.md|[^\\s"'<>)]*)`, 'g');
  for (const absolute of files) {
    const rel = normalized(path.relative(root, absolute));
    const ext = path.extname(rel).toLowerCase();
    if (!TEXT_EXTENSIONS.has(ext) && !['AGENTS.md', 'CLAUDE.md', 'Dockerfile', 'Makefile'].includes(path.basename(rel))) continue;
    let stat;
    try { stat = fs.statSync(absolute); }
    catch { problems.push(`Unreadable consumer file: ${rel}`); continue; }
    if (stat.size > MAX_BYTES) { unclassifiedTextFiles++; continue; }
    const content = fs.readFileSync(absolute, 'utf8');
    if (content.includes('\0')) { unclassifiedTextFiles++; continue; }
    textFiles++;
    const archive = isHistoricalEvidence(rel);
    if (archive) historicalEvidenceFiles++;
    const mentions = [...content.matchAll(idPattern)].length;
    if (archive) historicalEvidenceMentions += mentions;
    else if (mentions > 0) {
      currentFilesWithLegacyMentions++;
      if (currentMentionExamples.length < examplesLimit) currentMentionExamples.push({ file: rel, mentions });
    }
    if (!['.md', '.markdown', '.mdx', '.html', '.rst', '.adoc'].includes(ext)) continue;
    markdownFiles++;
    for (const item of markdownLinks(content)) {
      markdownLinksInspected++;
      const route = legacyTarget(item.url, absolute, root, retired);
      if (!route) continue;
      if (archive) continue;
      const line = content.slice(0, item.offset).split('\n').length;
      const location = `${rel}:${line}`;
      activeLegacyRouteLinks.push({ file: rel, line, url: item.url, ...route });
      problems.push(`Active link to retired package in ${location}: ${item.url}`);
    }
  }
  return {
    ok: problems.length === 0, filesEnumerated: files.length, textFiles,
    markdownFiles, markdownLinksInspected, historicalEvidenceFiles,
    historicalEvidenceMentions, currentFilesWithLegacyMentions,
    currentMentionExamples, activeLegacyRouteLinks, unclassifiedTextFiles, problems
  };
}

if (process.argv[1] && fileURLToPath(import.meta.url) === path.resolve(process.argv[1])) {
  const root = process.argv[2] ?? process.cwd();
  try {
    const ledger = JSON.parse(fs.readFileSync(path.join(root, 'registry/migration/frostwulf-independent-replacement-ledger-20261118.json'), 'utf8'));
    const ids = (ledger.rows ?? []).map(row => row.legacy_entrypoint?.match(/^skills\/([^/]+)\/SKILL\.md$/)?.[1]).filter(Boolean);
    const result = auditRetiredSkillConsumers(root, ids);
    console.log(JSON.stringify(result, null, 2));
    if (!result.ok) process.exitCode = 1;
  } catch (error) { console.error(`FAIL: ${error.message}`); process.exitCode = 1; }
}
