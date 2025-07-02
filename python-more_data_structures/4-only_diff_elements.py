#!/usr/bin/python3
"""4-only_diff_elements
Return a set of elements present in exactly one of the two input sets.
"""


def only_diff_elements(set_1, set_2):
    """Compute the symmetric difference of two sets.

    Args:
        set_1 (set): First input set.
        set_2 (set): Second input set.

    Returns:
        set: Elements that appear in *either* set but not in both.
    """
    return set_1 ^ set_2
