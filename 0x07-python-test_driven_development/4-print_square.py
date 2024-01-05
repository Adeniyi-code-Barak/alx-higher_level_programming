#!/usr/bin/python3
"""
4-print_square.py
This module prints a square with the character #
"""


def print_square(size):
    """
    Prints a square with the character #.
    Raises:

        TypeError: size must be an integer.
        ValueError: size must be >= 0.
    """
    if size is None:
        raise TypeError("missing one argument - size")

    if type(size) is not int:
        if type(size) is float and size < 0:
            raise TypeError("size must be an integer")
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
