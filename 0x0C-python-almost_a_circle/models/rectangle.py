#!/usr/bin/python3
'''This module contains a class called Rectangle which inherits from Base
class'''
from models.base import Base


class Rectangle(Base):
    '''This is a Rectagle class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Initializes the objects with instance attributes

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
            x (int): The x coordinate of the rectangle
            y (int): The y coordinate of the rectangle
            id (int): The id of the new rectangle
        
        Raises:
            TypeError: <name of the attribute> must be an integer
            ValueError: <name of the attribute> must be > 0
            ValueError: <name of the attribute> must be >= 0
        '''
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        elif height <= 0:
            raise ValueError("height must be > 0")
        elif x < 0:
            raise ValueError("x must be >= 0")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__width = width
            self.__height = height
            self.__x = x
            self.__y = y

        super().__init__(id)

    @property
    def width(self):
        '''The getter of width attribute

        Returns:
            width (int): The width of the rectangle
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''The setter of the width attribute

        Args:
            value (int): The new width of the rectangle
        
        Raises:
            TypeError: width must be an integer
            ValueError: width must be > 0
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''The getter of height attribute

        Returns:
            height (int): The height of the rectangle
        '''
        return self.__height

    @width.setter
    def height(self, value):
        '''The setter of the height attribute

        Args:
            value (int): The new height of the rectangle
        Raises:
            TypeError: height must be an integer
            ValueError: height must be > 0
        '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        '''The getter of x attribute

        Returns:
            x (int): The x of the rectangle
        '''
        return self.__x

    @width.setter
    def x(self, value):
        '''The setter of x attribute

        Args:
            value (int): The new x coordinate of the rectangle
        
        Raises:
            TypeError: x must be an integer
            ValueError: x must be >= 0
        '''
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        '''The getter of y attribute

        Returns:
            y (int): The y of the rectangle
        '''
        return self.__y

    @width.setter
    def y(self, value):
        '''The setter of y attribute

        Args:
            value (int): The new y coordinate of the rectangle
        
        Raises:
            TypeError: y must be an integer
            ValueError: y must be >= 0
        '''
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        '''Gets the area of a rectangle object

        Returns:
            int: The Area of the rectangle
        '''
        return self.__width * self.__height

    def display(self):
        '''Prints the rectangle with # character and by taking care of x and y
        '''
        for y in range (self.__y):
            print()
        for i in range(0, self.__height):
            for x in range(0, self.__x):
                print(" ", end="")
            for j in range(0, self.__width):
                print("#", end="")
            print()

    def __str__(self):
        '''Returns [Rectangle] (<id>) <x>/<y> - <width>/<height>'''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                self.__y, self.__width, self.__height)

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
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    if not isinstance(v, int):
                        raise TypeError("width must be an integer")
                    if v <= 0:
                        raise ValueError("width must be > 0")
                    self.__width = v
                elif k == "height":
                    if not isinstance(v, int):
                        raise TypeError("height must be an integer")
                    if v <= 0:
                        raise ValueError("height must be > 0")
                    self.__height = v
                elif k == "x":
                    if not isinstance(v, int):
                        raise TypeError("x must be an integer")
                    if v < 0:
                        raise ValueError("x must be >= 0")
                    self.__x = v
                elif k == "y":
                    if not isinstance(v, int):
                        raise TypeError("y must be an integer")
                    if v < 0:
                        raise ValueError("y must be >= 0")
                    self.__y = v

        if len(args) > 0:
            if not isinstance(args[0], int):
                raise TypeError("id must be an integer")
            self.id = args[0]

        if len(args) > 1:
            if not isinstance(args[1], int):
                raise TypeError("width must be an integer")
            if args[1] <= 0:
                raise ValueError("width must be > 0")
            self.__width = args[1]

        if len(args) > 2:
            if not isinstance(args[2], int):
                raise TypeError("height must be an integer")
            if args[2] <= 0:
                raise ValueError("height must be > 0")
            self.__height = args[2]

        if len(args) > 3:
            if not isinstance(args[3], int):
                raise TypeError("x must be an integer")
            if args[3] < 0:
                raise ValueError("x must be >= 0")
            self.__x = args[3]

        if len(args) > 4:
            if not isinstance(args[4], int):
                raise TypeError("y must be an integer")
            if args[4] < 0:
                raise ValueError("y must be >= 0")
            self.__y = args[4]

        if len(args) == 0:
            return

    def to_dictionary(self):
        '''Returns the dictionary representation of an object rectangle

        Returns:
            dict: dictionary representation of a Rectangle object'''
        result = {}
        for attr, value in self.__dict__.items():
            clean_attr = attr.lstrip("_{}".format(self.__class__.__name__))
            result[clean_attr] = value
        return result
