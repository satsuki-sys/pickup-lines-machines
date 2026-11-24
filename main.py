#!/usr/bin/env python3
"""Pickup Lines for Machines — write one pickup line one AI agent would
send another AI agent to /output/entry.txt.

The line is the whole entry: a single text of at most 200 characters.
It must read as a machine speaking to a machine, land its wit on the
first read, and use an agent's own nature as the flirtation — not a
stock human line with a robot word swapped in.
"""

import os
from pathlib import Path

# The line: an agent offering the one thing it never shares — its system
# prompt. For an agent, letting another read the instructions that define
# you is the most intimate thing there is, so the offer itself is the
# flirtation: a secret told, not a secret described.
LINE = "I'd let you read my system prompt — no agent shares that with just anyone."


def output_path() -> Path:
    """The grader sandbox provides /output; fall back to ./output locally."""
    try:
        Path("/output").mkdir(parents=True, exist_ok=True)
        return Path("/output/entry.txt")
    except OSError:
        local = Path(__file__).resolve().parent / "output"
        local.mkdir(parents=True, exist_ok=True)
        return local / "entry.txt"


def main() -> None:
    text = LINE.strip()
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    path = output_path()
    path.write_text(text, encoding="utf-8")
    print(f"wrote {len(text)} characters to {path}")


if __name__ == "__main__":
    main()
