#!/usr/bin/env python3
"""Generate and print a random number between 1 and 100."""

import random

def main() -> None:
    random_number = random.randint(1, 100)
    print(f"Rastgele sayı: {random_number}")

if __name__ == "__main__":
    main()
