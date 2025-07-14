#!/usr/bin/python3
"""
Module that returns the dictionary description of an object
for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns the dictionary representation of a simple data object.

    Args:
        obj: An instance of a class with serializable attributes.

    Returns:
        dict: Dictionary containing all serializable attributes.
    """
    return obj.__dict__
