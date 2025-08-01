#!/usr/bin/python3
"""
Lazy matrix multiplication module using NumPy.

This module defines a function that multiplies two matrices using NumPy's matmul.
It handles and raises clear error messages if the inputs are invalid.
"""

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a (list of lists): The first matrix to multiply.
        m_b (list of lists): The second matrix to multiply.

    Returns:
        numpy.ndarray: The result of the multiplication.

    Raises:
        ValueError: If matrices can't be multiplied or input is invalid.

    Examples:
        >>> lazy_matrix_mul([[1, 2]], [[3], [4]])
        array([[11]])

        >>> lazy_matrix_mul([[1, 2, 3]], [[1], [2], [3]])
        array([[14]])

        >>> lazy_matrix_mul([1, 2, 3], [[1, 2]])
        Traceback (most recent call last):
        ValueError: matmul: Input operand 1 has a mismatch in its core dimension ...

        >>> lazy_matrix_mul([[1, 2]], [1, 2, 3])
        Traceback (most recent call last):
        ValueError: matmul: Input operand 0 has a mismatch in its core dimension ...
    """
    try:
        return np.matmul(m_a, m_b)
    except (ValueError, TypeError) as e:
        # Reraise the exact error message to help with debugging and testing
        raise ValueError(str(e))
