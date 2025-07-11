#!/usr/bin/python3
"""
Module that defines a rebel integer class MyInt.
"""


class MyInt(int):
    """
    MyInt inherits from int but inverts == and !=.
    """

    def __eq__(self, other):
        """Invert == operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Invert != operator."""
        return super().__eq__(other)
