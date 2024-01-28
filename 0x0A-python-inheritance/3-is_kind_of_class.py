#!/usr/bin/python3
'''Contains a function that checks if an object is an instance of or
a class that inherited from'''


def is_kind_of_class(obj, a_class):
    '''checks if an object is an instance of or a class that inherited from

    Args:
        obj (object): The object to be checked
        a_class (class): The class to check if the object is an instance of it

    Returns:
        bool: True if the object is an instance of or a class that inherited
        from or False if not
    '''
    return isinstance(obj, a_class)
