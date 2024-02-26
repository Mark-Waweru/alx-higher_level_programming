#!/usr/bin/python3
'''This module has a function that prints a square'''


def print_square(size):
    '''Prints a square with the character "#"

    Args:
        size (int): The size of the square

    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
    '''
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size < 0 and isinstance(size, float):
        raise TypeError("size must be an integer")

    for width in range(0, size):
        for length in range(0, size):
            print("#", end="")
        print()
