#!/usr/bin/python3
'''This module is a script that adds all arguments to a Python list
    and then save them to a file

Attributes:
    json_list (list): The list to add the arguments to
    filename (object): The file to save the list to
    arg (object): The arguments to add to the list
    arguments (object): All the arguments given
'''
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    filename = "add_item.json"
    arguments = argv[1:]

    try:
        json_list = load_from_json_file(filename)
    except FileNotFoundError:
        json_list = []

    for arg in arguments:
        json_list.append(arg)

    save_to_json_file(json_list, filename)
