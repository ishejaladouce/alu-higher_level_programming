#!/usr/bin/python3
"""
This module defines a subclass MyList that inherits from list.
"""


class MyList(list):
    """
    MyList is a subclass of list with an additional method
    to print the list sorted.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order without modifying
        the original list.
        """
        print(sorted(self))
