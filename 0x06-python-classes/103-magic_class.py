#!/usr/bin/python3
"""103-magic_class.py"""
import math


class MagicClass:
    """Determines the are and circumference of a circle."""
    def __init__(self, radius=0):
        """This is a special method.

        Args:
            radius: the radius of the circle
        """
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

    def area(self):
        """Handles the area of the circle.

        Returns:
            float: The calculated area of the circle.
        """
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        """Handles the circumference of the circle

        Returns:
            float: The calculated circumference of the circle.
        """
        return 2 * math.pi * self._MagicClass__radius
