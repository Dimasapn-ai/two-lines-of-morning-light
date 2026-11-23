#!/usr/bin/env python3
"""Two Lines of Morning Light — make.fun entry.

Writes a two-line poem about morning light to entry.txt in the output
directory (MAKEFUN_OUTPUT_DIR if set, else /output). The poem is a fixed
constant: no clock, no randomness, byte-identical on every run.
"""

import os
import sys

# The couplet: one image of light arriving (striped through the blinds),
# opened by the second line — the stripes become a tiger's, worn by the cat.
# 94 characters including the line break, no trailing newline.
POEM = (
    "Light arrives through the blinds in stripes \u2014\n"
    "the cat wears them, and for a moment is a tiger."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Write as UTF-8 bytes so the file is byte-exact on any platform:
    # no newline translation, no locale-dependent encoding.
    data = POEM.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)
    return 0


if __name__ == "__main__":
    sys.exit(main())
