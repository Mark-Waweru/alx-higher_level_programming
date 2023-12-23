#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    print_matrix_integer - prints a matrix of integers
    @matrix: The matrix list to print

    Return: None
    """
    for row in matrix:
        for i, element in enumerate(row):
            print("{:d}".format(element), end="")
            if i < len(row) - 1:
                print(" ", end="")

        print()
