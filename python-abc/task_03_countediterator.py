#!/usr/bin/python3
"""
This module defines a class CountedIterator.
It keeps track of the number of iterations.
"""


class CountedIterator:
    """
    A class used to represent an iterator that counts the number of iterations.

    Attributes:
        iterator (iterator): The iterator for the iterable.
        __counter (int): The count of iterations.

    Methods:
        get_count: Returns the count of iterations.
        __next__: Returns next item from the iterable and increments count.
    """
    def __init__(self, iterable):
        """
        Initializes the CountedIterator with a given iterable.

        Args:
            iterable (iterable): The iterable to iterate over.
        """
        self.iterator = iter(iterable)
        self.__counter = 0

    def get_count(self):
        """
        Returns the count of iterations.

        Returns:
            int: The count of iterations.
        """
        return self.__counter

    def __next__(self):
        """
        Returns the next item from the iterable and increments the count.

        Raises:
            StopIteration: If there are no more items in the iterable.

        Returns:
            The next item from the iterable.
        """
        if not next(self.iterator):
            raise StopIteration
        self.__counter += 1
        return next(self.iterator)

    def __iter__(self):
        """
        Returns the iterator object itself.

        Returns:
            CountedIterator: The iterator object itself.
        """
        return self
