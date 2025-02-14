#!/usr/bin/python3
"""
This module defines a class CustomObject
that can be serialized and deserialized using pickle.
"""
import pickle


class CustomObject:
    """
    A class used to represent a CustomObject.

    Attributes:
        name (str): The name of the object.
        age (int): The age of the object.
        is_student (bool): Whether the object is a student.

    Methods:
        serialize(filename): Serializes the object to a file using pickle.
        deserialize(filename): Deserializes the object from a file
        using pickle.
        __str__(): Returns a string representation of the object.
        display(): Prints the string representation of the object.
    """
    def __init__(self, name, age, is_student):
        """
        Initializes the CustomObject with a name, age, and student status.

        Args:
            name (str): The name of the object.
            age (int): The age of the object.
            is_student (bool): Whether the object is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def serialize(self, filename):
        """
        Serializes the object to a file using pickle.

        Args:
            filename (str): The name of the file
            to save the serialized object to.
        """
        with open(filename, 'wb')as handler:
            pickle.dump(self, handler)

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes the object from a file using pickle.

        Args:
            filename (str): The name of the file to
            load the serialized object from.

        Returns:
            CustomObject: The deserialized object.
        """
        with open(filename, 'rb') as handler:
            return pickle.load(handler)

    def __str__(self):
        """
        Returns a string representation of the object.

        Returns:
            str: The string representation of the object.
        """
        return "Name: {}\nAge: {}\nIs Student: {}".format(
            self.name, self.age, self.is_student
        )

    def display(self):
        """
        Prints the string representation of the object.
        """
        print(self)
