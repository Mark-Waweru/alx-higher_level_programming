#!/usr/bin/python3
'''This module has a function tha creates an object from a JSON file'''
import json


def load_from_json_file(filename):
    '''Creates an object from a "JSON file"

    Args:
        filename (object): The file to get the JSON string from

    Returns:
        my_obj (object): The desirialized string
    '''
    with open(filename, encoding="UTF-8") as my_file:
        my_obj = json.load(my_file)
        return my_obj
