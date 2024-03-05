#!/usr/bin/python3
'''This module has a function which desirializes a JSON string to an object
(Python data structure)'''
import json


def from_json_string(my_str):
    '''Desirializes a JSON string to an object(Python data strucuter)

    Args:
        my_str (str): The string to desirialize to a python object

    Returns:
        my_obj (object): The string that was desirialized to an object'''
    my_obj = json.loads(my_str)
    return my_obj
