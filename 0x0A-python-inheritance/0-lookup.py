#!/usr/bin/python3
'''This module contains a function for retriving all the content of a class
'''


def lookup(obj):
    '''Returns a list of available attributes and methods of an object

    Args:
        obj (object): The object being loooked at

    Returns:
        (list): The list of  attributes and methods of the object
    '''
    return [dir(obj)]
