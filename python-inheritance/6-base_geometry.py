#!/usr/bin/python3
"""
This module defines a class BaseGeometry.
"""


class BaseGeometry:
    """
    A class used to represent basic geometric shapes.

    Methods:
        area: Raises an Exception with the message "area() is not implemented".
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
