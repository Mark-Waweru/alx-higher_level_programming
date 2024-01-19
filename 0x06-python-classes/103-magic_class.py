#!/usr/bin/python3
'''Defines a MagicClass matching the bytecode provided by ALX.'''

import math


class MagicClass:
    '''This is a Magic Class that represent a circle.

    Attributes:
        radius (int or float): The radius of the circle.
    '''
    def __init__(self, radius=0):
        '''Initializes an object with a radius.

        Args:
            radius (int or float): The radius of the circle.
        '''
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        '''Gets the Area of the object.

        Returns:
            The area of the object.
        '''
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        '''Gets the Circumference of the object.

        Returns:
            The Circumference of the object.
        '''
        return (2 * math.pi * self.__radius)
