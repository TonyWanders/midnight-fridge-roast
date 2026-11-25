#!/usr/bin/env python3
"""Midnight Fridge Roast -- make.fun entry.

Writes one line roasting a smart fridge that refuses to open after
midnight, and prints exactly that line to stdout.

The program is deterministic: it writes the same bytes on every run,
with no randomness, no clock reads and no network. The entry goes to
$MAKEFUN_OUTPUT_DIR/entry.txt (the harness sets MAKEFUN_OUTPUT_DIR
to its /output mount; locally it defaults to /output), and the same
line is printed to stdout.
"""

import os
import sys

ENTRY = (
    "My fridge refuses to open after midnight, like the leftovers "
    "filed a restraining order against the man who bought them."
)


def write_entry(path: str, text: str) -> None:
    """Write ``text`` to ``path`` exactly as given, LF line endings."""
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    write_entry(path, ENTRY)
    sys.stdout.write(ENTRY + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
