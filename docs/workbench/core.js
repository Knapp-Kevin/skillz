/* Pure, offline calculations and source normalization. No host actions. */
(function(root){
"use strict";
const repo="https://github.com/Knapp-Kevin/skillz";
const profiles=[
["github-copilot","GitHub Copilot","directory",".github/skills/<skill>/","https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills"],
["claude-code","Claude Code","directory",".claude/skills/<skill>/","https://code.claude.com/docs/en/skills"],
["openai-codex","OpenAI Codex","directory",".agents/skills/<skill>/","https://developers.openai.com/codex/skills"],
["gemini-cli","Gemini CLI","directory",".gemini/skills/<skill>/","https://geminicli.com/docs/cli/skills/"],
["hermes-agent","Hermes Agent","directory","~/.hermes/skills/<skill>/","https://hermes-agent.nousresearch.com/docs/user-guide/features/skills"],
["m365-copilot-chat","Microsoft 365 Copilot Chat","zip","Agents → More agents → Add → Upload skill","https://learn.microsoft.com/en-us/plugins/build-copilot-chat-skills"],
["m365-agent-builder","Microsoft 365 Agent Builder","zip","Agent Builder → Skills → Upload ZIP","https://learn.microsoft.com/en-us/plugins/agent-builder-add-skills"],
["m365-agents-toolkit","Microsoft 365 Agents Toolkit","directory","appPackage/skills/<skill>/","https://learn.microsoft.com/en-us/plugins/build-declarative-agents-add-custom-skills"],
["chatgpt","ChatGPT / OpenAI Skills","manual","Current account's supported Skills interface","https://developers.openai.com/plugins/concepts/skills"],
["gemini-apps","Gemini Apps","manual","Account-specific Skills interface","https://support.google.com/gemini/answer/17094296"],
["other","Other / not sure","manual","Identify exact host; portable handoff only",repo+"/blob/main/docs/getting-started-with-skills.md"]
].map(([id,label,mode,destination,docs])=>({id,label,mode,destination,docs,strict:["m365-agent-builder","m365-agents-toolkit"].includes(id)}));
const domains=[["planning","Planning & decisions"],["time-productivity","Personal productivity"],["software-engineering","Software engineering"],["cloud-devops","CI & delivery"],["technical-writing","Documentation"],["memory-context","Files & knowledge"],["research","Research & evidence"],["agent-mcp-development","AI agents & tools"],["security","Security & permissions"],["business","Business & operations"],["sales","Sales"],["finance","Finance"],["marketing","Marketing"],["communication","Communication"],["career","Career"],["education","Learning"],["fiction-narrative-worldbuilding","Creative writing"],["music-composition","Music"],["law","Legal review"]];
function normalize(a,g,proof={}){
 const retired=new Set((g.retired_legacy_ids||[]).map(x=>x.id)), seen=new Set(), rows=[];
 for(const s of a.skills||[]){
  const id="local-skills/"+s.id;
  if(retired.has(id)||seen.has(id))continue;
  const p=proof.cards?.[s.id];const verified=Boolean(p&&p.blob===s.skill_blob_sha&&s.license_spdx==="MIT"&&/^[0-9a-f]{40}$/.test(proof.revision||""));
  seen.add(id); rows.push({id,title:s.display_name||s.id,tags:s.capability_paths||[],type:"authored",family:"local-skills",path:s.entrypoint,version:s.package_version,license:s.license_spdx,review:s.review_status,behavior:s.behavioral_validation,blob:s.skill_blob_sha,tree:s.package_tree_sha,benefit:verified?p.benefit:null,evidence_example:verified?p.evidence:null,source_revision:verified?proof.revision:null});
 }
 for(const id of [...(g.first_party_ids||[]),...(g.third_party_ids||[])]){
  if(typeof id!=="string"||seen.has(id)||retired.has(id))continue;seen.add(id);
  rows.push({id,title:id.split("/").slice(1).join("/").replace(/-/g," "),family:id.split("/")[0],tags:[],type:"lead",rights_status:"REFERENCE_ONLY_UNVERIFIED_UPSTREAM_RIGHTS"});
 }
 return rows;
}
const stop=new Set(["the","and","with","for","my","our","want","need","help","into","from","that","this","work","using","can","would","like","more","better","how","to","of","in","on","a","an","is","it"]);
const words=s=>String(s||"").toLowerCase().split(/[^a-z0-9]+/).filter(x=>x.length>1&&!stop.has(x)).map(x=>x.length>4&&x.endsWith("s")&&!x.endsWith("ss")?x.slice(0,-1):x);
const unique=a=>[...new Set(a)];
function search(rows,query,domain,source){
 const terms=unique(words(query)); const domainTerms=words(domain);
 return rows.map(row=>{
  const hay=words([row.title,row.id,...row.tags,row.benefit,row.evidence_example].join(" "));const title=words(row.title);
  const matched=terms.filter(t=>hay.some(w=>w===t||w.startsWith(t)));const matches=matched.length;
  const domainMatch=!domain||row.tags.some(t=>t===domain||t.startsWith(domain+"/"))||domainTerms.every(t=>hay.includes(t));
  const score=matches*3+terms.filter(t=>title.includes(t)).length;
  return {row,score,domainMatch,matched};
 }).filter(x=>(!source||x.row.type===source)&&x.domainMatch&&(!terms.length||x.score>0))
 .sort((a,b)=>b.score-a.score||(a.row.type==="authored"?0:1)-(b.row.type==="authored"?0:1)||a.row.title.localeCompare(b.row.title)||a.row.id.localeCompare(b.row.id)).map(x=>({...x.row,matched_terms:x.matched}));
}
function nonnegative(value){const n=Number(value);return Number.isFinite(n)&&n>=0?n:0;}
function estimate(x,weeks=13){
 const use=nonnegative(x.uses), before=nonnegative(x.before), after=nonnegative(x.after);
 const setup=nonnegative(x.setup), maintenance=nonnegative(x.maintenance), rate=nonnegative(x.rate);
 const weekly=use*(before-after)/60-maintenance/60;
 const horizon=nonnegative(weeks);const net=weekly*horizon-setup/60;
 return {weekly,net,setupHours:setup/60,payback:weekly>0?setup/60/weekly:null,value:net*rate,rate,horizon};
}
function portfolio(items,weeks,rate){
 const groups=new Map();let setup=0,maintenance=0;
 for(const x of items){
  const key=String(x.need||"").trim().toLowerCase().replace(/\s+/g," ");
  if(!key)continue;
  const gross=nonnegative(x.uses)*(nonnegative(x.before)-nonnegative(x.after))/60;
  if(!groups.has(key))groups.set(key,[]);
  groups.get(key).push(gross);
  setup+=nonnegative(x.setup)/60;maintenance+=nonnegative(x.maintenance)/60;
 }
 // Same workflow: take at most the largest positive benefit, plus all negative effects.
 // This conservative screen is not a measured causal or financial result.
 const gross=[...groups.values()].reduce((s,v)=>s+Math.max(0,...v)+v.filter(x=>x<0).reduce((a,b)=>a+b,0),0);
 const weekly=gross-maintenance,net=weekly*nonnegative(weeks)-setup;
 return {weekly,net,value:net*nonnegative(rate),setup,overlap:[...groups].filter(([,v])=>v.length>1).map(([k])=>k),unassigned:items.filter(x=>!String(x.need||"").trim()).length};
}
function blueprint(fields,steps){
 const kind=fields.kind==="phased"?"phased":"single", name=fields.name.trim();
 const errors=[];if(!/^[a-z][a-z0-9]*(?:-[a-z0-9]+)*$/.test(name)||name.length>64)errors.push("Use a lowercase, hyphenated skill name of at most 64 characters.");
 for(const k of ["description","outcome","trigger","non_trigger","inputs","verification","failure_handling","copyright_holder"]){
  const v=(fields[k]||"").trim();if(v.length<(k==="copyright_holder"?4:12))errors.push("Complete "+k.replace(/_/g," ")+".");
  if(v.length>(k==="description"?300:16000))errors.push(k+" exceeds its blueprint length limit.");
  if(/\b(?:TODO|TBD|FIXME|lorem ipsum|fill in later)\b|<[^>\n]{1,70}>/i.test(v))errors.push("Remove placeholder text from "+k+".");
 }
 if(/[\r\n]/.test(fields.description||"")||/[\r\n]/.test(fields.copyright_holder||""))errors.push("Description and copyright holder must be single-line.");
 if(!fields.rights)errors.push("Confirm the material is original; adapted material needs separate review.");
 if(!["read-only","approval-gated"].includes(fields.authority))errors.push("Choose a valid authority ceiling.");
 if(steps.length<(kind==="phased"?2:1)||steps.length>32)errors.push("Supply the required number of actual steps (maximum 32).");
 const normalized=steps.map((s,i)=>({id:"step-"+(i+1),title:s.title.trim(),instructions:s.instructions.trim(),output:s.output.trim()}));
 for(const s of normalized)for(const k of ["title","instructions","output"]){if(s[k].length<(k==="title"?6:12)||s[k].length>16000||/\b(?:TODO|TBD|FIXME|lorem ipsum|fill in later)\b|<[^>\n]{1,70}>/i.test(s[k]))errors.push("Complete "+s.id+" "+k+" without placeholders.");}
 if(errors.length)return {errors};
 return {errors:[],blueprint:{schema_version:1,kind,name,description:fields.description.trim(),outcome:fields.outcome.trim(),trigger:fields.trigger.trim(),non_trigger:fields.non_trigger.trim(),inputs:fields.inputs.trim(),verification:fields.verification.trim(),failure_handling:fields.failure_handling.trim(),authority:fields.authority,copyright_holder:fields.copyright_holder.trim(),rights_declaration:"caller-asserts-original-content",steps:normalized,modules:[],preference_slots:[]}};
}
function handoff({need,host,items,weeks,rate,build,capabilities}){
 return {schema_version:1,kind:"skillz-workbench-handoff",status:"USER_AUTHORED_PLAN_NOT_INSTALLED",source:repo,bootstrap:repo+"/blob/main/engine/skills/skill-bootstrap/SKILL.md",discovery_contract:repo+"/blob/main/docs/discovery/full-corpus-search-contract.md",need,host:host||"other",capabilities,selection:items.map(({row,...x})=>({candidate:row,...x})),estimate:{assumptions:"User estimates, no observed improvement or guaranteed ROI. Group estimates by recurring task to avoid obvious duplication.",...portfolio(items,weeks,rate),weeks,rate},custom_skill:build||null,required_agent_actions:["Reconfirm host, scope and permission; model name is not the host.","Expand discovery across accessible source families by outcome and mechanism. Treat the shortlist as leads only.","Review exact upstream source, revision, package-level license, NOTICE and security/dependencies. Reference identifiers do not grant copying, adaptation, commercial use, redistribution or installation rights. If any applicable rights are unknown or prohibited, HOLD that action; compare lawful alternatives and decide USE_EXISTING, ADAPT, CREATE, COMPOSE or HOLD.","Run shared host compatibility preflight on the entire candidate; resolve blockers or provide portable handoff.","Challenge positive and negative triggers, unavailable capabilities, authority and false success. Never imply install or execution from a static pass.","Install only with explicit authorization and supported host mechanism; otherwise supply complete package and user instructions."]};
}
const api={profiles,domains,normalize,search,estimate,portfolio,blueprint,handoff};if(typeof module!=="undefined"&&module.exports)module.exports=api;else root.SkillzCore=api;
})(globalThis);
