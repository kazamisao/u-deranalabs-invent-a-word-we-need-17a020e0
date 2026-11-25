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
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
