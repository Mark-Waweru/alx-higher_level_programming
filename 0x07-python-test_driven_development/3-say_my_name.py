#!/usr/bin/python3
'''This module has a function that prints first and last name'''


def say_my_name(first_name, last_name=""):
    '''Prints "My name is <first name> <last name>"
    Args:
        first_name (string): Your first name
        last_name (string): Your last name

    Raises:
        TypeError: first_name must be a string
        TypeErro: last_name must be a stringr
    '''
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
