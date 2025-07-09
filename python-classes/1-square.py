#!/usr/bin/python3
"""1‑square
Adds a private size attribute to the Square class.
"""


class Square:
    """Represent a square with a private size."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int/float/any): Size of the square’s side.
                No type or value checks here (handled in later tasks).
        """
        self.__size = size  # private on purpose → _Square__size
