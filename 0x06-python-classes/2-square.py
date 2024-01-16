#!/usr/bin/python3
class Square:
    '''This is a square class which maniplates the square mathematics shape.

    Attributes:
        size (int): This is the size of the square.
    '''
    def __init__(self, size=0):
        '''This function initializes the size of a square instance object.

        Args:
            size (int): This is the size of the square.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if isze is less than zero.
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
