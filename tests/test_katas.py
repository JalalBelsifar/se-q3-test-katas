__author__ = "Jalal Belsifar with Dave/Greg"

import unittest
import katas


class TestKatas(unittest.TestCase):
    """tests the add function"""

    def test_add(self):
        self.assertEqual(katas.add(2, 1), 3)
        self.assertEqual(katas.add(-8, 4), -4)
        self.assertEqual(katas.add(120, 16), 136)

    def test_multiply(self):
        """tests the multiply function"""
        self.assertEqual(katas.multiply(5, 7), 35)
        self.assertEqual(katas.multiply(-8, 4), -32)
        self.assertEqual(katas.multiply(4, 4), 16)

    def test_power(self):
        """tests the power function"""
        self.assertEqual(katas.power(2, 3), 8)
        self.assertEqual(katas.power(3, 3), 27)
        self.assertEqual(katas.power(5, 2), 25)

    def test_factorial(self):
        """tests the factorial function"""
        self.assertEqual(katas.factorial(5), 120)
        self.assertEqual(katas.factorial(2), 2)
        self.assertEqual(katas.factorial(3), 6)

    def test_fibonacci(self):
        """tests the fibonacci function"""
        fibo_sequence = (
            0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,
            144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946,
            17711, 28657, 46368, 75025, 121393, 196418, 317811
        )
        for i, element in enumerate(fibo_sequence):
            self.assertEqual(
                katas.fibonacci(i),
                fibo_sequence[i],
            )
        with self.assertRaises(ValueError):
            katas.fibonacci(-22)


if __name__ == '__main__':
    unittest.main()
