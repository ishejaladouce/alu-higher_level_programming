#!/usr/bin/python3
"""
Module that defines a BaseGeometry class with an area method.
"""


class BaseGeometry:
    """
    BaseGeometry class with an area method that
    raises an exception because it's not implemented.
    """

    def area(self):
        """
        Raises an Exception to indicate
        that the area method is not implemented.
        """
        raise Exception("area() is not implemented")
