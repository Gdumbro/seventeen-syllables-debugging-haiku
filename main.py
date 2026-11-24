#!/usr/bin/env python3
"""Entry for make.fun bounty: Seventeen Syllables of Debugging.

Writes one haiku about debugging (5-7-5 syllables) to /output/entry.txt.
Anchor line: breakpoint holds its breath.
"""

import os

HAIKU = (
    "breakpoint holds its breath\n"
    "one wrong line, the whole night bends\n"
    "semicolon, gone"
)


def main() -> None:
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(HAIKU)


if __name__ == "__main__":
    main()
