#!/usr/bin/python3
"""
This module defines a function that inserts a line of text to a file,
after each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each line containing a specific
    string.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert after each line containing
            the search string.
    """
    new_lines = []
    with open(filename, 'r+', encoding='utf-8') as handler:
        file_lines = handler.readlines()
        for line in file_lines:
            new_lines.append(line)
            if search_string in line:
                new_lines.append(new_string)
        handler.seek(0)
        for line in new_lines:
            handler.write(line)
