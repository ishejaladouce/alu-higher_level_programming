#!/usr/bin/python3
"""1-search_replace
Return a new list where every occurrence of a given element
is replaced by another.
"""


def search_replace(my_list, search, replace):
    """Replace all occurrences of *search* by *replace* in *my_list*.

    The original list is **not** modified.

    Args:
        my_list (list): Original list.
        search: Element to look for.
        replace: Element to substitute.

    Returns:
        list: New list with replacements applied.
    """
    return [replace if elem == search else elem for elem in my_list]
