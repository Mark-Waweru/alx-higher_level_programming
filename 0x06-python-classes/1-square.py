#!/usr/bin/python3
'''This module contains a square class with some methods for manipulating it.
'''


class Square:
    '''This is a square class which manipulates the square mathematics shape.

    Attributes:
        size (int): This is the size of the square.
    '''
    def __init__(self, size):
        '''This function initializes the size of a square instance object.

        Args:
            size (int): This is the size of the square.
        '''
        self.__size = size
