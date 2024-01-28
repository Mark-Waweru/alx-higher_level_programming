#!/usr/bin/python3
'''This module has a function that adds a new attribute to a class'''


def add_attribute(obj, att_name, att_value):
    '''Adds a new attribute to a class

    Args:
        obj (object): The object to add its attribute
        att_name (string): The name of the attribute
        att_value (int, string, float): The new attribute value
    '''
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, att_name, att_value)
