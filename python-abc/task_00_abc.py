#!/usr/bin/python3
"""
This module defines abstract and concrete classes for animals.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    An abstract base class used to represent an animal.

    Methods:
        sound: Abstract method to be implemented by subclasses
        to define the sound the animal makes.
    """
    @abstractmethod
    def sound(cls):
        """
        Abstract method to be implemented by subclasses
        to define the sound the animal makes.
        """
        pass


class Dog(Animal):
    """
    A class used to represent a Dog, inheriting from Animal.

    Methods:
        sound: Returns the sound made by the dog.
    """
    def sound(self):
        """
        Returns the sound made by the dog.

        Returns:
            str: The sound "Bark".
        """
        return "Bark"


class Cat(Animal):
    """
    A class used to represent a Cat, inheriting from Animal.

    Methods:
        sound: Returns the sound made by the cat.
    """
    def sound(self):
        """
        Returns the sound made by the cat.

        Returns:
            str: The sound "Meow".
        """
        return "Meow"
