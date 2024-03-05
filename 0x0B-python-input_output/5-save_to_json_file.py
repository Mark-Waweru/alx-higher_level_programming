#!/usr/bin/python3
'''This module has a function that serializes an object to a text file using
JSON'''
import json


def save_to_json_file(my_obj, filename):
    '''Serializes an object to a text file

    Args:
        my_obj (object): The object to serialize
        filename (object): The file to store the JSON string
    '''
    with open(filename, mode="w", encoding="UTF-8") as my_file:
        json.dump(my_obj, my_file)
