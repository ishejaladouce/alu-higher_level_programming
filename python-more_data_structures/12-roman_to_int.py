#!/usr/bin/python3
"""12-roman_to_int
Convert a Roman numeral to an integer (1 – 3999).
"""


def roman_to_int(roman_string):
    """Return integer value of *roman_string* or 0 on invalid input."""
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    roman_vals = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}

    total = 0
    prev = 0
    for c in reversed(roman_string.upper()):
        value = roman_vals.get(c, 0)
        if value < prev:
            total -= value
        else:
            total += value
            prev = value
    return total
