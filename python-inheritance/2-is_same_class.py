#!/usr/bin/python3
"""
This module defines a function that checks if an object is
exactly an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of a specified class.

    Args:
        obj: The object to check.
        a_class: The class to match the type of obj to.

    Returns:
        bool: True if obj is exactly an instance of a_class, False otherwise.
    """
    return type(obj) is a_class
