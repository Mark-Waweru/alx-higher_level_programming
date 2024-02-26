#!/usr/bin/python3
'''This module has a function add_integer that adds 2 integers.'''


def add_integer(a, b=98):
    '''This function adds 2 integers

    Args:
        a (int): The first argument to add
        b (int): The second argument to be added

    Raises:
        TypeError: a must be an integer
        TypeError: b must be an integer

    Returns:
        int The sum or addition of a and b
    '''
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return (a + b)
