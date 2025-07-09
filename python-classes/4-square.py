#!/usr/bin/python3
"""4‑square
Square class with size property (getter / setter) and area method.
"""


class Square:
    """Represent a square with controlled access to its size."""

    def __init__(self, size=0):
        """Initialize a Square.

        Args:
            size (int, optional): Length of a side. Defaults to 0.
        """
        self.size = size  # leverage the setter for validation

    @property
    def size(self):
        """int: Current size of the square (private)."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set square size with validation.

        Args:
            value (int): New size value.

        Raises:
            TypeError: If value is not an int.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2
