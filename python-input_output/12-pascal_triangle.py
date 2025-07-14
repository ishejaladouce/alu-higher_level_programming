#!/usr/bin/python3
"""
Module that contains the function pascal_triangle(n)
which returns Pascal's triangle as a list of lists.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    the Pascal's triangle of n.

    Args:
        n (int): Number of rows of the triangle

    Returns:
        list: Pascal's triangle represented as a list of lists
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        prev_row = triangle[i - 1]
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)
        triangle.append(row)

    return triangle
