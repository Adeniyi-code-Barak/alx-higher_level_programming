#!/usr/bin/python3
"""6-load_from_json_file module"""
import json
"""import json module"""


def load_from_json_file(filename):
    """Creates an Object from a “JSON file.
    Args:
        filename: the file to be read
    Return: object from a “JSON file
    """
    with open(filename, "r") as file:
        return json.load(file)
