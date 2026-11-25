"""One Line, One Laugh — writes a single funny line to entry.txt.

Stdlib only, no network, fully deterministic.
"""

import os

LINE = "I told my Roomba it was adopted. Now it only vacuums the neighbour's house."


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
