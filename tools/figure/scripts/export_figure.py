#!/usr/bin/env python3
"""Small importable export helper. It never chooses colors or scientific content."""
from pathlib import Path

def export_figure(fig, basename, formats=('svg','png'), dpi=300, grayscale_preview=False):
    base=Path(basename); base.parent.mkdir(parents=True,exist_ok=True); written=[]
    for fmt in formats:
        out=base.with_suffix('.'+fmt); fig.savefig(out,dpi=dpi if fmt.lower() in {'png','jpg','jpeg','tif','tiff'} else None,bbox_inches='tight'); written.append(str(out))
    if grayscale_preview:
        from PIL import Image
        png=base.with_suffix('.png')
        if png.exists():
            prev=base.with_name(base.name+'_gray').with_suffix('.png'); Image.open(png).convert('L').save(prev); written.append(str(prev))
    return written
