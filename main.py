"""Describe Your Ex in One Word: write exactly one word to /output/entry.txt."""

import os

WORD = "Unsubscribe"


def main():
    # Gate: exactly one word, 1-111 chars, nothing else attached.
    assert WORD and len(WORD) <= 111 and len(WORD.split()) == 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        # No trailing newline: the file holds exactly the word, 11 bytes.
        f.write(WORD)


if __name__ == "__main__":
    main()
