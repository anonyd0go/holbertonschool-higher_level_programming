#!/usr/bin/python3
"""
This module defines a function that loads an object from a JSON file.
"""
import json


def load_from_json_file(filename):
    """
    Loads an object from a JSON file.

    Args:
        filename (str): The name of the file to load the object from.

    Returns:
        The object loaded from the JSON file.
    """
    object = None
    with open(filename, "r", encoding="utf-8") as handle:
        object = json.load(handle)
    return object
