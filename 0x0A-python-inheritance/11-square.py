#!/usr/bin/python3
'''Contains class called BaseGeometry and child class Rectangle'''


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
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")


class Rectangle(BaseGeometry):
    '''A child class Rectangle whose parent is BaseGeometry

    Attributes:
        width (int): The width of the rectangle
        height (int): The height of the rectangle
    '''
    def __init__(self, width, height):
        '''Initializes an object with width and height when instanciated

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        '''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''Gets the area of the rectangle object

        Returns:
            int: The area of a rectangle object which is width * height
        '''
        return self.__width * self.__height

    def __str__(self):
        '''Prints the width and rectangle of an object

        Returns:
            string: The name Rectangle and the width and height of an object
            instance.
        '''
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    '''A child class Square that inherits from Rectangle parent class which
    its parent class is BaseGeometry

    Attributes:
        size (int): The size of the square object
    '''
    def __init__(self, size):
        '''Initializes the square object with size when instanciated

        Args:
            size (int): The size of the square object
        '''
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        '''Gets the area of the square object

        Returns:
            int: The area of the square object which is size raised to power 2
        '''
        return self.__size**2

    def __str__(self):
        return "[Square] {0}/{0}".format(self.__size)
