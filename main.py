#!/usr/bin/env python3
"""Entry for make.fun bounty 'Have You Tried Turning It Off?'.

Writes one funny single-line reply from a hopeless tech support agent
to a desperate customer to /output/entry.txt (and, best effort, to the
repo root as entry.txt). Deterministic: same bytes every run.
"""

import os

ENTRY = (
    "I can hear how frustrated you are, so have you tried turning "
    "yourself off and on again \u2014 just power down for ten seconds "
    "and come back fresh?"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    try:
        with open("entry.txt", "w", encoding="utf-8") as f:
            f.write(ENTRY)
    except OSError:
        pass


if __name__ == "__main__":
    main()
