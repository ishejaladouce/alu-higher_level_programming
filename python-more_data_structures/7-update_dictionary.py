#!/usr/bin/python3
"""7-update_dictionary
Replace or add a key/value pair in a dictionary and return it.
"""


def update_dictionary(a_dictionary, key, value):
    """Insert *key* with *value* or overwrite existing entry.

    Args:
        a_dictionary (dict): The dictionary to modify.
        key (str): Key to add or update.
        value: Value to associate with *key*.

    Returns:
        dict: The same dictionary, updated in place.
    """
    a_dictionary[key] = value
    return a_dictionary
