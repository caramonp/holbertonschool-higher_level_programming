#!/usr/bin/python3
""""
classdefine a square.
"""


class Square:
    """Class square define a  value"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """method area to multiplicate size for himself"""
        size = self.__size
        return size * size
