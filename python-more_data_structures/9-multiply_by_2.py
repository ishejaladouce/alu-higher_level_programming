#!/usr/bin/python3
"""9-multiply_by_2
Return a new dictionary with each value doubled.
"""


def multiply_by_2(a_dictionary):
    """Return a new dict with every value × 2."""
    return {k: v * 2 for k, v in a_dictionary.items()}
