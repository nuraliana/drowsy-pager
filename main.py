#!/usr/bin/env python3
"""Break Production, Own It — one brutally honest line.

Writes the entry to entry.txt in the output directory
(MAKEFUN_OUTPUT_DIR, default /output) and prints it.
Standard library only.
"""

import os

ENTRY = (
    "I rotated the production secrets at 3 a.m. to be safe. "
    "Nothing can log in now, including me. "
    "The outage is secure."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
