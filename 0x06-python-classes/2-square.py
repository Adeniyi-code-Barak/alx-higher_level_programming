#!/usr/bin/python3
"""2-square.py"""


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
