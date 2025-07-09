#!/usr/bin/python3
"""8-rectangle module.

Extends Rectangle with area comparison via static method.
"""


class Rectangle:
    """Represents a rectangle.

    Class attributes
    ----------------
    number_of_instances : int
        Counts active Rectangle objects.
    print_symbol : any
        Symbol used when printing the rectangle (converted to str).
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Create a rectangle; increment instance counter."""
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
        """Return the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter (0 if either side is 0)."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    # -------- str / repr --------
    def __str__(self):
        """Return printable rectangle built with print_symbol."""
        if self.__width == 0 or self.__height == 0:
            return ""
        sym = str(self.print_symbol)
        line = sym * self.__width
        return "\n".join(line for _ in range(self.__height))

    def __repr__(self):
        """Return eval‑friendly string representation."""
        return f"Rectangle({self.__width}, {self.__height})"

    # -------- destructor --------
    def __del__(self):
        """Print message and decrement counter on deletion."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    # -------- static method --------
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the rectangle with the larger area.

        If areas are equal, return rect_1.

        Parameters
        ----------
        rect_1 : Rectangle
        rect_2 : Rectangle

        Raises
        ------
        TypeError
            If rect_1 or rect_2 is not an instance of Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1
