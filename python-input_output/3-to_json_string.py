#!/usr/bin/python3
"""
Module that returns the JSON representation of an object as a string.
"""

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of a Python object as a string.

    Args:
        my_obj (any): The Python object to serialize.

    Returns:
        str: The JSON string representation of the object.
    """
    return json.dumps(my_obj)
