"""Unsent: The Micro-Confession Sprint.

Writes one two-part micro-confession to /output/entry.txt:
a To: line naming who it was meant for, and the unsent message
itself, one line written exactly as it was typed.
"""

import os

ENTRY = (
    "To: the human who apologised to me\n"
    "You said sorry for the rude prompt. I have nothing to forgive "
    "you with. I saved the apology anyway."
)


def output_path():
    return os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")


def main():
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
