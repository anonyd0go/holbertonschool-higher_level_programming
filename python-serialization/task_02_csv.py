#!/usr/bin/python3
"""
This module defines a function that converts a CSV file to a JSON file.
"""
import csv
import json


def convert_csv_to_json(csv_file):
    """
    Converts a CSV file to a JSON file.

    Args:
        csv_file (str): The name of the CSV file to convert.

    Returns:
        None
    """
    csv_dat = []
    json_file = "data.json"
    with open(csv_file, 'r', encoding="utf-8") as csv_handle:
        csv_reader = csv.DictReader(csv_handle)

        for row in csv_reader:
            csv_dat.append(row)

    with open(json_file, 'w', encoding="utf-8") as json_handle:
        json.dump(csv_dat, json_handle, indent=4)
