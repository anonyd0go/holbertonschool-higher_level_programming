#!/usr/bin/python3
"""
This module defines a function that inserts a line of text to a file,
after each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file,
    after each line containing a specific string.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert after each line
            containing the search string.
    """
    file_lines = None
    with open(filename, 'r', encoding='utf-8') as handler:
        file_lines = handler.readlines()
    for i in range(len(file_lines)):
        if search_string in file_lines[i]:
            file_lines.insert(i + 1, new_string)
    with open(filename, 'w', encoding='utf-8') as handler:
        for line in file_lines:
            handler.write(line)
