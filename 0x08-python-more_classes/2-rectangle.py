#!/usr/bin/python3
""""
class define a rectabgle.
"""


class Rectangle:
    """Class my_rectangle define a empty value
    """
    def __init__(self, width=0, height=0):
        """ Instantiation
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter for height
        """
        return self.__height

    @width.setter
    def height(self, value):
        """ Setter for height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value


    def area(self):
        """ Returns area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns Perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.height + self.width)
