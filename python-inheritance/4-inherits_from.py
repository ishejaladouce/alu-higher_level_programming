#!/usr/bin/python3
"""
Module that defines a function to check if an object
is an instance of a subclass (directly or indirectly)
of a specified class.
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class that
    inherits from a_class (but not if it's exactly a_class).
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
