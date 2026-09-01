#!/usr/bin/env python3
import argparse, json
from pathlib import Path
from PIL import Image, ImageStat

def inspect(path, preview=None):
    im=Image.open(path).convert('RGB'); gray=im.convert('L'); stat=ImageStat.Stat(gray)
    extrema=gray.getextrema(); contrast=(extrema[1]-extrema[0])/255.0
    # Fraction of pixels that are almost white, useful as a mechanical blank/margin signal only.
    hist=gray.histogram(); near_white=sum(hist[245:])/max(1,im.width*im.height)
    if preview: gray.save(preview)
    warnings=[]
    if contrast < 0.20: warnings.append('low_global_grayscale_contrast')
    if near_white > 0.995: warnings.append('image_is_almost_blank')
    return {'path':str(path),'pixels':[im.width,im.height],'grayscale_extrema':list(extrema),'grayscale_mean':round(stat.mean[0],2),'global_contrast':round(contrast,4),'near_white_fraction':round(near_white,4),'preview':str(preview) if preview else None,'warnings':warnings}

def main():
    ap=argparse.ArgumentParser(description='Mechanical raster QA and grayscale preview; semantic readability still requires visual inspection.')
    ap.add_argument('image'); ap.add_argument('--preview'); ap.add_argument('--json',action='store_true'); a=ap.parse_args()
    out=inspect(Path(a.image),Path(a.preview) if a.preview else None)
    print(json.dumps(out,ensure_ascii=False,indent=2) if a.json else f"contrast={out['global_contrast']} near_white={out['near_white_fraction']} warnings={','.join(out['warnings']) or 'none'}")
    return 0
if __name__=='__main__': raise SystemExit(main())
