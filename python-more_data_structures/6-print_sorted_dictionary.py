#!/usr/bin/python3
"""6-print_sorted_dictionary
Print dictionary items sorted by key.
"""


def print_sorted_dictionary(a_dictionary):
    """Print dictionary's key-value pairs sorted by keys.

    Args:
        a_dictionary (dict): Input dictionary with string keys.

    Returns:
        None: Prints directly.
    """
    for key in sorted(a_dictionary):
        print(f"{key}: {a_dictionary[key]}")
