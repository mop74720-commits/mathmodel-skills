#!/usr/bin/env python3
"""Low-memory XLSX row streaming for very large read-only contest attachments."""
import argparse, csv, json, re
from pathlib import Path
from zipfile import ZipFile
import xml.etree.ElementTree as ET

MAIN_NS='http://schemas.openxmlformats.org/spreadsheetml/2006/main'
REL_NS='http://schemas.openxmlformats.org/officeDocument/2006/relationships'

def colnum(ref):
    m=re.match(r'([A-Z]+)',ref or 'A1'); n=0
    for ch in (m.group(1) if m else 'A'): n=n*26+ord(ch)-64
    return n

class StreamBook:
    def __init__(self,path):
        self.path=Path(path); self.z=ZipFile(self.path); self.sst=self._shared(); self.sheets=self._sheets()
    def close(self): self.z.close()
    def __enter__(self): return self
    def __exit__(self,*a): self.close()
    def _shared(self):
        name='xl/sharedStrings.xml'
        if name not in self.z.namelist(): return []
        out=[]; si=f'{{{MAIN_NS}}}si'; tt=f'{{{MAIN_NS}}}t'
        with self.z.open(name) as fh:
            for ev,el in ET.iterparse(fh,events=('end',)):
                if el.tag==si:
                    out.append(''.join((t.text or '') for t in el.iter(tt))); el.clear()
        return out
    def _sheets(self):
        wb=ET.fromstring(self.z.read('xl/workbook.xml')); rel=ET.fromstring(self.z.read('xl/_rels/workbook.xml.rels'))
        relmap={x.attrib['Id']:x.attrib['Target'] for x in rel}; out={}
        sheets=wb.find(f'{{{MAIN_NS}}}sheets')
        for s in sheets:
            tgt=relmap[s.attrib[f'{{{REL_NS}}}id']]
            out[s.attrib['name']]=tgt.lstrip('/') if tgt.startswith('/') else 'xl/'+tgt.lstrip('./')
        return out
    def iter_rows(self,sheet):
        row_tag=f'{{{MAIN_NS}}}row'; cell_tag=f'{{{MAIN_NS}}}c'; val_tag=f'{{{MAIN_NS}}}v'; text_tag=f'{{{MAIN_NS}}}t'
        with self.z.open(self.sheets[sheet]) as fh:
            for ev,el in ET.iterparse(fh,events=('end',)):
                if el.tag!=row_tag: continue
                vals={}
                for c in list(el):
                    if c.tag!=cell_tag: continue
                    j=colnum(c.attrib.get('r','A1')); typ=c.attrib.get('t'); v=c.find(val_tag); val=None if v is None else v.text
                    if val is not None and typ=='s': val=self.sst[int(val)]
                    elif val is not None and typ=='b': val=bool(int(val))
                    elif typ=='inlineStr': val=''.join(t.text or '' for t in c.iter(text_tag))
                    vals[j]=val
                maxj=max(vals) if vals else 0
                yield [vals.get(j) for j in range(1,maxj+1)]
                el.clear()

def main():
    ap=argparse.ArgumentParser(description='Stream rows from a large XLSX without loading workbook styles/cells into memory.')
    ap.add_argument('xlsx'); ap.add_argument('--sheet'); ap.add_argument('--skip-rows',type=int,default=0); ap.add_argument('--max-rows',type=int)
    ap.add_argument('--output'); ap.add_argument('--json-summary',action='store_true'); ap.add_argument('--sample-rows',type=int,default=5)
    a=ap.parse_args(); total=0; max_cols=0; sample=[]
    with StreamBook(a.xlsx) as wb:
        sheet=a.sheet or next(iter(wb.sheets))
        if sheet not in wb.sheets: raise SystemExit(f'unknown sheet: {sheet}; choices={list(wb.sheets)}')
        outfh=open(a.output,'w',encoding='utf-8-sig',newline='') if a.output else None; writer=csv.writer(outfh) if outfh else None
        try:
            for idx,row in enumerate(wb.iter_rows(sheet)):
                if idx<a.skip_rows: continue
                total+=1; max_cols=max(max_cols,len(row))
                if len(sample)<a.sample_rows: sample.append(row)
                if writer: writer.writerow(row)
                elif not a.json_summary: csv.writer(__import__('sys').stdout).writerow(row)
                if a.max_rows and total>=a.max_rows: break
        finally:
            if outfh: outfh.close()
    if a.json_summary:
        print(json.dumps({'path':str(Path(a.xlsx)),'sheet':sheet,'rows_streamed':total,'max_cols_seen':max_cols,'sample':sample,'mode':'read-only-stream'},ensure_ascii=False,indent=2))
if __name__=='__main__': main()
