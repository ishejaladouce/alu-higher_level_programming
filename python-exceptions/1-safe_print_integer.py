#!/usr/bin/python3
"""1-safe_print_integer
Safely print an integer using {:d}.format().
"""


def safe_print_integer(value):
    """Print *value* as integer.

    Returns:
        bool: True if printed (value is an int), else False.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
