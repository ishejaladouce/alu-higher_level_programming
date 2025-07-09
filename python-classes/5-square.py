#!/usr/bin/python3
"""5‑square
Square class with size property, area, and printable representation.
"""


class Square:
    """Represent a square with controlled size and printable form."""

    def __init__(self, size=0):
        """Initialize a Square.

        Args:
            size (int, optional): Length of a side. Defaults to 0.
        """
        self.size = size  # validation through the setter

    @property
    def size(self):
        """int: Current size of the square (private)."""
        return self.__size

    @size.setter
    def size(self, value):
        """Validate and set size.

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

    def my_print(self):
        """Print the square with '#' characters; empty line if size is 0."""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print("#" * self.__size)
