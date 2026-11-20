import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { auditRetiredSkillConsumers } from './check-retired-skill-consumers.mjs';

const ids = ['obsolete-one', 'obsolete-two'];
const sha = '0123456789abcdef0123456789abcdef01234567';

function temporary(files) {
  const root = fs.mkdtempSync(path.join(os.tmpdir(), 'skillz-consumer-audit-'));
  for (const [file, text] of Object.entries(files)) {
    const target = path.join(root, file);
    fs.mkdirSync(path.dirname(target), { recursive: true });
    fs.writeFileSync(target, text);
  }
  return { root, cleanup: () => fs.rmSync(root, { force: true, recursive: true }) };
}
function run(files, assertion) {
  const tmp = temporary(files);
  try { assertion(auditRetiredSkillConsumers(tmp.root, ids), tmp.root); }
  finally { tmp.cleanup(); }
}

test('reads all text files and does not classify archived original source citations as active', () => run({
  'README.md': '[new](skills/authored/replacement/SKILL.md)',
  'docs/reviews/old.md': '[old](../../skills/obsolete-one/SKILL.md)',
  'registry/migration.json': '{"original":"skills/obsolete-two/SKILL.md"}',
  'skills/authored/replacement/SKILL.md': '# replacement',
  'data/log.txt': 'the old reference skills/obsolete-one/SKILL.md was retired',
}, r => {
  assert.equal(r.ok, true);
  assert.equal(r.textFiles, 5);
  assert.equal(r.markdownFiles, 3);
  assert.equal(r.historicalEvidenceMentions, 2);
  assert.equal(r.currentFilesWithLegacyMentions, 1);
  assert.equal(r.activeLegacyRouteLinks.length, 0);
}));

test('fails stale active relative Markdown link anywhere in checkout', () => run({
  'docs/guides/entry.md': '[load](../../skills/obsolete-one/SKILL.md)'
}, r => {
  assert.equal(r.ok, false);
  assert.match(r.problems.join(' '), /Active link to retired package/);
  assert.equal(r.activeLegacyRouteLinks[0].target, 'skills/obsolete-one/SKILL.md');
}));

test('finds reference-definition and HTML links to removed content', () => run({
  'skills/categories/main/README.md': '[x][legacy]\n\n[legacy]: ../../../skills/obsolete-two/SKILL.md\n<a href="../../../skills/obsolete-one/SKILL.md">old</a>'
}, r => {
  assert.equal(r.ok, false);
  assert.equal(r.activeLegacyRouteLinks.length, 2);
}));

test('immutable Git historical URL is allowed, mutable main URL is rejected', () => run({
  'README.md': '[archive](https://github.com/Knapp-Kevin/skillz/blob/' + sha + '/skills/obsolete-one/SKILL.md)\n' +
    '[live](https://github.com/Knapp-Kevin/skillz/blob/main/skills/obsolete-one/SKILL.md)'
}, r => {
  assert.equal(r.ok, false);
  assert.equal(r.activeLegacyRouteLinks.length, 1);
  assert.equal(r.activeLegacyRouteLinks[0].mode, 'mutable-github-url');
}));

test('active non-link historical mentions are disclosed without automatically rewriting history', () => run({
  'docs/guidance.md': 'The old skills/obsolete-one/SKILL.md is historical, not a live route.'
}, r => {
  assert.equal(r.ok, true);
  assert.equal(r.currentFilesWithLegacyMentions, 1);
}));

test('no following symlinks to external targets', () => {
  const tmp = temporary({ 'README.md': '[new](skills/authored/current/SKILL.md)' });
  try {
    fs.symlinkSync(os.tmpdir(), path.join(tmp.root, 'outside'), 'dir');
    const r = auditRetiredSkillConsumers(tmp.root, ids);
    assert.equal(r.ok, true);
    assert.equal(r.textFiles, 1);
  } finally { tmp.cleanup(); }
});

test('scans nested Markdown not limited to curated navigation list', () => run({
  'engine/plugins/custom/docs/README.md': '[install](../../../../skills/obsolete-two/SKILL.md)'
}, r => assert.equal(r.activeLegacyRouteLinks.length, 1)));

test('fails closed if historical source identity input is missing', () => {
  const tmp = temporary({'README.md':'# R'});
  try { assert.throws(() => auditRetiredSkillConsumers(tmp.root, []), /empty/); }
  finally { tmp.cleanup(); }
});

test('does not follow archival symlinks pointing into live documentation', () => {
  const tmp = temporary({ 'README.md': '# current' });
  try {
    fs.mkdirSync(path.join(tmp.root, 'docs/reviews'), { recursive: true });
    fs.symlinkSync(path.join(tmp.root, 'README.md'),
      path.join(tmp.root, 'docs/reviews/fake.md'));
    assert.equal(auditRetiredSkillConsumers(tmp.root, ids).textFiles, 1);
  } finally { tmp.cleanup(); }
});
