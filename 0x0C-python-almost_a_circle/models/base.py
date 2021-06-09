#!bin/usr/python3
"""
the first class Base:
"""


class Base:
    """
    class Base is the base for all the project
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """inizialitation of the id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
