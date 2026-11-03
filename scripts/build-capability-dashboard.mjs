#!/usr/bin/env node
// Generated dashboard: no external packages, no network, no source repository writes.
import { readFileSync, writeFileSync, mkdirSync, existsSync } from "node:fs";
import { resolve, dirname } from "node:path";
import { fileURLToPath } from "node:url";
function html(s){return String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;").replace(/'/g,"&apos;")}

function md(s){return String(s).replace(/\|/g,"\\|").replace(/\r?\n/g," ").trim()}

function dashboardData(audit,catalog,manifest){
 if(!audit||!Array.isArray(audit.domains)||!catalog||!Array.isArray(catalog.valuable_references))throw Error("Source ledgers missing required arrays");
 const approved=catalog.recommended_for_use_in_this_shelf||[];
 if(!Array.isArray(approved))throw Error("Approved list is not an array");
 const ref=catalog.valuable_references,domainIDs=new Set(audit.domains.map(d=>d.id)),all=[...ref,...approved],names=new Set();
 for(const d of audit.domains){
   if(names.has(d.id)||!Array.isArray(d.subdomains)||!d.id||!d.name)throw Error(`Invalid or duplicate domain: ${d.id}`);
   names.add(d.id);const subs=new Set(d.subdomains.map(s=>s.id));if(subs.size!==d.subdomains.length)throw Error(`Duplicate subdomain: ${d.id}`);
 }
 const refs=new Set();
 for(const x of all){
   if(!domainIDs.has(x.domain))throw Error(`Selected method outside canonical domain: ${x.name}/${x.domain}`);
   const d=audit.domains.find(d=>d.id===x.domain);
   if(!d.subdomains.some(s=>s.id===x.subdomain))throw Error(`Selected method outside canonical subdomain: ${x.name}/${x.subdomain}`);
   const key=x.id||`${x.source?.repository}/${x.source?.path}`||x.name;
   if(refs.has(key))throw Error(`Duplicate selected method: ${key}`);
   refs.add(key);
 }
 if(catalog.starter_shelf_totals?.valuable_reference!==ref.length)throw Error("Catalog's Valuable Reference count disagrees with its records");
 if(catalog.starter_shelf_totals?.recommended_for_use!==approved.length)throw Error("Catalog's Recommended-for-use count disagrees with its records");
 const rows=audit.domains.map(d=>{
   const matches=ref.filter(x=>x.domain===d.id),grants=approved.filter(x=>x.domain===d.id);
   const topics=[...new Set([...matches,...grants].map(x=>x.subdomain))];
   return {id:d.id,name:d.name,research_topics:d.subdomains.filter(s=>s.has_any_review_or_candidate_link===true).length,total_topics:d.subdomains.length,reference_methods:matches.length,approved_methods:grants.length,selected_topics:topics.length};
 });
 const totals={domains:rows.length,topics:rows.reduce((a,x)=>a+x.total_topics,0),linked_topics:rows.reduce((a,x)=>a+x.research_topics,0),reference_methods:ref.length,approved_methods:approved.length,selected_topics:rows.reduce((a,x)=>a+x.selected_topics,0),selected_domains:rows.filter(x=>x.selected_topics>0).length};
 if(audit.summary && (audit.summary.canonical_domains!==totals.domains||audit.summary.canonical_subdomains!==totals.topics||audit.summary.subdomains_with_any_review_or_candidate_link!==totals.linked_topics))throw Error("Historical research summary disagrees with domain rows");
 if(catalog.starter_shelf_totals?.distinct_capability_domains_represented!==new Set(ref.map(x=>x.domain)).size)throw Error("Consumer shelf domain count disagrees with selected records");
 return {rows,totals,as_of:manifest.as_of,research_source:manifest.historical_research_audit,featured_source:manifest.current_featured_shelf,research_date:audit.as_of||"2026-11-02"};
}

function dashboardCsv(model){
 const lines=[["Domain ID","Capability domain","Research-linked topics","Total topics","Research link coverage %","Valuable Reference methods","Approved-as-written methods","Subdomains with selected methods"]];
 for(const r of model.rows)lines.push([r.id,r.name,r.research_topics,r.total_topics,r.total_topics?Math.round(r.research_topics/r.total_topics*100):0,r.reference_methods,r.approved_methods,r.selected_topics]);
 return lines.map(cells=>cells.map(x=>`"${String(x).replace(/"/g,'""')}"`).join(",")).join("\n")+"\n";
}

function dashboardSvg(model){
 const W=1500,H=1180,parts=[],T=model.totals;
 const rowHeight=40,columnWidth=710;
 const startX=43,startY=367;
 const tile=[{v:T.domains.toString(),label:"CAPABILITY DOMAINS"},{v:`${T.linked_topics}/${T.topics}`,label:"TOPICS WITH RESEARCH LINKS"},{v:T.reference_methods.toString(),label:"METHODS SELECTED TO STUDY"},{v:T.approved_methods.toString(),label:"APPROVED AS WRITTEN"}];
 parts.push(`<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}" role="img" aria-labelledby="heading explanation">`);
 parts.push(`<title id="heading">Skillz capability overview: ${T.domains} domains with research leads and selected study methods</title>`);
 parts.push(`<desc id="explanation">Research-linked topics can include rejected candidate links and are not approved skills. ${T.linked_topics} of ${T.topics} topics have research links. A separate bounded featured shelf has ${T.reference_methods} selected methods across ${T.selected_domains} domains and ${T.approved_methods} approved as written. Every domain is listed in the README's accessible table and CSV.</desc>`);
 parts.push(`<defs><linearGradient id="back" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#0c1729"/><stop offset="1" stop-color="#162744"/></linearGradient><linearGradient id="bar" x1="0" y1="0" x2="1" y2="0"><stop stop-color="#39b9ec"/><stop offset="1" stop-color="#5eead4"/></linearGradient><linearGradient id="violet" x1="0" y1="0" x2="1" y2="0"><stop stop-color="#6d53b3"/><stop offset="1" stop-color="#a78bfa"/></linearGradient></defs>`);
 parts.push(`<rect width="${W}" height="${H}" rx="26" fill="url(#back)"/>`);
 parts.push(`<circle cx="1320" cy="80" r="240" fill="#2c446d" opacity=".13"/>`);
 parts.push(`<text x="48" y="65" fill="#e9f2ff" font-size="36" font-weight="700" font-family="Arial,Helvetica,sans-serif">Skillz | Capability evidence</text>`);
 parts.push(`<text x="49" y="104" fill="#b7c9de" font-size="19" font-family="Arial,Helvetica,sans-serif">Explore the whole library. Featured methods are only one small, carefully reviewed shelf.</text>`);
 tile.forEach((item,i)=>{const x=48+i*367;parts.push(`<rect x="${x}" y="134" width="350" height="101" rx="13" fill="#1d304a" stroke="#38506a"/>`);parts.push(`<text x="${x+20}" y="180" fill="#f0f6ff" font-size="31" font-weight="700" font-family="Arial,Helvetica,sans-serif">${html(item.v)}</text><text x="${x+20}" y="211" fill="#bfcee1" font-size="14" font-family="Arial,Helvetica,sans-serif">${html(item.label)}</text>`)});
 parts.push(`<rect x="50" y="264" width="16" height="14" rx="3" fill="#4ccddf"/><text x="78" y="278" fill="#d7e5f5" font-size="17" font-family="Arial,Helvetica,sans-serif">Research links (including rejected leads)</text>`);
 parts.push(`<rect x="495" y="264" width="16" height="14" rx="3" fill="#a78bfa"/><text x="523" y="278" fill="#d7e5f5" font-size="17" font-family="Arial,Helvetica,sans-serif">Methods selected to study (not installation clearance)</text>`);
 parts.push(`<text x="50" y="315" fill="#a9bbd2" font-size="16" font-family="Arial,Helvetica,sans-serif">“Not featured” means keep searching, not that a domain lacks useful skills.</text>`);
 for(let col=0;col<2;col++){
   const ox=startX+col*735,subset=model.rows.slice(col*17,(col+1)*17);
   parts.push(`<rect x="${ox}" y="338" width="${columnWidth}" height="733" rx="15" fill="#111e32" stroke="#354863"/>`);
   parts.push(`<text x="${ox+17}" y="365" fill="#eef4ff" font-size="15" font-weight="700" font-family="Arial,Helvetica,sans-serif">Capability domain</text>`);
   parts.push(`<text x="${ox+280}" y="365" fill="#c9e6f4" font-size="15" font-family="Arial,Helvetica,sans-serif">Research links</text>`);
   parts.push(`<text x="${ox+546}" y="365" fill="#ddccff" font-size="15" font-family="Arial,Helvetica,sans-serif">Featured</text>`);
   subset.forEach((r,i)=>{
     const y=startY+26+i*rowHeight,rowFill=i%2===0?"#1d2e46":"#16243a",pct=r.total_topics?r.research_topics/r.total_topics:0;
     parts.push(`<g><title>${html(r.name)}: research links in ${r.research_topics} of ${r.total_topics} topics; ${r.reference_methods} selected study methods across ${r.selected_topics} topics; ${r.approved_methods} approved unchanged</title>`);
     parts.push(`<rect x="${ox+8}" y="${y-20}" width="694" height="38" rx="7" fill="${rowFill}"/>`);
     const display=r.name.length>32?r.name.slice(0,29)+"…":r.name;
     parts.push(`<text x="${ox+16}" y="${y+3}" fill="#e7eff9" font-size="15" font-family="Arial,Helvetica,sans-serif">${html(display)}</text>`);
     parts.push(`<rect x="${ox+280}" y="${y-10}" width="120" height="14" rx="5" fill="#394a61"/>`);
     if(pct>0)parts.push(`<rect x="${ox+280}" y="${y-10}" width="${(120*pct).toFixed(2)}" height="14" rx="5" fill="url(#bar)"/>`);
     parts.push(`<text x="${ox+409}" y="${y+3}" fill="#e1effc" font-size="15" font-family="Arial,Helvetica,sans-serif">${r.research_topics}/${r.total_topics}</text>`);
     const yes=r.reference_methods+r.approved_methods>0;
     parts.push(`<rect x="${ox+541}" y="${y-17}" width="152" height="27" rx="8" fill="${yes?"#403360":"#1a2b3e"}" stroke="${yes?"#7d68bc":"#3a4a61"}"/>`);
     const label=yes?`${r.reference_methods} study · ${r.selected_topics} topics`:"not featured";
     parts.push(`<text x="${ox+617}" y="${y+2}" text-anchor="middle" fill="${yes?"#efe6ff":"#a1b2c8"}" font-weight="${yes?"700":"400"}" font-size="14" font-family="Arial,Helvetica,sans-serif">${html(label)}</text>`);
     parts.push(`</g>`);
   });
 }
 parts.push(`<text x="52" y="1116" fill="#e8f0fc" font-size="18" font-family="Arial,Helvetica,sans-serif">Research breadth is not quality clearance. A selected method is not permission to install or run its original package.</text>`);
 parts.push(`<text x="52" y="1151" fill="#b9cce1" font-size="16" font-family="Arial,Helvetica,sans-serif">Source: ${html(model.research_date)} research audit + ${html(model.as_of)} curated shelf | Generated from evidence ledgers, not hand-drawn</text>`);
 parts.push(`</svg>`);
 return parts.join("\n")+"\n";
}

function dashboardMarkdown(model){
 const T=model.totals;
 const csv="docs/data/capability-dashboard.csv",svg="docs/assets/capability-dashboard.svg";
 const rows=model.rows.map(r=>`| ${md(r.name)} | ${r.research_topics} / ${r.total_topics} | ${r.reference_methods||"Not featured"} | ${r.selected_topics} / ${r.total_topics} |`).join("\n");
 return [
 "<!-- SKILLZ_CAPABILITY_DASHBOARD:START | generated: scripts/build-capability-dashboard.mjs -->",
 "### Capability dashboard",
 "",
 `**${T.domains} capability areas** · **${T.topics} topics** · **${T.linked_topics} topics with research leads** · **${T.reference_methods} useful methods selected for study** · **${T.approved_methods} approved unchanged**`,
 "",
 `![Generated Skillz capability evidence dashboard, with research-linked topic bars and separately selected study methods across ${T.domains} domains.](${svg})`,
 "",
 `**How to read this:** Turquoise means a topic has a research or candidate link, which can include rejected skills. Purple means at least one method has been selected to study in our *bounded* featured shelf. Neither is installation clearance, and an unfeatured domain can still contain useful candidates.`,
 "",
 `<details><summary>Explore all ${T.domains} capability areas in a spreadsheet-style table</summary>`,
 "",
 "| Capability area | Research-linked topics | Featured study methods | Topics with featured methods |",
 "|---|---:|---:|---:|",
 rows,
 "",
 "</details>",
 "",
 `**[View the full CSV table](${csv})** · [Research source ledger](${model.research_source}) · [Featured reference ledger](${model.featured_source}) · [How the dashboard updates](docs/capability-dashboard-maintenance.md)`,
 "",
 `*As of ${model.as_of}. The research links are from a historical audit; not every candidate is useful. All-corpus qualification totals remain unknown. Never add topic-link counts to selected-method counts.*`,
 "<!-- SKILLZ_CAPABILITY_DASHBOARD:END -->"
 ].join("\n")+"\n";
}

function updateReadme(readme,newBlock){
 const open="<!-- SKILLZ_CAPABILITY_DASHBOARD:START",close="<!-- SKILLZ_CAPABILITY_DASHBOARD:END -->";
 const a=readme.indexOf(open);
 if(a>=0){const b=readme.indexOf(close,a);if(b<0)throw Error("Missing dashboard END marker");return readme.slice(0,a)+newBlock.trimEnd()+readme.slice(b+close.length);}
 const a0=readme.indexOf("### Two different views: research leads and the small featured shelf");
 const b0=readme.indexOf("## Our featured methods:",a0);
 if(a0<0||b0<0||b0<=a0)throw Error("Cannot identify existing dashboard section; refusing to overwrite README");
 return readme.slice(0,a0)+newBlock+"\n"+readme.slice(b0);
}

function selfTest(){
 const fixture={domains:[{id:"fiction",name:"Research & <Study>",subdomains:[{id:"one",has_any_review_or_candidate_link:true},{id:"two",has_any_review_or_candidate_link:false}]}],summary:{canonical_domains:1,canonical_subdomains:2,subdomains_with_any_review_or_candidate_link:1}};
 const catalog={valuable_references:[{id:"a",name:"Method",domain:"fiction",subdomain:"one"}],recommended_for_use_in_this_shelf:[],starter_shelf_totals:{valuable_reference:1,recommended_for_use:0,distinct_capability_domains_represented:1}};
 const manifest={as_of:"2026-11-03",historical_research_audit:"audit.json",current_featured_shelf:"catalog.json"};
 const model=dashboardData(fixture,catalog,manifest);
 if(model.totals.topics!==2||model.totals.linked_topics!==1||model.totals.reference_methods!==1)throw Error("Self-test totals failed");
 if(!dashboardSvg(model).includes("Research &amp; &lt;Study&gt;"))throw Error("SVG escaping failed");
 if(!dashboardCsv(model).includes('"Research & <Study>"'))throw Error("CSV quoting failed");
 const body=dashboardMarkdown(model),intro="Above\n### Two different views: research leads and the small featured shelf\nOLD\n## Our featured methods:\nAfter";
 const once=updateReadme(intro,body),twice=updateReadme(once,body);
 if(once!==twice||!once.includes("## Our featured methods:")||once.includes("\nOLD\n"))throw Error("README idempotence failed");
 try{dashboardData(fixture,{...catalog,valuable_references:[{id:"a",domain:"wrong",subdomain:"one"}]},manifest);throw Error("Expected invalid mapping error")}catch(e){if(e.message==="Expected invalid mapping error")throw e;}
 return true;
}
const ROOT=resolve(dirname(fileURLToPath(import.meta.url)),"..");
const read=(p)=>readFileSync(resolve(ROOT,p),"utf8");
const manifest=JSON.parse(read("registry/capability-dashboard-sources.json"));
const model=dashboardData(JSON.parse(read(manifest.historical_research_audit)),JSON.parse(read(manifest.current_featured_shelf)),manifest);
const paths={
 "README.md":updateReadme(read("README.md"),dashboardMarkdown(model)),
 "docs/data/capability-dashboard.csv":dashboardCsv(model),
 "docs/assets/capability-dashboard.svg":dashboardSvg(model)
};
if(process.argv.includes("--self-test")){selfTest();console.log("dashboard self-test passed");process.exit(0)}
if(process.argv.includes("--check")){
 let dirty=0;
 for(const [p,content] of Object.entries(paths)){if(!existsSync(resolve(ROOT,p))||read(p)!==content){console.error("STALE dashboard output: "+p);dirty++;}}
 if(dirty)process.exit(1);console.log("Capability dashboard is current: "+model.totals.domains+" domains, "+model.totals.reference_methods+" reference methods");process.exit(0);
}
for(const [p,content] of Object.entries(paths)){mkdirSync(dirname(resolve(ROOT,p)),{recursive:true});writeFileSync(resolve(ROOT,p),content,"utf8");console.log("Updated "+p)}
console.log("Dashboard generated from "+manifest.historical_research_audit+" and "+manifest.current_featured_shelf);
