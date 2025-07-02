#!/usr/bin/python3
"""3-common_elements
Return a set containing only elements present in both input sets.
"""


def common_elements(set_1, set_2):
    """Compute the intersection of two sets.

    Args:
        set_1 (set): First input set.
        set_2 (set): Second input set.

    Returns:
        set: Elements common to both sets.
    """
    return set_1 & set_2
