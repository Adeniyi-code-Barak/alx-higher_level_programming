#!/usr/bin/python3
"""8-rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""BaseGeometry class module"""


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """The class constructor
        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
