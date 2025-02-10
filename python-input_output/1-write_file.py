#!/usr/bin/python3
"""
This module defines a function that writes a string to a text file
and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file
    and returns the number of characters written.

    Args:
        filename (str): The name of the file to write to.
        Defaults to an empty string.
        text (str): The text to write to the file. Defaults to an empty string.

    Returns:
        int: The number of characters written.
    """
    bytes = None
    with open(filename, "w", encoding="utf-8") as handle:
        bytes = handle.write(text)

    return bytes
