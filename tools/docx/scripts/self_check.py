#!/usr/bin/env python3
import argparse, json, subprocess, sys, tempfile
from pathlib import Path

def main():
    ap=argparse.ArgumentParser(description='Run DOCX audit and optional real render as one deterministic self-check.')
    ap.add_argument('docx'); ap.add_argument('--render',action='store_true'); ap.add_argument('--output-dir'); a=ap.parse_args(); root=Path(__file__).resolve().parent
    audit=subprocess.run([sys.executable,str(root/'docx_audit.py'),a.docx,'--json'],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
    try: audit_obj=json.loads(audit.stdout)
    except Exception: audit_obj={'status':'FAIL','raw':audit.stdout[-4000:]}
    render_obj=None
    if a.render:
        out=Path(a.output_dir) if a.output_dir else Path(tempfile.mkdtemp(prefix='docx_render_'))
        r=subprocess.run([sys.executable,str(root/'render_docx.py'),a.docx,'--output-dir',str(out)],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
        pages=sorted(str(x) for x in out.glob('page-*.png'))
        render_obj={'returncode':r.returncode,'pages':pages,'output_dir':str(out),'log_tail':r.stdout[-1500:]}
    status='FAIL' if audit_obj.get('status')=='FAIL' or (render_obj and render_obj['returncode']) else ('WARN' if audit_obj.get('status')=='WARN' else 'PASS')
    print(json.dumps({'status':status,'audit':audit_obj,'render':render_obj},ensure_ascii=False,indent=2)); raise SystemExit(1 if status=='FAIL' else 0)
if __name__=='__main__': main()
