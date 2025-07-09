#!/usr/bin/python3
"""6-square
Square class with size and position properties plus offset printing.
"""


class Square:
    """Represent a square with size and position offsets."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a Square.

        Args:
            size (int): Side length (default 0).
            position (tuple): Two positive ints for print offset
                              (default (0, 0)).
        """
        self.size = size
        self.position = position

    # -------- size property --------
    @property
    def size(self):
        """Return the square size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    # -------- position property --------
    @property
    def position(self):
        """Return the position tuple."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position with validation."""
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(n, int) for n in value) or
            not all(n >= 0 for n in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    # -------- public methods --------
    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with '#' taking position into account."""
        if self.__size == 0:
            print()
            return

        # vertical offset
        for _ in range(self.__position[1]):
            print()

        # each row with horizontal offset
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
