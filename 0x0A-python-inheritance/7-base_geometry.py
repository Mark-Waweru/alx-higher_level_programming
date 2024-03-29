#!/usr/bin/python3
'''Contains class called BaseGeometry'''


class BaseGeometry:
    '''A class called BaseGeometry'''
    def area(self):
        '''A public instance method that raises an exception

        Raises:
            Exception: Area() is not implemented
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''Validates value

        Args:
            name (string): A name of the value to be passed
            value (int): An integer value number

        Raises:
            TypeError: When the value is not an integer
            ValueError: When the value is less or equal to 0
        '''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
