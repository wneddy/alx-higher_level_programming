#!/usr/bin/python3
"""module to multiply two matrixes"""


def matrix_mul(m_a, m_b):
    """function to do the process"""
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    elif not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    elif not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    elif not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    elif m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    elif m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for row in m_a:
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_a):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    invertedMatrixb = [
            [m_b[row][column] for row in range(len(m_b))]
            for column in range(len(m_b[0]))
            ]

    newMatrix = []
    for row in m_a:
        n_row = []
        for column in invertedMatrixb:
            result = sum(i * j for i, j in zip(row, column))
            n_row.append(result)
        newMatrix.append(n_row)
    return newMatrix
