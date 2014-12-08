#!/usr/bin/env python
from __future__ import print_function

from PIL import Image, ImageDraw
import sys

USAGE = """
Usage: version.py file.txt file.png [version]

If no version is given it will be read from file.txt.
If a version is given it will be written to file.txt.
In either case version will be drawn to file.png.
"""

def run(text_path, image_path, version=None):
    if version is None:
        version = open(text_path).read().strip()
    else:
        open(text_path, 'w').write(version)
    width = len(version) * 6 + 4 + 4
    img = Image.new("RGB", (width, 16), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.text((4, 2), version, (0, 0, 0))
    img.save(image_path)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(USAGE.strip())
        exit()
    run(*sys.argv[1:])
