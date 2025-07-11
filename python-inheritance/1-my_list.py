#!/usr/bin/python3
"""
This module defines a class MyList that inherits from list.
"""


class MyList(list):
    """
    Represents a list subclass with an additional method
    to print the list sorted in ascending order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order without
        modifying the original list. Returns the sorted list.
        """
        sorted_list = sorted(self)
        print(sorted_list)
        return sorted_list

    def __str__(self):
        """
        Returns the string representation of the list.
        """
        return super().__str__()
