#!/usr/bin/env python3
"""
Solution module for Test Katas
"""

__author__ = 'madarp'

import unittest
import random
import katas


class TestKatas(unittest.TestCase):
    def test_add(self):
        """Check correctness of add"""
        for _ in range(100):
            x = random.randint(-100, 100)
            y = random.randint(-100, 100)
            self.assertEqual(katas.add(x, y), x + y)

    def test_multiply(self):
        """Check correctness of multiply"""
        for _ in range(100):
            x = random.randint(-100, 100)
            y = random.randint(-100, 100)
            self.assertEqual(katas.multiply(x, y), x * y)

    def test_power(self):
        """Check correctness of powers"""
        for _ in range(50):
            n = random.randint(0, 15)
            x = random.randint(0, 30)
            self.assertEqual(katas.power(x, n), x ** n)
        with self.assertRaises(ValueError):
            katas.power(2, -13)
            katas.power(2, 0.5)

    def test_factorial(self):
        """Check correctness of factorial"""
        factorials = (
            1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800,
            39916800, 479001600, 6227020800, 87178291200, 1307674368000
        )
        for i, f in enumerate(factorials):
            self.assertEqual(katas.factorial(i), f)
        # passing a negative number should raise an exception
        with self.assertRaises(ValueError):
            katas.factorial(-13)

    def test_fibonacci(self):
        """Check correctness of fibonacci"""
        # just test first 30 terms
        fibs = (
            0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,
            144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946,
            17711, 28657, 46368, 75025, 121393, 196418, 317811
        )
        for n, f in enumerate(fibs):
            self.assertEqual(
                katas.fibonacci(n),
                fibs[n],
                'The Fibonacci terms are incorrect'
            )
        # passing a negative number should raise an exception
        with self.assertRaises(ValueError):
            katas.fibonacci(-13)


if __name__ == '__main__':
    unittest.main()
