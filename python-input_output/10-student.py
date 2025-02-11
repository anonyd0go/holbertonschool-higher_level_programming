#!/usr/bin/python3
"""
This module defines a class Student.
"""


class Student:
    """
    A class used to represent a Student.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes the Student with a first name, last name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns the dictionary representation of the Student instance.

        Args:
            attrs (list, optional): A list of attribute names to include in the dictionary. Defaults to None.

        Returns:
            dict: The dictionary representation of the Student instance.
        """
        json_dict = {}
        if attrs and isinstance(attrs, list):
            for ele in attrs:
                if ele in self.__dict__.keys():
                    json_dict[ele] = self.__dict__[ele]
            return json_dict

        return self.__dict__
