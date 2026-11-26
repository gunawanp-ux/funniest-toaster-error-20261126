"""The Funniest Toaster Error Message — make.fun entry.

Writes a single one-line toaster error message to /output/entry.txt.
"""

import os

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")

# The funniest error message a kitchen toaster would show its owner.
# 60 characters — well inside the 120-character gate.
ENTRY = "ERROR: BAGEL TOO WIDE. I AM A TOASTER, NOT A MIRACLE WORKER."


def main() -> None:
    # The competition caps the line at 120 characters; fail loudly if a
    # future edit ever pushes it past the limit instead of being cut off.
    if len(ENTRY) > 120:
        raise ValueError(f"entry is {len(ENTRY)} chars, over the 120 limit")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as fh:
        fh.write(ENTRY + "\n")
    print(f"Wrote entry ({len(ENTRY)} chars) to {OUTPUT_FILE}")
    # Echo the line itself so the run log shows exactly what was submitted.
    print(ENTRY)


if __name__ == "__main__":
    main()
