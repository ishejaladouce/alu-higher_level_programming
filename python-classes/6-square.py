#!/usr/bin/python3
"""6‑square
Square class with position offset for printing.
"""


class Square:
    """Represent a square with controlled size and printable offset."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a Square.

        Args:
            size (int, optional): Length of a side. Defaults to 0.
            position (tuple, optional): (x, y) offset. Defaults to (0, 0).
        """
        self.size = size          # delegate validation to setter
        self.position = position  # delegate validat
