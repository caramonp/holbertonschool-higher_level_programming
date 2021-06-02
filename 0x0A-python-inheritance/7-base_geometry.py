#!/usr/bin/python3
"""
BaseGeometry class
"""


class BaseGeometry:
    """BaseGeometry empty class
    """
    def area(self):
        """Function that calculates the area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Funtion that valide the value
        """
        if type(value) != int:
            raise TypeError(name + " must be an integer")

        if value <= 0:
            raise ValueError(name + " must be greater than 0")
