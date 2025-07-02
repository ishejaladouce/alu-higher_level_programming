#!/usr/bin/python3
"""0-square_matrix_simple
Computes the square of every integer in a 2‑D matrix.
"""

def square_matrix_simple(matrix=[]):
    """Return a new matrix with each value squared.

    Args:
        matrix (list[list[int]]): Original 2‑D matrix of integers.

    Returns:
        list[list[int]]: New matrix of the same size with squared values.
    """
    # Create a new matrix using a nested list‑comprehension; keeps
    # original matrix intact (no in‑place modification).
    return [[value ** 2 for value in row] for row in matrix]


if __name__ == "__main__":
    # Simple self‑test
    sample = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(square_matrix_simple(sample))
