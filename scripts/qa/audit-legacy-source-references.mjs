#!/usr/bin/env node
// Explicit offline maintainer check. No network, installer, scheduler, writes or skill execution.
import fs from 'node:fs';
import path from 'node:path';
import {execFileSync} from 'node:child_process';

const root=process.cwd();
const args=process.argv.slice(2);
const opt=(name)=>{const i=args.indexOf(name);return i<0?null:args[i+1]};
const isSlug=s=>typeof s==='string'&&/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(s);
const esc=s=>s.replace(/[.*+?^$\{\}()|[\]\\]/g,'\\$&');
const matchPaths=(text,slug)=>{
  const p=new RegExp('(?:skills/'+esc(slug)+'(?:/[^\\s\\)\\]"\\x27<>]*)?|\\.\\./'+esc(slug)+'/|local-skills/'+esc(slug)+')','g');
  const hits=[];let m;
  while((m=p.exec(text))!==null){
    const before=text.slice(Math.max(0,m.index-130),m.index);
    const pinned=/https:\/\/github\.com\/[^\s]+\/blob\/[0-9a-f]{40}\/$/.test(before);
    hits.push({line:text.slice(0,m.index).split('\n').length,pinned});
  }
  return hits;
};
const historicalFile=(p,slug)=>
  p.startsWith('docs/reviews/')||
  p.startsWith('registry/review-freshness/')||
  p.startsWith('registry/migration/')||
  p.startsWith('registry/discovery/frostwulf-')||
  p==='registry/skills/local-skills/'+slug+'.yaml'||
  p==='registry/verification/local-skills/'+slug+'.yaml'||
  p==='registry/local-verification.json'||
  p==='registry/governed-review-name-index.json';
function selfTest(){
  const old='todo-harvester';
  const samples=[
    ['[old](../../todo-harvester/)',1,false],
    ['local-skills/todo-harvester',1,false],
    ['skills/todo-harvester/SKILL.md',1,false],
    ['skills/authored/source-debt-triage/SKILL.md',0,false],
    ['https://github.com/Knapp-Kevin/skillz/blob/c95b31e6d0955f00c5ae14bb59ceee821de20b2c/skills/todo-harvester/SKILL.md',1,true]
  ];
  for(const [s,count,pinned] of samples){
    const hits=matchPaths(s,old);
    if(hits.length!==count||(count&&hits[0].pinned!==pinned))throw Error('SELF_TEST_FAILED');
  }
  return {self_test:'PASS',cases:samples.length};
}
if(args.includes('--self-test')){
  console.log(JSON.stringify(selfTest()));
}else{
  const slug=opt('--legacy');
  if(!isSlug(slug)||args.length!==2||args[0]!=='--legacy')throw Error('Usage: node scripts/qa/audit-legacy-source-references.mjs --legacy <slug>');
  const ledger=JSON.parse(fs.readFileSync(path.join(root,'registry/migration/frostwulf-independent-replacement-ledger-20261118.json'),'utf8'));
  const source='skills/'+slug+'/SKILL.md';
  const row=ledger.rows.find(r=>r.legacy_entrypoint===source);
  if(!row||!row.replacement_entrypoint||!row.retirement_snapshot_commit)throw Error('Legacy source not in retirement pilot ledger');
  const first=JSON.parse(fs.readFileSync(path.join(root,'registry/governed-review-name-index.json'),'utf8'));
  const cap=JSON.parse(fs.readFileSync(path.join(root,'registry/capability-directory.json'),'utf8'));
  const local=JSON.parse(fs.readFileSync(path.join(root,'registry/local-verification.json'),'utf8'));
  const index=JSON.parse(fs.readFileSync(path.join(root,'index.json'),'utf8'));
  const activeId='local-skills/'+slug;
  const violations=[];
  if(fs.existsSync(path.join(root,source)))violations.push('Old entrypoint still present');
  if(!fs.existsSync(path.join(root,row.replacement_entrypoint)))violations.push('Replacement entrypoint missing');
  if(first.first_party_ids.includes(activeId))violations.push('Current name index still lists historical skill');
  if(cap.skill_records.some(r=>r.id===activeId))violations.push('Capability-directory skill_records includes historical skill');
  if(cap.domains.some(d=>d.subdomains.some(s=>s.matched_skill_ids.includes(activeId))))violations.push('Canonical capability route still includes historical skill');
  if(local.skills.some(r=>r.skill_name===slug))violations.push('Active local-verification list includes historical skill');
  if(!local.retired_legacy_records?.some(r=>r.skill_name===slug))violations.push('Historical review not archived');
  if(Object.values(index.first_party_categories??{}).some(ids=>Array.isArray(ids)&&ids.includes(slug)))violations.push('Root category index still lists historical skill');
  const tracked=execFileSync('git',['ls-files','-z'],{cwd:root,encoding:'utf8',maxBuffer:24*1024*1024,timeout:10000,env:{...process.env,GIT_OPTIONAL_LOCKS:'0'}}).split('\0').filter(Boolean);
  const activeLinks=[],history=[],unreadable=[],binary=[];
  const maxBytes=8*1024*1024;
  for(const rel of tracked){
    if(path.isAbsolute(rel)||rel.split(/[\\/]/).includes('..')){unreadable.push({path:rel,reason:'unsafe-path'});continue;}
    const absolute=path.join(root,rel);
    let stat;try{stat=fs.lstatSync(absolute);}catch(e){unreadable.push({path:rel,reason:'unreadable'});continue;}
    if(stat.isSymbolicLink()){unreadable.push({path:rel,reason:'symlink-not-followed'});continue;}
    if(!stat.isFile())continue;
    if(stat.size>maxBytes){unreadable.push({path:rel,reason:'large'});continue;}
    let text;try{text=fs.readFileSync(absolute,'utf8');}catch(e){unreadable.push({path:rel,reason:'unreadable'});continue;}
    if(text.includes('\0')){binary.push(rel);continue;}
    const matches=matchPaths(text,slug);
    for(const m of matches){
      const item={path:rel,line:m.line};
      if(m.pinned||historicalFile(rel,slug))history.push(item);
      else activeLinks.push(item);
    }
  }
  const result={legacy_slug:slug,legacy_source:source,replacement:row.replacement_entrypoint,tracked_files:tracked.length,binary_skipped:binary.length,history_reference_count:history.length,historical_reference_paths:[...new Set(history.map(x=>x.path))].slice(0,100),active_references:activeLinks.slice(0,100),active_reference_count:activeLinks.length,unreadable:unreadable.slice(0,100),unreadable_count:unreadable.length,index_violations:violations,complete_text_scan:unreadable.length===0,qualified_for_retirement:violations.length===0&&activeLinks.length===0&&unreadable.length===0,host_behavior:'not-run'};
  console.log(JSON.stringify(result,null,2));
  process.exitCode=result.qualified_for_retirement?0:(unreadable.length?3:2);
}
