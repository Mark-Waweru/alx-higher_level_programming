#!/usr/bin/python3
'''This module contains a class Square that inherits from the
Rectangle class'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''A Square class that inherits from class Rectangle'''
    def __init__(self, size, x=0, y=0, id=None):
        '''Initializes all objects of square with the following attributes

        Args:
            size (int): The size of the Square object
            x (int): The x coordinates of the square object
            y (int):cThe y coordinate of the square object
            id (int): The identification number of the square object
        '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''This function prints [Square] (<id>) <x>/<y> - <size>

        Returns:
            str: [Square] (<id>) <x>/<y> - <size>
        '''
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__, self.id,
                self.x, self.y, self.width)

    @property
    def size(self):
        '''This function returns the size of the square object

        Return:
            size (int): The size of the square object
        '''
        return self.width

    @size.setter
    def size(self, value):
        '''This function assigns new values to the size of the square
        object

        Args:
            Value (int): The new size of the square

        Raises:
            TypeError: width must be an integer
            ValueError: width must be > 0
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''Assigns an argument to each attribute

        Args:
            args (int): Multiple arguments

        Raises:
            TypeError: <name of the attribute> must be an integer
            ValueError: <name of the attribute> must be > 0

        Returns:
            None
        '''
        if len(args) == 0 and kwargs:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    if not isinstance(v, int):
                        raise TypeError("width must be an integer")
                    if v <= 0:
                        raise ValueError("width must be > 0")
                    self.size = v
                elif k == "x":
                    if not isinstance(v, int):
                        raise TypeError("x must be an integer")
                    if v < 0:
                        raise ValueError("x must be >= 0")
                    self.x = v
                elif k == "y":
                    if not isinstance(v, int):
                        raise TypeError("y must be an integer")
                    if v < 0:
                        raise ValueError("y must be >= 0")
                    self.y = v

        if len(args) > 0:
            if not isinstance(args[0], int):
                raise TypeError("id must be an integer")
            self.id = args[0]

        if len(args) > 1:
            if not isinstance(args[1], int):
                raise TypeError("width must be an integer")
            if args[1] <= 0:
                raise ValueError("width must be > 0")
            self.size = args[1]

        if len(args) > 2:
            if not isinstance(args[2], int):
                raise TypeError("height must be an integer")
            if args[2] <= 0:
                raise ValueError("height must be > 0")
            self.x = args[2]

        if len(args) > 3:
            if not isinstance(args[3], int):
                raise TypeError("x must be an integer")
            if args[3] < 0:
                raise ValueError("x must be >= 0")
            self.y = args[3]

        if len(args) == 0:
            return

    def to_dictionary(self):
        '''Returns the dictionary representation of an object rectangle

        Returns:
            dict: dictionary representation of a Square object'''
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
