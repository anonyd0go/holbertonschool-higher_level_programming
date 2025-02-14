#!/usr/bin/python3
"""
This module defines functions for serializing a dictionary to an XML file
and deserializing an XML file to a dictionary.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a dictionary to an XML file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The name of the file to save the serialized data to.
    """
    try:
        tree = ET.parse(filename)
    except FileNotFoundError:
        root = ET.Element("data")
        for key in dictionary.keys():
            element = ET.SubElement(root, key)
            element.text = str(dictionary[key])
        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8")


def deserialize_from_xml(filename):
    """
    Deserializes an XML file to a dictionary.

    Args:
        filename (str): The name of the file to load the data from.

    Returns:
        dict: The deserialized dictionary.
    """
    new_dcict = {}
    tree = ET.parse(filename)
    root = tree.getroot()

    for key in root.findall("./"):
        new_dcict[key.tag] = str(key.text)
    return new_dcict
