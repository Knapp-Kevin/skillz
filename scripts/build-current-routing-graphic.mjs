#!/usr/bin/env node
// Explicit maintainer-only chart generator. Reads passive JSON; no network, runtime skill use, or CI.
import {readFileSync,writeFileSync} from 'node:fs';
import {resolve} from 'node:path';
const root=process.cwd();
const d=JSON.parse(readFileSync(resolve(root,'registry/capability-directory.json'),'utf8'));
const m={date:d.snapshot_date,mapped:d.identity_level_capability_links_mapped,reviewed:d.governed_identity_denominator,
first:d.first_party_identity_links_mapped,third:d.third_party_identity_links_mapped,
unmapped:d.unmapped_review_identity_count,linkedSubdomains:d.navigation_population.subdomains_with_evidence_linked_examples,
totalSubdomains:d.navigation_population.total_subdomains};
const actualIds=new Set(d.domains.flatMap(x=>x.subdomains.flatMap(s=>s.matched_skill_ids)));
const countedSub=d.domains.flatMap(x=>x.subdomains).filter(s=>s.matched_skill_ids.length>0).length;
if(actualIds.size!==m.mapped||d.skill_records.length!==m.mapped||m.first+m.third!==m.mapped||m.reviewed-m.mapped!==m.unmapped||countedSub!==m.linkedSubdomains)throw Error('Capability directory metrics inconsistent');
const render=(m) => {
  const pct=(n,d)=>Math.round(1000*n/d)/10;
  const bar=(y,n,d,textLabel)=>{
    const width=752,filled=+(width*n/d).toFixed(2);
    return `<text x="64" y="${y}" fill="#edf4ff" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="22" font-weight="650">${textLabel}</text>
<text x="935" y="${y}" fill="#edf4ff" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="22" text-anchor="end" font-weight="700">${n.toLocaleString("en-US")} / ${d.toLocaleString("en-US")}</text>
<rect x="64" y="${y+19}" width="${width}" height="16" rx="8" fill="#25344a"/>
<rect x="64" y="${y+19}" width="${filled}" height="16" rx="8" fill="url(#routeFill)"/>
<text x="835" y="${y+34}" fill="#9fb1c8" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="16" font-weight="600">${pct(n,d).toFixed(1)}%</text>`;
  };
  return `<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="410" viewBox="0 0 1000 410" role="img" aria-labelledby="chartTitle chartDesc">
<title id="chartTitle">Skillz current capability mapping: ${m.mapped} of ${m.reviewed} reviewed skill identities mapped and ${m.linkedSubdomains} of ${m.totalSubdomains} subdomains linked</title>
<desc id="chartDesc">Current as of ${m.date}. ${m.first} first-party and ${m.third} third-party reviewed skill identities linked to capability areas. ${m.unmapped} reviewed identities still need mapping. This shows discoverability, not install or behavioral approval.</desc>
<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#091727"/><stop offset="1" stop-color="#18253e"/></linearGradient><linearGradient id="routeFill" x1="0" y1="0" x2="1" y2="0"><stop stop-color="#2aa7b2"/><stop offset="1" stop-color="#7a79dd"/></linearGradient></defs>
<rect x="1" y="1" width="998" height="408" rx="20" fill="url(#bg)" stroke="#354761" stroke-width="2"/>
<text x="64" y="49" fill="#5fcad5" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="15" letter-spacing="2" font-weight="800">SKILLZ · CAPABILITY NAVIGATION</text>
<text x="64" y="87" fill="#ffffff" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="32" font-weight="750">Where the reviewed skills map</text>
<text x="934" y="49" fill="#acb9ce" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="15" text-anchor="end">Updated ${m.date}</text>
<text x="64" y="117" fill="#a5b7cb" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="17">Links to evidence, not approvals to install, execute, or share data.</text>
${bar(165,m.mapped,m.reviewed,"Reviewed skill identities mapped")}
${bar(253,m.linkedSubdomains,m.totalSubdomains,"Subdomains with evidence links")}
<line x1="64" y1="326" x2="935" y2="326" stroke="#3c4d63"/>
<text x="64" y="358" fill="#dce7f7" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="18" font-weight="600">${m.first} first-party + ${m.third} external reviewed identities mapped</text>
<text x="64" y="385" fill="#9fb1c8" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="16">${m.unmapped.toLocaleString("en-US")} reviewed identities remain unmapped · study-only references tracked separately</text>
</svg>\n`;
};
const output=render(m);
const target=resolve(root,'docs/assets/current-capability-mapping.svg');
if(process.argv.includes('--check')){
  if(readFileSync(target,'utf8')!==output)throw Error('Current capability chart drift. Run node scripts/build-current-routing-graphic.mjs');
  console.log('Current capability chart matches source');
}else{
  writeFileSync(target,output,'utf8');
  console.log('Updated current capability chart',m);
}
