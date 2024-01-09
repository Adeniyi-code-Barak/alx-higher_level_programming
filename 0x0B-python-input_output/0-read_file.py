#!/usr/bin/python3
"""0-read_file module"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout
    Args:
        filename: file of the file
    """
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            print("{}".format(line), end='')
