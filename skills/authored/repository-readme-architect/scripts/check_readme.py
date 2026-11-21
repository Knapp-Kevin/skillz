#!/usr/bin/env python3
"""Read-only conservative README checks. Python 3.9+, standard library only.

Only local file paths, common GitHub heading anchors, and explicitly delimited
`generated:begin/end` blocks are checked. It is NOT a full Markdown renderer,
web link checker, claim verifier, or code executor.
"""
import argparse
import json
from pathlib import Path, PurePosixPath
import re
import sys
from urllib.parse import unquote, urlsplit

MAX_BYTES = 1_048_576
HEAD = re.compile(r'^ {0,3}(#{1,6})\s+(.+?)\s*$', re.M)
INLINE = re.compile(r'!?\[[^\]\n]+\]\(([^\n)]*)\)')
REFERENCE = re.compile(r'(?<!!)\[([^\]\n]+)\]\[([^\]\n]*)\]')
DEFINITION = re.compile(r'^ {0,3}\[([^\]\n]+)\]:\s*(?:<([^>\n]+)>|(\S+))',re.M)
GENERATED = re.compile(r'<!--\s*generated:(begin|end)\s*-->',re.I)
FENCE = re.compile(r'^ {0,3}(`{3,}|~{3,})')
SENSITIVE = re.compile(r'(?i)(?:token|key|secret|signature|password|auth|credential)=')


def clean_lines(text):
    """Retain line numbers, blank out fenced blocks and inline code spans."""
    result=[]; fenced=None
    for line in text.splitlines():
        m=FENCE.match(line)
        if m:
            ch=m.group(1)[0]; width=len(m.group(1))
            if fenced is None: fenced=(ch,width)
            elif ch==fenced[0] and width>=fenced[1]: fenced=None
            result.append(''); continue
        if fenced is not None: result.append(''); continue
        # Conservative: code spans will not be parsed as links.
        line=re.sub(r'(`+)(.*?)\1','',line)
        result.append(line)
    return result


def anchors(lines):
    slug_counts={}; out=set(); uncertain=False
    for line in lines:
        m=HEAD.match(line)
        if m:
            h=m.group(2).strip().rstrip('#').strip()
            if re.search(r'[<>\[\]{}]|\\',h): uncertain=True; continue
            h=re.sub(r'[*_`~]','',h).casefold()
            h=re.sub(r'[^\w\- ]','',h)
            h=re.sub(r'\s+','-',h)
            if not h: uncertain=True; continue
            n=slug_counts.get(h,0);slug_counts[h]=n+1
            out.add(h if n==0 else f'{h}-{n}')
        elif re.match(r'^ {0,3}(?:={3,}|-{3,})\s*$',line):
            uncertain=True  # Setext headings may create anchors.
    for line in lines:
        for a in re.finditer(r'<a\s+(?:id|name)\s*=\s*[\'\"]([^\'\"]+)[\'\"]',line,re.I):out.add(a.group(1))
    return out, uncertain


def bounded_path(root, path):
    p=PurePosixPath(path.replace('\\','/'))
    if p.is_absolute() or re.match(r'^[a-zA-Z]:',path):return None, 'OUT_OF_SCOPE_PATH'
    candidate=root
    for part in p.parts:
        if part in ('', '.'):continue
        if part=='..': candidate=candidate.parent
        else: candidate=candidate/part
        if not candidate.is_relative_to(root):return None, 'OUT_OF_SCOPE_PATH'
        if candidate.is_symlink():return None,'SYMLINK_NOT_FOLLOWED'
    return candidate,None


def local_link(value, source, root):
    s=value.strip()
    if s.startswith('<') and s.endswith('>'):s=s[1:-1]
    if re.search(r'\s+[\'\"]',s): s=re.split(r'\s+[\'\"]',s,maxsplit=1)[0]
    if not s:return 'AMBIGUOUS_LINK',None,None
    if SENSITIVE.search(s):return 'SENSITIVE_QUERY_NOT_INSPECTED',None,None
    if s.startswith('//'):return 'EXTERNAL_NOT_CHECKED',None,None
    if '(' in s or ')' in s:return 'COMPLEX_LINK_SYNTAX_NOT_CHECKED',None,None
    u=urlsplit(s)
    if u.scheme or u.netloc:
        return ('EXTERNAL_NOT_CHECKED' if u.scheme in ('https','http','mailto') else 'UNSUPPORTED_SCHEME'),None,None
    rawpath=unquote(u.path)
    if '\x00' in rawpath:return 'UNSAFE_PATH',None,None
    if rawpath.startswith('/'):
        return 'REPOSITORY_ROOT_ABSOLUTE_UNVERIFIED',None,None
    path,err=bounded_path(root,source.parent.relative_to(root).as_posix()+'/'+rawpath if rawpath else source.relative_to(root).as_posix())
    if err:return err,None,None
    if not path.exists():return 'BROKEN_LOCAL_FILE',path,u.fragment
    if not path.is_file():
        return 'DIRECTORY_ROUTING_NOT_CHECKED',path,u.fragment
    return 'LOCAL_FILE_EXISTS',path,unquote(u.fragment)


def generated_regions(text):
    # Mask code fences without moving character offsets so markers inside
    # documentation snippets are not mistaken for live generated blocks.
    mask=[];fenced=None
    for line in text.splitlines(keepends=True):
        m=FENCE.match(line)
        if m:
            ch=m.group(1)[0];width=len(m.group(1))
            if fenced is None:fenced=(ch,width)
            elif ch==fenced[0] and width>=fenced[1]:fenced=None
            mask.append(' '*len(line));continue
        mask.append(' '*len(line) if fenced else line)
    markers=[(x.group(1).lower(),x.start(),x.end()) for x in GENERATED.finditer(''.join(mask))]
    if not markers:return [],None
    regions=[]; start=None
    for kind,a,b in markers:
        if kind=='begin':
            if start is not None:return [],'MALFORMED_GENERATED_MARKERS'
            start=a
        else:
            if start is None:return [],'MALFORMED_GENERATED_MARKERS'
            regions.append(text[start:b]);start=None
    if start is not None:return [],'MALFORMED_GENERATED_MARKERS'
    return regions,None


def audit(root, readme, baseline=None):
    findings=[];counts={}
    def emit(line,status,kind):
        findings.append({'line':line,'status':status,'kind':kind})
        counts[status]=counts.get(status,0)+1
    raw=readme.read_text('utf-8'); lines=clean_lines(raw)
    definitions={}
    for line_no,line in enumerate(lines,1):
        for m in DEFINITION.finditer(line):
            key=' '.join(m.group(1).casefold().split())
            definitions[key]=m.group(2) or m.group(3)
    for line_no,line in enumerate(lines,1):
        links=[(m.group(1),'inline') for m in INLINE.finditer(line)]
        remainder=INLINE.sub('',line)
        if not DEFINITION.match(line):
            for m in REFERENCE.finditer(remainder):
                key=' '.join((m.group(2) or m.group(1)).casefold().split())
                if key in definitions:links.append((definitions[key],'reference'))
                else:emit(line_no,'UNRESOLVED_REFERENCE_DEFINITION','reference')
        for target,kind in links:
            status,path,fragment=local_link(target,readme,root)
            if status=='LOCAL_FILE_EXISTS' and fragment:
                if path.suffix.lower() not in ('.md','.markdown'):
                    status='ANCHOR_UNVERIFIED_NON_MARKDOWN'
                elif path.stat().st_size>MAX_BYTES:
                    status='TARGET_TOO_LARGE_TO_CHECK_ANCHOR'
                else:
                    text=path.read_text('utf-8')
                    seen,uncertain=anchors(clean_lines(text))
                    status='LOCAL_ANCHOR_FOUND' if fragment in seen else ('ANCHOR_UNVERIFIED_COMPLEX_MARKDOWN' if uncertain else 'BROKEN_LOCAL_ANCHOR')
            elif status=='LOCAL_FILE_EXISTS':status='LOCAL_FILE_EXISTS'
            emit(line_no,status,kind)
    regions,malformed=generated_regions(raw)
    if malformed:emit(0,malformed,'generated')
    if baseline is not None:
        prior,prior_malformed=generated_regions(baseline.read_text('utf-8'))
        if prior_malformed:emit(0,'BASELINE_GENERATED_MARKERS_MALFORMED','generated')
        elif prior!=regions:emit(0,'GENERATED_REGIONS_CHANGED','generated')
        else:emit(0,'GENERATED_REGIONS_UNCHANGED','generated')
    elif regions:emit(0,'GENERATED_BASELINE_NOT_SUPPLIED','generated')
    # Lack of findings does not imply a clean README; this is a bounded method.
    errors={'BROKEN_LOCAL_FILE','BROKEN_LOCAL_ANCHOR','UNRESOLVED_REFERENCE_DEFINITION',
            'MALFORMED_GENERATED_MARKERS','GENERATED_REGIONS_CHANGED',
            'BASELINE_GENERATED_MARKERS_MALFORMED','UNSUPPORTED_SCHEME',
            'OUT_OF_SCOPE_PATH','SYMLINK_NOT_FOLLOWED','UNSAFE_PATH'}
    return {'scope':'LOCAL_MARKDOWN_LINKS_AND_MARKED_GENERATED_REGIONS_ONLY',
            'source_authenticity_verified':False,'external_links_tested':False,'commands_executed':False,
            'readme_claims_verified':False,'reader_success_verified':False,
            'markdown_coverage_complete':False,
            'counts':counts,'findings':findings,'local_blockers':sum(counts.get(x,0) for x in errors)}


def safe_file(root,relative):
    if not relative or Path(relative).is_absolute():raise ValueError('relative file required')
    p,err=bounded_path(root,relative)
    if err:raise ValueError(err)
    if not p.is_file():raise ValueError('file missing or unsupported')
    if p.stat().st_size>MAX_BYTES:raise ValueError('file exceeds 1MiB')
    return p


def main(argv=None):
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--root',required=True,help='Authorized local repository root')
    p.add_argument('--readme',default='README.md',help='Relative README path')
    p.add_argument('--baseline',help='Optional relative baseline README to compare generated sections')
    args=p.parse_args(argv)
    try:
        root=Path(args.root).absolute()
        if any(x.is_symlink() for x in (root,*root.parents)):raise ValueError('symlinked root disallowed')
        if not root.is_dir():raise ValueError('root is not a directory')
        out=audit(root,safe_file(root,args.readme),safe_file(root,args.baseline) if args.baseline else None)
    except (OSError,ValueError,UnicodeError) as e:
        print('INVALID_INPUT: '+str(e),file=sys.stderr);return 2
    print(json.dumps(out,indent=2,sort_keys=True))
    return 1 if out['local_blockers'] else 0

if __name__=='__main__':sys.exit(main())
