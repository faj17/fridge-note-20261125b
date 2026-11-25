#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge entry.

Writes one short passive-aggressive note (130 characters) from a
smart fridge to its owner to /output/entry.txt (1-200 characters,
UTF-8, a single line). Standard library only, no network, no input.

The note is built from two fragments: a setup (the door sensor
caught the owner — 47 seconds open, and the yogurt witnessed it
all: the fridge's smug inventory of the crime) and a punch (the
fridge claims it is not angry, then admits it is keeping the
light on for the owner's 2 a.m. bad decisions — the grudge stays
small and domestic, and the sting lands in the last words).
``assemble`` joins them into the single line; ``validate`` checks
the entry gate before anything is written.
"""

from pathlib import Path

SETUP = "Door left open 47 seconds. The yogurt saw everything. I'm not angry \u2014"
PUNCH = "I'm just keeping the light on for your 2 a.m. bad decisions."

OUTPUT_PATH = Path("/output/entry.txt")


def assemble(setup: str, punch: str) -> str:
    """Join the setup and punch fragments into one note line."""
    return f"{setup} {punch}"


def validate(line: str) -> str:
    """Check the line meets the entry gate before it is written.

    Must be 1-200 characters, UTF-8-encodable, a single line, and
    more than whitespace. Raises ValueError otherwise.
    """
    if not 1 <= len(line) <= 200:
        raise ValueError(f"line must be 1-200 characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line (no newline characters)")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    line.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return line


def main() -> None:
    line = validate(assemble(SETUP, PUNCH))
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
