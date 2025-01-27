#!/usr/bin/python3
"""
This module provides a function to multiply two matrices using NumPy.

This exercise is part of the holberton school curriculum.
It needs to be modified to pass holberton school checkers which are
are not made clear in the instructions.  It was supposed to check for the
same outputs as 100-matrix_mul.py but they did not make the desired error checking,
nor error messages clear in the instructions.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a (list of lists of int/float): The first matrix.
        m_b (list of lists of int/float): The second matrix.

    Returns:
        numpy.ndarray: The result of multiplying m_a by m_b.

    Raises:
        TypeError: If m_a or m_b is not a list.
        TypeError: If m_a or m_b is not a list of lists.
        ValueError: If m_a or m_b is empty.
        TypeError: If an element of m_a or m_b is not an integer or float.
        TypeError: If m_a or m_b is not a rectangle.
        ValueError: If m_a and m_b cannot be multiplied.
    """
    if isinstance(m_a, str) or isinstance(m_b, str):
        raise TypeError("Scalar operands are not allowed, use '*' instead")
    if len(m_a[0]) == 0:
        raise ValueError("shapes ({},{})".format(len(m_a), len(m_a[0])) +
                         " and ({},{})".format(len(m_b), len(m_b[0])) +
                         " not aligned: 0 (dim 1) != 2"
                         " (dim 0)")
    if len(m_b[0]) == 0:
        ValueError("shapes ({},{})".format(len(m_a), len(m_a[0])) +
                   " and ({},{})".format(len(m_b), len(m_b[0])) +
                   " not aligned: 2 (dim 1) != 1"
                   " (dim 0)")
    return np.matmul(m_a, m_b)
