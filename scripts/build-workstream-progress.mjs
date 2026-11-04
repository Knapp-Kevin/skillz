#!/usr/bin/env node
// Source-pinned review snapshot, no network, no external dependencies.
import {readFileSync,writeFileSync,mkdirSync,existsSync} from "node:fs";
import {resolve,dirname} from "node:path";
import {fileURLToPath} from "node:url";

function xml(s){return String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;").replace(/'/g,"&apos;")}

function validateStatus(s,q7cat,q8cat,p){
 if(s.schema_version!=="skillz-workstream-qualification-progress-v1"||s.publication_state!=="BRANCH_PREVIEW_NOT_MERGED")throw Error("Only pinned branch-preview source permitted");
 const f=s.merged_baseline,g=s.q8,h=s.q9,k=s.q10;
 if(![f.featured,f.represented_domains,g.proposed_featured,g.represented_domains,g.canonical_domains,h.pinned_entrypoints,h.source_repositories,h.covered_domains,k.individually_reviewed,k.remaining_q9_entrypoints,k.promising_but_held,k.other_held,k.featured_promotions,k.security_scans_run,k.actual_behavioral_runs,g.approved_unchanged,g.behaviorally_validated,g.static_security.passed,g.static_security.failed,g.static_security.incomplete].every(x=>Number.isInteger(x)&&x>=0))throw Error("Invalid nonnegative count");
 if(f.featured!==q7cat.starter_shelf_totals.valuable_reference||f.represented_domains!==q7cat.starter_shelf_totals.distinct_capability_domains_represented)throw Error("Merged baseline mismatch");
 if(g.proposed_featured!==q8cat.valuable_references.length||g.represented_domains!==q8cat.starter_shelf_totals.distinct_capability_domains_represented||g.represented_domains>g.canonical_domains)throw Error("Proposed shelf mismatch");
 const stage=id=>p.stages.find(x=>x.id===id);
 if(stage("positively_selected").value!==g.proposed_featured||stage("security_gate_passed_featured").value!==g.static_security.passed)throw Error("Pipeline shelf mismatch");
 if(stage("security_gate_passed_featured").parts.failed!==g.static_security.failed||stage("security_gate_passed_featured").parts.incomplete!==g.static_security.incomplete)throw Error("Scanner breakdown mismatch");
 if(g.static_security.passed+g.static_security.failed+g.static_security.incomplete!==g.proposed_featured)throw Error("Scanner denominator mismatch");
 if(stage("behaviorally_validated").value!==g.behaviorally_validated||stage("approved_unchanged").value!==g.approved_unchanged)throw Error("Approval mismatch");
 if(h.pinned_entrypoints!==k.individually_reviewed+k.remaining_q9_entrypoints)throw Error("Q9/Q10 overlap count mismatch");
 if(k.remaining_boundary){const b=k.remaining_boundary;if(b.stage!=="SCOPE_MAPPED_NOT_COMPLETE_NOT_GRADED"||k.remaining_q9_entrypoints!==1||b.portable_bundle_files<=0||b.source_repo_git_blobs!==b.portable_bundle_files+b.excluded_repo_files||b.python_scripts<=0||b.reference_files<=0)throw Error("Pending package boundary failed validation")};
 if(k.individually_reviewed!==k.promising_but_held+k.other_held||k.methods.length!==k.individually_reviewed)throw Error("Q10 review breakdown mismatch");
 if(k.methods.filter(x=>x.decision==="PROMISING_HELD").length!==k.promising_but_held||k.methods.filter(x=>x.decision!=="PROMISING_HELD").length!==k.other_held)throw Error("Disposition mismatch");
 const names=new Set();for(const x of k.methods){if(names.has(x.name)||!Number.isInteger(x.score)||x.score<0||x.score>20)throw Error("Invalid Q10 method");names.add(x.name);}
 if(k.featured_promotions!==0||g.approved_unchanged!==0||g.behaviorally_validated!==0||k.actual_behavioral_runs!==0||k.security_scans_run!==0)throw Error("Unexpected clearance: independent review required");
 return true;
}

function renderSvg(s){
 const w=1120,h=740,m=s.merged_baseline,q=s.q8,dis=s.q9,rev=s.q10;
 const a=[],add=x=>a.push(x),rect=(x,y,width,height,fill,r=9)=>'<rect x="'+x+'" y="'+y+'" width="'+width+'" height="'+height+'" rx="'+r+'" fill="'+fill+'"/>';
 const txt=(x,y,t,sz=16,color="#e2eaf5",extra="")=>'<text x="'+x+'" y="'+y+'" font-family="Arial,Helvetica,sans-serif" font-size="'+sz+'" fill="'+color+'" '+extra+'>'+xml(t)+'</text>';
 const bx=324,bw=604,bh=25,blue="#87a5ef",purple="#bc9cf8",teal="#64d7cd",amber="#eabf72",red="#e18c90",gray="#647b9a";
 add('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 '+w+' '+h+'" width="'+w+'" height="'+h+'" role="img" aria-labelledby="workstream-title workstream-desc">');
 add('<title id="workstream-title">Skillz qualification progress, merged baseline and unmerged Q8 Q9 Q10</title>');
 add('<desc id="workstream-desc">Merged main has '+m.featured+' study references in '+m.represented_domains+' domains. Q8 draft proposes '+q.proposed_featured+' in '+q.represented_domains+' domains. '+rev.individually_reviewed+' of '+dis.pinned_entrypoints+' Q9 source leads have received Q10 static reviews; '+rev.remaining_q9_entrypoints+(rev.remaining_q9_entrypoints===1?' remains':' remain')+'. Q8 static security: '+q.static_security.passed+' pass, '+q.static_security.failed+' fail, '+q.static_security.incomplete+' incomplete. '+q.approved_unchanged+' approved unchanged.</desc>');
 add('<defs><linearGradient id="workstream-bg" x1="0" x2="1" y1="0" y2="1"><stop stop-color="#0d1a2f"/><stop offset="1" stop-color="#183250"/></linearGradient></defs>');
 add(rect(0,0,w,h,"url(#workstream-bg)",24));add(txt(38,54,"Skillz | Curation progress",32,"#f4f8ff",'font-weight="700"'));add(txt(38,86,"Source-pinned evidence, not automatic installation or release approval",17,"#b8ccdf"));
 add(rect(887,35,194,39,"#3c3458",10));add(txt(984,61,"UNMERGED DRAFT",14,"#f0ddff",'text-anchor="middle" font-weight="700"'));
 const cards=[{n:q.proposed_featured,t:"Q8 proposed references",c:purple},{n:dis.pinned_entrypoints,t:"Q9 pinned leads",c:blue},{n:rev.individually_reviewed,t:"Q10 static reviews",c:teal},{n:q.approved_unchanged,t:"Approved unchanged",c:amber}];
 cards.forEach((card,i)=>{const x=37+i*270;add(rect(x,117,248,99,"#1d3451",12));add('<rect x="'+x+'" y="117" width="248" height="99" rx="12" fill="none" stroke="#405b7b"/>');add(txt(x+16,166,String(card.n),34,card.c,'font-weight="700"'));add(txt(x+16,195,card.t,15,"#d1ddeb"));});
 add(txt(39,263,"Featured study methods | merged versus Q8 proposal",21,"#f2f7ff",'font-weight="700"'));
 add(txt(42,312,"Merged main (Q7)",17,"#dce8f6"));add(rect(bx,291,bw,bh,"#293f5c",6));add(rect(bx,291,Math.round(bw*m.featured/q.proposed_featured),bh,blue,6));add(txt(952,312,m.featured+" / "+q.proposed_featured,17,"#eaf2fc",'font-weight="700"'));
 add(txt(42,355,"Q8 draft (not merged)",17,"#dce8f6"));add(rect(bx,334,bw,bh,"#293f5c",6));add(rect(bx,334,bw,bh,purple,6));add(txt(952,355,String(q.proposed_featured),17,"#eaf2fc",'font-weight="700"'));
 add(txt(39,413,"Q9 discovered leads | Q10 static review coverage",21,"#f2f7ff",'font-weight="700"'));
 add(txt(42,453,dis.pinned_entrypoints+" pinned leads",17,"#dce8f6"));add(rect(bx,433,bw,bh,"#293f5c",6));add(rect(bx,433,bw*rev.individually_reviewed/dis.pinned_entrypoints,bh,teal,6));add(rect(bx+bw*rev.individually_reviewed/dis.pinned_entrypoints,433,bw*rev.remaining_q9_entrypoints/dis.pinned_entrypoints,bh,amber,0));add(txt(952,453,rev.individually_reviewed+" reviewed",17,"#eaf2fc",'font-weight="700"'));
 add(txt(324,490,rev.promising_but_held+" promising concepts, held",15,teal));add(txt(673,490,rev.other_held+" other reviews held",15,amber));add(txt(42,514,rev.remaining_boundary ? rev.remaining_q9_entrypoints+" lead still needs full review: ROS 2 bundle mapped ("+rev.remaining_boundary.portable_bundle_files+"/"+rev.remaining_boundary.source_repo_git_blobs+" repo files)." : rev.remaining_q9_entrypoints+(rev.remaining_q9_entrypoints===1?" lead still needs":" leads still need")+" full static review. These are the same Q9 leads, not extra candidates.",14,"#afc4db"));
 add(txt(39,557,"Q8 featured methods | pinned static security scan",21,"#f2f7ff",'font-weight="700"'));
 add(txt(42,598,q.proposed_featured+" total",17,"#dce8f6"));add(rect(bx,578,bw,bh,"#293f5c",6));
 let offset=0;for(const [count,color] of [[q.static_security.passed,teal],[q.static_security.failed,red],[q.static_security.incomplete,gray]]){let width=bw*count/q.proposed_featured;add(rect(bx+offset,578,width,bh,color,0));offset+=width}
 add(txt(952,598,q.static_security.passed+" passed",17,"#eaf2fc",'font-weight="700"'));
 add(rect(42,634,13,13,teal,2));add(txt(65,646,q.static_security.passed+" passed (not approved)",15,"#d2e3f1"));add(rect(353,634,13,13,red,2));add(txt(376,646,q.static_security.failed+" failed",15,"#d2e3f1"));add(rect(596,634,13,13,gray,2));add(txt(619,646,q.static_security.incomplete+" incomplete",15,"#d2e3f1"));
 add('<line x1="39" y1="677" x2="1082" y2="677" stroke="#3c5675"/>');
 add(txt(39,707,"No new unchanged-use approvals or behavioral validations. Branch snapshot as of "+s.as_of+".",16,"#e7eef7"));
 add(txt(39,729,"Different populations: Q9 leads overlap Q10 reviews; security passes do not imply safe installation.",14,"#a8c1db"));
 add("</svg>");return a.join("\n")+"\n";
}

function renderCsv(s){
 const columns=["Workstream","Source revision","Metric","Count","Review state","PR URL"];
 const rows=[
 ["Merged main",s.merged_baseline.main_sha,"Valuable References",s.merged_baseline.featured,"MERGED_AT_CHECKPOINT","https://github.com/Knapp-Kevin/skillz/commit/"+s.merged_baseline.main_sha],
 ["Merged main",s.merged_baseline.main_sha,"Domains with selected methods",s.merged_baseline.represented_domains,"MERGED_AT_CHECKPOINT","https://github.com/Knapp-Kevin/skillz/commit/"+s.merged_baseline.main_sha],
 ["Q8",s.q8.head_sha,"Proposed Valuable References",s.q8.proposed_featured,"DRAFT_NOT_MERGED",s.q8.url],
 ["Q8",s.q8.head_sha,"Proposed represented domains",s.q8.represented_domains,"DRAFT_NOT_MERGED",s.q8.url],
 ...[["Static gate pass",s.q8.static_security.passed,"STATIC_PASS_NOT_APPROVAL"],["Static gate failed",s.q8.static_security.failed,"STATIC_FAILED"],["Static gate incomplete",s.q8.static_security.incomplete,"STATIC_INCOMPLETE"],["Behaviorally validated",s.q8.behaviorally_validated,"NOT_RUN"],["Approved unchanged",s.q8.approved_unchanged,"NO_APPROVAL"]].map(([label,value,state])=>["Q8",s.q8.head_sha,label,value,state,s.q8.url]),
 ["Q9",s.q9.head_sha,"Pinned entrypoints",s.q9.pinned_entrypoints,"DRAFT_DISCOVERY_ONLY",s.q9.url],
 ["Q9",s.q9.head_sha,"Independent publisher repositories",s.q9.source_repositories,"DRAFT_DISCOVERY_ONLY",s.q9.url],
 ["Q10",s.q10.head_sha,"Individually statically reviewed Q9 leads",s.q10.individually_reviewed,"DRAFT_STATIC_REVIEW_ONLY",s.q10.url],
 ["Q10",s.q10.head_sha,"Promising concepts still held",s.q10.promising_but_held,"NOT_FEATURED",s.q10.url],
 ["Q10",s.q10.head_sha,"Other research/reject unchanged",s.q10.other_held,"NOT_FEATURED",s.q10.url],
 ["Q10",s.q10.head_sha,"Q9 leads remaining static review",s.q10.remaining_q9_entrypoints,"NOT_REVIEWED",s.q10.url],
 ...s.q10.methods.map(m=>["Q10",s.q10.head_sha,m.name+" (score / 20)",m.score,m.decision,s.q10.url])
 ];
 return [columns,...rows].map(r=>r.map(v=>'"'+String(v).replace(/"/g,'""')+'"').join(",")).join("\n")+"\n";
}

function renderReadme(s){
 return [
 "<!-- SKILLZ_WORKSTREAM_PROGRESS:START | generated: scripts/build-workstream-progress.mjs -->",
 "### Qualification progress: what is merged and what is still in review",
 "",
 "**Merged is not the same as proposed.** The current `main` checkpoint has **"+s.merged_baseline.featured+" Valuable References across "+s.merged_baseline.represented_domains+" domains**. Draft Q8 proposes **"+s.q8.proposed_featured+" study references across "+s.q8.represented_domains+" / "+s.q8.canonical_domains+" domains**. This is broad study-method representation, **not** full domain qualification or approval to install any skill.",
 "",
 "![Generated Skillz curation workstream progress: merged baseline, Q8 proposal, Q9 leads, Q10 static reviews and scanner outcomes.](docs/assets/qualification-workstream-progress.svg)",
 "",
 "| Workstream | Evidence-backed progress | Still required |",
 "|---|---|---|",
 "| **[Q8 draft]("+s.q8.url+")** | "+s.q8.proposed_featured+" proposed Valuable References; "+s.q8.represented_domains+" / "+s.q8.canonical_domains+" domains represented; pinned scanner "+s.q8.static_security.passed+" passed / "+s.q8.static_security.failed+" failed / "+s.q8.static_security.incomplete+" incomplete | Independent merge acceptance, security finding adjudication and separate behavioral testing |",
 "| **[Q9 draft]("+s.q9.url+")** | "+s.q9.pinned_entrypoints+" pinned discovery leads from "+s.q9.source_repositories+" source repositories across "+s.q9.covered_domains+" domains | Exact identity, rights and fit assessment; leads are not accepted skills |",
 "| **[Q10 draft]("+s.q10.url+")** | "+s.q10.individually_reviewed+" of those "+s.q9.pinned_entrypoints+" Q9 leads statically reviewed: "+s.q10.promising_but_held+" promising study concepts held, "+s.q10.other_held+" other research/rejected unchanged | "+s.q10.remaining_q9_entrypoints+(s.q10.remaining_q9_entrypoints===1?" lead still needs":" leads still need")+" detailed static review; external scanner/behavioral checks not run |",
 "",
 "**Remaining package boundary:** [ROS 2 Engineering scope mapping]("+s.q10.url+") found **"+s.q10.remaining_boundary.portable_bundle_files+" files** selected by the portable installer from **"+s.q10.remaining_boundary.source_repo_git_blobs+" repository files**, including "+s.q10.remaining_boundary.python_scripts+" Python scripts and "+s.q10.remaining_boundary.reference_files+" references. The plugin has a separate hook-enabled profile. This is **not** the eighth completed skill review, a security scan, an installation approval, or a hardware test.",
 "",
 "**Never add Q9 and Q10 counts:** Q10 examined "+s.q10.individually_reviewed+" of the same "+s.q9.pinned_entrypoints+" Q9 candidates, not "+(s.q9.pinned_entrypoints+s.q10.individually_reviewed)+" distinct skills. No Q9/Q10 approvals or shelf promotions occurred. **Zero unchanged-use approvals and zero behavioral validations** remain the governing outcome.",
 "",
 "[Spreadsheet-ready progress CSV](docs/data/qualification-workstream-progress.csv) · [Pinned progress snapshot](registry/curation-workstream-status-20261103.json) · [How to regenerate](docs/capability-dashboard-maintenance.md)",
 "",
 "*Snapshot "+s.as_of+". Draft branch revisions are pinned in the status ledger and may advance independently. This section is a review preview based on the Q8 draft, not a claim that Q8/Q9/Q10 has merged to `main`.*",
 "<!-- SKILLZ_WORKSTREAM_PROGRESS:END -->"
 ].join("\n")+"\n";
}

function updateReadme(readme,block){
 const start="<!-- SKILLZ_WORKSTREAM_PROGRESS:START",end="<!-- SKILLZ_WORKSTREAM_PROGRESS:END -->",anchor="<!-- SKILLZ_CAPABILITY_DASHBOARD:END -->";
 const i=readme.indexOf(start);
 if(i>=0){const j=readme.indexOf(end,i);if(j<0)throw Error("Missing progress closing marker");return readme.slice(0,i)+block.trimEnd()+readme.slice(j+end.length);}
 const a=readme.indexOf(anchor);if(a<0)throw Error("Missing canonical dashboard marker");
 const insertAt=a+anchor.length;return readme.slice(0,insertAt)+"\n\n"+block.trimEnd()+"\n"+readme.slice(insertAt);
}

const root=resolve(dirname(fileURLToPath(import.meta.url)),"..");
const load=(path)=>readFileSync(resolve(root,path),"utf8");
const status=JSON.parse(load("registry/curation-workstream-status-20261103.json"));
const q7=JSON.parse(load(status.merged_baseline.source));
const q8=JSON.parse(load(status.q8.source));
const pipe=JSON.parse(load("registry/qualification-pipeline-20261103.json"));
validateStatus(status,q7,q8,pipe);
const files={
  "README.md":updateReadme(load("README.md"),renderReadme(status)),
  "docs/assets/qualification-workstream-progress.svg":renderSvg(status),
  "docs/data/qualification-workstream-progress.csv":renderCsv(status)
};
const args=new Set(process.argv.slice(2));
if(args.has("--self-test")){
  if(args.has("--check"))throw Error("Use --self-test and --check separately");
  const a=files["README.md"];
  if(updateReadme(a,renderReadme(status))!==a)throw Error("Non-idempotent README");
  if((files["docs/data/qualification-workstream-progress.csv"].match(/\n/g)||[]).length!==(16+status.q10.methods.length))throw Error("CSV row count");
  if(!files["docs/assets/qualification-workstream-progress.svg"].includes('viewBox="0 0 1120 740"'))throw Error("SVG viewport");
  if(status.q10.remaining_q9_entrypoints===1 && (files["README.md"].includes("1 leads")||files["docs/assets/qualification-workstream-progress.svg"].includes("1 leads")))throw Error("Singular grammar regression");
  if(files["docs/assets/qualification-workstream-progress.svg"].includes("Six of eight Q9"))throw Error("Stale SVG accessibility description");
  if(status.q10.remaining_q9_entrypoints===1 && files["docs/assets/qualification-workstream-progress.svg"].includes("1 remain."))throw Error("Singular SVG accessibility grammar");
  const broken=JSON.parse(JSON.stringify(status));broken.q10.remaining_q9_entrypoints++;
  let rejected=false;try{validateStatus(broken,q7,q8,pipe)}catch(_){rejected=true}
  if(!rejected)throw Error("Mismatch not rejected");
  console.log("Workstream progress self-test passed");process.exit(0);
}
if(args.has("--check")){
 let stale=0;for(const [path,expected] of Object.entries(files)){if(!existsSync(resolve(root,path))||load(path)!==expected){console.error("STALE "+path);stale++;}}
 if(stale)process.exit(1);console.log("Workstream progress generated outputs are current");process.exit(0);
}
for(const [path,content] of Object.entries(files)){mkdirSync(dirname(resolve(root,path)),{recursive:true});writeFileSync(resolve(root,path),content,"utf8");console.log("Updated "+path)}
