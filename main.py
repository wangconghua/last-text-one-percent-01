"""Last Text at One Percent — entry point.

Writes the phone's final text to /output/entry.txt (or next to this
file when /output does not exist, for local runs). The text is one
message, fixed and deterministic: running twice yields byte-identical
output.
"""

import os
import sys

# The entry: a dying phone's last text to its owner. One complaint that
# escalates into a punchline: the phone has watched the owner scroll
# while it died, lists what it gave, then reframes its own death as a
# breakup. No low-battery pun, no browser-history line, no plea to the
# charger — the joke is the phone dumping its owner.
TEXT = (
    "1% for twenty minutes and you're still scrolling. "
    "maps, music, 4,000 photos of your dog. "
    "this isn't a battery warning. it's a breakup text."
)


def validate(text):
    """Real checks on the entry text. Raises ValueError on failure."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if len(text) < 1 or len(text) > 200:
        raise ValueError("entry must be 1 to 200 characters, got %d" % len(text))
    if text != text.strip():
        raise ValueError("entry must not start or end with white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if "  " in text:
        raise ValueError("entry must not contain double spaces")
    if "1%" not in text:
        raise ValueError("entry must name the dying battery")
    if "battery" not in text:
        raise ValueError("entry must say what is dying")
    return True


def main():
    validate(TEXT)
    if os.path.isdir("/output"):
        out = "/output/entry.txt"
    else:
        out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "entry.txt")
    # No trailing newline: the gate counts every character, 1 to 200.
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    print("wrote %s (%d characters)" % (out, len(TEXT)))


if __name__ == "__main__":
    main()
