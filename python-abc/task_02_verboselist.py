#!/usr/bin/python3
"""
This module defines a class VerboseList.
It extends the built-in list class with verbose output.
"""


class VerboseList(list):
    """
    A class used to represent a list with verbose output.

    Methods:
        append: Adds an item to the list with verbose output.
        extend: Extends the list with items
        from an iterable with verbose output.
        remove: Removes the first occurrence
        of an item from the list with verbose output.
        pop: Removes and returns an item at a given index with verbose output.
    """
    def append(self, data):
        """
        Adds an item to the list with verbose output.

        Args:
            data: The item to add to the list.
        """
        print("Added [{}] to the list.".format(data))
        super().append(data)

    def extend(self, data):
        """
        Extends the list with items from an iterable with verbose output.

        Args:
            data: An iterable of items to add to the list.
        """
        print("Extended the list with [{}] items.".format(len(data)))
        super().extend(data)

    def remove(self, data):
        """
        Removes the first occurrence of an item
        from the list with verbose output.

        Args:
            data: The item to remove from the list.
        """
        print("Removed [{}] from the list.".format(data))
        super().remove(data)

    def pop(self, index=-1):
        """
        Removes and returns an item at a given index with verbose output.

        Args:
            index (int, optional): The index of the item to remove.
            Defaults to -1 (the last item).

        Returns:
            The item that was removed from the list.
        """
        popped = super().pop(index)
        print("Popped [{}] from the list.".format(popped))
        return popped
