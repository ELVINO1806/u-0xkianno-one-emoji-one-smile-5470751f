#!/usr/bin/env python3
"""One Emoji, One Smile — entry program.

Writes exactly one emoji to /output/entry.txt: the heart-hands emoji,
a small wordless gesture meant to make a stranger smile.
Python 3 standard library only, deterministic, no network, no input.
"""

import os

EMOJI = "\U0001FAF6"  # 🫶 heart hands

OUTPUT_DIR = "/output"
OUTPUT_NAME = "entry.txt"


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, OUTPUT_NAME), "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
