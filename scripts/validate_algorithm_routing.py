from pathlib import Path
import re, sys
ROOT=Path(__file__).resolve().parents[1]
expected={
"ALGO_GREY_FORECAST":"grey-forecasting",
"ALGO_EFFICIENCY_ANALYSIS":"efficiency-analysis",
"ALGO_QUEUEING":"queueing",
"ALGO_SYSTEM_DYNAMICS":"system-dynamics",
"ALGO_CELLULAR_AUTOMATA":"cellular-automata",
"ALGO_GAME_THEORY":"game-theory",
"ALGO_LINEAR_INTEGER":"linear-integer-optimization",
"ALGO_NONLINEAR_OPT":"nonlinear-optimization",
"ALGO_NETWORK_ROUTING":"network-routing",
"ALGO_TIME_SERIES":"time-series",
"ALGO_SUPERVISED_LEARNING":"supervised-learning",
"ALGO_UNSUPERVISED_LEARNING":"unsupervised-learning",
"ALGO_MULTI_CRITERIA":"multi-criteria-evaluation",
"ALGO_ODE_DYNAMICS":"ode-dynamics",
"ALGO_PDE_DYNAMICS":"pde-dynamics",
"ALGO_STOCHASTIC_SIM":"stochastic-simulation",
"ALGO_STATISTICAL_INFERENCE":"statistical-inference",
"ALGO_CAUSAL_INFERENCE":"causal-inference",
"ALGO_GEOMETRY":"geometry-reconstruction",
"ALGO_BAYESIAN_MODELING":"bayesian-modeling",
"ALGO_SIGNAL_PROCESSING":"signal-processing",
"ALGO_AGENT_BASED_MODELING":"agent-based-modeling",
}
errors=[]
for event,name in expected.items():
    p=ROOT/'skills'/'algorithm'/name/'SKILL.md'
    if not p.exists(): errors.append(f'missing {p.relative_to(ROOT)}'); continue
    text=p.read_text(encoding='utf-8')
    if f'trigger: {event}' not in text: errors.append(f'{name}: wrong trigger')
    for section in ['## Decision Rules','## Validation Design']:
        if section not in text: errors.append(f'{name}: missing {section}')
    if len(text)<1500: errors.append(f'{name}: content too shallow ({len(text)} chars)')
ms=(ROOT/'skills/modeling/model-selection/SKILL.md').read_text(encoding='utf-8')
for event in expected:
    if event not in ms: errors.append(f'model-selection does not dispatch {event}')
reg=(ROOT/'registry.yaml').read_text(encoding='utf-8')
for event,name in expected.items():
    if event not in reg or name not in reg: errors.append(f'registry missing {event}/{name}')
for banned in ['每类至少 3 张','至少 8 幅正式图','固定 ±10%','必须用户确认后','无 Subagent 就 BLOCKED']:
    for p in (ROOT/'skills'/'algorithm').glob('*/SKILL.md'):
        if banned in p.read_text(encoding='utf-8'): errors.append(f'{p.name}: banned rigid rule {banned}')
if errors:
    print('FAIL')
    for e in errors: print('-',e)
    sys.exit(1)
print('ALGORITHM_ROUTING_PASS: 22 algorithm skills')
