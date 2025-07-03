#!/usr/bin/python3
"""8-simple_delete
Delete a key from a dictionary if it exists.
"""


def simple_delete(a_dictionary, key=""):
    """Remove *key* from *a_dictionary* if present, then return the dict."""
    a_dictionary.pop(key, None)
    return a_dictionary
