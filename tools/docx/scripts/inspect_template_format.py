#!/usr/bin/env python3
import argparse, json, zipfile
from pathlib import Path
from lxml import etree
NS={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
def val(el,name): return el.get('{%s}%s'%(NS['w'],name)) if el is not None else None

def main():
    ap=argparse.ArgumentParser(description='Inspect reusable Word style/page settings without changing the document.')
    ap.add_argument('docx'); ap.add_argument('--json',action='store_true'); a=ap.parse_args(); p=Path(a.docx)
    with zipfile.ZipFile(p) as z:
        styles=etree.fromstring(z.read('word/styles.xml')); doc=etree.fromstring(z.read('word/document.xml'))
        rows=[]
        for st in styles.xpath('.//w:style',namespaces=NS):
            sid=val(st,'styleId'); typ=val(st,'type'); name=st.xpath('./w:name/@w:val',namespaces=NS); based=st.xpath('./w:basedOn/@w:val',namespaces=NS)
            ppr=st.find('w:pPr',NS); rpr=st.find('w:rPr',NS)
            fs=rpr.find('w:sz',NS) if rpr is not None else None; fonts=rpr.find('w:rFonts',NS) if rpr is not None else None
            rows.append({'id':sid,'type':typ,'name':name[0] if name else None,'based_on':based[0] if based else None,'font_ascii':val(fonts,'ascii') if fonts is not None else None,'font_eastAsia':val(fonts,'eastAsia') if fonts is not None else None,'font_size_half_points':val(fs,'val') if fs is not None else None})
        sects=[]
        for s in doc.xpath('.//w:sectPr',namespaces=NS):
            pg=s.find('w:pgSz',NS); mar=s.find('w:pgMar',NS)
            sects.append({'width_twips':val(pg,'w') if pg is not None else None,'height_twips':val(pg,'h') if pg is not None else None,'orientation':val(pg,'orient') if pg is not None else None,'margins_twips':{k:val(mar,k) for k in ('top','right','bottom','left','header','footer')} if mar is not None else None})
        out={'file':str(p),'styles':rows,'sections':sects}
        print(json.dumps(out,ensure_ascii=False,indent=2))
if __name__=='__main__': main()
