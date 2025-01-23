#!/usr/bin/python3
"""
This module provides a function
to print text with 2 new lines after: '.', '?', and ':'.
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after chars: '.', '?', and ':'.

    Args:
        text (str): The text to be processed.

    Raises:
        TypeError: If text is not a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] in ['.', '?', ':']:
            print(text[i])
            print()
            i += 1
        else:
            print(text[i], end="")
        i += 1
