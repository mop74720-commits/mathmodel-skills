#!/usr/bin/env python3
import argparse, hashlib, importlib.metadata, json, platform, shutil, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path

FEATURES = {
    'data': [('python','numpy'), ('python','pandas')],
    'visualization': [('python','matplotlib'), ('python','Pillow')],
    'optimization': [('python','scipy')],
    'ml': [('python','scikit-learn')],
    'xlsx': [('python','openpyxl')],
    'docx': [('python','python-docx'), ('python','lxml')],
    'pdf': [('python','PyMuPDF')],
    'latex': [('exe','xelatex')],
    'word-render': [('exe','libreoffice')],
    'matlab': [('exe','matlab')],
}

def digest(p):
    p=Path(p).resolve(); h=hashlib.sha256()
    with p.open('rb') as f:
        for chunk in iter(lambda:f.read(1024*1024), b''): h.update(chunk)
    return {'path':str(p),'bytes':p.stat().st_size,'sha256':h.hexdigest()}

def package_version(name):
    try: return importlib.metadata.version(name)
    except importlib.metadata.PackageNotFoundError: return None

def git_state(cwd):
    if not shutil.which('git'): return None
    try:
        top=subprocess.run(['git','rev-parse','--show-toplevel'],cwd=cwd,text=True,stdout=subprocess.PIPE,stderr=subprocess.DEVNULL,timeout=5)
        if top.returncode: return None
        commit=subprocess.run(['git','rev-parse','HEAD'],cwd=cwd,text=True,stdout=subprocess.PIPE,stderr=subprocess.DEVNULL,timeout=5).stdout.strip()
        dirty=bool(subprocess.run(['git','status','--porcelain'],cwd=cwd,text=True,stdout=subprocess.PIPE,stderr=subprocess.DEVNULL,timeout=5).stdout.strip())
        return {'root':top.stdout.strip(),'commit':commit,'dirty':dirty}
    except Exception: return None

def doctor(a):
    rows=[]; missing=[]
    for feature in a.features:
        if feature not in FEATURES:
            rows.append({'feature':feature,'status':'unknown_feature'}); missing.append(feature); continue
        for kind,name in FEATURES[feature]:
            if kind=='python':
                v=package_version(name); ok=v is not None; rows.append({'feature':feature,'kind':kind,'name':name,'ok':ok,'version':v})
            else:
                path=shutil.which(name); ok=bool(path); rows.append({'feature':feature,'kind':kind,'name':name,'ok':ok,'path':path})
            if not ok: missing.append(f'{feature}:{name}')
    print(json.dumps({'ok':not missing,'checks':rows,'missing':missing},ensure_ascii=False,indent=2))
    return 0 if not missing else 2

def parse_dependency(items):
    out={}
    for raw in items:
        if '=' not in raw:
            raise ValueError(f'dependency must be name=version, got: {raw}')
        name,version=raw.split('=',1)
        name=name.strip(); version=version.strip()
        if not name: raise ValueError(f'empty dependency name: {raw}')
        out[name]=version
    return out

def create(a):
    cwd=Path(a.cwd or '.').resolve(); inputs=[]; artifacts=[]; missing=[]
    for x in a.input:
        p=Path(x)
        if not p.exists(): missing.append(str(p))
        else: inputs.append(digest(p))
    for x in a.artifact:
        p=Path(x)
        if not p.exists(): missing.append(str(p))
        else: artifacts.append(digest(p))
    if missing:
        print(json.dumps({'ok':False,'missing_files':missing},ensure_ascii=False,indent=2),file=sys.stderr); return 2
    packages={name:package_version(name) for name in sorted(set(a.package))}
    try: dependencies=parse_dependency(a.dependency)
    except ValueError as e:
        print(json.dumps({'ok':False,'error':str(e)},ensure_ascii=False,indent=2),file=sys.stderr); return 2
    runtime_name=a.runtime or 'python'
    runtime_version=a.runtime_version or (sys.version.split()[0] if runtime_name=='python' else None)
    manifest={
        'schema':'mathmodel-run-manifest/v2',
        'created_at_utc':datetime.now(timezone.utc).isoformat(),
        'run_id':a.run_id,
        'command':a.command,
        'cwd':str(cwd),
        'seed':a.seed,
        'runtime':{'name':runtime_name,'version':runtime_version},
        'host':{'python':sys.version.split()[0],'implementation':platform.python_implementation(),'platform':platform.platform()},
        'git':git_state(cwd),
        'python_packages':packages,
        'dependencies':dependencies,
        'inputs':inputs,
        'artifacts':artifacts,
        'notes':a.note,
    }
    out=Path(a.output); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
    print(out); return 0

def verify(a):
    m=json.loads(Path(a.manifest).read_text(encoding='utf-8')); checks=[]; ok=True
    schema=m.get('schema')
    if schema not in ('mathmodel-run-manifest/v1','mathmodel-run-manifest/v2'):
        print(json.dumps({'ok':False,'reason':'unsupported_schema','schema':schema},ensure_ascii=False,indent=2)); return 2
    for group in ('inputs','artifacts'):
        for item in m.get(group,[]):
            p=Path(item['path'])
            if not p.exists(): checks.append({'group':group,'path':str(p),'ok':False,'reason':'missing'}); ok=False; continue
            now=digest(p); same=(now['sha256']==item.get('sha256') and now['bytes']==item.get('bytes'))
            checks.append({'group':group,'path':str(p),'ok':same,'sha256':now['sha256']})
            ok &= same
    print(json.dumps({'ok':ok,'schema':schema,'run_id':m.get('run_id'),'runtime':m.get('runtime'),'checks':checks},ensure_ascii=False,indent=2)); return 0 if ok else 1

def main():
    ap=argparse.ArgumentParser(description='Create/verify reproducible run manifests and check feature-scoped dependencies.')
    sub=ap.add_subparsers(dest='cmd',required=True)
    p=sub.add_parser('doctor'); p.add_argument('--features',nargs='+',required=True); p.set_defaults(func=doctor)
    p=sub.add_parser('create'); p.add_argument('--output',required=True); p.add_argument('--run-id',required=True); p.add_argument('--command',required=True); p.add_argument('--seed'); p.add_argument('--cwd'); p.add_argument('--runtime',default='python'); p.add_argument('--runtime-version'); p.add_argument('--dependency',action='append',default=[]); p.add_argument('--input',action='append',default=[]); p.add_argument('--artifact',action='append',default=[]); p.add_argument('--package',action='append',default=[]); p.add_argument('--note',action='append',default=[]); p.set_defaults(func=create)
    p=sub.add_parser('verify'); p.add_argument('manifest'); p.set_defaults(func=verify)
    a=ap.parse_args(); raise SystemExit(a.func(a))
if __name__=='__main__': main()
