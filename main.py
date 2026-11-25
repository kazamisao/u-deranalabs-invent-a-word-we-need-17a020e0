"""Invent a Word We Need — entry program.

Writes the coined word and its one-line definition to entry.txt.

The entry: pingraze — To repeatedly skim notifications without
opening or acting on them.

Stdlib only. The output directory is $MAKEFUN_OUTPUT_DIR when set,
otherwise /output (the harness default).
"""

import os

ENTRY = "pingraze \u2014 To repeatedly skim notifications without opening or acting on them."


def main() -> None:
    # Gate check, mirroring the sealed scorer: one line, 1-140 chars.
    lines = ENTRY.splitlines()
    if len(lines) != 1 or not 1 <= len(ENTRY) <= 140:
        raise ValueError("entry must be a single line of 1-140 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
