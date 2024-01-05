#!/usr/bin/python3
"""
This module contains 2-matrix_divided.
It divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """This function divides all elements of a matrix.
    Args:

        matrix (list of lists): the matrix to be divided.
        div (int or float): the divisor to divide the matrix.

    Return:
        new_matrix (list of lists): returns the new list created.

    Raises:
        TypeError: matrix must be a matrix (list of lists) of integers/floats.
        ZeroDivisionError: If `div` is zero.
    """
    new_matrix = []

    if type(matrix) is not list or len(matrix) is 0:
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
                )

    row_size = len(matrix[0])
    for row in matrix:
        if type(row) is not list or len(row) is 0:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
                )

        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
        for i in row:
            if type(i) is not int and type(i) is not float:
                raise TypeError(
                    "matrix must be a matrix (list of lists) "
                    "of integers/floats"
                    )

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div is 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(i / div, 2) for i in row] for row in matrix]

    return new_matrix
