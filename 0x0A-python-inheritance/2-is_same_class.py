#!/usr/bin/python3
'''Contains a function for cheking the instance of an objects class
'''


def is_same_class(obj, a_class):
    '''Checks the instance of an object
    This function is like the isinstance()

    Args:
        obj (object): The object to be checked
        a_class (class): The class to check if the object is an instance of it

    Returns:
        bool: True if the object is an instance of a_class or False if not
    '''
    return type(obj) == a_class
