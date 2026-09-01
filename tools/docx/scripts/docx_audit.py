#!/usr/bin/env python3
import argparse, json, re, zipfile
from collections import Counter
from pathlib import Path
from lxml import etree

NS={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main','m':'http://schemas.openxmlformats.org/officeDocument/2006/math','r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships','pr':'http://schemas.openxmlformats.org/package/2006/relationships'}

def xml(z,name):
    try: return etree.fromstring(z.read(name))
    except KeyError: return None

def text_of(root):
    if root is None: return ''
    return ''.join(root.xpath('.//w:t/text()',namespaces=NS))

def main():
    ap=argparse.ArgumentParser(description='Read-only DOCX structural/format/equation/revision audit.')
    ap.add_argument('docx'); ap.add_argument('--json',action='store_true'); a=ap.parse_args(); p=Path(a.docx)
    issues=[]; warnings=[]
    if not p.exists(): raise SystemExit('file not found')
    with zipfile.ZipFile(p) as z:
        names=set(z.namelist()); doc=xml(z,'word/document.xml'); styles=xml(z,'word/styles.xml'); rels=xml(z,'word/_rels/document.xml.rels')
        if doc is None: issues.append('missing_word_document_xml')
        paras=doc.xpath('.//w:p',namespaces=NS) if doc is not None else []
        tables=doc.xpath('.//w:tbl',namespaces=NS) if doc is not None else []
        omml=len(doc.xpath('.//m:oMath|.//m:oMathPara',namespaces=NS)) if doc is not None else 0
        revisions=len(doc.xpath('.//w:ins|.//w:del|.//w:moveFrom|.//w:moveTo',namespaces=NS)) if doc is not None else 0
        comments=len(xml(z,'word/comments.xml').xpath('.//w:comment',namespaces=NS)) if 'word/comments.xml' in names else 0
        hyperlinks=len(doc.xpath('.//w:hyperlink',namespaces=NS)) if doc is not None else 0
        fields=len(doc.xpath('.//w:fldSimple|.//w:instrText',namespaces=NS)) if doc is not None else 0
        drawings=len(doc.xpath('.//w:drawing|.//w:pict',namespaces=NS)) if doc is not None else 0
        media=[n for n in names if n.startswith('word/media/') and not n.endswith('/')]
        fulltext=text_of(doc)
        latex_markers=re.findall(r'(?<!\\)\$[^$]{1,200}\$|\\begin\{(?:equation|align|gather)|\\frac\{|\\alpha\b|\\beta\b',fulltext)
        if latex_markers: warnings.append('literal_latex_markers_present')
        if revisions: warnings.append('tracked_changes_present')
        if comments: warnings.append('comments_present')
        # paragraph styles and headings
        style_counts=Counter(); heading_count=0; empty_heading=0
        for par in paras:
            sid=par.xpath('./w:pPr/w:pStyle/@w:val',namespaces=NS); sid=sid[0] if sid else '(none)'; style_counts[sid]+=1
            if re.match(r'(?i)heading|标题',sid):
                heading_count+=1
                if not ''.join(par.xpath('.//w:t/text()',namespaces=NS)).strip(): empty_heading+=1
        if empty_heading: warnings.append(f'empty_heading_paragraphs:{empty_heading}')
        # relationships integrity
        broken=[]; external=0
        if rels is not None:
            for rel in rels:
                target=rel.get('Target',''); mode=rel.get('TargetMode')
                if mode=='External': external+=1; continue
                if not target: continue
                base=Path('word'); candidate=(base/target).as_posix()
                # normalize ..
                parts=[]
                for x in candidate.split('/'):
                    if x=='..':
                        if parts: parts.pop()
                    elif x!='.': parts.append(x)
                norm='/'.join(parts)
                if norm not in names: broken.append(norm)
        if broken: issues.append('broken_internal_relationships')
        # section setup
        sects=doc.xpath('.//w:sectPr',namespaces=NS) if doc is not None else []
        section_info=[]
        for s in sects:
            pg=s.xpath('./w:pgSz',namespaces=NS); mar=s.xpath('./w:pgMar',namespaces=NS)
            section_info.append({'page_size':dict(pg[0].attrib) if pg else None,'margins':dict(mar[0].attrib) if mar else None})
        # styles summary
        declared_styles=[]
        if styles is not None:
            for st in styles.xpath('.//w:style',namespaces=NS):
                declared_styles.append({'id':st.get('{%s}styleId'%NS['w']),'type':st.get('{%s}type'%NS['w'])})
        status='FAIL' if issues else ('WARN' if warnings else 'PASS')
        obj={'status':status,'file':str(p),'bytes':p.stat().st_size,'paragraphs':len(paras),'tables':len(tables),'headings':heading_count,'drawings':drawings,'media_files':len(media),'omml_equations':omml,'tracked_changes':revisions,'comments':comments,'hyperlinks':hyperlinks,'fields':fields,'external_relationships':external,'style_usage':dict(style_counts.most_common(25)),'declared_styles':len(declared_styles),'sections':section_info,'broken_relationship_targets':broken[:20],'literal_latex_marker_count':len(latex_markers),'issues':issues,'warnings':warnings,'note':'Read-only mechanical audit; it does not establish scientific correctness.'}
    print(json.dumps(obj,ensure_ascii=False,indent=2) if a.json else json.dumps(obj,ensure_ascii=False,indent=2))
    raise SystemExit(1 if issues else 0)
if __name__=='__main__': main()
