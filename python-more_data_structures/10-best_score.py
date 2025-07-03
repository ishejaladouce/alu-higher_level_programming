#!/usr/bin/python3
"""10-best_score
Return the key with the highest integer value in a dictionary.
"""


def best_score(a_dictionary):
    """Return key of max value, or None if dict is empty / None."""
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)
