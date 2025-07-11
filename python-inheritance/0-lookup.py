#!/usr/bin/python3
"""
This module defines the lookup function.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of strings containing names of the attributes and methods.
    """
    return dir(obj)
