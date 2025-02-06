#!/usr/bin/python3
"""
This module defines classes for Fish, Bird, and FlyingFish.
"""


class Fish:
    """
    A class used to represent a Fish.

    Methods:
        swim: Prints that the fish is swimming.
        habitat: Prints the habitat of the fish.
    """
    def swim(self):
        """
        Prints that the fish is swimming.
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Prints the habitat of the fish.
        """
        print("The fish lives in water")


class Bird:
    """
    A class used to represent a Bird.

    Methods:
        fly: Prints that the bird is flying.
        habitat: Prints the habitat of the bird.
    """
    def fly(self):
        """
        Prints that the bird is flying.
        """
        print("The bird is flying")

    def habitat(self):
        """
        Prints the habitat of the bird.
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    A class used to represent a FlyingFish, inheriting from Fish and Bird.

    Methods:
        fly: Prints that the flying fish is soaring.
        swim: Prints that the flying fish is swimming.
        habitat: Prints the habitat of the flying fish.
    """
    def fly(self):
        """
        Prints that the flying fish is soaring.
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        Prints that the flying fish is swimming.
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        Prints the habitat of the flying fish.
        """
        print("The flying fish lives both in water and the sky!")
