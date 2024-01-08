#!/usr/bin/python3
"""
This is the "2-matrix_divided" module.
The 2-matrix_divided module supplies one function, matrix_divided(matrix, div).
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix"""
    length = len(matrix[0])
    new_matrix = []

    if type(div) not in (float, int):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    msg = 'matrix must be a matrix (list of lists) of integers/floats'
    for item in matrix:
        if len(item) != length:
            raise TypeError('Each row of the matrix must have the same size')
        if type(item) is not list:
            raise TypeError(msg)
        for i in item:
            if type(i) not in (float, int):
                raise TypeError(msg)

    for item in matrix:
        row = []
        for i in item:
            row.append(round(i / div, 2))
        new_matrix.append(row)
    return new_matrix
