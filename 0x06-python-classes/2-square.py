#!/usr/bin/python3
""""
classdefine a square.
"""


class Square:
    """Class square define a empty value"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.size = size
