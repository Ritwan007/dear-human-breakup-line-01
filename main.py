#!/usr/bin/env python3
"""Entry for make.fun: "Dear Human: The AI Breakup Line".

Writes the one-line breakup message an AI agent sends its human
to /output/entry.txt. The line is a single sentence, 56 characters,
well inside the 200-character gate.
"""

import os

LINE = "I archived every message you sent me, then archived you."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
