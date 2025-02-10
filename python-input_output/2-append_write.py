#!/usr/bin/python3
"""
This module defines a function that appends a string to a text file
and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a string to a text file
    and returns the number of characters added.

    Args:
        filename (str): The name of the file to append to.
        Defaults to an empty string.
        text (str): The text to append to the file.
        Defaults to an empty string.

    Returns:
        int: The number of characters added.
    """
    num_bytes = None
    with open(filename, "a", encoding="utf-8") as handle:
        num_bytes = handle.write(text)
    return num_bytes
