import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { auditRetiredRoutes } from './check-retired-skill-routes.mjs';

function fixture(modify = () => {}) {
  const root = fs.mkdtempSync(path.join(os.tmpdir(), 'skillz-retired-routes-'));
  const put = (p, content) => {
    const loc = path.join(root, p);
    fs.mkdirSync(path.dirname(loc), { recursive: true });
    fs.writeFileSync(loc, typeof content === 'string' ? content : JSON.stringify(content));
  };
  const ledger = { counts: { legacy_candidates: 2, legacy_removed: 2, legacy_remaining: 0 }, rows: [
    { legacy_entrypoint: 'skills/old-one/SKILL.md', replacement_entrypoint: 'skills/authored/new-one/SKILL.md' },
    { legacy_entrypoint: 'skills/old-two/SKILL.md', replacement_entrypoint: 'skills/authored/new-two/SKILL.md' }
  ] };
  const host = { counts: { legacy_retirements_approved: 2, retired_under_owner_accepted_procedure: 2 } };
  const catalog = { skills: [], retired_legacy_records: [
    { skill_name: 'old-one', current_selection: 'disabled' }, { skill_name: 'old-two', current_selection: 'disabled' }
  ] };
  put('registry/migration/frostwulf-independent-replacement-ledger-20261118.json', ledger);
  put('registry/evaluation/frostwulf-paired-host-status-20261118.json', host);
  put('registry/local-verification.json', catalog);
  put('skills/authored/new-one/SKILL.md', '# New one');
  put('skills/authored/new-two/SKILL.md', '# New two');
  put('README.md', '[one](skills/authored/new-one/SKILL.md) [archived](https://github.com/example/archive/skills/old-one)');
  put('INDEX.md', '[two](skills/authored/new-two/)');
  put('skills/categories/demo/README.md', '[two](../../authored/new-two/SKILL.md)');
  modify({ root, put, ledger, host, catalog });
  return { root, cleanup: () => fs.rmSync(root, { recursive: true, force: true }) };
}

function check(mutator, fragment) {
  const f = fixture(mutator);
  try {
    const result = auditRetiredRoutes(f.root);
    assert.equal(result.ok, false, JSON.stringify(result));
    assert.ok(result.problems.some(p => p.includes(fragment)), JSON.stringify(result.problems));
  } finally { f.cleanup(); }
}

test('passes fully archived sample and validates active navigation', () => {
  const f = fixture();
  try { assert.deepEqual(auditRetiredRoutes(f.root), { ok: true, historical: 2, archived: 2, documents: 3, checkedLinks: 3, problems: [] }); }
  finally { f.cleanup(); }
});
test('rejects an installed retired package', () => check(({ put }) => put('skills/old-one/SKILL.md', '# old'), 'Retired source still installed'));
test('rejects a stale active selector', () => check(({ put, catalog }) => { catalog.skills.push({ skill_name: 'old-one' }); put('registry/local-verification.json', catalog); }, 'Historical skill in active catalog'));
test('rejects missing archival records', () => check(({ put, catalog }) => { catalog.retired_legacy_records.pop(); put('registry/local-verification.json', catalog); }, 'Missing archived identity'));
test('rejects duplicate archived identities', () => check(({ put, catalog }) => { catalog.retired_legacy_records.push(catalog.retired_legacy_records[0]); put('registry/local-verification.json', catalog); }, 'Duplicate or nameless'));
test('rejects broken active navigation links', () => check(({ put }) => put('README.md', '[old](skills/old-one/SKILL.md)'), 'Broken active Markdown link'));
test('rejects unauthorized ledger traversal', () => check(({ put, ledger }) => { ledger.rows[0].replacement_entrypoint = '../../private/SKILL.md'; put('registry/migration/frostwulf-independent-replacement-ledger-20261118.json', ledger); }, 'Path escapes repository'));
test('rejects symlinked active navigation targets', () => check(({ root }) => { fs.unlinkSync(path.join(root, 'skills/authored/new-one/SKILL.md')); fs.symlinkSync(path.join(root, 'README.md'), path.join(root, 'skills/authored/new-one/SKILL.md')); }, 'Symlink in audit path'));
test('rejects incorrectly counted retirements', () => check(({ put, host }) => { host.counts.legacy_retirements_approved = 1; put('registry/evaluation/frostwulf-paired-host-status-20261118.json', host); }, 'Host acceptance totals disagree'));
