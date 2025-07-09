#!/usr/bin/python3
"""7-rectangle module
Adds a flexible print_symbol to Rectangle class.
"""


class Rectangle:
    """Represents a rectangle.

    Class attributes:
        number_of_instances (int): Counts active Rectangle objects.
        print_symbol (any): Symbol used for the string representation.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle; increment instance counter."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    # ---------- width property ----------
    @property
    def width(self):
        """Retrieve the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    # ---------- height property ----------
    @property
    def height(self):
        """Retrieve the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    # ---------- public instance methods ----------
    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle.
        If ei
