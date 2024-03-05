#!/usr/bin/python3
'''This module has a function that performs a JSON representation of an object
'''
import json


def to_json_string(my_obj):
    '''Performs serialization of an obj to json string

    Args:
        my_obj (object): The object to serialize to JSON string

    Returns:
        ser_obj (str): The JSON string representation'''
    ser_obj = json.dumps(my_obj)
    return ser_obj
