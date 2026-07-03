#!/usr/bin/env python3
"""
Trim transparent / near-transparent margins from all sprite PNGs so each
character fills its frame and sits correctly on the ground in-game.

Usage:  python trim_sprites.py
Originals are backed up to sprites/_raw/ (only once). Re-running is safe:
it always re-trims from the pristine _raw/ copy.
"""
import os
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
RAW  = os.path.join(HERE, "_raw")
ALPHA_THRESHOLD = 30   # ignore fainter-than-this pixels (kills AI artifacts)

os.makedirs(RAW, exist_ok=True)

for fn in sorted(os.listdir(HERE)):
    if not fn.lower().endswith(".png"):
        continue
    src_path = os.path.join(HERE, fn)
    raw_path = os.path.join(RAW, fn)

    # Back up pristine original once, then always work from it.
    if not os.path.exists(raw_path):
        Image.open(src_path).save(raw_path)
    im = Image.open(raw_path).convert("RGBA")

    # Build a clean alpha mask that ignores faint artifacts, find its bbox.
    alpha = im.getchannel("A").point(lambda a: 255 if a > ALPHA_THRESHOLD else 0)
    bbox = alpha.getbbox()
    if not bbox:
        print(f"{fn}: empty / fully transparent, skipped")
        continue

    cropped = im.crop(bbox)
    cropped.save(src_path)
    ow, oh = im.size
    cw, ch = cropped.size
    print(f"{fn}: {ow}x{oh} -> {cw}x{ch}  (trimmed {ow-cw}px W, {oh-ch}px H)")

print("Done. Hard-reload the game (Ctrl+F5).")
