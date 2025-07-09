#!/usr/bin/python3
"""3‑square
Square class that validates size and computes its area.
"""


class Square:
    """Represent a square with size validation and area method."""

    def __init__(self, size=0):
        """Initialize a Square.

        Args:
            size (int, optional): Length of a side. Defaults to 0.

        Raises:
            TypeError: If size is not an int.
            ValueError: If size is negative.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2
