#!/usr/bin/env python3
"""Dad Joke Showdown entry: writes one original dad joke to /output/entry.txt."""

import os

JOKE = (
    "My kids laughed when I said I'd become a baker. "
    "'Dad, you can't even boil water.' "
    "I said, 'Relax \u2014 dough is the yeast of my worries.'"
)

if not 1 <= len(JOKE) <= 200:
    raise ValueError(f"Joke must be 1-200 characters, got {len(JOKE)}")

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(JOKE)
    print(f"Wrote {len(JOKE)}-char joke to /output/entry.txt")

if __name__ == "__main__":
    main()
