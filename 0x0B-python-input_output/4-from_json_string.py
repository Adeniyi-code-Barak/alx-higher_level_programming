#!/usr/bin/python3
"""4-from_json_string module"""
import json
"""import json module"""


def from_json_string(my_str):
    """Returns an object (Python data structure) represented
    by a JSON string.
    Args:
        my_str: string to be converted to object
    """
    return json.loads(my_str)
