#!/usr/bin/python3
"""2-uniq_add
Sum all unique integers in a list.
"""


def uniq_add(my_list=[]):
    """Return the sum of unique integers in *my_list*.

    Args:
        my_list (list[int]): List that may contain duplicates.

    Returns:
        int: Sum of each distinct integer exactly once.
    """
    return sum(set(my_list))
