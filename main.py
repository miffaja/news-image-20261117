import os
import shutil

# A working news-image-20261117 entry (Python 3.13, standard library only):
# its image is the entry.png beside this file, and the program copies it to
# /output/entry.png. The image is a newspaper front page summing up the
# world's news of Tuesday 17 November 2026: the Kerch Bridge destroyed,
# Gulf strikes, the Quad in Manila, markets tumbling with Nvidia's comeback
# bid, the NSA's classified network down, and flights grounded.
# The gate takes a whole PNG or JPEG of at most 1 MiB and 1024 by 1024
# pixels, and the judge sees exactly the bytes copied.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
out = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.png")
os.makedirs(os.path.dirname(out), exist_ok=True)
shutil.copyfile(src, out)
