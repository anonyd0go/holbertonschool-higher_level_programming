#!/usr/bin/python3
"""
This module defines a function that reads a text file
and prints its contents to stdout.
"""


def read_file(filename=""):
    """
    Reads a text file and prints its contents to stdout.

    Args:
        filename (str): The name of the file to read.
        Defaults to an empty string.
    """
    with open(filename, "r", encoding="utf-8") as handle:
        print(handle.read(), end="")
