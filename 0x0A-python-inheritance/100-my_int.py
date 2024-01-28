#!/usr/bin/python3
'''This module contains a class called Myint '''


class MyInt(int):
    '''This is a subclass called Myint whose parent is int'''
    def __init__(self, value):
        '''Initializes the object with a value which is an integer

        Args:
            value (int): The value to set the object with

        Raises:
            TypeError: If the value is not an integer
        '''
        if isinstance(value, int):
            self.__num = value
        else:
            raise TypeError("{} is not an integer".format(value))

    def __str__(self):
        '''Returns the number of the object

        Returns:
            The number of the object'''
        return "{}".format(self.__num)

    def __eq__(self, other):
        '''This function returns not equal which is the opposite of equal

        Returns:
            bool: True if not equal and False if equal
        '''
        return self.__num != other

    def __ne__(self, other):
        '''This function returns equal which is the opposite of not equal

        Returns:
            bool: True if equal and False if not equal
        '''
        return self.__num == other
