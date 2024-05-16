#!/usr/bin/python3
'''This module contains a Base class that will be the base of other classes'''


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
