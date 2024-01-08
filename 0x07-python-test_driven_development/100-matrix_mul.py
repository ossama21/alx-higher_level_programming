#!/usr/bin/python3
"""
This module contain a function that multiplies two matrixes
"""


def matrix_mul(m_a, m_b):
    """matrix_mul function that multiplies two matrix
    Args:
        m_a (list of lists): first matrix
        m_b (list of lists): second matrix
    """
    """check if matrixes are of type list"""
    if type(m_a) is not list:
        raise TypeError('m_a must be a list')
    if type(m_b) is not list:
        raise TypeError('m_b must be a list')

    """check if matrixes are empty"""
    if m_a == [] or m_a == [[]]:
        raise ValueError('m_a can\'t be empty')
    if m_b == [] or m_b == [[]]:
        raise ValueError('m_b can\'t be empty')

    """other requirements checks for m_a"""
    for row in m_a:
        if type(row) is not list:
            raise TypeError('m_a must be a list of lists')
        if len(row) != len(m_a[0]):
            raise TypeError('each row of m_a must be of the same size')
        for col in row:
            if type(col) not in (int, float):
                raise TypeError('m_a should contain only integers or floats')

    """other requirements checks for m_a"""
    for row in m_b:
        if type(row) is not list:
            raise TypeError('m_b must be a list of lists')
        if len(row) != len(m_b[0]):
            raise TypeError('each row of m_b must be of the same size')
        for col in row:
            if type(col) not in (int, float):
                raise TypeError('m_b should contain only integers or floats')

    if len(m_a[0]) != len(m_b):
        raise ValueError('m_a and m_b can\'t be multiplied')

    mul_matrix = []

    for row_a in m_a:
        length = 0
        l_row = []
        while length < len(m_b[0]):
            result = 0
            k = 0
            for item in row_a:
                result += item * m_b[k][length]
                k += 1
            l_row.append(result)
            length += 1
        mul_matrix.append(l_row)

    return mul_matrix
