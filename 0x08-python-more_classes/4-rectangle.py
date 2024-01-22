#!/usr/bin/python3
'''This module defines a Class Rectangle with some attributee'''


class Rectangle:
    '''This is a Rectangle class

    Attributes:
        width (int): The width of the rectangle
        height (int): The height of the rectangle
    '''
    def __init__(self, width=0, height=0):
        '''Initializes the objects with two attributes - width and height

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle

        Raises:
            TypeError: When the value is not an integer
            ValueError: When the value is less than 0
        '''
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    @property
    def width(self):
        '''Used ot get or access the attribute width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''This sets the width attribute of the object to a new value

        Args:
            value (int): The value to be checked before setting the attribute

        Raises:
            TypeError: When the value is not an integer
            ValueError: When the value is less than 0
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''Gets or access the attribute height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''This sets the height attribute of the object to a new value

        Args:
            value (int): The value to be checked before setting the attribute

        Raises:
            TypeError: When the value is not an integer
            ValueError: When the value is less than 0'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        '''Gets the Area of the Rectangle

        Returns:
            int: The area of the rectangle width * height
        '''
        return self.__height * self.__width

    def perimeter(self):
        '''Gets the perimeter of the rectangle

        Returns:
            int: 0 when either sides of the rectangle is 0 or perimeter
            (width + height) * 2
        '''
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__height + self.__width) * 2

    def __str__(self):
        '''Prints the rectangle on the stdout using # character

        Returns:
            str: # Rectangle dimensions
        '''
        string = ""
        if self.__width != 0 and self.__height != 0:
            for h in range(self.__height):
                for w in range(self.__width):
                    string += "#"
                if h < self.__height - 1:
                    string += "\n"

        return string

    def __repr__(self):
        '''Returns the width and height of the rectangle

        Returns:
            str: Rectangle(width, height)
        '''
        return "Rectangle({}, {})".format(self.__width, self.__height)
