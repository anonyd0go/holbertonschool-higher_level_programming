#!/usr/bin/python3
"""
This module defines a class MyInt that inherits from int.
It inverts the behavior of the equality and inequality operators.
"""


class MyInt(int):
    """
    A class used to represent an integer with
    inverted equality and inequality operators.

    Attributes:
        value (int): The integer value.

    Methods:
        __eq__: Inverts the behavior of the equality operator.
        __ne__: Inverts the behavior of the inequality operator.
    """
    def __init__(self, value):
        """
        Initializes the MyInt with a given integer value.

        Args:
            value (int): The integer value.
        """
        self.value = value

    def __eq__(self, other):
        """
        Inverts the behavior of the equality operator.

        Args:
            other (int): The integer to compare with.

        Returns:
            bool: True if the values are not equal, False otherwise.
        """
        return self.value != other

    def __ne__(self, other):
        """
        Inverts the behavior of the inequality operator.

        Args:
            other (int): The integer to compare with.

        Returns:
            bool: True if the values are equal, False otherwise.
        """
        return self.value == other
