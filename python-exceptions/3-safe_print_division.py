#!/usr/bin/python3
"""3-safe_print_division
Divide two integers and print the result safely.
"""


def safe_print_division(a, b):
    """Divide a by b, print result in finally.

    Return result or None if error.
    """
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
