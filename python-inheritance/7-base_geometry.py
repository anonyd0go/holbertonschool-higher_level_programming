#!/usr/bin/python3
"""
This module defines a class BaseGeometry.
"""


class BaseGeometry:
    """
    A class used to represent basic geometric shapes.

    Methods:
        area: Raises an Exception with the message "area() is not implemented".
        integer_validator: Validates that a value is a positive integer.
    """

    def area(self):
        """
        Raises an Exception to indicate
        that the area method is not implemented.

        Raises:
            Exception: Always raises an Exception
            with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a value is a positive integer.

        Args:
            name (str): The name of the value.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is not greater than 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
