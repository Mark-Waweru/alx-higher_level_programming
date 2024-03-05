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

    def to_json(self):
        '''Gest the dictionary representation of a Student object

        Returns:
             a dictionary representation of a Student object'''
        return self.__dict__
