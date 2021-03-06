#!/usr/bin/python3
""" matrix_divided divides the given matrix
by the parameter "div", and returns the divided matrix
"""


def matrix_divided(matrix, div):
    """ Divides all elements of a matrix by "div"
    checks if the arguments in matrix are int/float
    checks if the two list have the same size
    checks if "div" is an int/float or is 0
    """
    matrix_u = "matrix must be a matrix (list of lists) of integers/floats"
    rows = "Each row of the matrix must have the same size"
    result_matrix = []

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for lists in matrix:
        if len(lists) != len(matrix[0]):
            raise TypeError(rows)
        inner_list = []
        for items in lists:
            if not isinstance(items, (int, float)):
                raise TypeError(matrix_u)
            else:
                inner_list.append(round(items / div, 2))
        result_matrix.append(inner_list)

    return result_matrix
