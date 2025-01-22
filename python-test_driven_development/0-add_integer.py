#!/usr/bin/python3
"""
This is the add_integer module
The module supplies one function, add_integer(a, b).
The function only accepts two int or float arguments.
"""


def add_integer(a, b=98):
    """Adds two integers or floats.
    Returns int: the sum of a and b.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
