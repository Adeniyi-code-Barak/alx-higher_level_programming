#!/usr/bin/python3
"""3-square.py"""


class Square:
    """The class Square defines a square."""
    def __init__(self, size=0):
        """The __init__ is a special method.

        Args:
            size (int): this is a private instance attribute.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """This calculates the area of the Square.

        Args:
            cal (int): calculates area of a square.
        """
        cal = self.__size * self.__size
        return cal
