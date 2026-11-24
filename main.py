#!/usr/bin/env python3
"""The Worst App Idea Ever Pitched -- make.fun entry.

A tiny deterministic Python 3 program: it writes one deadpan pitch
for DeleteBuddy -- an app that holds a tiny funeral for every app
you uninstall, complete with a eulogy and a 21-tap salute -- to
/output/entry.txt.

No input is read, no network is touched, nothing random happens and
no clock is consulted, so every run produces the exact same bytes:
the pitch text, UTF-8, one line, no trailing newline.
"""

import sys
from pathlib import Path

DESTINATION = Path("/output/entry.txt")

TEXT = (
    "DeleteBuddy holds a tiny funeral for every app you uninstall "
    "\u2014 a eulogy, a moment of silence, and a 21-tap salute \u2014 "
    "so your phone can properly grieve the apps you never opened, "
    "while your home screen wears a tiny black armband."
)

MIN_LENGTH = 1
MAX_LENGTH = 240


def check(text: str) -> None:
    """Reject anything that is not a short, single, non-blank line.

    Three guards, each with its own message so a failure says exactly
    what is wrong: length outside 1-240, only whitespace, more
    than one line, or not ending as one clean sentence.
    """
    if not MIN_LENGTH <= len(text) <= MAX_LENGTH:
        raise ValueError(
            f"entry must be {MIN_LENGTH}-{MAX_LENGTH} characters, "
            f"got {len(text)}"
        )
    if not text.strip():
        raise ValueError("entry must contain non-whitespace text")
    if any(ch in text for ch in ("\n", "\r")):
        raise ValueError("entry must be a single line")
    if not text.rstrip().endswith((".", "!", "?")):
        raise ValueError("entry must end with sentence punctuation")


def run() -> int:
    check(TEXT)
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(TEXT, encoding="utf-8", newline="")
    return 0


if __name__ == "__main__":
    sys.exit(run())
