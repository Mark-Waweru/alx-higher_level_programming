#!/usr/bin/python3
'''Contains a function that checks if an object  is an instance
of a class that inherited (directly or indirectly)
rom the specified class '''


def inherits_from(obj, a_class):
    '''Checks  if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class

    Args:
        obj (object): The object to be checked
        a_class (class): The class to check if the object is an instance of it

    Returns:
        bool: True if the object  is an instance of a class that inherited
        (directly or indirectly) from the specified class or False if not
    '''
    return isinstance(obj, a_class) and type(obj) != a_class
