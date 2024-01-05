#!/usr/bin/python3
"""1-rectangle.py"""


class Rectangle:
    """Class Rectangle that defines a rectangle.
    Args:
        width(int): the width of the rectangle
        height(int): the height of the rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """This is the width, using getter and setter.
        Args:
            value(int): the value for the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        if (
                type(value) is not int or value is None
                ):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """This is the height, using getter and setter.
        Args:
            value(int): the value for the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        if (
                type(value) is not int or value is None
                ):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
