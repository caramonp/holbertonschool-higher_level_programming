#!/usr/bin/python3
"""
Square inheriting Rectangle class
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Class Square
    """
    def __init__(self, size):
        """Initilization class attributes
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return Rectangle.area(self)

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
