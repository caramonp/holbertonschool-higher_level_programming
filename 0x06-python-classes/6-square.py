#!/usr/bin/python3
""""
classdefine a square.
"""


class Square:
    """Class square define a  value"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != tuple or len(value) != 2:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if len(value) != 2 and type(value) != int:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """method area to multiplicate size for himself"""
        size = self.__size
        return size * size

    def my_print(self):
        size = self.__size
        position = self.__position

        for p in range(position[1]):
            print()

        for row in range(size):
            print((" " * position[0]) + ("#" * size))

        if size == 0:
            print()
