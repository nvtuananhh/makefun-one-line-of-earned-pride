"""One Line of Earned Pride — a quiet, earned moment.

The program writes a single line to /output/entry.txt: a quiet,
earned moment of pride for someone in a scene, a small person
doing something hard, a long effort finally landing.
"""

import os

MAX_CHARS = 240
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_FILENAME = "entry.txt"

# The pride is earned inside the line: two years of evening
# classes, and the moment is a signature, not a trophy — he
# signs his name on the library card without copying it from
# the piece of paper in his pocket. The scene is concrete
# (library, card, pocket paper), the effort is felt, and the
# pride arrives by the last word: pocket. No trophy, no
# podium, no graduation — the fresh image is the folded
# paper he no longer needs.
LINE = "At seventy-three, after two years of evening classes, he signed his name on the library card without copying it from the piece of paper in his pocket."


def build_line():
    """Return the entry line, checked: one line, 1-240 characters."""
    line = LINE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= MAX_CHARS, "entry must be 1-240 characters"
    return line


def ensure_output_dir(out_dir):
    os.makedirs(out_dir, exist_ok=True)


def write_entry(line, out_dir=OUTPUT_DIR):
    path = os.path.join(out_dir, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    return path


def main():
    line = build_line()
    ensure_output_dir(OUTPUT_DIR)
    write_entry(line)


if __name__ == "__main__":
    main()
