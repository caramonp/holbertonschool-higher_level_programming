#!/usr/bin/python3
"""
   function that returns True if the object is
   exactly an instance of the specified class
"""


def is_kind_of_class(obj, a_class):
    """funtion that is true is an object is an instance
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
