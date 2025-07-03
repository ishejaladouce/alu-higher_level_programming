#!/usr/bin/python3
"""0-safe_print_list
Print up to x elements of a list, safely.
"""


def safe_print_list(my_list=[], x=0):
    """Print first x elements of *my_list* and return how many were printed."""
    count = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            count += 1
        except IndexError:
            break
    print()
    return count
