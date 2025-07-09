#!/usr/bin/python3
"""5-rectangle module
Defines a Rectangle class that announces its deletion.
"""


class Rectangle:
    """Represents a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle."""
        self.width = width
        self.height = height

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
        If either dimension is zero, perimeter is zero.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    # ---------- string / repr ----------
    def __str__(self):
        """Return the rectangle as a string of '#' characters."""
        if self.__width == 0 or self.__height == 0:
            return ""
        line = "#" * self.__width
        return "\n".join(line for _ in range(self.__height))

    def __repr__(self):
        """Return a string that can recreate the instance via eval()."""
        return f"Rectangle({self.__width}, {self.__height})"

    # ---------- destructor ----------
    def __del__(self):
        """Print a message when the instance is deleted."""
        print("Bye rectangle...")
