#!/usr/bin/env python3
import argparse, ast, json
from pathlib import Path

PLOT_CALLS={'plot','scatter','bar','barh','hist','imshow','contour','contourf','boxplot','violinplot','errorbar','fill_between','pcolormesh'}
LABEL_CALLS={'set_xlabel','set_ylabel','xlabel','ylabel'}
SAVE_CALLS={'savefig'}

def call_name(node):
    f=node.func
    if isinstance(f,ast.Attribute): return f.attr
    if isinstance(f,ast.Name): return f.id
    return ''

def inspect(path):
    text=Path(path).read_text(encoding='utf-8',errors='replace')
    try: tree=ast.parse(text)
    except SyntaxError as e: return {'path':str(path),'ok':False,'errors':[f'syntax_error:{e.lineno}:{e.msg}'],'warnings':[]}
    calls=[]; jpeg=False; tight=False
    for n in ast.walk(tree):
        if isinstance(n,ast.Call):
            name=call_name(n); calls.append(name)
            if name=='savefig':
                for arg in n.args:
                    if isinstance(arg,ast.Constant) and isinstance(arg.value,str) and arg.value.lower().endswith(('.jpg','.jpeg')): jpeg=True
                for kw in n.keywords:
                    if kw.arg=='bbox_inches' and isinstance(kw.value,ast.Constant) and kw.value.value=='tight': tight=True
    has_plot=any(c in PLOT_CALLS for c in calls); has_label=any(c in LABEL_CALLS for c in calls); has_save=any(c in SAVE_CALLS for c in calls)
    warnings=[]
    if has_plot and not has_label: warnings.append('plot_detected_but_no_axis_label_call_found')
    if has_plot and not has_save: warnings.append('plot_detected_but_no_savefig_call_found')
    if jpeg: warnings.append('jpeg_export_is_lossy_for_line_art')
    if tight: warnings.append('bbox_inches_tight_can_change_physical_figure_dimensions')
    return {'path':str(path),'ok':True,'plot_calls':sum(c in PLOT_CALLS for c in calls),'has_axis_label_call':has_label,'has_savefig':has_save,'warnings':warnings}

def main():
    ap=argparse.ArgumentParser(description='Static QA for Python plotting source. Warnings require visual review; they are not scientific errors.')
    ap.add_argument('path'); ap.add_argument('--json',action='store_true'); a=ap.parse_args(); p=Path(a.path)
    files=[p] if p.is_file() else sorted(p.rglob('*.py')); out=[inspect(x) for x in files]
    print(json.dumps(out,ensure_ascii=False,indent=2) if a.json else '\n'.join(f"{x['path']}: warnings={','.join(x.get('warnings',[])) or 'none'}" for x in out))
    raise SystemExit(1 if any(not x.get('ok') for x in out) else 0)
if __name__=='__main__': main()
