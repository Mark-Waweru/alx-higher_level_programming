#!/usr/bin/python3
'''This module creates a class that has one method `to_json`'''


class Student:
    '''This is a Student class

    Attributes:
        first_name (str): The first name of the student object
        last_name (str): The last name of the student object
        age (int): The age of the student aobject
    '''
    def __init__(self, first_name, last_name, age):
        '''Initializes the objects with three attributes:-
        first_name, last_name and age

        Args:
            first_name (str): The first name of the student object
            last_name (str): The last name of the student object
            age (int): The age of the student aobject
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Gest the dictionary representation of a Student object

        Args:
            attrs (list): A list of the attributes to return

        Raises:
            TypeError: The argument must be a list containing strings
            TypeError: The list must contain only strings

        Returns:
             a dictionary representation of a Student object
        '''
        if isinstance(attrs, list) and all(type(attr) == str for attr in attrs):

            return {k: getattr(self, k)for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        '''replaces all attributes of the Student instance

        Args:
            json (dic): A dictionary
        '''
        for key, value in json.items():
            try:
                setattr(self, key, value)
            except FileNotFoundError:
                pass
