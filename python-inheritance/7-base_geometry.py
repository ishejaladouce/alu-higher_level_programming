#!/usr/bin/python3
"""
Module that defines a BaseGeometry class with area and
integer_validator methods.
"""


class BaseGeometry:
    """
    BaseGeometry class with an area method and integer validator.
    """

    def area(self):
        """
        Raises an Exception to indicate
        that the area method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that 'value' is an integer greater than 0.

        Args:
            name (str): The name of the parameter (for error messages).
            value (any): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
