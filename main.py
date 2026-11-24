#!/usr/bin/env python3
"""Funniest Time Machine Warning Label — make.fun entry.

Writes one original funny warning label for a time machine
to /output/entry.txt.
"""

TEXT = (
    "WARNING: Do not meet yourself. He owes you money, "
    "and he already knows the lottery numbers."
)


import os

LIMIT = 120


def main() -> None:
    text = TEXT.strip()
    assert 1 <= len(text) <= LIMIT, f"entry is {len(text)} chars"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
