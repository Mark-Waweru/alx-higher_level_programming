#!/usr/bin/python3
'''This module defines a Class Rectangle with some attributee'''


class Rectangle:
    '''This is a Rectangle class

    Attributes:
        number_of_instances (int): A counter of rectangle objects instanciated
        print_symbol (str): A string character to print the rectangle object
        width (int): The width of the rectangle
        height (int): The height of the rectangle
    '''

    number_of_instances = 0
    print_symbol = "#"

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

        Rectangle.number_of_instances += 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''Compares the area of two rectangles and determines the bigger one or
        equal

        Args:
            rect_1 (Rectangle): The first rectangle object to compare
            rect_2 (Rectangle): The second rectangle object to compare to

        Returns:
            Rectangle: The biggest rectangle between the two or rect_1 if
            equal
        '''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        '''Instanciates a new square

        Args:
            size (int): The size of sides of the new rectangle

        Returns:
            Rectangle: A New Rectangle with same size, inshort a square
        '''
        return cls(size, size)

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
                    string += str(self.print_symbol)
                if h < self.__height - 1:
                    string += "\n"

        return string

    def __repr__(self):
        '''Returns the width and height of the rectangle

        Returns:
            str: Rectangle(width, height)
        '''
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        '''Prints a message when a rectangle instance is deleted'''
        print("Bye rectangle...")

        Rectangle.number_of_instances -= 1
