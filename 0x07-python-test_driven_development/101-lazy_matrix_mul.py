#!/usr/bin/python3
"""module for matrix multiplication function using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of 2 matrix"""

    return (np.matmul(m_a, m_b))
