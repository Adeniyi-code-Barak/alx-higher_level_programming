#!/usr/bin/python3
"""100-append_after module"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after each line containing
    a specific string.

    Args:
        filename: the name of the file
        search_string: the string to search for
        new_string: the new string to be added to the test file
    """
    with open(filename, "r", encoding='utf-8') as file:
        lines = file.readlines()

    with open(filename, "w", encoding='utf-8') as file:
        for row in lines:
            file.write(row)
            if search_string in row:
                file.write(new_string)
