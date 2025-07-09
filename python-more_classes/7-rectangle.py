#!/usr/bin/python3
"""7-rectangle module.

Defines class Rectangle with dynamic string symbol and
instance counter.
"""


class Rectangle:
    """Represents a rectangle.

    Class attributes
    ----------------
    number_of_instances : int
        Counts active Rectangle objects.
    print_symbol : any
        Symbol used when the rectangle is printed. Converted to str().
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Create a rectangle and increment instance counter."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    # -------- width --------
    @property
    def width(self):
        """Width getter."""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    # -------- height --------
    @property
    def height(self):
        """Height getter."""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    # -------- public ops --------
    def area(self):
        """Return the area."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter (0 if either side is 0)."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    # -------- str / repr --------
    def __str__(self):
        """Return a printable rectangle of `print_symbol` characters."""
        if self.__width == 0 or self.__height == 0:
            return ""
        sym = str(self.print_symbol)
        line = sym * self.__width
        return "\n".join(line for _ in range(self.__height))

    def __repr__(self):
        """Return eval‑friendly string."""
        return f"Rectangle({self.__width}, {self.__height})"

    # -------- destructor --------
    def __del__(self):
        """On destruction, print message and decrement counter."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
