#!/usr/bin/python3
"""function that divides all element of a matrix"""


def matrix_divided(matrix, div):
    """function responsible for the operation.

    Args:
        matrix: matrix to be diveded.
        div: number to divide the matrix.
    
    Return: new matrix after division.
    """
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    len_row = len(matrix[0])
    for row in matrix:
        if len_row != len(row):
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for row in matrix:
        result = [round(item / div, 2) for item in row]
        new_matrix.append(result)
    return new_matrix
