"""Describe Your Ex in One Word — entry program.

Writes exactly one word to /output/entry.txt: the verdict on an ex.

The word: "Unsubscribe".

Why this word: an ex is someone you once opted into who keeps
showing up uninvited, like a newsletter you never asked to keep
receiving. "Unsubscribe" is the one-word verdict — the action every
person who has had an ex has wanted to take, delivered as a dry,
instantly readable joke with no caption needed. It is a single
correctly spelled word, no punctuation tricks, and it lands at a
glance.

The program is deterministic: it writes the same bytes on every run.
"""

from pathlib import Path

WORD = "Unsubscribe"
OUT = Path("/output/entry.txt")


def main() -> None:
    # Gate self-check: 1-111 chars, a single word, not only whitespace.
    assert 1 <= len(WORD) <= 111, "word outside the 1-111 character gate"
    assert WORD == WORD.strip(), "word has surrounding whitespace"
    assert not any(ch.isspace() for ch in WORD), "word must be a single word"
    assert WORD.isalpha(), "word must be letters only"

    OUT.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the file is exactly the word, byte for byte.
    OUT.write_bytes(WORD.encode("utf-8"))

    # Read-back verification: what we wrote is exactly the word.
    written = OUT.read_bytes()
    assert written == WORD.encode("utf-8"), "written bytes differ from the word"


if __name__ == "__main__":
    main()
