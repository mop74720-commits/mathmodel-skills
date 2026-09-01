#!/usr/bin/env python3
import argparse, csv, hashlib, importlib.metadata, json, math, platform, shutil, subprocess, sys
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

def sha256_file(p):
    h=hashlib.sha256()
    with Path(p).open('rb') as f:
        for chunk in iter(lambda:f.read(1024*1024), b''): h.update(chunk)
    return h.hexdigest()

def resolve_user_path(raw, cwd):
    p=Path(raw)
    return p.resolve() if p.is_absolute() else (cwd/p).resolve()

def stored_path(p, cwd):
    p=Path(p).resolve()
    try: return str(p.relative_to(cwd))
    except ValueError: return str(p)

def normalize_number(v, decimals):
    if isinstance(v, bool) or v is None: return v
    if isinstance(v, int): return v
    if isinstance(v, float):
        if not math.isfinite(v): return str(v)
        return round(v, decimals)
    return v

def semantic_fingerprint(path, decimals):
    p=Path(path)
    ext=p.suffix.lower()
    if decimals is None or ext not in {'.csv','.json'}: return None
    h=hashlib.sha256()
    if ext=='.json':
        obj=json.loads(p.read_text(encoding='utf-8-sig'))
        def walk(x):
            if isinstance(x, dict): return {k:walk(x[k]) for k in sorted(x)}
            if isinstance(x, list): return [walk(v) for v in x]
            if isinstance(x, (int,float)) and not isinstance(x,bool): return normalize_number(x,decimals)
            return x
        data=json.dumps(walk(obj),ensure_ascii=False,sort_keys=True,separators=(',',':')).encode('utf-8')
        h.update(data)
    else:
        with p.open(encoding='utf-8-sig',newline='') as f:
            for row in csv.reader(f):
                out=[]
                for cell in row:
                    s=cell.strip()
                    try:
                        v=float(s)
                        if math.isfinite(v): s=format(round(v,decimals),f'.{decimals}f')
                    except Exception:
                        pass
                    out.append(s)
                h.update(('\x1f'.join(out)+'\n').encode('utf-8'))
    return {'method':f'rounded_numeric_content/v1','decimals':decimals,'sha256':h.hexdigest()}

def digest(p, cwd, semantic_decimals=None):
    p=Path(p).resolve()
    item={'path':stored_path(p,cwd),'bytes':p.stat().st_size,'sha256':sha256_file(p)}
    sem=semantic_fingerprint(p,semantic_decimals)
    if sem: item['semantic_fingerprint']=sem
    return item

def item_path(item, base):
    p=Path(item['path'])
    return p if p.is_absolute() else (base/p)

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
        if '=' not in raw: raise ValueError(f'dependency must be name=version, got: {raw}')
        name,version=raw.split('=',1); name=name.strip(); version=version.strip()
        if not name: raise ValueError(f'empty dependency name: {raw}')
        out[name]=version
    return out

def create(a):
    cwd=Path(a.cwd or '.').resolve(); inputs=[]; artifacts=[]; missing=[]
    for x in a.input:
        p=resolve_user_path(x,cwd)
        if not p.exists(): missing.append(str(p))
        else: inputs.append(digest(p,cwd,a.semantic_decimals))
    for x in a.artifact:
        p=resolve_user_path(x,cwd)
        if not p.exists(): missing.append(str(p))
        else: artifacts.append(digest(p,cwd,a.semantic_decimals))
    if missing:
        print(json.dumps({'ok':False,'missing_files':missing,'note':'relative paths are resolved against --cwd'},ensure_ascii=False,indent=2),file=sys.stderr); return 2
    packages={name:package_version(name) for name in sorted(set(a.package))}
    try: dependencies=parse_dependency(a.dependency)
    except ValueError as e:
        print(json.dumps({'ok':False,'error':str(e)},ensure_ascii=False,indent=2),file=sys.stderr); return 2
    runtime_name=a.runtime or 'python'
    runtime_version=a.runtime_version or (sys.version.split()[0] if runtime_name=='python' else None)
    manifest={
        'schema':'mathmodel-run-manifest/v3',
        'created_at_utc':datetime.now(timezone.utc).isoformat(),
        'run_id':a.run_id,'command':a.command,'cwd':str(cwd),'seed':a.seed,
        'runtime':{'name':runtime_name,'version':runtime_version},
        'host':{'python':sys.version.split()[0],'implementation':platform.python_implementation(),'platform':platform.platform()},
        'git':git_state(cwd),'python_packages':packages,'dependencies':dependencies,
        'inputs':inputs,'artifacts':artifacts,'notes':a.note,
        'reproducibility_contract':{
            'artifact_integrity':'exact bytes + SHA-256 of recorded files',
            'replay_reproducibility':'rerun command, then compare artifacts exactly and optionally by semantic fingerprint',
            'semantic_decimals':a.semantic_decimals,
        }
    }
    out=Path(a.output); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
    print(out); return 0

def load_manifest(path):
    m=json.loads(Path(path).read_text(encoding='utf-8'))
    if m.get('schema') not in ('mathmodel-run-manifest/v1','mathmodel-run-manifest/v2','mathmodel-run-manifest/v3'):
        raise ValueError(f"unsupported_schema: {m.get('schema')}")
    return m

def base_cwd(m, override=None):
    return Path(override or m.get('cwd') or '.').resolve()

def integrity_checks(m, base, groups=('inputs','artifacts')):
    checks=[]; ok=True
    for group in groups:
        for item in m.get(group,[]):
            p=item_path(item,base)
            if not p.exists(): checks.append({'group':group,'path':str(p),'ok':False,'reason':'missing'}); ok=False; continue
            same=(sha256_file(p)==item.get('sha256') and p.stat().st_size==item.get('bytes'))
            checks.append({'group':group,'path':str(p),'ok':same,'sha256':sha256_file(p)})
            ok &= same
    return ok,checks

def verify(a):
    try: m=load_manifest(a.manifest)
    except Exception as e:
        print(json.dumps({'ok':False,'check_type':'artifact_integrity','error':str(e)},ensure_ascii=False,indent=2)); return 2
    base=base_cwd(m,a.cwd); ok,checks=integrity_checks(m,base)
    print(json.dumps({'ok':ok,'check_type':'artifact_integrity','schema':m.get('schema'),'run_id':m.get('run_id'),'cwd':str(base),'checks':checks,
                      'note':'PASS means recorded files are unchanged; it does NOT prove the command can reproduce them.'},ensure_ascii=False,indent=2))
    return 0 if ok else 1

def replay(a):
    try: m=load_manifest(a.manifest)
    except Exception as e:
        print(json.dumps({'ok':False,'check_type':'replay_reproducibility','error':str(e)},ensure_ascii=False,indent=2)); return 2
    base=base_cwd(m,a.cwd)
    input_ok,input_checks=integrity_checks(m,base,groups=('inputs',))
    if not input_ok and not a.allow_input_drift:
        print(json.dumps({'ok':False,'check_type':'replay_reproducibility','status':'INPUT_DRIFT','input_checks':input_checks,
                          'note':'Use --allow-input-drift only when the changed input is intentional.'},ensure_ascii=False,indent=2)); return 2
    try:
        r=subprocess.run(m.get('command',''),cwd=base,shell=True,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=a.timeout)
    except subprocess.TimeoutExpired as e:
        print(json.dumps({'ok':False,'check_type':'replay_reproducibility','status':'TIMEOUT','timeout':a.timeout,'log_tail':(e.stdout or '')[-4000:] if isinstance(e.stdout,str) else None},ensure_ascii=False,indent=2)); return 2
    rows=[]; all_exact=True; all_semantic=True; semantic_available=False
    for item in m.get('artifacts',[]):
        p=item_path(item,base)
        if not p.exists():
            rows.append({'path':str(p),'exact_match':False,'semantic_match':False,'reason':'missing'}); all_exact=False; all_semantic=False; continue
        exact=(sha256_file(p)==item.get('sha256') and p.stat().st_size==item.get('bytes'))
        sem_old=item.get('semantic_fingerprint'); sem_match=None
        if sem_old:
            semantic_available=True
            sem_now=semantic_fingerprint(p,sem_old.get('decimals'))
            sem_match=bool(sem_now and sem_now.get('sha256')==sem_old.get('sha256'))
        all_exact &= exact
        if sem_old: all_semantic &= bool(sem_match)
        else: all_semantic &= exact
        rows.append({'path':str(p),'exact_match':exact,'semantic_match':sem_match,'sha256':sha256_file(p)})
    status='EXACT_MATCH' if r.returncode==0 and all_exact else ('SEMANTIC_MATCH' if r.returncode==0 and all_semantic and semantic_available else 'MISMATCH')
    ok=status in ('EXACT_MATCH','SEMANTIC_MATCH')
    print(json.dumps({'ok':ok,'check_type':'replay_reproducibility','status':status,'command_exit':r.returncode,'cwd':str(base),
                      'input_integrity':input_ok,'artifacts':rows,'log_tail':r.stdout[-4000:],
                      'note':'EXACT_MATCH is byte reproducibility; SEMANTIC_MATCH means configured numeric canonicalization matched despite byte drift.'},ensure_ascii=False,indent=2))
    return 0 if ok else 1


def bundle(a):
    cwd=Path(a.cwd or '.').resolve()
    fields={
        'run_manifest': a.manifest,
        'run_ledger': a.ledger,
        'rule_profile': a.rule_profile,
        'claim_evidence_map': a.claim_evidence,
    }
    refs={}; missing=[]
    for key,raw in fields.items():
        if not raw: continue
        path=resolve_user_path(raw,cwd)
        if not path.exists():
            missing.append(str(path)); continue
        refs[key]=digest(path,cwd,None)
    if missing:
        print(json.dumps({'ok':False,'missing_files':missing,'note':'relative paths are resolved against --cwd'},ensure_ascii=False,indent=2),file=sys.stderr); return 2
    try:
        manifest_obj=load_manifest(resolve_user_path(a.manifest,cwd))
    except Exception as e:
        print(json.dumps({'ok':False,'error':f'invalid manifest: {e}'},ensure_ascii=False,indent=2),file=sys.stderr); return 2
    obj={
        'schema':'mathmodel-provenance-bundle/v1',
        'created_at_utc':datetime.now(timezone.utc).isoformat(),
        'status':a.status,
        'run_id':manifest_obj.get('run_id'),
        'run_manifest_schema':manifest_obj.get('schema'),
        'cwd':str(cwd),
        'refs':refs,
        'notes':a.note,
        'claim_boundary':{
            'hashes_establish':'recorded artifact identity/integrity',
            'hashes_do_not_establish':'scientific correctness or replay reproducibility',
        },
    }
    out=Path(a.output); out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(obj,ensure_ascii=False,indent=2),encoding='utf-8')
    print(out); return 0

def verify_bundle(a):
    try:
        b=json.loads(Path(a.bundle).read_text(encoding='utf-8'))
    except Exception as e:
        print(json.dumps({'ok':False,'check_type':'provenance_bundle_integrity','reason':'invalid_json','error':str(e)},ensure_ascii=False,indent=2)); return 2
    if b.get('schema')!='mathmodel-provenance-bundle/v1':
        print(json.dumps({'ok':False,'check_type':'provenance_bundle_integrity','reason':'unsupported_schema','schema':b.get('schema')},ensure_ascii=False,indent=2)); return 2
    base=Path(a.cwd or b.get('cwd') or '.').resolve(); checks=[]; ok=True
    for key,item in b.get('refs',{}).items():
        path=item_path(item,base)
        if not path.exists():
            checks.append({'ref':key,'path':str(path),'ok':False,'reason':'missing'}); ok=False; continue
        now_sha=sha256_file(path); same=(now_sha==item.get('sha256') and path.stat().st_size==item.get('bytes'))
        checks.append({'ref':key,'path':str(path),'ok':same,'sha256':now_sha}); ok &= same
    print(json.dumps({'ok':ok,'check_type':'provenance_bundle_integrity','schema':b.get('schema'),'run_id':b.get('run_id'),'status':b.get('status'),'cwd':str(base),'checks':checks,
                      'note':'PASS verifies referenced bundle artifacts are unchanged; it does not prove scientific correctness or command replay.'},ensure_ascii=False,indent=2))
    return 0 if ok else 1

def main():
    ap=argparse.ArgumentParser(description='Run manifest + provenance bundle tool with separate artifact-integrity and replay-reproducibility semantics.')
    sub=ap.add_subparsers(dest='cmd',required=True)
    p=sub.add_parser('doctor'); p.add_argument('--features',nargs='+',required=True); p.set_defaults(func=doctor)
    p=sub.add_parser('create'); p.add_argument('--output',required=True); p.add_argument('--run-id',required=True); p.add_argument('--command',required=True); p.add_argument('--seed'); p.add_argument('--cwd'); p.add_argument('--runtime',default='python'); p.add_argument('--runtime-version'); p.add_argument('--dependency',action='append',default=[]); p.add_argument('--input',action='append',default=[]); p.add_argument('--artifact',action='append',default=[]); p.add_argument('--package',action='append',default=[]); p.add_argument('--note',action='append',default=[]); p.add_argument('--semantic-decimals',type=int); p.set_defaults(func=create)
    p=sub.add_parser('verify',help='artifact integrity only; does not execute the run'); p.add_argument('manifest'); p.add_argument('--cwd'); p.set_defaults(func=verify)
    p=sub.add_parser('replay',help='execute recorded command and compare regenerated artifacts'); p.add_argument('manifest'); p.add_argument('--cwd'); p.add_argument('--timeout',type=int,default=600); p.add_argument('--allow-input-drift',action='store_true'); p.set_defaults(func=replay)
    p=sub.add_parser('bundle',help='bind a run manifest and selected evidence indexes by SHA-256 without claiming replay reproducibility'); p.add_argument('--manifest',required=True); p.add_argument('--output',required=True); p.add_argument('--cwd'); p.add_argument('--ledger'); p.add_argument('--rule-profile'); p.add_argument('--claim-evidence'); p.add_argument('--status',choices=['exploratory','confirmatory','final'],default='final'); p.add_argument('--note',action='append',default=[]); p.set_defaults(func=bundle)
    p=sub.add_parser('verify-bundle',help='verify provenance bundle artifact identity only'); p.add_argument('bundle'); p.add_argument('--cwd'); p.set_defaults(func=verify_bundle)
    a=ap.parse_args(); raise SystemExit(a.func(a))
if __name__=='__main__': main()
