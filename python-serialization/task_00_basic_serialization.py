#!/usr/bin/python3
import json
"""
This module defines functions for basic serialization and deserialization
using JSON.
"""


def serialize_and_save_to_file(data, filename):
    """
    Serializes data to JSON and saves it to a file.

    Args:
        data: The data to serialize.
        filename (str): The name of the file to save the serialized data to.
    """
    with open(filename, 'w', encoding="utf-8") as handler:
        json.dump(data, handler)

def load_and_deserialize(filename):
    """
    Loads data from a JSON file and deserializes it.

    Args:
        filename (str): The name of the file to load the data from.

    Returns:
        The deserialized data.
    """
    with open(filename, 'r', encoding="utf-8") as handler:
        obj = json.load(handler)
    return obj