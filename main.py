#!/usr/bin/env python3
"""Write the out-of-office entry line to /output/entry.txt.

Deterministic, stdlib only, no network, no secrets, no files
outside this repository. The entry line is a single constant
assembled from its three parts so each clause is easy to read
and edit without touching the writer logic below.
"""

import os

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")

# The entry: a real auto-reply opening, then the twist — the cat
# minding the inbox has already approved a budget increase.
_PARTS = (
    "Out of office until Monday",
    "my cat is watching my inbox,",
    "and has already approved a budget increase.",
)
ENTRY = " \u2014 ".join((_PARTS[0], " ".join(_PARTS[1:])))


def write_entry(path=OUTPUT_PATH):
    """Write exactly one line (plus trailing newline) to path."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY + "\n")


def main():
    write_entry()


if __name__ == "__main__":
    main()
