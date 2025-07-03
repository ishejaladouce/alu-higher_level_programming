#!/usr/bin/python3
"""2-safe_print_list_integers
Print first x elements that are integers.
"""


def safe_print_list_integers(my_list=[], x=0):
    """Print digits among the first *x* items, return how many were printed."""
    count = 0
    for i in range(x):           # May raise IndexError — expected by task
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            pass
    print()
    return count
