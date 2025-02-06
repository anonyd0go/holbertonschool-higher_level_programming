#!/usr/bin/python3
"""
This module defines abstract and concrete classes for shapes
and a function to display shape information.
"""
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """
    An abstract base class used to represent a shape.

    Methods:
        area: Abstract method to be implemented by
        subclasses to calculate the area of the shape.
        perimeter: Abstract method to be implemented by
        subclasses to calculate the perimeter of the shape.
    """

    @abstractmethod
    def area(self):
        """
        Abstract method to be implemented by
        subclasses to calculate the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method to be implemented by
        subclasses to calculate the perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    A class used to represent a Circle, inheriting from Shape.

    Attributes:
        radius (float): The radius of the circle.
    """

    def __init__(self, radius):
        """
        Initializes the circle with a given radius.

        Args:
            radius (float): The radius of the circle.
        """
        self.__radius = abs(radius)

    def area(self):
        """
        Calculates the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return pi * (self.__radius ** 2)

    def perimeter(self):
        """
        Calculates the perimeter of the circle.

        Returns:
            float: The perimeter of the circle.
        """
        return (2 * self.__radius) * pi


class Rectangle(Shape):
    """
    A class used to represent a Rectangle, inheriting from Shape.

    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes the rectangle with a given width and height.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle.
        """
        return 2 * (self.__width + self.__height)


def shape_info(shape):
    """
    Prints the area and perimeter of a shape.

    Args:
        shape (Shape): The shape object to display information for.
    """
    print("Area: {}".format(shape.area()))
    print("Perimiter: {}".format(shape.perimeter()))
