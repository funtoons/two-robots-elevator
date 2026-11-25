#!/usr/bin/env python3
"""Two Robots in an Elevator -- make.fun entry.

Writes one line of awkward robot small talk to /output/entry.txt.
Deterministic and offline: the line is a fixed literal, no randomness,
no network, no clock, no environment input. Every run writes the
same bytes.
"""

import os
from pathlib import Path

ENTRY = "I calibrated my eye-contact sensor for 47 minutes, and I still don't know where to look in this elevator."

OUTPUT_PATH = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
