#!/usr/bin/python3
"""
This module defines a function that checks if an object
is an instance of a class that
inherited (directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to match the type of obj to.

    Returns:
        bool: True if obj is an instance of a class that
        inherited from a_class, False otherwise.
    """
    return issubclass(obj.__class__, a_class) and not type(obj) is a_class
