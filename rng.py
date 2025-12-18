"""A simple linear congruential generator for reproducible pseudo-random numbers."""
from __future__ import annotations

from dataclasses import dataclass
from time import time_ns
from typing import Iterable, List, Optional


@dataclass
class LCGRandom:
    """A minimal linear congruential generator.

    The generator is deterministic and produces the same sequence when the
    same seed is provided. A seed can be omitted to derive one from the
    current time in nanoseconds.
    """

    seed: int
    modulus: int = 2**32
    multiplier: int = 1664525
    increment: int = 1013904223

    def __init__(
        self,
        seed: Optional[int] = None,
        *,
        modulus: int = 2**32,
        multiplier: int = 1664525,
        increment: int = 1013904223,
    ) -> None:
        self.modulus = modulus
        self.multiplier = multiplier
        self.increment = increment
        self.seed = seed if seed is not None else time_ns() % modulus
        self._state = self.seed % modulus

    def _next_state(self) -> int:
        self._state = (self.multiplier * self._state + self.increment) % self.modulus
        return self._state

    def random(self) -> float:
        """Return the next random float in the range [0.0, 1.0)."""
        return self._next_state() / self.modulus

    def randrange(self, start: int, stop: Optional[int] = None) -> int:
        """Return a random integer in the range ``[start, stop)``.

        If ``stop`` is omitted, the range becomes ``[0, start)``.
        """
        if stop is None:
            start, stop = 0, start
        if start >= stop:
            raise ValueError("start must be less than stop")
        span = stop - start
        return start + int(self.random() * span)

    def randint(self, a: int, b: int) -> int:
        """Return a random integer N such that ``a <= N <= b``."""
        if a > b:
            raise ValueError("a must be less than or equal to b")
        return self.randrange(a, b + 1)

    def sample(self, start: int, stop: int, count: int) -> List[int]:
        """Generate ``count`` integers in the range ``[start, stop)``."""
        if count < 0:
            raise ValueError("count must be non-negative")
        return [self.randrange(start, stop) for _ in range(count)]

    def __iter__(self) -> Iterable[int]:
        """Iterate indefinitely over integers in ``[0, modulus)``."""
        while True:
            yield self._next_state()


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Generate pseudo-random numbers using an LCG.")
    parser.add_argument("count", type=int, nargs="?", help="How many numbers to generate")
    parser.add_argument("minimum", type=int, nargs="?", help="Inclusive lower bound")
    parser.add_argument("maximum", type=int, nargs="?", help="Inclusive upper bound")
    parser.add_argument("--seed", type=int, default=None, help="Optional seed for reproducibility")
    parser.add_argument(
        "--gui",
        action="store_true",
        help="Launch a simple GUI for generating numbers between 0 and a provided upper bound.",
    )
    args = parser.parse_args()

    if args.gui:
        launch_gui(seed=args.seed)
        return

    if args.count is None or args.minimum is None or args.maximum is None:
        parser.error("count, minimum, and maximum are required unless --gui is set")

    generator = LCGRandom(seed=args.seed)
    for _ in range(args.count):
        print(generator.randint(args.minimum, args.maximum))


def launch_gui(*, seed: Optional[int] = None) -> None:
    """Launch a minimal Tkinter GUI to generate numbers from 0 up to a given bound."""
    import tkinter as tk
    from tkinter import messagebox

    generator = LCGRandom(seed=seed)

    root = tk.Tk()
    root.title("Rastgele Sayı Üreteci")

    tk.Label(root, text="Üst sınırı girin:").pack(padx=10, pady=(10, 0))
    upper_entry = tk.Entry(root)
    upper_entry.pack(padx=10, pady=5)

    result_var = tk.StringVar(value="Henüz sayı üretilmedi")
    tk.Label(root, textvariable=result_var).pack(padx=10, pady=5)

    def generate() -> None:
        raw_value = upper_entry.get()
        try:
            upper_bound = int(raw_value)
        except ValueError:
            messagebox.showerror("Hata", "Lütfen geçerli bir sayı girin.")
            return
        if upper_bound < 0:
            messagebox.showerror("Hata", "Üst sınır negatif olamaz.")
            return
        value = generator.randint(0, upper_bound)
        result_var.set(f"Üretilen sayı: {value}")

    tk.Button(root, text="Üret", command=generate).pack(padx=10, pady=(5, 10))

    root.mainloop()


if __name__ == "__main__":
    main()
