#!/usr/bin/python3
"""6-square
Defines a Square class with size and position properties, and prints the square with offsets.
"""


class Square:
    """Represent a square with size and position attributes."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size (int): Length of a side (default 0).
            position (tuple): Tuple of two positive integers for printing offset (default (0, 0)).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with validation.

        Raises:
            TypeError: if size is not an int.
            ValueError: if size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position with validation.

        Raises:
            TypeError: if position is not a tuple of 2 positive integers.
        """
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(n, int) for n in value)
            or not all(n >= 0 for n in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with '#' respecting position offset.

        Prints an empty line if size is 0.
        """
        if self.__size == 0:
            print()
            return

        # Print vertical offset (newlines)
        for _ in range(self.__position[1]):
            print()

        # Print each line of the square with horizontal offset (spaces)
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
