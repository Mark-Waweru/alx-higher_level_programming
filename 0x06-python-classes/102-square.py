#!/usr/bin/python3
'''This module contains a square class with some methods for manipulating it.
'''


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
            ValueError: if size is less than zero.
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def size(self):
        '''This function is used to get or access the size of the square.

        Returns:
            (int): The size of the square.
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''This function is used for setting the size of the square.

        Args:
            value (int): This is the value to set the size of the square.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than zero.
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        '''This function gets the area of a square object

        Returns:
            int: The area of the square.
        '''
        return self.__size * self.__size

    def __gt__(self, other):
        '''Checks for the greater than btwn two objects.

        Returns:
            (bool): True or False.
        '''
        return self.area() > other.area()

    def __eq__(self, other):
        '''Checks for equality btwn two objects.

        Returns:
            (bool): True or False.
        '''
        return self.area() == other.area()

    def __ne__(self, other):
        '''Checks for non equality btwn two objects.

        Returns:
            (bool): True or False.
        '''
        return self.area() != other.area()

    def __ge__(self, other):
        '''Checks for the greater than or equal btwn two objects.

        Returns:
            (bool): True or False.
        '''
        return self.area() >= other.area()

    def __lt__(self, other):
        '''Checks for the less than  btwn two objects.

        Returns:
            (bool): True or False.
        '''
        return self.area() < other.area()

    def __le__(self, other):
        '''Checks for the less than or equal btwn two objects.

        Returns:
            (bool): True or False.
        '''
        return self.area() <= other.area()
