#!/usr/bin/env python3
import argparse, json
from pathlib import Path

def main():
    ap=argparse.ArgumentParser(description='Detect PDF text/image blocks crossing page bounds or sitting too close to trim edge.')
    ap.add_argument('pdf'); ap.add_argument('--edge-mm',type=float,default=2.0); a=ap.parse_args(); import fitz
    d=fitz.open(a.pdf); edge=a.edge_mm*72/25.4; findings=[]
    for i,pg in enumerate(d):
        r=pg.rect
        for b in pg.get_text('blocks'):
            x0,y0,x1,y1=b[:4]
            if x0 < -0.5 or y0 < -0.5 or x1 > r.width+0.5 or y1 > r.height+0.5: findings.append({'page':i+1,'kind':'text','issue':'outside_page','bbox':[x0,y0,x1,y1]})
            elif min(x0,y0,r.width-x1,r.height-y1)<edge: findings.append({'page':i+1,'kind':'text','issue':'near_edge','bbox':[round(x0,1),round(y0,1),round(x1,1),round(y1,1)]})
    d.close(); print(json.dumps({'file':str(Path(a.pdf)),'edge_mm':a.edge_mm,'findings':findings,'status':'WARN' if findings else 'PASS'},ensure_ascii=False,indent=2))
if __name__=='__main__': main()
