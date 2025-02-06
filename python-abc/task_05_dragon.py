#!/usr/bin/python3
"""
This module defines mixin classes for swimming and flying abilities, and a Dragon class that uses these mixins.
"""


class SwimMixin:
    """
    A mixin class that provides swimming ability.
    """

    def swim(self):
        """
        Prints that the creature swims.
        """
        print("The creature swims!")


class FlyMixin:
    """
    A mixin class that provides flying ability.
    """

    def fly(self):
        """
        Prints that the creature flies.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A class used to represent a Dragon, inheriting from SwimMixin and FlyMixin.

    Methods:
        roar: Prints that the dragon roars.
        fire: Prints that the dragon breathes fire.
    """

    def roar(self):
        """
        Prints that the dragon roars.
        """
        print("The dragon roars!")

    def fire(self):
        """
        Prints that the dragon breathes fire.
        """
        print("The dragon breathes fire!")
