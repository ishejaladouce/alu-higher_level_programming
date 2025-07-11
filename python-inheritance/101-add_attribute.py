#!/usr/bin/python3
"""
Function that adds a new attribute to an object if it’s possible.
"""


def add_attribute(obj, attr_name, value):
    """
    Adds a new attribute to an object if possible.

    Args:
        obj: The object to modify.
        attr_name (str): Name of the attribute to add.
        value: Value of the new attribute.

    Raises:
        TypeError: If the object can't accept new attributes.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, value)
