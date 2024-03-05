#!/usr/bin/python3
'''This module has a function which returns the dictionary
description with simple data structure'''


def class_to_json(obj):
    ''' returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object

    Args:
        obj (object): The object to serialize

    Returns:
        dict: The dictionary description of the object
    '''
    return obj.__dict__
