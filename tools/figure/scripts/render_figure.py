#!/usr/bin/env python3
"""Render common scientific charts from tabular data under an explicit Figure Contract.

This CLI is intentionally conservative: it does not invent statistical transformations,
annotations, labels, or claims. It renders only fields and aggregations requested by the caller.
For specialized scientific figures, create a dedicated project script and reuse export_figure.py.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Iterable

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from export_figure import export_figure


SUPPORTED = ("line", "scatter", "bar", "hist", "box", "heatmap", "errorbar")


def load_table(path: str, sep: str | None = None) -> pd.DataFrame:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(p)
    if sep is not None:
        return pd.read_csv(p, sep=sep)
    if p.suffix.lower() in {".tsv", ".tab"}:
        return pd.read_csv(p, sep="\t")
    return pd.read_csv(p)


def require_columns(df: pd.DataFrame, names: Iterable[str | None]) -> None:
    missing = [n for n in names if n and n not in df.columns]
    if missing:
        raise ValueError(f"missing columns: {missing}")


def _group_values(df: pd.DataFrame, group: str | None):
    if group is None:
        yield None, df
        return
    for key, part in df.groupby(group, sort=False, dropna=False):
        yield key, part


def render(args: argparse.Namespace):
    df = load_table(args.input, args.sep)
    require_columns(df, [args.x, args.y, args.group, args.yerr])

    if args.filter_query:
        df = df.query(args.filter_query)
    if df.empty:
        raise ValueError("no rows remain after filtering")

    fig, ax = plt.subplots(figsize=(args.width, args.height), constrained_layout=True)

    if args.chart == "line":
        require_columns(df, [args.x, args.y])
        for key, part in _group_values(df, args.group):
            part = part.sort_values(args.x)
            ax.plot(part[args.x], part[args.y], marker=args.marker, label=None if key is None else str(key))

    elif args.chart == "scatter":
        require_columns(df, [args.x, args.y])
        for key, part in _group_values(df, args.group):
            ax.scatter(part[args.x], part[args.y], alpha=args.alpha, label=None if key is None else str(key))

    elif args.chart == "bar":
        require_columns(df, [args.x, args.y])
        if args.group:
            pivot = df.pivot_table(index=args.x, columns=args.group, values=args.y, aggfunc=args.aggregate, sort=False)
            pivot.plot(kind="bar", ax=ax)
        else:
            series = df.groupby(args.x, sort=False, dropna=False)[args.y].agg(args.aggregate)
            ax.bar(series.index.astype(str), series.values)

    elif args.chart == "hist":
        target = args.y or args.x
        require_columns(df, [target])
        for key, part in _group_values(df, args.group):
            ax.hist(part[target].dropna(), bins=args.bins, alpha=args.alpha, label=None if key is None else str(key))

    elif args.chart == "box":
        require_columns(df, [args.x, args.y])
        groups = []
        labels = []
        for key, part in df.groupby(args.x, sort=False, dropna=False):
            values = pd.to_numeric(part[args.y], errors="coerce").dropna().to_numpy()
            if len(values):
                groups.append(values)
                labels.append(str(key))
        if not groups:
            raise ValueError("box plot has no numeric observations")
        ax.boxplot(groups, labels=labels, showfliers=args.show_fliers)

    elif args.chart == "heatmap":
        numeric = df.select_dtypes(include=[np.number])
        if args.heatmap_columns:
            cols = [x.strip() for x in args.heatmap_columns.split(",") if x.strip()]
            require_columns(df, cols)
            numeric = df[cols].apply(pd.to_numeric, errors="coerce")
        if numeric.shape[1] < 2:
            raise ValueError("heatmap requires at least two numeric columns")
        matrix = numeric.corr(method=args.corr_method)
        image = ax.imshow(matrix.to_numpy(), aspect="auto")
        ax.set_xticks(range(len(matrix.columns)), matrix.columns, rotation=45, ha="right")
        ax.set_yticks(range(len(matrix.index)), matrix.index)
        fig.colorbar(image, ax=ax, fraction=0.046, pad=0.04)
        if args.annotate:
            for i in range(matrix.shape[0]):
                for j in range(matrix.shape[1]):
                    value = matrix.iat[i, j]
                    if np.isfinite(value):
                        ax.text(j, i, f"{value:.2f}", ha="center", va="center", fontsize=max(7, args.font_size - 2))

    elif args.chart == "errorbar":
        require_columns(df, [args.x, args.y, args.yerr])
        for key, part in _group_values(df, args.group):
            part = part.sort_values(args.x)
            ax.errorbar(part[args.x], part[args.y], yerr=part[args.yerr], marker=args.marker, capsize=3, label=None if key is None else str(key))

    if args.log_x:
        ax.set_xscale("log")
    if args.log_y:
        ax.set_yscale("log")
    if args.zero_baseline and not args.log_y and args.chart in {"bar"}:
        _, hi = ax.get_ylim()
        ax.set_ylim(0, hi if hi > 0 else 1)

    if args.title:
        ax.set_title(args.title)
    if args.xlabel:
        ax.set_xlabel(args.xlabel)
    elif args.x and args.chart not in {"heatmap"}:
        ax.set_xlabel(args.x)
    if args.ylabel:
        ax.set_ylabel(args.ylabel)
    elif args.y and args.chart not in {"heatmap"}:
        ax.set_ylabel(args.y)

    if args.group and args.chart not in {"heatmap", "bar"}:
        ax.legend(frameon=False)

    written = export_figure(fig, args.output, formats=tuple(args.formats), dpi=args.dpi, grayscale_preview=args.grayscale_preview)
    plt.close(fig)
    return {
        "status": "ok",
        "chart": args.chart,
        "input": str(Path(args.input)),
        "rows": int(len(df)),
        "columns": list(df.columns),
        "outputs": written,
        "contract": {
            "x": args.x,
            "y": args.y,
            "group": args.group,
            "aggregate": args.aggregate if args.chart == "bar" else None,
            "yerr": args.yerr,
            "filter_query": args.filter_query,
        },
    }


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Render a common scientific chart from CSV/TSV.")
    p.add_argument("input")
    p.add_argument("--chart", required=True, choices=SUPPORTED)
    p.add_argument("--output", required=True, help="Output stem without extension.")
    p.add_argument("--x")
    p.add_argument("--y")
    p.add_argument("--group")
    p.add_argument("--yerr")
    p.add_argument("--sep")
    p.add_argument("--filter-query", help="Optional pandas query; must be an explicit Figure Contract transformation.")
    p.add_argument("--aggregate", choices=("mean", "median", "sum", "min", "max"), default="mean")
    p.add_argument("--bins", type=int, default=20)
    p.add_argument("--corr-method", choices=("pearson", "spearman", "kendall"), default="pearson")
    p.add_argument("--heatmap-columns")
    p.add_argument("--annotate", action="store_true")
    p.add_argument("--show-fliers", action="store_true")
    p.add_argument("--marker", default="o")
    p.add_argument("--alpha", type=float, default=0.75)
    p.add_argument("--width", type=float, default=6.4)
    p.add_argument("--height", type=float, default=4.2)
    p.add_argument("--font-size", type=float, default=10.0)
    p.add_argument("--dpi", type=int, default=300)
    p.add_argument("--formats", nargs="+", default=["svg", "png"], choices=("svg", "png", "pdf"))
    p.add_argument("--grayscale-preview", action="store_true")
    p.add_argument("--log-x", action="store_true")
    p.add_argument("--log-y", action="store_true")
    p.add_argument("--zero-baseline", action="store_true")
    p.add_argument("--title")
    p.add_argument("--xlabel")
    p.add_argument("--ylabel")
    p.add_argument("--json", action="store_true")
    return p


def main() -> int:
    args = build_parser().parse_args()
    plt.rcParams.update({"font.size": args.font_size})
    try:
        report = render(args)
    except Exception as exc:
        report = {"status": "error", "error": f"{type(exc).__name__}: {exc}"}
        if args.json:
            print(json.dumps(report, ensure_ascii=False, indent=2))
        else:
            print(f"FIGURE_RENDER_FAIL: {report['error']}")
        return 1
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print("FIGURE_RENDER_PASS")
        for item in report["outputs"]:
            print("-", item)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
