#!/usr/bin/env python3
"""
Math functions to be tested with test_katas.py

Students should not change this file.
"""

__author__ = 'madarp and Q3 friends'


def add(x, y):
    """Return the result of adding x to y."""
    return x + y


def multiply(x, y):
    """Return the result of multiplying x by y."""
    result = 0
    for _ in range(abs(y)):
        result = add(result, x)
    return -result if y < 0 else result


def power(x, n):
    """Return the result of taking x to the nth power."""
    # Negative and fractional powers are not allowed
    if n < 0:
        raise ValueError('n cannot be negative')
    elif 0 < n < 1.0:
        raise ValueError('n cannot be fractional')

    result = 1
    for _ in range(n):
        result = multiply(result, x)
    return result


def factorial(n):
    """Return the result of calculating the factorial of n."""
    if n < 0:
        raise ValueError("n cannot be negative")
    result = 1
    for i in range(1, n + 1):
        result = multiply(result, i)
    return result


def fibonacci(n):
    """Returns the nth term of the Fibonacci sequence, starting from 0."""
    if n < 0:
        raise ValueError("n cannot be negative")
    elif n < 2:
        return n
    else:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, add(a, b)
        return a
