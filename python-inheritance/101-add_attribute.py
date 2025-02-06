#!/usr/bin/python3
"""
This module defines a function that
adds a new attribute to an object if possible.
"""


def add_attribute(object, attribute, value):
    """
    Adds a new attribute to an object if possible.

    Args:
        obj: The object to add the attribute to.
        attribute (str): The name of the attribute to add.
        value: The value of the attribute to add.

    Raises:
        TypeError: If the object can't have new attributes.
    """
    if '__dict__' not in dir(object):
        raise TypeError("can't add new attribute")
    object.__dict__[attribute] = value
