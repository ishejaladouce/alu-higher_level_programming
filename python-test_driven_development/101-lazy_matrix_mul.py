#!/usr/bin/python3
"""
Module for lazy matrix multiplication using NumPy
"""
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using NumPy

    Args:
        m_a: list of lists of integers/floats
        m_b: list of lists of integers/floats

    Returns:
        A new matrix that is the product of m_a and m_b
    """
    return np.matmul(m_a, m_b)

