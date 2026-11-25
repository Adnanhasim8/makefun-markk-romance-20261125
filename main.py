"""Robot Romance: One-Line Pickup Lines for AI.

Writes a single-line joke pickup line, aimed at a robot/AI, to
/output/entry.txt (UTF-8, no network at run time).
"""

import os

ENTRY = "I asked the model for a pickup line. It just printed your name."


def main() -> None:
    # Gate assertions: the entry must be exactly one line, 1-199
    # characters, non-empty.
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be exactly one line"
    assert 1 <= len(text) <= 199, f"entry must be 1-199 chars, got {len(text)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")
    # Verify what was written matches the gate too.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == text + "\n", "written output does not match entry"
    assert written.count("\n") == 1, "output must be exactly one line"


if __name__ == "__main__":
    main()
