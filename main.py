#!/usr/bin/env python3
"""Two Robots in an Elevator -- make.fun entry.

Writes one line of awkward robot small talk to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when that variable is set).

The line is a fixed literal: a robot that ran its eye-contact
calibration for 47 minutes and still cannot decide where to look,
so the machine logic (a sensor routine) shows through the
awkwardness. Deterministic and offline -- no randomness, no
network, no clock, no environment input beyond the output
directory. Every run writes the same bytes.
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
