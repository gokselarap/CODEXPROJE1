import unittest

from rng import LCGRandom


class TestLCGRandom(unittest.TestCase):
    def test_reproducible_sequence(self) -> None:
        seed = 12345
        first = LCGRandom(seed=seed)
        second = LCGRandom(seed=seed)
        self.assertEqual([first.random() for _ in range(5)], [second.random() for _ in range(5)])

    def test_randint_range(self) -> None:
        gen = LCGRandom(seed=42)
        for _ in range(100):
            value = gen.randint(10, 20)
            self.assertGreaterEqual(value, 10)
            self.assertLessEqual(value, 20)

    def test_randrange_validation(self) -> None:
        gen = LCGRandom(seed=0)
        with self.assertRaises(ValueError):
            gen.randrange(5, 5)

    def test_sample_count(self) -> None:
        gen = LCGRandom(seed=99)
        result = gen.sample(0, 10, 3)
        self.assertEqual(len(result), 3)
        for value in result:
            self.assertGreaterEqual(value, 0)
            self.assertLess(value, 10)


if __name__ == "__main__":
    unittest.main()
