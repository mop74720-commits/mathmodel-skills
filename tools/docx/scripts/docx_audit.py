#!/usr/bin/env python3
import argparse, json, zipfile, re, hashlib
from pathlib import Path
from lxml import etree
from docx import Document
NS={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main','m':'http://schemas.openxmlformats.org/officeDocument/2006/math'}

def sha256(p):
    h=hashlib.sha256();
    with open(p,'rb') as f:
        for c in iter(lambda:f.read(1024*1024),b''): h.update(c)
    return h.hexdigest()

def main():
    ap=argparse.ArgumentParser(description='Audit DOCX structure, equations, revisions, comments and media.')
    ap.add_argument('docx'); ap.add_argument('--json',action='store_true'); a=ap.parse_args(); p=Path(a.docx)
    d=Document(p); headings=sum(1 for x in d.paragraphs if x.style and x.style.name.lower().startswith('heading'))
    with zipfile.ZipFile(p) as z:
        names=set(z.namelist()); xml=etree.fromstring(z.read('word/document.xml'))
        omml=len(xml.xpath('.//m:oMath | .//m:oMathPara',namespaces=NS)); ins=len(xml.xpath('.//w:ins',namespaces=NS)); dele=len(xml.xpath('.//w:del',namespaces=NS))
        media=[n for n in names if n.startswith('word/media/')]; comments='word/comments.xml' in names
        text='\n'.join(x.text or '' for x in d.paragraphs)
        latex_markers=len(re.findall(r'\$[^\n$]+\$|\\\[[\s\S]*?\\\]',text))
    out={'path':str(p),'sha256':sha256(p),'paragraphs':len(d.paragraphs),'tables':len(d.tables),'headings':headings,'sections':len(d.sections),'images':len(media),'omml_equations':omml,'tracked_insertions':ins,'tracked_deletions':dele,'comments_part':comments,'literal_latex_markers':latex_markers}
    out['warnings']=[]
    if ins or dele: out['warnings'].append('tracked_changes_present')
    if comments: out['warnings'].append('comments_present')
    if latex_markers: out['warnings'].append('literal_latex_markers_present')
    print(json.dumps(out,ensure_ascii=False,indent=2) if a.json else '\n'.join(f"{k}: {v}" for k,v in out.items()))
    raise SystemExit(1 if out['warnings'] else 0)
if __name__=='__main__': main()
