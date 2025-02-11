#!/usr/bin/python3
"""
This script adds all arguments to a Python list and saves them to a file.
"""
import sys
stjson = __import__('5-save_to_json_file').save_to_json_file
lfjson = __import__('6-load_from_json_file').load_from_json_file


def add_items():
    """
    Adds all command-line arguments to a Python list and saves them to a file.
    """
    try:
        args_list = lfjson('add_item.json')
    except FileNotFoundError:
        if len(sys.argv) > 1:
            stjson(sys.argv[1:], 'add_item.json')
        else:
            stjson([], 'add_item.json')
    args_list.extend(sys.argv[1:])
    stjson(args_list, 'add_item.json')


if __name__ == "__main__":
    add_items()
