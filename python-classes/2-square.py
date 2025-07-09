#!/usr/bin/python3
"""2‑square
Square class with validated private size.
"""


class Square:
    """Represent a square with a validated size."""

    def __init__(self, size=0):
        """Initialize a Square.

        Args:
            size (int, optional): Length of a side. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size  # private attribute
