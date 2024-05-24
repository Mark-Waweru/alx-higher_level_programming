#!/usr/bin/python3
'''This module contains a Base class that will be the base of other classes'''
import json


class Base():
    '''This is a base class for other classes in python_as_a_circle project

    Attributes:
        __nb_objects (int): Contains the number of objects in this class
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''This is a initialization function which initializes objects with a
        new id

        Args:
            id (int): The id of a new object initialized
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Returns the json string representation of list_dictionaries

        Returns:
            str: An empty string if argument is None or Empty
            str: json string representation of list_dictionaries
        '''
        if list_dictionaries is None or not list_dictionaries:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''writes the JSON string representation of list_objs to a file
        '''
        filename = f"{cls.__name__}.json"
        with open(filename, 'w', encoding = 'utf-8') as my_file:
            if list_objs is None:
                json.dump([], my_file)
            else:
                json.dump([cls.to_json_string(obj) for obj in list_objs], my_file)
