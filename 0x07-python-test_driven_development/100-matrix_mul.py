#!/usr/bin/python3
"""Module name: 100-matrix_mul.py
multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """
    multiplies 2 matrices.

    Raises:
        TypeError: If m_a or m_b is not a list, not a list of lists,
            or contains non-integer/float values.
        ValueError: If m_a or m_b is empty, or if m_a and m_b
        cannot be multiplied.
        TypeError: If m_a and m_b are not rectangular.
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")

    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")

    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or any(len(row) == 0 for row in m_a):
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or any(len(row) == 0 for row in m_b):
        raise ValueError("m_b can't be empty")

    if not all(isinstance(value, (int, float))
                for row in m_a
                for value in row):
        raise TypeError("m_a should contain only integers or floats")

    if not all(isinstance(value, (int, float))
                for row in m_b
                for value in row):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
