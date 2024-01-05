#!/usr/bin/python3
"""
3-say_my_name.
This module prints My name is <first name> <last name>.
"""


def say_my_name(first_name, last_name=""):
    """
    This function prints My name is <first name> <last name>.

    Raises:
        TypeError: first_name must be a string.
        TypeError: last_name must be a string.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if (
            first_name and not
            all(char.isalpha() or char.isspace() for char in first_name)
            ):
        raise TypeError("first_name must be a string containing letters")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    if (
            last_name and not
            all(char.isalpha() or char.isspace() for char in last_name)
            ):
        raise TypeError("last_name must be a string containing letters")

    print("My name is {} {}".format(first_name, last_name))
