#!/usr/bin/python3
"""
This module defines a class MyList that inherits from list.
"""


class MyList(list):
    """
    A class used to represent a custom list.
    It inherits from the built-in list.

    Methods:
        print_sorted: Prints the list in sorted order.
    """
    def print_sorted(self):
        """
        Prints the list in sorted order.
        """
        print(sorted(self))
