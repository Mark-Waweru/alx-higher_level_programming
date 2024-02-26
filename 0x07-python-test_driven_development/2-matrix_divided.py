#!/usr/bin/python3
'''This module has a function that divides all elements of a matrix'''


def matrix_divided(matrix, div):
    '''Divides all elements of a matrix
    Args:
        matrix (list): This is a matrix of (list of lists)
        div (int, float): This is the divider number

    Raises:
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        TypeError: Each row of the matrix must have the same size
        TypeError: div must be a number
        ZeroDivisionError: division by zero

    Returns:
        list: A matrix result of the divided elements
    '''
    err_msg = "matrix must be a matrix(list of lists) of integers/floats"

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError(err_msg)

    for row in matrix:
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError(err_msg)

    row_length = set(len(row) for row in matrix)
    if len(row_length) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for elem in row:
            new_elem = round(elem / div, 2)
            new_row.append(new_elem)
        new_matrix.append(new_row)

    return new_matrix
