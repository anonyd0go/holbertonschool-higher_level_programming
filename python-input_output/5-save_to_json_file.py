#!/usr/bin/python3
"""
This module defines a function that saves an object to a file in JSON format.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Saves an object to a file in JSON format.

    Args:
        my_obj: The object to save.
        filename (str): The name of the file to save the object to.
    """
    with open(filename, "w", encoding="utf-8") as handle:
        json.dump(my_obj, handle)
