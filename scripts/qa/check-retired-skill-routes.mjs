#!/usr/bin/env node
// Passive Skillz catalog check. No network, shell execution, installs or writes.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const INDEX_DOCS = ['README.md', 'INDEX.md', 'AGENTS.md', 'CLAUDE.md', 'AGENT_START_HERE.md', 'BOOTSTRAP.md'];
const isInside = (root, target) => target === root || target.startsWith(root + path.sep);

function assertWithin(root, rel) {
  if (path.isAbsolute(rel) || !rel || rel.includes('\\')) throw new Error(`Unsafe relative path: ${rel}`);
  const abs = path.resolve(root, rel);
  if (!isInside(root, abs)) throw new Error(`Path escapes repository: ${rel}`);
  // Don't allow a symlink within an untrusted repository to redirect this audit.
  let at = root;
  for (const component of path.relative(root, abs).split(path.sep)) {
    if (!component) continue;
    at = path.join(at, component);
    if (fs.existsSync(at) && fs.lstatSync(at).isSymbolicLink()) throw new Error(`Symlink in audit path: ${rel}`);
  }
  return abs;
}

function loadJson(root, rel) {
  const file = assertWithin(root, rel);
  return JSON.parse(fs.readFileSync(file, 'utf8'));
}

function readText(root, rel) { return fs.readFileSync(assertWithin(root, rel), 'utf8'); }

function localUrls(markdown) {
  const urls = [];
  // Both inline Markdown links and reference-definition links.
  for (const match of markdown.matchAll(/\[[^\]]+\]\((<?[^)\n]+>?)\)/g)) urls.push(match[1]);
  for (const match of markdown.matchAll(/^\s*\[[^\]]+\]:\s*(\S+)/gm)) urls.push(match[1]);
  return urls;
}

export function auditRetiredRoutes(rootDirectory) {
  const root = fs.realpathSync(rootDirectory);
  const problems = [];
  const ledger = loadJson(root, 'registry/migration/frostwulf-independent-replacement-ledger-20261118.json');
  const host = loadJson(root, 'registry/evaluation/frostwulf-paired-host-status-20261118.json');
  const catalog = loadJson(root, 'registry/local-verification.json');
  const rows = ledger.rows ?? [];
  const historical = new Set();
  const archives = catalog.retired_legacy_records ?? [];
  const archivedNames = new Set();

  for (const record of archives) {
    if (!record.skill_name || archivedNames.has(record.skill_name)) problems.push(`Duplicate or nameless archived identity: ${record.skill_name ?? '<missing>'}`);
    archivedNames.add(record.skill_name);
  }
  for (const row of rows) {
    const rel = row.legacy_entrypoint;
    const m = /^skills\/([^/]+)\/SKILL\.md$/.exec(rel ?? '');
    if (!m) { problems.push(`Invalid historical entrypoint: ${rel}`); continue; }
    const id = m[1];
    if (historical.has(id)) problems.push(`Duplicate historical source ID: ${id}`);
    historical.add(id);
    try {
      if (fs.existsSync(assertWithin(root, rel))) problems.push(`Retired source still installed: ${rel}`);
      if (fs.existsSync(assertWithin(root, `skills/${id}`))) problems.push(`Retired package directory still active: skills/${id}/`);
      if (!fs.existsSync(assertWithin(root, row.replacement_entrypoint ?? ''))) problems.push(`Missing successor for ${id}: ${row.replacement_entrypoint}`);
    } catch (error) { problems.push(error.message); }
    const archived = archives.find(r => r.skill_name === id);
    if (!archived) problems.push(`Missing archived identity: ${id}`);
    else if (archived.current_selection !== 'disabled') problems.push(`Archived source still selectable: ${id}`);
  }
  for (const item of (catalog.skills ?? [])) {
    if (historical.has(item.skill_name) || rows.some(row => row.legacy_entrypoint === item.local_path)) problems.push(`Historical skill in active catalog: ${item.skill_name}`);
  }
  const expected = ledger.counts?.legacy_candidates;
  if (!Number.isInteger(expected) || expected !== rows.length) problems.push(`Legacy candidate denominator differs from ledger rows: ${expected}/${rows.length}`);
  if (ledger.counts?.legacy_removed !== rows.length || ledger.counts?.legacy_remaining !== 0) problems.push('Legacy retirement totals disagree with source rows');
  if (host.counts?.legacy_retirements_approved !== rows.length || host.counts?.retired_under_owner_accepted_procedure !== rows.length) problems.push('Host acceptance totals disagree with source rows');
  if (archivedNames.size !== rows.length || [...archivedNames].some(id => !historical.has(id))) problems.push(`Archive identity mismatch: ${archivedNames.size}/${rows.length}`);

  const docs = INDEX_DOCS.filter(rel => fs.existsSync(assertWithin(root, rel)));
  const categoryRoot = assertWithin(root, 'skills/categories');
  if (fs.existsSync(categoryRoot)) {
    for (const entry of fs.readdirSync(categoryRoot, { withFileTypes: true })) {
      if (!entry.isDirectory()) continue;
      const file = `skills/categories/${entry.name}/README.md`;
      if (fs.existsSync(assertWithin(root, file))) docs.push(file);
    }
  }
  let checkedLinks = 0;
  for (const doc of docs) {
    const markdown = readText(root, doc);
    for (const raw of localUrls(markdown)) {
      const url = raw.trim().replace(/^<|>$/g, '').split(/\s+"/)[0];
      if (!url || /^(?:[a-z][a-z0-9+.-]*:|\/\/|#)/i.test(url)) continue;
      let local;
      try { local = decodeURIComponent(url.split(/[?#]/)[0]); }
      catch { problems.push(`Invalid URL encoding in ${doc}: ${url}`); continue; }
      if (!local) continue;
      const rel = path.relative(root, path.resolve(root, path.dirname(doc), local));
      try {
        const target = assertWithin(root, rel);
        checkedLinks++;
        if (!fs.existsSync(target)) problems.push(`Broken active Markdown link in ${doc}: ${url}`);
      } catch (error) { problems.push(`${doc}: ${error.message}`); }
    }
  }
  return { ok: problems.length === 0, historical: rows.length, archived: archivedNames.size, documents: docs.length, checkedLinks, problems };
}

if (process.argv[1] && fileURLToPath(import.meta.url) === path.resolve(process.argv[1])) {
  const args = process.argv.slice(2);
  if (args.length > 1) { console.error('Usage: node scripts/qa/check-retired-skill-routes.mjs [repository-root]'); process.exitCode = 2; }
  else {
    try {
      const result = auditRetiredRoutes(args[0] ?? process.cwd());
      if (!result.ok) {
        for (const issue of result.problems) console.error(`FAIL: ${issue}`);
        process.exitCode = 1;
      } else console.log(`Retired routes OK: ${result.historical} retired, ${result.archived} archived; ${result.checkedLinks} internal links in ${result.documents} active docs`);
    } catch (error) { console.error(`FAIL: ${error.message}`); process.exitCode = 1; }
  }
}
