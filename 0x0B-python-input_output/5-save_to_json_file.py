#!/usr/bin/python3
"""5-save_to_json_file module"""
import json
"""import json module"""


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation.
    Args:
        my_obj: the object file
        filename: the file we are writing too
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
