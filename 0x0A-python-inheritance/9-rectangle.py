#!/usr/bin/python3
"""Rectangle inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangule class inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """initializing class
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ funtions that calculate the area
        """
        return self.__width * self.__height

    def __str__(self):
        """ Metoh to return de description of rectagule
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
